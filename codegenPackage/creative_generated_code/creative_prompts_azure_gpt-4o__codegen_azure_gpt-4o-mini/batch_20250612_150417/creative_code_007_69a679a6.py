"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passiveinvestincome.com
Prompt: Create a Python script to calculate the total earnings for investors based on PassiveInvestIncome's investment plans, including parameters like "capital will back" and "duration lifetime."
Generated: DETERMINISTIC_69a679a682751e63
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        capital (float): The initial capital invested.
        interest_rate (float): The annual interest rate as a percentage.
        duration (int): The duration of the investment in years.
    """

    def __init__(self, capital: float, interest_rate: float, duration: int):
        """
        Initializes the InvestmentPlan with capital, interest rate, and duration.

        Args:
            capital (float): The initial capital invested.
            interest_rate (float): The annual interest rate as a percentage.
            duration (int): The duration of the investment in years.
        """
        if capital <= 0:
            logging.error("Capital must be greater than 0.")
            raise ValueError("Capital must be greater than 0.")
        if interest_rate < 0:
            logging.error("Interest rate cannot be negative.")
            raise ValueError("Interest rate cannot be negative.")
        if duration <= 0:
            logging.error("Duration must be greater than 0.")
            raise ValueError("Duration must be greater than 0.")

        self.capital = capital
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.duration = duration

    def calculate_earnings(self) -> float:
        """
        Calculates the total earnings from the investment.

        Returns:
            float: Total earnings after the investment duration.
        """
        earnings = self.capital * (1 + self.interest_rate) ** self.duration
        logging.info(f"Calculated earnings: {earnings}")
        return earnings

def main():
    """
    Main function to execute the investment earnings calculation.
    """
    try:
        # Example parameters
        capital = 10000  # Example capital
        interest_rate = 5  # Example interest rate (5%)
        duration = 10  # Example duration (10 years)

        # Create an investment plan instance
        investment_plan = InvestmentPlan(capital, interest_rate, duration)

        # Calculate total earnings
        total_earnings = investment_plan.calculate_earnings()
        logging.info(f"Total earnings after {duration} years: {total_earnings:.2f}")

    except ValueError as e:
        logging.error(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
