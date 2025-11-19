"""
Generated Code Metadata:
========================
Original URL: https://alphapremiertrd.com
Prompt: "Create a simple investment plan calculator using a programming language of your choice, considering daily returns and deposit limits similar to Alpha Premier Trade's investment plans."
Generated: DETERMINISTIC_4ddbad495cc3866d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investment Plan Calculator
This script calculates the projected returns for an investment plan similar to Alpha Premier Trade's plans.
It considers daily returns, deposit limits, and compounding over a specified period.
"""

import sys
from typing import Optional

class InvestmentCalculator:
    """
    A class to calculate investment returns based on daily percentage returns and deposit limits.
    
    Attributes:
        daily_return_rate (float): Daily return rate as a percentage (e.g., 1.5 for 1.5%)
        min_deposit (float): Minimum allowed deposit amount
        max_deposit (float): Maximum allowed deposit amount
        investment_duration (int): Duration of investment in days
    """
    
    def __init__(self, daily_return_rate: float, min_deposit: float, max_deposit: float):
        """
        Initialize the InvestmentCalculator with given parameters.
        
        Args:
            daily_return_rate: Daily return rate percentage (e.g., 1.5 for 1.5%)
            min_deposit: Minimum allowed deposit amount
            max_deposit: Maximum allowed deposit amount
            
        Raises:
            ValueError: If any parameter is invalid
        """
        if daily_return_rate <= 0:
            raise ValueError("Daily return rate must be positive")
        if min_deposit <= 0:
            raise ValueError("Minimum deposit must be positive")
        if max_deposit <= min_deposit:
            raise ValueError("Maximum deposit must be greater than minimum deposit")
            
        self.daily_return_rate = daily_return_rate / 100  # Convert to decimal
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
    
    def calculate_returns(self, principal: float, duration_days: int) -> Optional[float]:
        """
        Calculate the projected returns for the investment.
        
        Args:
            principal: Initial investment amount
            duration_days: Investment duration in days
            
        Returns:
            The total projected returns or None if principal is outside limits
            
        Raises:
            ValueError: If duration_days is not positive
        """
        if duration_days <= 0:
            raise ValueError("Investment duration must be positive")
            
        if principal < self.min_deposit or principal > self.max_deposit:
            return None
            
        return principal * (1 + self.daily_return_rate) ** duration_days

def main():
    """Main function to run the investment calculator interactively."""
    print("Investment Plan Calculator")
    print("--------------------------")
    
    try:
        # Get user input with validation
        daily_rate = float(input("Enter daily return rate (%): "))
        min_deposit = float(input("Enter minimum deposit amount: "))
        max_deposit = float(input("Enter maximum deposit amount: "))
        
        calculator = InvestmentCalculator(daily_rate, min_deposit, max_deposit)
        
        principal = float(input("\nEnter your investment amount: "))
        duration = int(input("Enter investment duration (days): "))
        
        result = calculator.calculate_returns(principal, duration)
        
        if result is None:
            print(f"\nError: Investment amount must be between ${calculator.min_deposit:,.2f} "
                  f"and ${calculator.max_deposit:,.2f}")
        else:
            print(f"\nProjected return after {duration} days:")
            print(f"Initial investment: ${principal:,.2f}")
            print(f"Total return: ${result:,.2f}")
            print(f"Profit: ${result - principal:,.2f}")
            print(f"Daily return: ${principal * calculator.daily_return_rate:,.2f}")
            
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
```
