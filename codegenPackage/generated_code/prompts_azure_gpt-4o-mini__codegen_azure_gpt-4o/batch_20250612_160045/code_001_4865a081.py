"""
Generated Code Metadata:
========================
Original URL: https://vejanoticiabrasil.online
Prompt: Write a Python script that calculates the total cost of an imported item, including customs taxes and postal fees, based on the new regulations mentioned in the article.
Generated: DETERMINISTIC_4865a081c5bb6efc
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_total_cost(item_cost, customs_tax_rate, postal_fee):
    """
    Calculate the total cost of an imported item, including customs taxes and postal fees.

    Parameters:
        item_cost (float): The base cost of the item.
        customs_tax_rate (float): The customs tax rate as a percentage (e.g., 10 for 10%).
        postal_fee (float): The fixed postal fee.

    Returns:
        float: The total cost of the imported item.
    """
    try:
        # Validate inputs
        if item_cost < 0 or customs_tax_rate < 0 or postal_fee < 0:
            raise ValueError("Item cost, customs tax rate, and postal fee must be non-negative.")

        # Calculate customs tax
        customs_tax = (customs_tax_rate / 100) * item_cost

        # Calculate total cost
        total_cost = item_cost + customs_tax + postal_fee

        return total_cost
    except TypeError:
        raise TypeError("Invalid input type. Ensure item_cost, customs_tax_rate, and postal_fee are numbers.")
    except ValueError as ve:
        raise ValueError(f"Input error: {ve}")

def main():
    """
    Main function to interact with the user and calculate the total cost of an imported item.
    """
    try:
        # Prompt user for inputs
        print("Welcome to the Imported Item Cost Calculator!")
        item_cost = float(input("Enter the base cost of the item: "))
        customs_tax_rate = float(input("Enter the customs tax rate (as a percentage): "))
        postal_fee = float(input("Enter the fixed postal fee: "))

        # Calculate total cost
        total_cost = calculate_total_cost(item_cost, customs_tax_rate, postal_fee)

        # Display the result
        print(f"The total cost of the imported item is: ${total_cost:.2f}")
    except ValueError:
        print("Error: Please enter valid numeric values for all inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
