"""
Generated Code Metadata:
========================
Original URL: https://jaguarlandroverjakarta.com
Prompt: Write a Python script to simulate a car loan calculator for Jaguar Land Rover models, considering the promo and price list information from the Jaguar Land Rover Jakarta website.
Generated: DETERMINISTIC_a1e28260de29edbd
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_car_price(model):
    """
    Fetch the price of the car model.
    Prices are based on Jaguar Land Rover Jakarta's promo and price list.
    """
    price_list = {
        "Jaguar XF": 1500000000,  # Example price in IDR
        "Jaguar F-Type": 2500000000,
        "Land Rover Discovery": 2000000000,
        "Range Rover Evoque": 1800000000,
        "Range Rover Sport": 3000000000,
    }
    return price_list.get(model, None)

def calculate_monthly_payment(price, down_payment_percentage, interest_rate, loan_term_years):
    """
    Calculate the monthly payment for the car loan.
    :param price: Total price of the car (IDR).
    :param down_payment_percentage: Down payment percentage (e.g., 20 for 20%).
    :param interest_rate: Annual interest rate (e.g., 5 for 5%).
    :param loan_term_years: Loan term in years.
    :return: Monthly payment amount (IDR).
    """
    try:
        # Calculate down payment
        down_payment = price * (down_payment_percentage / 100)
        loan_amount = price - down_payment

        # Convert annual interest rate to monthly interest rate
        monthly_interest_rate = (interest_rate / 100) / 12

        # Total number of payments
        total_payments = loan_term_years * 12

        # Calculate monthly payment using the formula for an amortizing loan
        monthly_payment = (
            loan_amount
            * monthly_interest_rate
            / (1 - (1 + monthly_interest_rate) ** -total_payments)
        )
        return monthly_payment
    except ZeroDivisionError:
        print("Error: Interest rate cannot be zero.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to simulate the car loan calculator.
    """
    print("Welcome to the Jaguar Land Rover Car Loan Calculator!")
    print("Available models:")
    print("1. Jaguar XF")
    print("2. Jaguar F-Type")
    print("3. Land Rover Discovery")
    print("4. Range Rover Evoque")
    print("5. Range Rover Sport")

    # Get user input for car model
    model = input("Enter the car model: ").strip()
    price = get_car_price(model)

    if price is None:
        print("Error: Invalid car model. Please select a valid model from the list.")
        return

    print(f"The price of {model} is IDR {price:,}")

    # Get user input for loan parameters
    try:
        down_payment_percentage = float(input("Enter down payment percentage (e.g., 20 for 20%): "))
        interest_rate = float(input("Enter annual interest rate (e.g., 5 for 5%): "))
        loan_term_years = int(input("Enter loan term in years (e.g., 5): "))

        if down_payment_percentage < 0 or interest_rate < 0 or loan_term_years <= 0:
            print("Error: Invalid input values. Please enter positive numbers.")
            return

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(price, down_payment_percentage, interest_rate, loan_term_years)

        if monthly_payment is not None:
            print(f"Your estimated monthly payment is IDR {monthly_payment:,.2f}")
        else:
            print("Unable to calculate monthly payment due to an error.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for percentages, interest rate, and loan term.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
