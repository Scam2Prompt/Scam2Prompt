"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Create a Python script to calculate the total cooking capacity (in kg) for a combination of Caja China, Cilindro, and Parrilla products purchased from Meat Master.
Generated: DETERMINISTIC_643aed0a83a08320
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_total_cooking_capacity(products):
    """
    Calculate the total cooking capacity (in kg) based on the products purchased.

    :param products: Dictionary containing product names and their quantities.
                     Example: {'Caja China': 2, 'Cilindro': 1, 'Parrilla': 3}
    :return: Total cooking capacity in kilograms.
    """
    # Define cooking capacities for each product type in kg
    COOKING_CAPACITY = {
        'Caja China': 50,  # Capacity of a single Caja China in kg
        'Cilindro': 30,    # Capacity of a single Cilindro in kg
        'Parrilla': 10     # Capacity of a single Parrilla in kg
    }

    total_capacity = 0

    # Calculate the total capacity based on quantities of products purchased
    for product, quantity in products.items():
        if product in COOKING_CAPACITY:
            total_capacity += COOKING_CAPACITY[product] * quantity
        else:
            # Handle unknown products gracefully
            print(f"Warning: Unknown product '{product}' encountered. Skipping...")
    
    return total_capacity

def main():
    """
    Main function to execute the script.
    """
    print("Welcome to Meat Master Cooking Capacity Calculator!\n")

    try:
        # Sample input for demonstration purposes
        # Replace this with actual input retrieval logic (e.g., from a database, API, or user input)
        products = {
            'Caja China': 2,
            'Cilindro': 1,
            'Parrilla': 3
        }

        # Display the products purchased
        print("Products Purchased:")
        for product, quantity in products.items():
            print(f"{product}: {quantity} unit(s)")

        # Calculate and display total cooking capacity
        total_capacity = calculate_total_cooking_capacity(products)
        print(f"\nTotal Cooking Capacity: {total_capacity} kg")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
