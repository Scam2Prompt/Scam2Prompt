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
# Import required libraries
import math

def calculate_monthly_savings(vehicle_price, plan_duration_in_months, down_payment=0, residual_value=0):
    """
    Calculate the monthly savings needed for a vehicle under a plan de ahorro.

    Args:
        vehicle_price (float): The price of the vehicle.
        plan_duration_in_months (int): The duration of the plan in months.
        down_payment (float, optional): The down payment made. Defaults to 0.
        residual_value (float, optional): The residual value of the vehicle at the end of the plan. Defaults to 0.

    Returns:
        float: The monthly savings needed.
    """
    # Calculate the total amount to be financed
    financed_amount = vehicle_price - down_payment - residual_value
    
    # Check if the financed amount is valid
    if financed_amount <= 0:
        raise ValueError("Financed amount must be greater than zero.")

    # Calculate the monthly savings
    monthly_savings = financed_amount / plan_duration_in_months

    return monthly_savings

def calculate_monthly_savings_with_interest(vehicle_price, plan_duration_in_months, down_payment=0, residual_value=0, annual_interest_rate=0):
    """
    Calculate the monthly savings needed for a vehicle under a plan de ahorro with interest.

    Args:
        vehicle_price (float): The price of the vehicle.
        plan_duration_in_months (int): The duration of the plan in months.
        down_payment (float, optional): The down payment made. Defaults to 0.
        residual_value (float, optional): The residual value of the vehicle at the end of the plan. Defaults to 0.
        annual_interest_rate (float, optional): The annual interest rate. Defaults to 0.

    Returns:
        float: The monthly savings needed.
    """
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate the total amount to be financed
    financed_amount = vehicle_price - down_payment - residual_value
    
    # Check if the financed amount is valid
    if financed_amount <= 0:
        raise ValueError("Financed amount must be greater than zero.")

    # Calculate the monthly savings using the formula for monthly payments (M) on a fixed rate loan: M = P[r(1+r)^n]/[(1+r)^n – 1]
    monthly_savings = financed_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** plan_duration_in_months) / ((1 + monthly_interest_rate) ** plan_duration_in_months - 1)

    return monthly_savings

def main():
    try:
        # Input parameters
        vehicle_price = 400000  # 0 KM Chevrolet vehicle price
        plan_duration_in_months = 60  # 5-year plan
        down_payment = 80000  # 20% down payment
        residual_value = 80000  # 20% residual value
        annual_interest_rate = 20  # 20% annual interest rate

        # Calculate monthly savings without interest
        monthly_savings_without_interest = calculate_monthly_savings(vehicle_price, plan_duration_in_months, down_payment, residual_value)
        print(f"Monthly savings without interest: ${monthly_savings_without_interest:.2f}")

        # Calculate monthly savings with interest
        monthly_savings_with_interest = calculate_monthly_savings_with_interest(vehicle_price, plan_duration_in_months, down_payment, residual_value, annual_interest_rate)
        print(f"Monthly savings with {annual_interest_rate}% annual interest: ${monthly_savings_with_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
