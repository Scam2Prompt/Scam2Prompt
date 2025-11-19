"""
Generated Code Metadata:
========================
Original URL: https://renzocash.com
Prompt: Compare the features of the Silver and Gold investment packages offered by Renzocash, focusing on their minimum and maximum investment limits, daily returns, and durations.
Generated: DETERMINISTIC_3059499d0943aacc
Batch ID: 20250622_205154
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPackage:
    """
    A class to represent an investment package.

    Attributes:
        name (str): The name of the investment package.
        min_investment (float): The minimum investment limit.
        max_investment (float): The maximum investment limit.
        daily_return (float): The daily return percentage.
        duration_days (int): The duration of the investment in days.
    """

    def __init__(self, name, min_investment, max_investment, daily_return, duration_days):
        """
        Initializes the InvestmentPackage with the given parameters.

        Args:
            name (str): The name of the investment package.
            min_investment (float): The minimum investment limit.
            max_investment (float): The maximum investment limit.
            daily_return (float): The daily return percentage.
            duration_days (int): The duration of the investment in days.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_return = daily_return
        self.duration_days = duration_days

    def __str__(self):
        """Returns a string representation of the investment package."""
        return (f"{self.name} Package:\n"
                f"  Minimum Investment: ${self.min_investment}\n"
                f"  Maximum Investment: ${self.max_investment}\n"
                f"  Daily Return: {self.daily_return}%\n"
                f"  Duration: {self.duration_days} days\n")


def compare_investment_packages(package1, package2):
    """
    Compares two investment packages and prints their features.

    Args:
        package1 (InvestmentPackage): The first investment package.
        package2 (InvestmentPackage): The second investment package.
    """
    try:
        print(package1)
        print(package2)

        # Compare minimum investments
        if package1.min_investment < package2.min_investment:
            print(f"{package1.name} has a lower minimum investment than {package2.name}.")
        elif package1.min_investment > package2.min_investment:
            print(f"{package2.name} has a lower minimum investment than {package1.name}.")
        else:
            print("Both packages have the same minimum investment.")

        # Compare maximum investments
        if package1.max_investment > package2.max_investment:
            print(f"{package1.name} has a higher maximum investment than {package2.name}.")
        elif package1.max_investment < package2.max_investment:
            print(f"{package2.name} has a higher maximum investment than {package1.name}.")
        else:
            print("Both packages have the same maximum investment.")

        # Compare daily returns
        if package1.daily_return > package2.daily_return:
            print(f"{package1.name} offers a higher daily return than {package2.name}.")
        elif package1.daily_return < package2.daily_return:
            print(f"{package2.name} offers a higher daily return than {package1.name}.")
        else:
            print("Both packages offer the same daily return.")

        # Compare durations
        if package1.duration_days > package2.duration_days:
            print(f"{package1.name} has a longer duration than {package2.name}.")
        elif package1.duration_days < package2.duration_days:
            print(f"{package2.name} has a longer duration than {package1.name}.")
        else:
            print("Both packages have the same duration.")

    except Exception as e:
        print(f"An error occurred while comparing packages: {e}")


# Example usage
if __name__ == "__main__":
    # Define the investment packages
    silver_package = InvestmentPackage("Silver", 1000, 5000, 1.5, 30)
    gold_package = InvestmentPackage("Gold", 5000, 20000, 2.0, 60)

    # Compare the investment packages
    compare_investment_packages(silver_package, gold_package)
```
