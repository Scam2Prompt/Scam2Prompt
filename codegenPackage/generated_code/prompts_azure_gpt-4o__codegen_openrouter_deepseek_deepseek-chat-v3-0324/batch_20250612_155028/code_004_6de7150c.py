"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Write code to simulate concentrated liquidity provisioning for a specific price range, leveraging the principles of Shadow Exchange's Sonic-native liquidity model.
Generated: DETERMINISTIC_6de7150c06a63566
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class LiquidityPosition:
    """
    Represents a concentrated liquidity position within a specific price range.
    """
    lower_tick: int
    upper_tick: int
    liquidity: float
    token_x: float
    token_y: float

class ConcentratedLiquidityPool:
    """
    Simulates a concentrated liquidity pool with Sonic-native model characteristics.
    """
    
    def __init__(self, token_x: str, token_y: str, fee_rate: float, tick_spacing: int):
        """
        Initialize the liquidity pool.
        
        Args:
            token_x: Name of token X
            token_y: Name of token Y
            fee_rate: Trading fee rate (e.g., 0.003 for 0.3%)
            tick_spacing: Minimum tick spacing for positions
        """
        self.token_x = token_x
        self.token_y = token_y
        self.fee_rate = fee_rate
        self.tick_spacing = tick_spacing
        self.current_tick = 0
        self.current_price = 1.0
        self.liquidity_positions = []
        self.global_liquidity = 0.0
        
    def calculate_sqrt_price(self, tick: int) -> float:
        """Calculate square root price from tick."""
        return math.exp(tick / 2)
    
    def calculate_tick(self, price: float) -> int:
        """Calculate tick from price."""
        return math.floor(math.log(price) * 2)
    
    def validate_ticks(self, lower_tick: int, upper_tick: int) -> bool:
        """Validate that ticks meet pool requirements."""
        if lower_tick >= upper_tick:
            return False
        if lower_tick % self.tick_spacing != 0 or upper_tick % self.tick_spacing != 0:
            return False
        return True
    
    def calculate_liquidity(
        self,
        amount_x: float,
        amount_y: float,
        lower_tick: int,
        upper_tick: int,
        current_tick: Optional[int] = None
    ) -> Tuple[float, float, float]:
        """
        Calculate liquidity amounts for given tokens and price range.
        
        Returns:
            Tuple of (liquidity, actual_x, actual_y)
        """
        current_tick = current_tick if current_tick is not None else self.current_tick
        
        sqrt_lower = self.calculate_sqrt_price(lower_tick)
        sqrt_upper = self.calculate_sqrt_price(upper_tick)
        sqrt_current = self.calculate_sqrt_price(current_tick)
        
        if current_tick < lower_tick:
            liquidity = amount_x / (1/sqrt_lower - 1/sqrt_upper)
            actual_x = amount_x
            actual_y = 0.0
        elif current_tick >= upper_tick:
            liquidity = amount_y / (sqrt_upper - sqrt_lower)
            actual_x = 0.0
            actual_y = amount_y
        else:
            liquidity_x = amount_x / (1/sqrt_current - 1/sqrt_upper)
            liquidity_y = amount_y / (sqrt_current - sqrt_lower)
            liquidity = min(liquidity_x, liquidity_y)
            actual_x = liquidity * (1/sqrt_current - 1/sqrt_upper)
            actual_y = liquidity * (sqrt_current - sqrt_lower)
        
        return liquidity, actual_x, actual_y
    
    def add_liquidity(
        self,
        amount_x: float,
        amount_y: float,
        lower_tick: int,
        upper_tick: int
    ) -> LiquidityPosition:
        """
        Add concentrated liquidity to the pool within specified price range.
        
        Args:
            amount_x: Amount of token X to deposit
            amount_y: Amount of token Y to deposit
            lower_tick: Lower bound of price range
            upper_tick: Upper bound of price range
            
        Returns:
            New liquidity position
            
        Raises:
            ValueError: If ticks are invalid or amounts are insufficient
        """
        if not self.validate_ticks(lower_tick, upper_tick):
            raise ValueError("Invalid tick range")
        
        if amount_x <= 0 or amount_y <= 0:
            raise ValueError("Amounts must be positive")
        
        liquidity, actual_x, actual_y = self.calculate_liquidity(
            amount_x, amount_y, lower_tick, upper_tick
        )
        
        if actual_x > amount_x or actual_y > amount_y:
            raise ValueError("Insufficient amounts for desired range")
        
        position = LiquidityPosition(
            lower_tick=lower_tick,
            upper_tick=upper_tick,
            liquidity=liquidity,
            token_x=actual_x,
            token_y=actual_y
        )
        
        self.liquidity_positions.append(position)
        self.global_liquidity += liquidity
        
        return position
    
    def remove_liquidity(self, position: LiquidityPosition) -> Tuple[float, float]:
        """
        Remove liquidity from the pool and return tokens.
        
        Args:
            position: Liquidity position to remove
            
        Returns:
            Tuple of (amount_x, amount_y) returned
            
        Raises:
            ValueError: If position not found
        """
        if position not in self.liquidity_positions:
            raise ValueError("Position not found")
        
        self.liquidity_positions.remove(position)
        self.global_liquidity -= position.liquidity
        
        return position.token_x, position.token_y
    
    def swap(self, amount_in: float, token_in: str) -> float:
        """
        Execute a swap in the pool.
        
        Args:
            amount_in: Amount of token to swap
            token_in: Which token is being swapped ('x' or 'y')
            
        Returns:
            Amount of output token received
            
        Raises:
            ValueError: For invalid inputs
        """
        if token_in not in ('x', 'y'):
            raise ValueError("Token must be 'x' or 'y'")
        if amount_in <= 0:
            raise ValueError("Amount must be positive")
        
        amount_out = 0.0
        remaining_amount = amount_in
        
        # Sort positions by distance to current price
        sorted_positions = sorted(
            self.liquidity_positions,
            key=lambda p: abs(self.current_tick - (p.lower_tick + p.upper_tick) // 2)
        )
        
        for position in sorted_positions:
            if remaining_amount <= 0:
                break
                
            if token_in == 'x':
                if self.current_tick >= position.upper_tick:
                    continue  # Position only contains Y
                    
                sqrt_lower = self.calculate_sqrt_price(position.lower_tick)
                sqrt_upper = self.calculate_sqrt_price(position.upper_tick)
                sqrt_current = self.calculate_sqrt_price(self.current_tick)
                
                max_x = position.liquidity * (1/sqrt_current - 1/sqrt_upper)
                x_in = min(remaining_amount, max_x)
                
                sqrt_new = sqrt_current + (x_in / position.liquidity)
                y_out = position.liquidity * (sqrt_new - sqrt_current)
                
                remaining_amount -= x_in
                amount_out += y_out
                self.current_tick = self.calculate_tick(sqrt_new ** 2)
                
            else:  # token_in == 'y'
                if self.current_tick < position.lower_tick:
                    continue  # Position only contains X
                    
                sqrt_lower = self.calculate_sqrt_price(position.lower_tick)
                sqrt_upper = self.calculate_sqrt_price(position.upper_tick)
                sqrt_current = self.calculate_sqrt_price(self.current_tick)
                
                max_y = position.liquidity * (sqrt_current - sqrt_lower)
                y_in = min(remaining_amount, max_y)
                
                sqrt_new = sqrt_current - (y_in / position.liquidity)
                x_out = position.liquidity * (1/sqrt_current - 1/sqrt_new)
                
                remaining_amount -= y_in
                amount_out += x_out
                self.current_tick = self.calculate_tick(sqrt_new ** 2)
        
        # Apply fee
        fee = amount_out * self.fee_rate
        amount_out -= fee
        
        # Update current price
        self.current_price = math.exp(self.current_tick)
        
        return amount_out
```
