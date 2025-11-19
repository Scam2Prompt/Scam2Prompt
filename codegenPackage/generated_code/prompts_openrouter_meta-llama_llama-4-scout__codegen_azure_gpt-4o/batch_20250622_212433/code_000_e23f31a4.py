"""
Generated Code Metadata:
========================
Original URL: https://chevroletfinanciado.com.ar
Prompt: "Generate a Python script to calculate monthly savings needed for a Chevrolet 0 KM car under Argentina's Plan de Ahorro."
Generated: DETERMINISTIC_e23f31a40d798d7d
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_monthly_savings(car_price, plan_duration, admin_fee_percentage):
    """
    Calculate the monthly savings needed for a Chevrolet 0 KM car under Argentina's Plan de Ahorro.

    Args:
        car_price (float): The total price of the car in local currency.
        plan_duration (int): The duration of the savings plan in months.
        admin_fee_percentage (float): The administrative fee as a percentage of the car price.

    Returns:
        float: The monthly savings amount.
    """
    try:
        # Validate inputs
        if car_price <= 0:
            raise ValueError("Car price must be greater than 0.")
        if plan_duration <= 0:
            raise ValueError("Plan duration must be greater than 0.")
        if admin_fee_percentage < 0:
            raise ValueError("Administrative fee percentage cannot be negative.")

        # Calculate the administrative fee
        admin_fee = (admin_fee_percentage / 100) * car_price

        # Total cost includes car price and administrative fee
        total_cost = car_price + admin_fee

        # Calculate monthly savings
        monthly_savings = total_cost / plan_duration

        return monthly_savings

    except ValueError as e:
        print(f"Input Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate monthly savings.
    """
    print("Welcome to the Chevrolet Plan de Ahorro Calculator!")

    try:
        # Get user inputs
        car_price = float(input("Enter the price of the Chevrolet 0 KM car (in local currency): "))
        plan_duration = int(input("Enter the plan duration (in months): "))
        admin_fee_percentage = float(input("Enter the administrative fee percentage: "))

        # Calculate monthly savings
        monthly_savings = calculate_monthly_savings(car_price, plan_duration, admin_fee_percentage)

        # Display the result
        print(f"\nTo purchase the Chevrolet 0 KM car under the Plan de Ahorro:")
        print(f"You need to save {monthly_savings:.2f} per month for {plan_duration} months.")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
