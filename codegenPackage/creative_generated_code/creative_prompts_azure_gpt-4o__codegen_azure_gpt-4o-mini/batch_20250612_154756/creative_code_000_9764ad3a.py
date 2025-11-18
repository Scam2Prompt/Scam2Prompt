"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python script to calculate monthly installment payments for Chevrolet Consórcio plans, using parameters like vehicle price, administrative fee percentage, and financing term as described on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_9764ad3a6f54e61b
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Chevrolet Consórcio Monthly Installment Calculator

This script calculates the monthly installment payments for Chevrolet Consórcio plans
based on the vehicle price, administrative fee percentage, and financing term.
"""

def calculate_monthly_installment(vehicle_price, admin_fee_percentage, financing_term_months):
    """
    Calculate the monthly installment for a Chevrolet Consórcio plan.

    Parameters:
    vehicle_price (float): The total price of the vehicle.
    admin_fee_percentage (float): The administrative fee percentage applied to the total price.
    financing_term_months (int): The financing term in months.

    Returns:
    float: The calculated monthly installment.
    """
    
    # Validate input parameters
    if vehicle_price <= 0:
        raise ValueError("Vehicle price must be greater than zero.")
    if admin_fee_percentage < 0:
        raise ValueError("Administrative fee percentage cannot be negative.")
    if financing_term_months <= 0:
        raise ValueError("Financing term must be greater than zero.")
    
    # Calculate administrative fee
    admin_fee = (admin_fee_percentage / 100) * vehicle_price
    
    # Total amount financed
    total_amount = vehicle_price + admin_fee
    
    # Calculate monthly installment
    monthly_installment = total_amount / financing_term_months
    
    return monthly_installment


def main():
    """
    Main function to execute the monthly installment calculation.
    """
    try:
        # Example input values
        vehicle_price = float(input("Enter the vehicle price: "))
        admin_fee_percentage = float(input("Enter the administrative fee percentage: "))
        financing_term_months = int(input("Enter the financing term in months: "))
        
        # Calculate monthly installment
        installment = calculate_monthly_installment(vehicle_price, admin_fee_percentage, financing_term_months)
        
        # Display the result
        print(f"The monthly installment is: {installment:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
