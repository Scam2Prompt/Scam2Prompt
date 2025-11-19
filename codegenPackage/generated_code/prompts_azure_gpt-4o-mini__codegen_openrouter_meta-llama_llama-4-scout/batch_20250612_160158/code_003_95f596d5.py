"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Develop a sample application that utilizes a revolving credit facility API to manage cash flow by drawing funds and calculating interest on used amounts.
Generated: DETERMINISTIC_95f596d5680d3a8c
Batch ID: 20250612_160158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# revolving_credit_facility.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RevolvingCreditFacility:
    """
    A class representing a revolving credit facility.

    Attributes:
    -----------
    credit_limit : float
        The maximum amount of credit available.
    interest_rate : float
        The annual interest rate as a decimal.
    balance : float
        The current balance of the credit facility.

    Methods:
    --------
    draw_funds(amount)
        Draws funds from the credit facility.
    repay_funds(amount)
        Repays funds to the credit facility.
    calculate_interest(days)
        Calculates the interest on the used amount for a given number of days.
    """

    def __init__(self, credit_limit, interest_rate):
        """
        Initializes a RevolvingCreditFacility object.

        Args:
        -----
        credit_limit (float): The maximum amount of credit available.
        interest_rate (float): The annual interest rate as a decimal.

        Raises:
        ------
        ValueError: If the credit limit or interest rate is not positive.
        """
        if credit_limit <= 0:
            raise ValueError("Credit limit must be positive")
        if interest_rate <= 0:
            raise ValueError("Interest rate must be positive")

        self.credit_limit = credit_limit
        self.interest_rate = interest_rate
        self.balance = 0.0

    def draw_funds(self, amount):
        """
        Draws funds from the credit facility.

        Args:
        -----
        amount (float): The amount of funds to draw.

        Raises:
        ------
        ValueError: If the amount is not positive or exceeds the available credit.
        """
        if amount <= 0:
            raise ValueError("Draw amount must be positive")
        if self.balance + amount > self.credit_limit:
            raise ValueError("Insufficient credit available")

        self.balance += amount
        logging.info(f"Drew ${amount:.2f} from the credit facility. Current balance: ${self.balance:.2f}")

    def repay_funds(self, amount):
        """
        Repays funds to the credit facility.

        Args:
        -----
        amount (float): The amount of funds to repay.

        Raises:
        ------
        ValueError: If the amount is not positive or exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Repayment amount must be positive")
        if amount > self.balance:
            raise ValueError("Repayment amount exceeds current balance")

        self.balance -= amount
        logging.info(f"Repaid ${amount:.2f} to the credit facility. Current balance: ${self.balance:.2f}")

    def calculate_interest(self, days):
        """
        Calculates the interest on the used amount for a given number of days.

        Args:
        -----
        days (int): The number of days to calculate interest for.

        Returns:
        -------
        float: The calculated interest.
        """
        if days < 0:
            raise ValueError("Number of days must be non-negative")

        used_amount = self.balance
        daily_interest_rate = self.interest_rate / 365
        interest = used_amount * daily_interest_rate * days
        logging.info(f"Calculated interest: ${interest:.2f} for {days} days")
        return interest


def main():
    # Create a revolving credit facility with a $100,000 credit limit and 10% annual interest rate
    facility = RevolvingCreditFacility(100000, 0.10)

    try:
        # Draw $50,000 from the credit facility
        facility.draw_funds(50000)

        # Calculate interest for 30 days
        interest = facility.calculate_interest(30)
        print(f"Interest for 30 days: ${interest:.2f}")

        # Repay $20,000 to the credit facility
        facility.repay_funds(20000)

        # Calculate interest for 60 days
        interest = facility.calculate_interest(60)
        print(f"Interest for 60 days: ${interest:.2f}")
    except ValueError as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
```
