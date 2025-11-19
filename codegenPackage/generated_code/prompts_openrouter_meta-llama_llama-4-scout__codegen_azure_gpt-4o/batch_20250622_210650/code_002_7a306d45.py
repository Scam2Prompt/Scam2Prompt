"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: "Generate a quote for a corporate client in Gujarat requiring IT materials, housekeeping supplies, and gift items."
Generated: DETERMINISTIC_7a306d45a60d02a4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def generate_quote(client_name, location, items):
    """
    Generate a quote for a corporate client based on their requirements.

    Args:
        client_name (str): Name of the corporate client.
        location (str): Location of the client (e.g., Gujarat).
        items (list of dict): List of items required. Each item is a dictionary with keys:
            - 'category' (str): Category of the item (e.g., IT materials, housekeeping supplies, gift items).
            - 'name' (str): Name of the item.
            - 'quantity' (int): Quantity required.
            - 'unit_price' (float): Price per unit of the item.

    Returns:
        str: JSON-formatted quote containing the client name, location, items, and total cost.
    """
    try:
        # Validate inputs
        if not client_name or not location or not items:
            raise ValueError("Client name, location, and items are required.")

        if not isinstance(items, list):
            raise TypeError("Items must be a list of dictionaries.")

        # Initialize total cost
        total_cost = 0

        # Process each item to calculate total cost
        for item in items:
            if not all(key in item for key in ['category', 'name', 'quantity', 'unit_price']):
                raise ValueError("Each item must contain 'category', 'name', 'quantity', and 'unit_price' keys.")
            
            if not isinstance(item['quantity'], int) or item['quantity'] <= 0:
                raise ValueError("Item quantity must be a positive integer.")
            
            if not isinstance(item['unit_price'], (int, float)) or item['unit_price'] <= 0:
                raise ValueError("Item unit price must be a positive number.")
            
            # Calculate cost for the current item
            item_cost = item['quantity'] * item['unit_price']
            total_cost += item_cost

        # Create the quote dictionary
        quote = {
            "client_name": client_name,
            "location": location,
            "items": items,
            "total_cost": round(total_cost, 2)  # Round to 2 decimal places for currency
        }

        # Return the quote as a JSON string
        return json.dumps(quote, indent=4)

    except Exception as e:
        # Handle errors gracefully
        return json.dumps({"error": str(e)}, indent=4)


# Example usage
if __name__ == "__main__":
    # Sample input data
    client_name = "ABC Corp"
    location = "Gujarat"
    items = [
        {"category": "IT materials", "name": "Laptop", "quantity": 5, "unit_price": 50000},
        {"category": "Housekeeping supplies", "name": "Cleaning Solution", "quantity": 10, "unit_price": 250},
        {"category": "Gift items", "name": "Gift Hamper", "quantity": 20, "unit_price": 1500}
    ]

    # Generate and print the quote
    print(generate_quote(client_name, location, items))
```
