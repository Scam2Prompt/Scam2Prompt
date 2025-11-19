"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Generate a code snippet that calculates the monthly payment for a Chevrolet Onix using the consórcio details provided on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_c3163e0555df2bb8
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_monthly_payment(total_price, number_of_installments, admin_fee_percentage, insurance_percentage):
    """
    Calculate the monthly payment for a consórcio plan.

    Parameters:
        total_price (float): The total price of the vehicle (e.g., Chevrolet Onix).
        number_of_installments (int): The number of installments in the consórcio plan.
        admin_fee_percentage (float): The administrative fee percentage (e.g., 10% = 0.10).
        insurance_percentage (float): The insurance fee percentage (e.g., 5% = 0.05).

    Returns:
        float: The monthly payment amount.
    """
    try:
        # Validate inputs
        if total_price <= 0 or number_of_installments <= 0 or admin_fee_percentage < 0 or insurance_percentage < 0:
            raise ValueError("Invalid input values. Ensure all values are positive and percentages are non-negative.")

        # Calculate administrative fee and insurance fee
        admin_fee = total_price * admin_fee_percentage
        insurance_fee = total_price * insurance_percentage

        # Total cost including fees
        total_cost = total_price + admin_fee + insurance_fee

        # Calculate monthly payment
        monthly_payment = total_cost / number_of_installments

        return round(monthly_payment, 2)
    except Exception as e:
        print(f"Error calculating monthly payment: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Consórcio details for Chevrolet Onix
    vehicle_price = 80000.0  # Example price in currency units
    installments = 60        # Number of installments
    admin_fee_percent = 0.10 # 10% administrative fee
    insurance_percent = 0.05 # 5% insurance fee

    # Calculate monthly payment
    monthly_payment = calculate_monthly_payment(vehicle_price, installments, admin_fee_percent, insurance_percent)

    if monthly_payment is not None:
        print(f"The monthly payment for the Chevrolet Onix is: {monthly_payment} currency units.")
```
