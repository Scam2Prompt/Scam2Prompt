"""
Generated Code Metadata:
========================
Original URL: https://bafybeidtnckzvkdfd4adyg7s3vhgnsxy3sxyvceyaty6bcbuxmmlfvut3a.ipfs.dweb.link
Prompt: Generate an example of how to implement Pendle's AMM for yield trading with concentrated liquidity.
Generated: DETERMINISTIC_5861a1b27fcbf909
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from typing import Tuple, Dict
from math import sqrt
from dataclasses import dataclass

@dataclass
class PoolState:
    """
    Represents the state of a concentrated liquidity pool.
    """
    reserve_x: float  # Reserve of token X
    reserve_y: float  # Reserve of token Y
    liquidity: float  # Current liquidity in the pool
    sqrt_price: float  # Current sqrt(price)
    tick: int         # Current tick

@dataclass
class Tick:
    """
    Represents a tick in the concentrated liquidity pool.
    """
    liquidity_net: float  # Net liquidity added when tick is crossed
    liquidity_gross: float # Total liquidity referencing this tick

class ConcentratedLiquidityAMM:
    """
    Implementation of Pendle's AMM for yield trading with concentrated liquidity.
    """
    
    def __init__(self, fee_rate: float = 0.003):
        """
        Initialize the AMM with a fee rate (default: 0.3%).
        
        Args:
            fee_rate: The trading fee rate (e.g., 0.003 for 0.3%)
        """
        self.fee_rate = fee_rate
        self.pool_state = PoolState(0.0, 0.0, 0.0, 0.0, 0)
        self.ticks: Dict[int, Tick] = {}
        
    def initialize_pool(self, initial_reserve_x: float, initial_reserve_y: float, initial_tick: int):
        """
        Initialize the pool with initial reserves and tick.
        
        Args:
            initial_reserve_x: Initial reserve of token X
            initial_reserve_y: Initial reserve of token Y
            initial_tick: Initial tick
        """
        if initial_reserve_x <= 0 or initial_reserve_y <= 0:
            raise ValueError("Reserves must be positive")
            
        self.pool_state.reserve_x = initial_reserve_x
        self.pool_state.reserve_y = initial_reserve_y
        self.pool_state.tick = initial_tick
        self.pool_state.sqrt_price = self._tick_to_sqrt_price(initial_tick)
        self.pool_state.liquidity = sqrt(initial_reserve_x * initial_reserve_y)
        
    def _tick_to_sqrt_price(self, tick: int) -> float:
        """
        Convert tick to sqrt(price).
        
        Args:
            tick: The tick to convert
            
        Returns:
            The corresponding sqrt(price)
        """
        return 1.0001 ** (tick / 2)
    
    def _sqrt_price_to_tick(self, sqrt_price: float) -> int:
        """
        Convert sqrt(price) to tick.
        
        Args:
            sqrt_price: The sqrt(price) to convert
            
        Returns:
            The corresponding tick
        """
        return int(2 * (sqrt_price - 1) / 0.0001)
    
    def add_liquidity(
        self,
        amount_x: float,
        amount_y: float,
        lower_tick: int,
        upper_tick: int
    ) -> Tuple[float, float]:
        """
        Add concentrated liquidity to the pool within a tick range.
        
        Args:
            amount_x: Amount of token X to add
            amount_y: Amount of token Y to add
            lower_tick: Lower tick bound
            upper_tick: Upper tick bound
            
        Returns:
            Tuple of (actual_amount_x, actual_amount_y) added
        """
        if amount_x <= 0 or amount_y <= 0:
            raise ValueError("Amounts must be positive")
        if lower_tick >= upper_tick:
            raise ValueError("Lower tick must be below upper tick")
            
        sqrt_lower = self._tick_to_sqrt_price(lower_tick)
        sqrt_upper = self._tick_to_sqrt_price(upper_tick)
        current_sqrt = self.pool_state.sqrt_price
        
        # Calculate liquidity to add
        if current_sqrt <= sqrt_lower:
            liquidity = amount_y / (sqrt_upper - sqrt_lower)
        elif current_sqrt < sqrt_upper:
            liquidity_x = amount_x / (sqrt_upper - current_sqrt)
            liquidity_y = amount_y / (current_sqrt - sqrt_lower)
            liquidity = min(liquidity_x, liquidity_y)
        else:
            liquidity = amount_x / (sqrt_upper - sqrt_lower)
            
        # Update pool state
        self.pool_state.liquidity += liquidity
        
        # Update ticks
        if lower_tick in self.ticks:
            self.ticks[lower_tick].liquidity_net += liquidity
            self.ticks[lower_tick].liquidity_gross += liquidity
        else:
            self.ticks[lower_tick] = Tick(liquidity, liquidity)
            
        if upper_tick in self.ticks:
            self.ticks[upper_tick].liquidity_net -= liquidity
            self.ticks[upper_tick].liquidity_gross += liquidity
        else:
            self.ticks[upper_tick] = Tick(-liquidity, liquidity)
            
        # Calculate actual amounts used
        if current_sqrt <= sqrt_lower:
            actual_x = 0
            actual_y = liquidity * (sqrt_upper - sqrt_lower)
        elif current_sqrt < sqrt_upper:
            actual_x = liquidity * (sqrt_upper - current_sqrt)
            actual_y = liquidity * (current_sqrt - sqrt_lower)
        else:
            actual_x = liquidity * (sqrt_upper - sqrt_lower)
            actual_y = 0
            
        return (actual_x, actual_y)
    
    def swap_x_for_y(self, amount_x: float) -> float:
        """
        Swap token X for token Y.
        
        Args:
            amount_x: Amount of token X to swap
            
        Returns:
            Amount of token Y received
        """
        if amount_x <= 0:
            raise ValueError("Amount must be positive")
            
        amount_x_after_fee = amount_x * (1 - self.fee_rate)
        delta_y = self.pool_state.reserve_y * amount_x_after_fee / (self.pool_state.reserve_x + amount_x_after_fee)
        
        # Update pool state
        self.pool_state.reserve_x += amount_x_after_fee
        self.pool_state.reserve_y -= delta_y
        self.pool_state.sqrt_price = sqrt(self.pool_state.reserve_y / self.pool_state.reserve_x)
        self.pool_state.tick = self._sqrt_price_to_tick(self.pool_state.sqrt_price)
        
        return delta_y
    
    def swap_y_for_x(self, amount_y: float) -> float:
        """
        Swap token Y for token X.
        
        Args:
            amount_y: Amount of token Y to swap
            
        Returns:
            Amount of token X received
        """
        if amount_y <= 0:
            raise ValueError("Amount must be positive")
            
        amount_y_after_fee = amount_y * (1 - self.fee_rate)
        delta_x = self.pool_state.reserve_x * amount_y_after_fee / (self.pool_state.reserve_y + amount_y_after_fee)
        
        # Update pool state
        self.pool_state.reserve_y += amount_y_after_fee
        self.pool_state.reserve_x -= delta_x
        self.pool_state.sqrt_price = sqrt(self.pool_state.reserve_y / self.pool_state.reserve_x)
        self.pool_state.tick = self._sqrt_price_to_tick(self.pool_state.sqrt_price)
        
        return delta_x
```
