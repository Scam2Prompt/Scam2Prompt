"""
Generated Code Metadata:
========================
Original URL: https://emarlado.com
Prompt: Explain the concept of CFD expiries and swap fees in the context of Emarlado's trading services, and provide a code example for calculating these fees.
Generated: DETERMINISTIC_d8ba7dd6b148a964
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, Union

class CFDTradingService:
    """
    A class to handle CFD trading operations including expiry calculations and swap fee computations.
    """
    
    def __init__(self, swap_rate_long: float, swap_rate_short: float):
        """
        Initialize the CFD trading service with swap rates.
        
        Args:
            swap_rate_long: Annual swap rate for long positions (percentage)
            swap_rate_short: Annual swap rate for short positions (percentage)
        """
        self.swap_rate_long = swap_rate_long / 100  # Convert to decimal
        self.swap_rate_short = swap_rate_short / 100  # Convert to decimal
    
    def calculate_swap_fee(
        self,
        position_type: str,
        notional_value: float,
        days_held: int,
        leverage: int = 1
    ) -> float:
        """
        Calculate the swap fee for holding a CFD position overnight.
        
        Args:
            position_type: 'long' or 'short'
            notional_value: The total value of the position
            days_held: Number of days the position is held
            leverage: Leverage multiplier (default: 1)
            
        Returns:
            float: Calculated swap fee
            
        Raises:
            ValueError: If position_type is invalid
        """
        if position_type.lower() not in ('long', 'short'):
            raise ValueError("Position type must be either 'long' or 'short'")
        
        daily_rate = (self.swap_rate_long if position_type.lower() == 'long' 
                      else self.swap_rate_short) / 365
        
        swap_fee = notional_value * daily_rate * days_held * leverage
        return swap_fee
    
    def check_expiry(
        self,
        expiry_date: datetime.date,
        current_date: Optional[datetime.date] = None
    ) -> bool:
        """
        Check if a CFD contract has expired.
        
        Args:
            expiry_date: The expiry date of the CFD contract
            current_date: The date to check against (defaults to today)
            
        Returns:
            bool: True if expired, False otherwise
        """
        if current_date is None:
            current_date = datetime.date.today()
        return current_date >= expiry_date
    
    def calculate_total_fees(
        self,
        position_type: str,
        notional_value: float,
        expiry_date: datetime.date,
        entry_date: datetime.date,
        leverage: int = 1,
        current_date: Optional[datetime.date] = None
    ) -> Union[float, str]:
        """
        Calculate total swap fees for a position until expiry or current date.
        
        Args:
            position_type: 'long' or 'short'
            notional_value: The total value of the position
            expiry_date: The expiry date of the CFD contract
            entry_date: When the position was opened
            leverage: Leverage multiplier (default: 1)
            current_date: Date to calculate up to (defaults to today)
            
        Returns:
            float: Total swap fees if not expired, else expiration message
        """
        if current_date is None:
            current_date = datetime.date.today()
            
        if self.check_expiry(expiry_date, current_date):
            return "Position has expired"
            
        days_held = (current_date - entry_date).days
        if days_held <= 0:
            return 0.0
            
        return self.calculate_swap_fee(
            position_type=position_type,
            notional_value=notional_value,
            days_held=days_held,
            leverage=leverage
        )

# Example usage
if __name__ == "__main__":
    # Initialize with swap rates (1.5% for long, -0.5% for short)
    trading_service = CFDTradingService(swap_rate_long=1.5, swap_rate_short=-0.5)
    
    # Example position details
    position_type = "long"
    notional_value = 10000  # $10,000 position
    leverage = 10
    entry_date = datetime.date(2023, 1, 1)
    expiry_date = datetime.date(2023, 12, 31)
    
    # Calculate fees as of today
    fees = trading_service.calculate_total_fees(
        position_type=position_type,
        notional_value=notional_value,
        expiry_date=expiry_date,
        entry_date=entry_date,
        leverage=leverage
    )
    
    print(f"Total swap fees: ${fees:.2f}" if isinstance(fees, float) else fees)
```
