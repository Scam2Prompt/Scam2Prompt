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

def calculate_monthly_savings(total_price, down_payment_percentage, months):
    """
    Calculate the monthly savings needed for a car purchase under Argentina's Plan de Ahorro.

    Parameters:
    total_price (float): The total price of the car.
    down_payment_percentage (float): The percentage of the total price to be paid as a down payment.
    months (int): The number of months over which to save.

    Returns:
    float: The amount to save each month.
    """
    try:
        # Validate inputs
        if total_price <= 0:
            raise ValueError("Total price must be greater than zero.")
        if not (0 <= down_payment_percentage <= 100):
            raise ValueError("Down payment percentage must be between 0 and 100.")
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")

        # Calculate down payment
        down_payment = (down_payment_percentage / 100) * total_price
        
        # Calculate the remaining amount to be financed
        remaining_amount = total_price - down_payment
        
        # Calculate monthly savings needed
        monthly_savings = remaining_amount / months
        
        return monthly_savings

    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the savings calculation.
    """
    # Example values for the calculation
    total_price = 3000000  # Total price of the car in Argentine Pesos
    down_payment_percentage = 20  # Down payment percentage
    months = 24  # Number of months to save

    # Calculate monthly savings
    monthly_savings = calculate_monthly_savings(total_price, down_payment_percentage, months)

    # Output the result
    print(f"Monthly savings needed: ARS {monthly_savings:.2f}")

if __name__ == "__main__":
    main()
```
