"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: Write a Python script to simulate cryptocurrency staking returns based on the investment packages offered by MFX-Online Trade, including parameters like minimum deposit, maximum deposit, and return percentages.
Generated: DETERMINISTIC_02fad961ec045a92
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPackage:
    """Class representing an investment package for staking returns."""

    def __init__(self, name, min_deposit, max_deposit, return_percentage):
        """
        Initialize an investment package.

        :param name: Name of the investment package
        :param min_deposit: Minimum deposit required for the package
        :param max_deposit: Maximum deposit allowed for the package
        :param return_percentage: Return percentage offered by the package
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.return_percentage = return_percentage

    def calculate_return(self, deposit_amount):
        """
        Calculate the return based on the deposit amount.

        :param deposit_amount: Amount deposited
        :return: The total return on investment
        """
        if deposit_amount < self.min_deposit or deposit_amount > self.max_deposit:
            raise ValueError(f"Deposit amount must be between {self.min_deposit} and {self.max_deposit}.")

        return deposit_amount * (self.return_percentage / 100)


class StakingSimulator:
    """Class to simulate staking returns based on investment packages."""

    def __init__(self):
        """Initialize the staking simulator with predefined investment packages."""
        self.packages = [
            InvestmentPackage("Basic", 100, 1000, 5),
            InvestmentPackage("Standard", 1001, 5000, 7),
            InvestmentPackage("Premium", 5001, 20000, 10),
        ]

    def display_packages(self):
        """Display available investment packages."""
        print("Available Investment Packages:")
        for package in self.packages:
            print(f"{package.name}: Min Deposit: {package.min_deposit}, Max Deposit: {package.max_deposit}, Return: {package.return_percentage}%")

    def simulate_staking(self, package_name, deposit_amount):
        """
        Simulate the staking process.

        :param package_name: Name of the investment package
        :param deposit_amount: Amount to deposit
        :return: None
        """
        try:
            # Find the investment package by name
            package = next(pkg for pkg in self.packages if pkg.name.lower() == package_name.lower())
            total_return = package.calculate_return(deposit_amount)
            print(f"Total return on investment for {deposit_amount} in {package.name} package: {total_return}")
        except StopIteration:
            print("Error: Investment package not found.")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """Main function to run the staking simulator."""
    simulator = StakingSimulator()
    simulator.display_packages()

    # Example input for testing
    try:
        package_name = input("Enter the investment package name: ").strip()
        deposit_amount = float(input("Enter the deposit amount: "))
        simulator.simulate_staking(package_name, deposit_amount)
    except ValueError:
        print("Error: Please enter a valid number for the deposit amount.")


if __name__ == "__main__":
    main()
```
