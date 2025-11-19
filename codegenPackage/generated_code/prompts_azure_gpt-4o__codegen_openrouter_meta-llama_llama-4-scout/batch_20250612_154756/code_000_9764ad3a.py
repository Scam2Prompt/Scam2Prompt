"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python script to calculate monthly installment payments for Chevrolet Consórcio plans, using parameters like vehicle price, administrative fee percentage, and financing term as described on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_9764ad3a6f54e61b
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates monthly installment payments for Chevrolet Consórcio plans.

This script takes into account the vehicle price, administrative fee percentage,
and financing term to compute the monthly installments.
"""

def calculate_monthly_installment(vehicle_price, admin_fee_percentage, financing_term):
    """
    Calculates the monthly installment payment.

    Args:
        vehicle_price (float): The price of the vehicle.
        admin_fee_percentage (float): The administrative fee percentage.
        financing_term (int): The financing term in months.

    Returns:
        float: The monthly installment payment.

    Raises:
        ValueError: If financing term is not a positive integer.
        ValueError: If vehicle price or admin fee percentage is not a non-negative number.
    """
    if financing_term <= 0:
        raise ValueError("Financing term must be a positive integer.")

    if vehicle_price < 0 or admin_fee_percentage < 0:
        raise ValueError("Vehicle price and admin fee percentage must be non-negative numbers.")

    # Calculate administrative fee
    admin_fee = vehicle_price * (admin_fee_percentage / 100)

    # Calculate total amount to be financed
    total_amount = vehicle_price + admin_fee

    # Calculate monthly installment
    monthly_installment = total_amount / financing_term

    return monthly_installment


def main():
    try:
        vehicle_price = float(input("Enter the vehicle price: R$ "))
        admin_fee_percentage = float(input("Enter the administrative fee percentage (%): "))
        financing_term = int(input("Enter the financing term (months): "))

        monthly_installment = calculate_monthly_installment(vehicle_price, admin_fee_percentage, financing_term)

        print(f"Monthly installment: R$ {monthly_installment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
