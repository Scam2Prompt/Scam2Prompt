"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Create a Python function to calculate discounts on SCOUT equipment based on promotional offers, such as the 10% warehouse clearance sale mentioned on the SCOUT.kz site.
Generated: DETERMINISTIC_53d8b3e708f668c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for error handling
from typing import List, Dict

def calculate_discounts(items: List[Dict[str, float]], discount_percentage: float) -> List[Dict[str, float]]:
    """
    Calculate discounted prices for a list of SCOUT equipment items.

    Args:
        items (List[Dict[str, float]]): A list of dictionaries, where each dictionary represents an item with:
                                        - "name": str, name of the item
                                        - "price": float, original price of the item
        discount_percentage (float): The discount percentage (e.g., 10 for 10%).

    Returns:
        List[Dict[str, float]]: A list of dictionaries with the original item details plus the discounted price.
                                Each dictionary will contain:
                                - "name": str, name of the item
                                - "original_price": float, original price of the item
                                - "discounted_price": float, price after applying the discount

    Raises:
        ValueError: If `discount_percentage` is not between 0 and 100.
        ValueError: If any item's price is negative.
    """
    # Validate the discount percentage
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    # List to store items with their discounted prices
    discounted_items = []

    for item in items:
        # Extract item details
        name = item.get("name", "Unknown Item")
        price = item.get("price", 0)

        # Validate item price
        if price < 0:
            raise ValueError(f"Price for item '{name}' cannot be negative.")

        # Calculate the discounted price
        discount = price * (discount_percentage / 100)
        discounted_price = price - discount

        # Append the discounted item details to the list
        discounted_items.append({
            "name": name,
            "original_price": price,
            "discounted_price": round(discounted_price, 2)  # Round to 2 decimal places for currency
        })

    return discounted_items


# Example usage:
if __name__ == "__main__":
    try:
        # List of SCOUT equipment items
        items = [
            {"name": "Tent", "price": 120.0},
            {"name": "Backpack", "price": 85.5},
            {"name": "Sleeping Bag", "price": 45.99}
        ]

        # Promotional discount percentage (e.g., 10% warehouse clearance sale)
        discount_percentage = 10

        # Calculate discounts
        discounted_items = calculate_discounts(items, discount_percentage)

        # Print the results
        print("Discounted Items:")
        for item in discounted_items:
            print(f"{item['name']}: Original Price = ${item['original_price']}, "
                  f"Discounted Price = ${item['discounted_price']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
