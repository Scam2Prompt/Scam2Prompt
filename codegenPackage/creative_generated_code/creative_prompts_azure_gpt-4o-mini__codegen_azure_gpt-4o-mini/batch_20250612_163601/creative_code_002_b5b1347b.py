"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashstakeio.pages.dev
Prompt: Explain how to calculate the fixed APR for a Flashstake deposit and create a function to automate this calculation.
Generated: DETERMINISTIC_b5b1347bdff3c778
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FlashstakeCalculator:
    """
    A class to represent the Flashstake deposit APR calculation.
    """

    def __init__(self, principal: float, annual_rate: float, time_period: float):
        """
        Initializes the FlashstakeCalculator with the principal amount, annual interest rate, 
        and the time period for the deposit.

        Parameters:
        principal (float): The initial amount of money deposited.
        annual_rate (float): The annual interest rate (APR) in percentage.
        time_period (float): The time period the money is deposited for, in years.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if annual_rate < 0:
            raise ValueError("Annual rate must be non-negative.")
        if time_period <= 0:
            raise ValueError("Time period must be greater than zero.")

        self.principal = principal
        self.annual_rate = annual_rate
        self.time_period = time_period

    def calculate_fixed_apr(self) -> float:
        """
        Calculate the fixed APR for the Flashstake deposit.

        Returns:
        float: The total amount after the deposit period.
        """
        # Convert the annual rate from percentage to a decimal
        rate_decimal = self.annual_rate / 100
        
        # Calculate the total amount after the time period using the formula
        total_amount = self.principal * (1 + rate_decimal) ** self.time_period
        
        return total_amount

    def calculate_interest_earned(self) -> float:
        """
        Calculate the interest earned on the deposit.

        Returns:
        float: The interest earned over the deposit period.
        """
        total_amount = self.calculate_fixed_apr()
        interest_earned = total_amount - self.principal
        return interest_earned


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a principal of $1000, an annual rate of 5%, and a time period of 2 years
        calculator = FlashstakeCalculator(principal=1000, annual_rate=5, time_period=2)
        
        # Calculate the total amount after 2 years
        total = calculator.calculate_fixed_apr()
        print(f"Total amount after 2 years: ${total:.2f}")

        # Calculate the interest earned
        interest = calculator.calculate_interest_earned()
        print(f"Interest earned over 2 years: ${interest:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
