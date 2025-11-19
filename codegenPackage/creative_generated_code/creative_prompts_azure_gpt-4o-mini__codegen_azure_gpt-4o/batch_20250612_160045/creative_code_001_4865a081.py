"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vejanoticiabrasil.online
Prompt: Write a Python script that calculates the total cost of an imported item, including customs taxes and postal fees, based on the new regulations mentioned in the article.
Generated: DETERMINISTIC_4865a081c5bb6efc
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(item_cost, import_tax_rate, postal_fee):
    """
    Calculate the total cost of an imported item, including customs taxes and postal fees.

    Parameters:
        item_cost (float): The base cost of the item in the local currency.
        import_tax_rate (float): The import tax rate as a percentage (e.g., 15 for 15%).
        postal_fee (float): The fixed postal fee for delivery in the local currency.

    Returns:
        float: The total cost, including taxes and fees.
    """
    try:
        # Validate input values
        if item_cost < 0 or import_tax_rate < 0 or postal_fee < 0:
            raise ValueError("Item cost, import tax rate, and postal fee must be non-negative values.")
        
        # Calculate import tax
        import_tax = (import_tax_rate / 100) * item_cost
        
        # Calculate total cost
        total_cost = item_cost + import_tax + postal_fee
        return total_cost
    except TypeError as e:
        raise ValueError("Invalid input type. All parameters must be numbers.") from e


def main():
    """
    Main function to execute the script. Prompts the user for input and calculates the total cost.
    """
    print("Welcome to the Total Cost Calculator for Imported Items!")
    try:
        # Get user input
        item_cost = float(input("Enter the base cost of the item: "))
        import_tax_rate = float(input("Enter the import tax rate (as a percentage): "))
        postal_fee = float(input("Enter the postal fee: "))
        
        # Calculate total cost
        total_cost = calculate_total_cost(item_cost, import_tax_rate, postal_fee)
        
        # Display the result
        print(f"The total cost of the imported item is: {total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry-point for the script
    main()
```
