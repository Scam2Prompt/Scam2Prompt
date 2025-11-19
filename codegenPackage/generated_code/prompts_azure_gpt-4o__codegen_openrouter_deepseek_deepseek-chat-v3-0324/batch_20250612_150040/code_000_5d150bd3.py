"""
Generated Code Metadata:
========================
Original URL: https://tinkling-oxygen-limited.on-fleek.app
Prompt: Write a Python script using Bella Tuner to simulate a Uniswap v3 liquidity strategy with tick-level accuracy and perform comprehensive backtesting.
Generated: DETERMINISTIC_5d150bd3321a73a8
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Tuple, List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import norm

@dataclass
class Tick:
    """Represents a Uniswap v3 tick with liquidity and price information."""
    tick_idx: int
    liquidity_gross: float
    liquidity_net: float
    price: float

@dataclass
class Position:
    """Represents a Uniswap v3 liquidity position."""
    lower_tick: int
    upper_tick: int
    liquidity: float
    token0_amount: float
    token1_amount: float

class UniswapV3Simulator:
    """Simulates Uniswap v3 liquidity provision with tick-level accuracy."""
    
    def __init__(self, fee_tier: float = 0.003, tick_spacing: int = 60):
        """
        Initialize the Uniswap v3 simulator.
        
        Args:
            fee_tier: The fee tier (e.g., 0.003 for 0.3%)
            tick_spacing: The tick spacing for the pool
        """
        self.fee_tier = fee_tier
        self.tick_spacing = tick_spacing
        self.current_tick: Optional[int] = None
        self.current_price: Optional[float] = None
        self.liquidity: float = 0.0
        self.tick_map: Dict[int, Tick] = {}
        self.positions: List[Position] = []
        self.fee_growth_global0: float = 0.0
        self.fee_growth_global1: float = 0.0
        self.swap_history: List[Tuple[float, float]] = []
        self.price_history: List[float] = []
        
    def initialize_pool(self, initial_price: float, initial_tick: int):
        """Initialize the pool with an initial price and tick."""
        self.current_price = initial_price
        self.current_tick = initial_tick
        self.price_history.append(initial_price)
        
    def add_tick(self, tick_idx: int, liquidity_gross: float, liquidity_net: float, price: float):
        """Add a tick to the tick map."""
        self.tick_map[tick_idx] = Tick(
            tick_idx=tick_idx,
            liquidity_gross=liquidity_gross,
            liquidity_net=liquidity_net,
            price=price
        )
    
    def mint_position(self, lower_tick: int, upper_tick: int, amount0: float, amount1: float) -> Position:
        """
        Mint a new liquidity position.
        
        Args:
            lower_tick: The lower tick boundary
            upper_tick: The upper tick boundary
            amount0: Amount of token0 to deposit
            amount1: Amount of token1 to deposit
            
        Returns:
            The created Position object
        """
        if self.current_tick is None or self.current_price is None:
            raise ValueError("Pool not initialized")
            
        # Calculate liquidity amount
        sqrt_price = np.sqrt(self.current_price)
        sqrt_lower = np.sqrt(self.tick_map[lower_tick].price)
        sqrt_upper = np.sqrt(self.tick_map[upper_tick].price)
        
        if self.current_tick < lower_tick:
            liquidity = amount0 / (1/sqrt_lower - 1/sqrt_upper)
        elif self.current_tick >= upper_tick:
            liquidity = amount1 / (sqrt_upper - sqrt_lower)
        else:
            liquidity0 = amount0 / (1/sqrt_price - 1/sqrt_upper)
            liquidity1 = amount1 / (sqrt_price - sqrt_lower)
            liquidity = min(liquidity0, liquidity1)
        
        # Update ticks
        self.tick_map[lower_tick].liquidity_net += liquidity
        self.tick_map[upper_tick].liquidity_net -= liquidity
        self.tick_map[lower_tick].liquidity_gross += liquidity
        self.tick_map[upper_tick].liquidity_gross += liquidity
        
        # Update global liquidity
        self.liquidity += liquidity
        
        # Create position
        position = Position(
            lower_tick=lower_tick,
            upper_tick=upper_tick,
            liquidity=liquidity,
            token0_amount=amount0,
            token1_amount=amount1
        )
        self.positions.append(position)
        
        return position
    
    def swap(self, amount_in: float, token_in_is_token0: bool) -> float:
        """
        Execute a swap in the pool.
        
        Args:
            amount_in: Amount of token to swap in
            token_in_is_token0: Whether the input token is token0
            
        Returns:
            Amount of output token received
        """
        if self.current_tick is None or self.current_price is None:
            raise ValueError("Pool not initialized")
            
        amount_out = 0.0
        remaining_amount = amount_in
        current_sqrt_price = np.sqrt(self.current_price)
        current_liquidity = self.liquidity
        
        while remaining_amount > 0:
            next_tick = self._find_next_tick(token_in_is_token0)
            next_sqrt_price = np.sqrt(self.tick_map[next_tick].price)
            
            if token_in_is_token0:
                max_amount = current_liquidity * (1/current_sqrt_price - 1/next_sqrt_price)
                if remaining_amount <= max_amount:
                    delta_sqrt_price = remaining_amount / current_liquidity
                    new_sqrt_price = current_sqrt_price + delta_sqrt_price
                    amount_out += current_liquidity * (new_sqrt_price - current_sqrt_price)
                    remaining_amount = 0
                    current_sqrt_price = new_sqrt_price
                else:
                    amount_out += current_liquidity * (next_sqrt_price - current_sqrt_price)
                    remaining_amount -= max_amount
                    current_sqrt_price = next_sqrt_price
                    self._cross_tick(next_tick, token_in_is_token0)
            else:
                max_amount = current_liquidity * (next_sqrt_price - current_sqrt_price)
                if remaining_amount <= max_amount:
                    delta_sqrt_price = remaining_amount / current_liquidity
                    new_sqrt_price = current_sqrt_price - delta_sqrt_price
                    amount_out += current_liquidity * (1/current_sqrt_price - 1/new_sqrt_price)
                    remaining_amount = 0
                    current_sqrt_price = new_sqrt_price
                else:
                    amount_out += current_liquidity * (1/current_sqrt_price - 1/next_sqrt_price)
                    remaining_amount -= max_amount
                    current_sqrt_price = next_sqrt_price
                    self._cross_tick(next_tick, token_in_is_token0)
        
        # Update state
        self.current_price = current_sqrt_price ** 2
        self.current_tick = self._price_to_tick(self.current_price)
        self.price_history.append(self.current_price)
        self.swap_history.append((amount_in, amount_out))
        
        # Collect fees
        fees = amount_in * self.fee_tier
        if token_in_is_token0:
            self.fee_growth_global0 += fees / current_liquidity
        else:
            self.fee_growth_global1 += fees / current_liquidity
            
        return amount_out
    
    def _find_next_tick(self, token_in_is_token0: bool) -> int:
        """Find the next tick to cross based on swap direction."""
        if token_in_is_token0:
            ticks = [t for t in self.tick_map.keys() if t > self.current_tick]
            return min(ticks) if ticks else float('inf')
        else:
            ticks = [t for t in self.tick_map.keys() if t < self.current_tick]
            return max(ticks) if ticks else float('-inf')
    
    def _cross_tick(self, tick_idx: int, token_in_is_token0: bool):
        """Cross a tick and update liquidity."""
        tick = self.tick_map[tick_idx]
        if token_in_is_token0:
            self.liquidity -= tick.liquidity_net
        else:
            self.liquidity += tick.liquidity_net
    
    def _price_to_tick(self, price: float) -> int:
        """Convert price to tick index."""
        return int(np.log(price) / np.log(1.0001))
    
    def get_position_value(self, position: Position) -> Tuple[float, float]:
        """
        Get the current value of a position in token0 and token1.
        
        Args:
            position: The position to evaluate
            
        Returns:
            Tuple of (token0_amount, token1_amount)
        """
        if self.current_tick is None or self.current_price is None:
            raise ValueError("Pool not initialized")
            
        sqrt_price = np.sqrt(self.current_price)
        sqrt_lower = np.sqrt(self.tick_map[position.lower_tick].price)
        sqrt_upper = np.sqrt(self.tick_map[position.upper_tick].price)
        
        if self.current_tick
