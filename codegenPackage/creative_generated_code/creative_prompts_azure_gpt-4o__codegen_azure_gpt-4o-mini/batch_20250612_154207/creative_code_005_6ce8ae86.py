"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qbt.finance
Prompt: Develop a Python script to calculate the estimated monthly profit for a user on Qubit Finance based on their supply and borrow balances and APR rates.
Generated: DETERMINISTIC_6ce8ae8616f13098
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class QubitFinanceProfitCalculator:
    """
    A class to calculate estimated monthly profit for a user on Qubit Finance.
    """

    def __init__(self, supply_balance: float, borrow_balance: float, supply_apr: float, borrow_apr: float):
        """
        Initializes the calculator with user balances and APRs.

        :param supply_balance: The amount supplied by the user.
        :param borrow_balance: The amount borrowed by the user.
        :param supply_apr: The Annual Percentage Rate for supplied funds (as a percentage).
        :param borrow_apr: The Annual Percentage Rate for borrowed funds (as a percentage).
        """
        self.supply_balance = self.validate_balance(supply_balance)
        self.borrow_balance = self.validate_balance(borrow_balance)
        self.supply_apr = self.validate_apr(supply_apr)
        self.borrow_apr = self.validate_apr(borrow_apr)

    @staticmethod
    def validate_balance(balance: float) -> float:
        """
        Validates the balance to ensure it is not negative.

        :param balance: The balance to validate.
        :return: The validated balance.
        :raises ValueError: If the balance is negative.
        """
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        return balance

    @staticmethod
    def validate_apr(apr: float) -> float:
        """
        Validates the APR to ensure it is non-negative.

        :param apr: The APR to validate (as a percentage).
        :return: The validated APR.
        :raises ValueError: If the APR is negative.
        """
        if apr < 0:
            raise ValueError("APR cannot be negative.")
        return apr

    def calculate_monthly_profit(self) -> float:
        """
        Calculates the estimated monthly profit based on supply and borrow balances and APRs.

        :return: The estimated monthly profit.
        """
        monthly_supply_profit = (self.supply_balance * (self.supply_apr / 100)) / 12
        monthly_borrow_cost = (self.borrow_balance * (self.borrow_apr / 100)) / 12
        monthly_profit = monthly_supply_profit - monthly_borrow_cost
        return monthly_profit

# Example usage:
if __name__ == "__main__":
    try:
        supply_balance = 1000.0  # Example supply balance
        borrow_balance = 500.0    # Example borrow balance
        supply_apr = 5.0          # Example supply APR (5%)
        borrow_apr = 3.0          # Example borrow APR (3%)

        calculator = QubitFinanceProfitCalculator(supply_balance, borrow_balance, supply_apr, borrow_apr)
        estimated_profit = calculator.calculate_monthly_profit()
        print(f"Estimated monthly profit: ${estimated_profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
