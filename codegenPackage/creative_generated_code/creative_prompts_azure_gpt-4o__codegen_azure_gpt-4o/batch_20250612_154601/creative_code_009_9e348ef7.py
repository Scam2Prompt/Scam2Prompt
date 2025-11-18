"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Develop a script to automate the process of managing real estate investments, similar to Astragoldbitx.org's approach to real estate portfolio management.
Generated: DETERMINISTIC_9e348ef733d448d2
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of Python code for automating the process of managing real estate investments:

```python
"""
Automated Real Estate Portfolio Management Script

This script allows users to manage their real estate investments by tracking property details,
calculating ROI (Return on Investment), and generating portfolio reports.
"""

import json
import sys


class RealEstateProperty:
    """
    Represents a single real estate property in the portfolio.
    """

    def __init__(self, name, purchase_price, rental_income, expenses):
        """
        Initializes a property with the given details.

        :param name: Name or identifier of the property.
        :param purchase_price: Initial purchase price of the property.
        :param rental_income: Monthly rental income from the property.
        :param expenses: Monthly expenses associated with the property.
        """
        self.name = name
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses

    def calculate_annual_roi(self):
        """
        Calculates the annual ROI (Return on Investment) for the property.

        :return: Annual ROI as a percentage.
        """
        annual_cash_flow = (self.rental_income - self.expenses) * 12
        try:
            roi = (annual_cash_flow / self.purchase_price) * 100
        except ZeroDivisionError:
            roi = 0
        return round(roi, 2)


class RealEstatePortfolio:
    """
    Manages a portfolio of real estate properties.
    """

    def __init__(self):
        """
        Initializes an empty portfolio.
        """
        self.properties = []

    def add_property(self, property):
        """
        Adds a property to the portfolio.

        :param property: An instance of RealEstateProperty.
        """
        self.properties.append(property)

    def remove_property(self, name):
        """
        Removes a property from the portfolio by its name.

        :param name: Name of the property to remove.
        """
        self.properties = [prop for prop in self.properties if prop.name != name]

    def generate_report(self):
        """
        Generates a report summarizing the portfolio.

        :return: A dictionary containing portfolio details and ROI for each property.
        """
        report = {"properties": []}
        for property in self.properties:
            report["properties"].append({
                "name": property.name,
                "purchase_price": property.purchase_price,
                "rental_income": property.rental_income,
                "expenses": property.expenses,
                "annual_roi": property.calculate_annual_roi()
            })
        return report


def save_report_to_file(report, filename="portfolio_report.json"):
    """
    Saves the portfolio report to a JSON file.

    :param report: The portfolio report dictionary.
    :param filename: Name of the file to save the report.
    """
    try:
        with open(filename, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Portfolio report saved to {filename}")
    except Exception as e:
        print(f"Error saving report: {e}")


def main():
    """
    Main function to interactively manage the real estate portfolio.
    """
    portfolio = RealEstatePortfolio()

    while True:
        print("\nReal Estate Portfolio Management")
        print("1. Add Property")
        print("2. Remove Property")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                name = input("Enter property name: ")
                purchase_price = float(input("Enter purchase price: "))
                rental_income = float(input("Enter monthly rental income: "))
                expenses = float(input("Enter monthly expenses: "))
                property = RealEstateProperty(name, purchase_price, rental_income, expenses)
                portfolio.add_property(property)
                print(f"Property '{name}' added successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric values for price, income, and expenses.")

        elif choice == "2":
            name = input("Enter the name of the property to remove: ")
            portfolio.remove_property(name)
            print(f"Property '{name}' removed successfully.")

        elif choice == "3":
            report = portfolio.generate_report()
            save_report_to_file(report)
            print(json.dumps(report, indent=4))

        elif choice == "4":
            print("Exiting portfolio management.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
