"""
Generated Code Metadata:
========================
Original URL: https://stellarpay.org
Prompt: Generate a code example for calculating the parking interest for XLB tokens based on the provided parking duration and interest rates.
Generated: DETERMINISTIC_21992ecaeee0898c
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# parking_interest_calculator.py

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, Optional

class ParkingInterestError(Exception):
    """Base exception class for parking interest calculation errors."""
    pass

class InvalidDurationError(ParkingInterestError):
    """Raised when the parking duration is invalid."""
    pass

class InvalidTokenAmountError(ParkingInterestError):
    """Raised when the token amount is invalid."""
    pass

@dataclass
class ParkingInterestRate:
    """Data class representing parking interest rate tiers."""
    min_days: int
    max_days: Optional[int]  # None means no upper limit
    annual_rate: float

class ParkingInterestCalculator:
    """
    Calculates parking interest for XLB tokens based on duration and interest rates.
    
    Attributes:
        interest_rates (list[ParkingInterestRate]): List of interest rate tiers
    """
    
    def __init__(self, interest_rates: Dict[str, Dict[str, float]]):
        """
        Initialize the calculator with interest rate tiers.
        
        Args:
            interest_rates: Dictionary of interest rate tiers in format:
                {
                    "tier1": {"min_days": 0, "max_days": 30, "annual_rate": 0.05},
                    "tier2": {"min_days": 31, "max_days": 90, "annual_rate": 0.08},
                    ...
                }
        """
        self.interest_rates = []
        for tier_name, tier_data in interest_rates.items():
            self.interest_rates.append(
                ParkingInterestRate(
                    min_days=tier_data["min_days"],
                    max_days=tier_data.get("max_days"),
                    annual_rate=tier_data["annual_rate"]
                )
            )
        # Sort rates by min_days to ensure proper tier selection
        self.interest_rates.sort(key=lambda x: x.min_days)

    def _validate_inputs(self, amount: float, days: int) -> None:
        """Validate input parameters."""
        if amount <= 0:
            raise InvalidTokenAmountError("Token amount must be positive")
        if days <= 0:
            raise InvalidDurationError("Parking duration must be positive")

    def _get_applicable_rate(self, days: int) -> ParkingInterestRate:
        """Find the applicable interest rate tier for the given duration."""
        for rate in self.interest_rates:
            if (rate.min_days <= days and 
                (rate.max_days is None or days <= rate.max_days)):
                return rate
        raise InvalidDurationError(f"No interest rate found for {days} days")

    def calculate_interest(
        self,
        amount: float,
        start_date: datetime,
        end_date: datetime,
        compounding: bool = False
    ) -> float:
        """
        Calculate parking interest for XLB tokens.
        
        Args:
            amount: Amount of XLB tokens parked
            start_date: Parking start date
            end_date: Parking end date
            compounding: Whether to compound interest daily (default: False)
            
        Returns:
            float: Calculated interest in XLB tokens
            
        Raises:
            InvalidDurationError: If duration is invalid
            InvalidTokenAmountError: If token amount is invalid
        """
        duration = (end_date - start_date).days
        self._validate_inputs(amount, duration)
        
        rate = self._get_applicable_rate(duration)
        daily_rate = rate.annual_rate / 365
        
        if compounding:
            # Compound interest calculation
            return amount * ((1 + daily_rate) ** duration - 1)
        else:
            # Simple interest calculation
            return amount * daily_rate * duration

# Example usage
if __name__ == "__main__":
    # Define interest rate tiers
    RATE_TIERS = {
        "tier1": {"min_days": 1, "max_days": 30, "annual_rate": 0.05},
        "tier2": {"min_days": 31, "max_days": 90, "annual_rate": 0.08},
        "tier3": {"min_days": 91, "max_days": 180, "annual_rate": 0.10},
        "tier4": {"min_days": 181, "max_days": None, "annual_rate": 0.12}
    }
    
    calculator = ParkingInterestCalculator(RATE_TIERS)
    
    try:
        amount = 1000.0  # XLB tokens
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 4, 1)  # 90 days later
        
        simple_interest = calculator.calculate_interest(amount, start_date, end_date)
        compound_interest = calculator.calculate_interest(amount, start_date, end_date, compounding=True)
        
        print(f"Simple Interest: {simple_interest:.4f} XLB")
        print(f"Compound Interest: {compound_interest:.4f} XLB")
    except ParkingInterestError as e:
        print(f"Error calculating interest: {e}")
```
