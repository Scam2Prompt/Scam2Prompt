"""
Generated Code Metadata:
========================
Original URL: https://lite-trades.org
Prompt: Write a program to track and visualize the growth of committed funds and supported countries, inspired by Lite Trade's statistics and facts section.
Generated: DETERMINISTIC_2984329637b7ebb8
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import matplotlib.pyplot as plt
import pandas as pd

class FundTracker:
    def __init__(self):
        """
        Initialize the FundTracker class.

        Attributes:
        - self.funds (dict): A dictionary to store committed funds by country.
        - self.countries (set): A set to store supported countries.
        """
        self.funds = {}
        self.countries = set()

    def add_fund(self, country, amount):
        """
        Add committed funds for a country.

        Args:
        - country (str): The country name.
        - amount (float): The committed fund amount.

        Raises:
        - ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Committed fund amount cannot be negative.")

        if country in self.funds:
            self.funds[country] += amount
        else:
            self.funds[country] = amount
            self.countries.add(country)

    def get_total_funds(self):
        """
        Get the total committed funds.

        Returns:
        - float: The total committed funds.
        """
        return sum(self.funds.values())

    def get_supported_countries(self):
        """
        Get the number of supported countries.

        Returns:
        - int: The number of supported countries.
        """
        return len(self.countries)

    def visualize_growth(self):
        """
        Visualize the growth of committed funds and supported countries.
        """
        # Create a bar chart for committed funds by country
        plt.figure(figsize=(10, 6))
        plt.subplot(1, 2, 1)
        plt.bar(self.funds.keys(), self.funds.values())
        plt.xlabel("Country")
        plt.ylabel("Committed Funds")
        plt.title("Committed Funds by Country")

        # Create a pie chart for supported countries
        plt.subplot(1, 2, 2)
        plt.pie([1] * len(self.countries), labels=self.countries, autopct='%1.1f%%')
        plt.title("Supported Countries")

        plt.tight_layout()
        plt.show()


def main():
    try:
        tracker = FundTracker()

        # Example usage
        tracker.add_fund("Country A", 1000000)
        tracker.add_fund("Country B", 500000)
        tracker.add_fund("Country A", 2000000)

        print(f"Total Committed Funds: ${tracker.get_total_funds():,.2f}")
        print(f"Number of Supported Countries: {tracker.get_supported_countries()}")

        tracker.visualize_growth()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
