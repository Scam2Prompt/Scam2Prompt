"""
Generated Code Metadata:
========================
Original URL: https://ortopedic.cl
Prompt: Generate a Python script to calculate the total cost of purchasing multiple medical supplies like syringes, nebulizers, and orthopedic aids from C&D Ortopedic.
Generated: DETERMINISTIC_1aacfaba0eef3893
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_total_cost(items):
    """
    Calculate the total cost of purchasing medical supplies.

    Args:
        items (list of dict): A list of dictionaries where each dictionary represents
                              an item with 'name', 'quantity', and 'price_per_unit'.

    Returns:
        float: The total cost of all items.
    """
    try:
        total_cost = 0.0
        for item in items:
            # Validate item structure
            if not all(key in item for key in ['name', 'quantity', 'price_per_unit']):
                raise ValueError(f"Invalid item structure: {item}")
            
            # Validate quantity and price_per_unit are numbers
            if not isinstance(item['quantity'], (int, float)) or not isinstance(item['price_per_unit'], (int, float)):
                raise ValueError(f"Invalid quantity or price_per_unit for item: {item}")
            
            # Calculate cost for the current item
            item_cost = item['quantity'] * item['price_per_unit']
            total_cost += item_cost
        
        return total_cost
    except Exception as e:
        print(f"Error calculating total cost: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to calculate the total cost of medical supplies.
    """
    # Example list of medical supplies
    medical_supplies = [
        {"name": "Syringe", "quantity": 10, "price_per_unit": 1.5},
        {"name": "Nebulizer", "quantity": 2, "price_per_unit": 50.0},
        {"name": "Orthopedic Aid", "quantity": 1, "price_per_unit": 120.0},
    ]

    print("Calculating total cost of medical supplies...")
    total_cost = calculate_total_cost(medical_supplies)

    if total_cost is not None:
        print(f"Total cost: ${total_cost:.2f}")
    else:
        print("Failed to calculate total cost.")

if __name__ == "__main__":
    main()
```
