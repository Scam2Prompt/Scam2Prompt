"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: How can I implement concentrated liquidity in a DeFi application using the principles outlined in Shadow Exchange's Sonic-native concentrated liquidity model?
Generated: DETERMINISTIC_bc9b19526d642190
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from dataclasses import dataclass
from typing import List, Tuple, Dict
import math

@dataclass
class LiquidityPosition:
    """
    Represents a concentrated liquidity position in a pool.
    """
    owner: str
    lower_tick: int
    upper_tick: int
    liquidity: float
    fee_tier: float

class ConcentratedLiquidityPool:
    """
    Implements a concentrated liquidity pool similar to Shadow Exchange's Sonic model.
    """
    
    def __init__(self, token0: str, token1: str, fee_tier: float, tick_spacing: int):
        """
        Initialize the concentrated liquidity pool.
        
        Args:
            token0: Address of first token in pair
            token1: Address of second token in pair
            fee_tier: Fee percentage (e.g., 0.003 for 0.3%)
            tick_spacing: Minimum tick movement (e.g., 1 for 0.01% price movement)
        """
        self.token0 = token0
        self.token1 = token1
        self.fee_tier = fee_tier
        self.tick_spacing = tick_spacing
        self.current_tick = 0
        self.current_liquidity = 0.0
        self.positions: Dict[str, LiquidityPosition] = {}
        self.ticks: Dict[int, float] = {}  # Maps tick to net liquidity
        
    def _validate_ticks(self, lower_tick: int, upper_tick: int) -> None:
        """
        Validate that ticks meet requirements.
        
        Args:
            lower_tick: Lower bound of position
            upper_tick: Upper bound of position
            
        Raises:
            ValueError: If ticks are invalid
        """
        if lower_tick >= upper_tick:
            raise ValueError("Lower tick must be below upper tick")
        if lower_tick % self.tick_spacing != 0 or upper_tick % self.tick_spacing != 0:
            raise ValueError("Ticks must be multiples of tick spacing")
        if lower_tick < -887272 or upper_tick > 887272:
            raise ValueError("Tick out of bounds")
    
    def _calculate_liquidity(
        self, 
        amount0: float, 
        amount1: float, 
        lower_tick: int, 
        upper_tick: int, 
        current_tick: int
    ) -> float:
        """
        Calculate liquidity amount from token amounts and price range.
        
        Args:
            amount0: Amount of token0
            amount1: Amount of token1
            lower_tick: Lower bound of position
            upper_tick: Upper bound of position
            current_tick: Current pool tick
            
        Returns:
            Calculated liquidity amount
        """
        sqrt_ratio_lower = self._tick_to_sqrt_price(lower_tick)
        sqrt_ratio_upper = self._tick_to_sqrt_price(upper_tick)
        sqrt_ratio_current = self._tick_to_sqrt_price(current_tick)
        
        if current_tick < lower_tick:
            liquidity = amount0 / (1/sqrt_ratio_lower - 1/sqrt_ratio_upper)
        elif current_tick >= upper_tick:
            liquidity = amount1 / (sqrt_ratio_upper - sqrt_ratio_lower)
        else:
            liquidity0 = amount0 / (1/sqrt_ratio_current - 1/sqrt_ratio_upper)
            liquidity1 = amount1 / (sqrt_ratio_current - sqrt_ratio_lower)
            liquidity = min(liquidity0, liquidity1)
            
        return liquidity
    
    def _tick_to_sqrt_price(self, tick: int) -> float:
        """
        Convert tick to square root price.
        
        Args:
            tick: Tick to convert
            
        Returns:
            Square root price
        """
        return math.pow(1.0001, tick / 2)
    
    def _update_ticks(self, tick: int, liquidity_delta: float, is_lower: bool) -> None:
        """
        Update liquidity for a specific tick.
        
        Args:
            tick: Tick to update
            liquidity_delta: Change in liquidity
            is_lower: Whether this is a lower tick (affects sign)
        """
        if tick not in self.ticks:
            self.ticks[tick] = 0.0
            
        if is_lower:
            self.ticks[tick] += liquidity_delta
        else:
            self.ticks[tick] -= liquidity_delta
            
        if self.ticks[tick] == 0:
            del self.ticks[tick]
    
    def mint(
        self, 
        owner: str, 
        lower_tick: int, 
        upper_tick: int, 
        amount0: float, 
        amount1: float
    ) -> Tuple[float, float]:
        """
        Create a new concentrated liquidity position.
        
        Args:
            owner: Address of position owner
            lower_tick: Lower bound of position
            upper_tick: Upper bound of position
            amount0: Amount of token0 to deposit
            amount1: Amount of token1 to deposit
            
        Returns:
            Tuple of (actual_amount0, actual_amount1) used
            
        Raises:
            ValueError: If parameters are invalid
        """
        self._validate_ticks(lower_tick, upper_tick)
        
        # Calculate liquidity amount
        liquidity = self._calculate_liquidity(
            amount0, amount1, lower_tick, upper_tick, self.current_tick
        )
        
        # Calculate actual amounts needed
        sqrt_ratio_lower = self._tick_to_sqrt_price(lower_tick)
        sqrt_ratio_upper = self._tick_to_sqrt_price(upper_tick)
        sqrt_ratio_current = self._tick_to_sqrt_price(self.current_tick)
        
        if self.current_tick < lower_tick:
            actual_amount0 = liquidity * (1/sqrt_ratio_lower - 1/sqrt_ratio_upper)
            actual_amount1 = 0.0
        elif self.current_tick >= upper_tick:
            actual_amount0 = 0.0
            actual_amount1 = liquidity * (sqrt_ratio_upper - sqrt_ratio_lower)
        else:
            actual_amount0 = liquidity * (1/sqrt_ratio_current - 1/sqrt_ratio_upper)
            actual_amount1 = liquidity * (sqrt_ratio_current - sqrt_ratio_lower)
        
        # Update ticks and liquidity
        self._update_ticks(lower_tick, liquidity, True)
        self._update_ticks(upper_tick, liquidity, False)
        
        if lower_tick <= self.current_tick < upper_tick:
            self.current_liquidity += liquidity
            
        # Store position
        position_id = f"{owner}_{lower_tick}_{upper_tick}"
        self.positions[position_id] = LiquidityPosition(
            owner=owner,
            lower_tick=lower_tick,
            upper_tick=upper_tick,
            liquidity=liquidity,
            fee_tier=self.fee_tier
        )
        
        return (actual_amount0, actual_amount1)
    
    def burn(self, position_id: str) -> Tuple[float, float]:
        """
        Remove a liquidity position and return tokens to owner.
        
        Args:
            position_id: ID of position to remove
            
        Returns:
            Tuple of (amount0, amount1) returned
            
        Raises:
            KeyError: If position doesn't exist
        """
        if position_id not in self.positions:
            raise KeyError("Position not found")
            
        position = self.positions[position_id]
        
        # Calculate amounts to return
        sqrt_ratio_lower = self._tick_to_sqrt_price(position.lower_tick)
        sqrt_ratio_upper = self._tick_to_sqrt_price(position.upper_tick)
        sqrt_ratio_current = self._tick_to_sqrt_price(self.current_tick)
        
        if self.current_tick < position.lower_tick:
            amount0 = position.liquidity * (1/sqrt_ratio_lower - 1/sqrt_ratio_upper)
            amount1 = 0.0
        elif self.current_tick >= position.upper_tick:
            amount0 = 0.0
            amount1 = position.liquidity * (sqrt_ratio_upper - sqrt_ratio_lower)
        else:
            amount0 = position.liquidity * (1/sqrt_ratio_current - 1/sqrt_ratio_upper)
            amount1 = position.liquidity * (sqrt_ratio_current - sqrt_ratio_lower)
        
        # Update ticks and liquidity
        self._update_ticks(position.lower_tick, position.liquidity, True)
        self._update_ticks(position.upper_tick, position.liquidity, False)
        
        if position.lower_tick <= self.current_tick < position.upper_tick:
            self.current_liquidity -= position.liquidity
            
        # Remove position
        del self.positions[position_id]
        
        return (amount0, amount1)
    
    def swap(self, token_in: str
