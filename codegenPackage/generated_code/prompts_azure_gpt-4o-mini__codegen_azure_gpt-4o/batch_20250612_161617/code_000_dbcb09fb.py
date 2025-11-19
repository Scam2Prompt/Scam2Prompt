"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Generate a Python script that calculates the potential return on investment for properties in the $2 million to $20 million range, as described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dbcb09fbf4bae916
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_roi(property_price, annual_rent, annual_expenses):
    """
    Calculate the Return on Investment (ROI) for a property.

    ROI = (Annual Net Income / Property Price) * 100

    :param property_price: float, the price of the property in dollars
    :param annual_rent: float, the total annual rent income in dollars
    :param annual_expenses: float, the total annual expenses in dollars
    :return: float, the ROI percentage
    """
    try:
        # Validate inputs
        if property_price <= 0:
            raise ValueError("Property price must be greater than zero.")
        if annual_rent < 0 or annual_expenses < 0:
            raise ValueError("Annual rent and expenses must be non-negative.")

        # Calculate annual net income
        annual_net_income = annual_rent - annual_expenses

        # Calculate ROI
        roi = (annual_net_income / property_price) * 100
        return roi
    except ZeroDivisionError:
        raise ValueError("Property price cannot be zero.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating ROI: {e}")


def main():
    """
    Main function to calculate ROI for properties in the $2M to $20M range.
    """
    print("Welcome to the Rosebud Holdings Property Income REIT ROI Calculator!")

    try:
        # Get user input for property price, annual rent, and annual expenses
        property_price = float(input("Enter the property price (in dollars): "))
        if property_price < 2_000_000 or property_price > 20_000_000:
            print("Error: Property price must be between $2,000,000 and $20,000,000.")
            sys.exit(1)

        annual_rent = float(input("Enter the total annual rent income (in dollars): "))
        annual_expenses = float(input("Enter the total annual expenses (in dollars): "))

        # Calculate ROI
        roi = calculate_roi(property_price, annual_rent, annual_expenses)

        # Display the result
        print(f"\nThe ROI for the property is: {roi:.2f}%")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the ROI Calculator. Goodbye!")


if __name__ == "__main__":
    main()
```
