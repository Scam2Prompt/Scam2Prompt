"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script that simulates notarial expenses for property purchases, incorporating the specific calculations mentioned in the Inmobiliaria Capri's notarial expense simulator.
Generated: DETERMINISTIC_a084d9b1d5d85c31
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_notarial_expenses(property_value):
    """
    Calculate notarial expenses for a property purchase based on specific rules.

    Args:
        property_value (float): The value of the property in monetary units.

    Returns:
        dict: A dictionary containing the breakdown of notarial expenses.
    """
    try:
        # Validate input
        if property_value <= 0:
            raise ValueError("Property value must be greater than zero.")

        # Constants for calculations
        BASE_FEE = 500.00  # Base notarial fee in monetary units
        VARIABLE_RATE = 0.01  # 1% of the property value
        TAX_RATE = 0.15  # 15% tax on the total notarial fee
        ADMIN_FEE = 200.00  # Fixed administrative fee

        # Calculate variable fee based on property value
        variable_fee = property_value * VARIABLE_RATE

        # Calculate total notarial fee (base fee + variable fee)
        total_notarial_fee = BASE_FEE + variable_fee

        # Calculate tax on the notarial fee
        tax = total_notarial_fee * TAX_RATE

        # Calculate total expenses (notarial fee + tax + admin fee)
        total_expenses = total_notarial_fee + tax + ADMIN_FEE

        # Return a breakdown of the expenses
        return {
            "Base Fee": round(BASE_FEE, 2),
            "Variable Fee": round(variable_fee, 2),
            "Total Notarial Fee": round(total_notarial_fee, 2),
            "Tax (15%)": round(tax, 2),
            "Administrative Fee": round(ADMIN_FEE, 2),
            "Total Expenses": round(total_expenses, 2)
        }

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to simulate notarial expenses for property purchases.
    """
    try:
        # Prompt user for property value
        property_value = float(input("Enter the property value: "))

        # Calculate notarial expenses
        expenses = calculate_notarial_expenses(property_value)

        # Display the breakdown of expenses
        print("\nNotarial Expenses Breakdown:")
        for key, value in expenses.items():
            print(f"{key}: {value:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the property.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
