"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Create a script to calculate bulk purchase discounts for items like "کابل LDNIO LC631i اپل لایتنینگ به تایپ سی" based on the discount percentages provided on the website.
Generated: DETERMINISTIC_7bcac86b009ec920
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_discounted_price(item_name, original_price, discount_percentage):
    """
    Calculate the discounted price of an item based on the discount percentage.

    Parameters:
        item_name (str): Name of the item.
        original_price (float): Original price of the item.
        discount_percentage (float): Discount percentage to apply.

    Returns:
        float: Discounted price after applying the discount.
    """
    try:
        # Ensure inputs are valid
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        # Calculate the discounted price
        discounted_price = original_price * (1 - discount_percentage / 100)
        return round(discounted_price, 2)
    except ValueError as ve:
        print(f"Error calculating discounted price for '{item_name}': {ve}")
        return None


def bulk_discount_calculator(prices_with_discounts):
    """
    Calculate discounted prices for bulk purchases.

    Parameters:
        prices_with_discounts (list of dict): A list of dictionaries, where each dictionary contains:
            - "item_name" (str): Name of the item.
            - "original_price" (float): Original price of the item.
            - "discount_percentage" (float): Discount percentage to apply.

    Returns:
        list of dict: A list of dictionaries with discounted prices added.
    """
    discounted_items = []

    for item in prices_with_discounts:
        try:
            item_name = item["item_name"]
            original_price = item["original_price"]
            discount_percentage = item["discount_percentage"]

            discounted_price = calculate_discounted_price(
                item_name, original_price, discount_percentage
            )
            if discounted_price is not None:
                discounted_items.append({
                    "item_name": item_name,
                    "original_price": original_price,
                    "discount_percentage": discount_percentage,
                    "discounted_price": discounted_price,
                })
        except KeyError as ke:
            print(f"Missing key in item data: {ke}")
        except Exception as e:
            print(f"Unexpected error processing item '{item.get('item_name', 'Unknown')}': {e}")

    return discounted_items


if __name__ == "__main__":
    # Example data
    items_to_discount = [
        {
            "item_name": "کابل LDNIO LC631i اپل لایتنینگ به تایپ سی",
            "original_price": 200000,
            "discount_percentage": 20,
        },
        {
            "item_name": "کابل USB C به Type C",
            "original_price": 150000,
            "discount_percentage": 15,
        },
    ]

    # Calculate bulk discounts
    results = bulk_discount_calculator(items_to_discount)

    # Print the results
    print("Discounted Prices:")
    for item in results:
        print(
            f"Item: {item['item_name']}, "
            f"Original Price: {item['original_price']} IRR, "
            f"Discount: {item['discount_percentage']}%, "
            f"Discounted Price: {item['discounted_price']} IRR"
        )
```
