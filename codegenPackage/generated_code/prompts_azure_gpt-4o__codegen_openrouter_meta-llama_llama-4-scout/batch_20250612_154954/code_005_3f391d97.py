"""
Generated Code Metadata:
========================
Original URL: https://cryptoxglobal.com
Prompt: Develop a function to calculate profits for various investment packages (Bronze, Silver, Gold, Premium, Executive) using input parameters like amount and profit percentage, as described on Cryptoexglobal.
Generated: DETERMINISTIC_3f391d9789c64c0d
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class InvestmentPackage(Enum):
    """Enum for different investment packages"""
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PREMIUM = "Premium"
    EXECUTIVE = "Executive"

class CryptoexglobalCalculator:
    """Class to calculate profits for various investment packages"""

    def __init__(self):
        # Profit percentages for each investment package
        self.profit_percentages: Dict[InvestmentPackage, float] = {
            InvestmentPackage.BRONZE: 0.05,
            InvestmentPackage.SILVER: 0.10,
            InvestmentPackage.GOLD: 0.15,
            InvestmentPackage.PREMIUM: 0.20,
            InvestmentPackage.EXECUTIVE: 0.25
        }

    def calculate_profit(self, package: InvestmentPackage, amount: float) -> float:
        """
        Calculate profit for a given investment package and amount

        Args:
        package (InvestmentPackage): The investment package
        amount (float): The investment amount

        Returns:
        float: The calculated profit

        Raises:
        ValueError: If the investment package is not valid
        TypeError: If the amount is not a positive number
        """
        if not isinstance(package, InvestmentPackage):
            raise ValueError("Invalid investment package")

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise TypeError("Amount must be a positive number")

        profit_percentage = self.profit_percentages.get(package)
        if profit_percentage is None:
            raise ValueError("Invalid investment package")

        profit = amount * profit_percentage
        return profit

    def calculate_profits(self, amount: float) -> Dict[InvestmentPackage, float]:
        """
        Calculate profits for all investment packages

        Args:
        amount (float): The investment amount

        Returns:
        Dict[InvestmentPackage, float]: A dictionary of profits for each package

        Raises:
        TypeError: If the amount is not a positive number
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise TypeError("Amount must be a positive number")

        profits = {}
        for package, profit_percentage in self.profit_percentages.items():
            profit = amount * profit_percentage
            profits[package] = profit

        return profits


def main():
    calculator = CryptoexglobalCalculator()
    amount = 1000.0

    # Calculate profit for a specific package
    package = InvestmentPackage.GOLD
    profit = calculator.calculate_profit(package, amount)
    print(f"Profit for {package.value} package: ${profit:.2f}")

    # Calculate profits for all packages
    profits = calculator.calculate_profits(amount)
    print("Profits for all packages:")
    for package, profit in profits.items():
        print(f"{package.value}: ${profit:.2f}")


if __name__ == "__main__":
    main()
```
