"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Write Python code to calculate the total cost of purchasing multiple Panasonic LED lights, including discounted prices for items like "Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288" and "Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688."
Generated: DETERMINISTIC_669c1e2851b9a168
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict


# Define a function to calculate the total cost of Panasonic LED lights
def calculate_total_cost(items: List[Dict[str, str]], discounts: Dict[str, float]) -> float:
    """
    Calculate the total cost of purchasing LED lights with applicable discounts.

    Args:
        items (List[Dict[str, str]]): A list of dictionaries, where each item contains:
            - 'name' (str): Name of the LED light.
            - 'quantity' (int): Number of units to purchase.
            - 'price_per_unit' (float): Price of one unit before discounts.

        discounts (Dict[str, float]): A dictionary containing the discount percentage for specific LED lights.

    Returns:
        float: The total cost with applied discounts.
    """
    total_cost = 0.0

    for item in items:
        try:
            # Extract item details
            name = item['name']
            quantity = int(item['quantity'])
            price_per_unit = float(item['price_per_unit'])

            # Apply discount if available, otherwise use full price
            discount = discounts.get(name, 0.0)  # Default discount is 0%
            discounted_price_per_unit = price_per_unit * (1 - discount / 100)

            # Calculate total cost for this item and add to the total
            total_cost += discounted_price_per_unit * quantity

        except KeyError as e:
            print(f"Error: Missing required field '{e}' in item data.")
        except ValueError as e:
            print(f"Error: Invalid value detected - {e}")

    return round(total_cost, 2)  # Round to 2 decimal places for currency precision


# Example usage
if __name__ == "__main__":
    # Define the list of LED lights to purchase
    items_to_purchase = [
        {"name": "Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288", "quantity": 3, "price_per_unit": 500000},
        {"name": "Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688", "quantity": 5, "price_per_unit": 300000},
        {"name": "Đèn LED Ốp Trần Panasonic 18w HH-LA061788", "quantity": 2, "price_per_unit": 200000},
    ]

    # Define the discounts for specific items (percentage off)
    discounts_available = {
        "Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288": 10.0,  # 10% off
        "Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688": 15.0,  # 15% off
    }

    # Calculate the total cost
    total = calculate_total_cost(items_to_purchase, discounts_available)
    print(f"The total cost for the purchase is: {total} VND")
```
