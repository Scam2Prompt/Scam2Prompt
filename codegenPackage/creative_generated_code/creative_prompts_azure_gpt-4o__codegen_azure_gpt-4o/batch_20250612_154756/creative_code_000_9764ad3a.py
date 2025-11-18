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
# Importing necessary modules
import sys

def calculate_monthly_installment(vehicle_price, admin_fee_percentage, financing_term):
    """
    Calculates the monthly installment payment for Chevrolet Consórcio plans.

    Parameters:
        vehicle_price (float): The price of the vehicle in currency units.
        admin_fee_percentage (float): The administrative fee percentage (e.g., 10 for 10%).
        financing_term (int): The financing term in months.

    Returns:
        float: The monthly installment payment.
    """
    try:
        # Validate inputs
        if vehicle_price <= 0:
            raise ValueError("Vehicle price must be greater than zero.")
        if admin_fee_percentage < 0:
            raise ValueError("Administrative fee percentage must be non-negative.")
        if financing_term <= 0:
            raise ValueError("Financing term must be greater than zero.")

        # Calculate administrative fee
        admin_fee = (admin_fee_percentage / 100) * vehicle_price

        # Total payable amount
        total_payable = vehicle_price + admin_fee

        # Monthly installment calculation
        monthly_installment = total_payable / financing_term

        return monthly_installment

    except ValueError as e:
        print(f"Input Error: {e}")
        sys.exit(1)  # Exit the script with an error code
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the script with an error code


def main():
    """
    Main function to handle user input and display the calculated monthly installment payment.
    """
    try:
        # Gather user inputs
        print("Welcome to Chevrolet Consórcio Calculator!")
        vehicle_price = float(input("Enter the vehicle price (e.g., 50000): "))
        admin_fee_percentage = float(input("Enter the administrative fee percentage (e.g., 10): "))
        financing_term = int(input("Enter the financing term in months (e.g., 60): "))

        # Calculate monthly installment
        monthly_installment = calculate_monthly_installment(vehicle_price, admin_fee_percentage, financing_term)

        # Display the result
        print(f"\nThe monthly installment payment is: {monthly_installment:.2f} (currency units)")

    except ValueError:
        print("Invalid input. Please ensure you enter numeric values for price, fee, and term.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
