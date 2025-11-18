"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Create a script to calculate discounts and cashback offers for promotional items, based on the promotional campaigns mentioned on the Merchandiso website.
Generated: DETERMINISTIC_cf8275a84e7b1fa2
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PromotionalItem:
    """
    A class to represent a promotional item with discount and cashback offers.
    """

    def __init__(self, item_id, original_price, discount_percentage, cashback_amount):
        """
        Initializes a PromotionalItem instance.

        :param item_id: Unique identifier for the promotional item
        :param original_price: Original price of the item
        :param discount_percentage: Discount percentage applied to the item
        :param cashback_amount: Cashback amount provided for the item
        """
        self.item_id = item_id
        self.original_price = original_price
        self.discount_percentage = discount_percentage
        self.cashback_amount = cashback_amount

    def calculate_discounted_price(self):
        """
        Calculates the price after applying the discount.

        :return: Discounted price of the item
        """
        try:
            discount = (self.discount_percentage / 100) * self.original_price
            discounted_price = self.original_price - discount
            return discounted_price
        except Exception as e:
            raise ValueError("Error calculating discounted price: " + str(e))

    def calculate_final_price(self):
        """
        Calculates the final price after applying cashback.

        :return: Final price of the item after cashback
        """
        try:
            discounted_price = self.calculate_discounted_price()
            final_price = discounted_price - self.cashback_amount
            return final_price if final_price >= 0 else 0
        except Exception as e:
            raise ValueError("Error calculating final price: " + str(e))


def load_promotional_items_from_file(file_path):
    """
    Loads promotional items from a JSON file.

    :param file_path: Path to the JSON file containing promotional items
    :return: List of PromotionalItem objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [PromotionalItem(**item) for item in data]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except Exception as e:
        raise RuntimeError("An error occurred while loading the promotional items: " + str(e))


def main():
    """
    Main function to execute the discount and cashback calculation.
    """
    file_path = 'promotional_items.json'  # Path to the promotional items JSON file

    try:
        items = load_promotional_items_from_file(file_path)
        for item in items:
            print(f"Item ID: {item.item_id}")
            print(f"Original Price: ${item.original_price:.2f}")
            print(f"Discounted Price: ${item.calculate_discounted_price():.2f}")
            print(f"Final Price after Cashback: ${item.calculate_final_price():.2f}")
            print("-" * 30)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
``` 

Note: Ensure that there is a JSON file named `promotional_items.json` structured as follows for the code to work:

```json
[
    {
        "item_id": "001",
        "original_price": 100.0,
        "discount_percentage": 20,
        "cashback_amount": 10.0
    },
    {
        "item_id": "002",
        "original_price": 50.0,
        "discount_percentage": 10,
        "cashback_amount": 5.0
    }
]
```
