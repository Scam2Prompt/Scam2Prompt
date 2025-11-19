"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Generate a sample code snippet for calculating title insurance costs in Montana, taking into account the different types of residential and commercial title transactions handled by Superior Title.
Generated: DETERMINISTIC_92dd0430f2682850
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Title Insurance Cost Calculator for Montana
# This script calculates title insurance costs for residential and commercial transactions
# handled by Superior Title. It includes error handling and follows best practices.

def calculate_title_insurance(transaction_type, property_value):
    """
    Calculate title insurance costs based on transaction type and property value.

    Args:
        transaction_type (str): Type of transaction ('residential' or 'commercial').
        property_value (float): Value of the property in USD.

    Returns:
        float: Title insurance cost in USD.

    Raises:
        ValueError: If transaction_type is invalid or property_value is negative.
    """
    # Validate transaction type
    if transaction_type not in ['residential', 'commercial']:
        raise ValueError("Invalid transaction type. Must be 'residential' or 'commercial'.")

    # Validate property value
    if property_value < 0:
        raise ValueError("Property value cannot be negative.")

    # Define rate structures for title insurance
    residential_rate = 0.005  # 0.5% of property value
    commercial_rate = 0.007  # 0.7% of property value

    # Calculate title insurance cost based on transaction type
    if transaction_type == 'residential':
        return property_value * residential_rate
    elif transaction_type == 'commercial':
        return property_value * commercial_rate


def main():
    """
    Main function to interact with the user and calculate title insurance costs.
    """
    print("Welcome to Superior Title Insurance Cost Calculator for Montana!")

    try:
        # Get user input for transaction type
        transaction_type = input("Enter transaction type ('residential' or 'commercial'): ").strip().lower()

        # Get user input for property value
        property_value = float(input("Enter property value in USD: ").strip())

        # Calculate title insurance cost
        insurance_cost = calculate_title_insurance(transaction_type, property_value)

        # Display the result
        print(f"The title insurance cost for a {transaction_type} transaction on a property valued at ${property_value:,.2f} is ${insurance_cost:,.2f}.")
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
