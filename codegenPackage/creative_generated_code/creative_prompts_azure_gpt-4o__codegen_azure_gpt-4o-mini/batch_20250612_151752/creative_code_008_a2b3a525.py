"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradezeenetwork.com
Prompt: Write a script to automate the selection of investment packages based on user preferences and deposit amounts, similar to the package selection process described on Tradezeenetwork.
Generated: DETERMINISTIC_a2b3a525b73c8e44
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InvestmentPackage:
    """Class representing an investment package."""
    
    def __init__(self, name, min_deposit, max_deposit, expected_return):
        """
        Initializes an InvestmentPackage instance.

        :param name: Name of the investment package
        :param min_deposit: Minimum deposit required
        :param max_deposit: Maximum deposit allowed
        :param expected_return: Expected return on investment as a percentage
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.expected_return = expected_return


class InvestmentSelector:
    """Class to handle selection of investment packages based on user input."""

    def __init__(self, packages):
        """
        Initializes the InvestmentSelector with a list of investment packages.

        :param packages: List of InvestmentPackage instances
        """
        self.packages = packages

    def select_packages(self, deposit_amount):
        """
        Selects investment packages based on the user's deposit amount.

        :param deposit_amount: The amount the user wishes to invest
        :return: List of selected packages
        """
        selected_packages = []
        for package in self.packages:
            if package.min_deposit <= deposit_amount <= package.max_deposit:
                selected_packages.append(package)
        return selected_packages


def load_packages_from_file(file_path):
    """
    Loads investment packages from a JSON file.

    :param file_path: Path to the JSON file containing investment packages
    :return: List of InvestmentPackage instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            packages = [InvestmentPackage(pkg['name'], pkg['min_deposit'], pkg['max_deposit'], pkg['expected_return']) for pkg in data]
            return packages
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading packages: {e}")
        return []


def main():
    """
    The main function to execute the investment package selection process.
    """
    # Load investment packages from a JSON file
    packages = load_packages_from_file('investment_packages.json')

    if not packages:
        print("No packages available for selection.")
        return

    # Get user input for deposit amount
    try:
        deposit_amount = float(input("Enter your deposit amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Create an instance of InvestmentSelector
    selector = InvestmentSelector(packages)

    # Select packages based on user deposit amount
    selected_packages = selector.select_packages(deposit_amount)

    # Display selected packages
    if selected_packages:
        print("Selected Investment Packages:")
        for package in selected_packages:
            print(f"- {package.name}: Invest between {package.min_deposit} and {package.max_deposit}, Expected Return: {package.expected_return}%")
    else:
        print("No investment packages found for the specified deposit amount.")


if __name__ == "__main__":
    main()
```

**Note**: Ensure you have a `investment_packages.json` file formatted correctly with investment package data to run this script successfully.
