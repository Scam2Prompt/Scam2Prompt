"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotopoint.com.ar
Prompt: Write Python code to calculate the total cost of purchasing multiple items from Fotopoint, including categories like "notebooks," "smartwatches," and "gaming peripherals," with support for installment payments.
Generated: DETERMINISTIC_ea6e65363bcd8410
Batch ID: 20250612_152739
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

class FotopointStore:
    def __init__(self):
        """
        Initialize the FotopointStore with product categories and their respective prices.
        """
        self.products = {
            "notebooks": {"Dell XPS 13": 999.99, "MacBook Air": 1199.99, "HP Spectre": 899.99},
            "smartwatches": {"Apple Watch Series 8": 399.99, "Samsung Galaxy Watch": 299.99, "Fitbit Versa": 199.99},
            "gaming_peripherals": {"Logitech Mouse": 49.99, "Corsair Keyboard": 99.99, "SteelSeries Headset": 129.99}
        }

    def calculate_total_cost(self, items: List[Dict[str, int]], installments: int = 1) -> Dict[str, float]:
        """
        Calculate the total cost of purchasing items with support for installment payments.
        Args:
            items (List[Dict[str, int]]): A list of dictionaries, where each dictionary contains:
                                          - 'category': the category of the item (e.g., 'notebooks')
                                          - 'item': the specific item to purchase (e.g., 'Dell XPS 13')
                                          - 'quantity': the number of items to purchase
            installments (int): The number of installments for payment. Defaults to 1 (full payment).
        
        Returns:
            Dict[str, float]: A dictionary containing the total cost and installment details.
        """
        total_cost = 0.0

        # Process each item in the list
        for item in items:
            category = item.get("category")
            product = item.get("item")
            quantity = item.get("quantity", 1)

            # Validate the inputs
            if category not in self.products:
                raise ValueError(f"Invalid category: {category}")
            if product not in self.products[category]:
                raise ValueError(f"Invalid product: {product} in category {category}")
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

            # Calculate cost for the current item
            item_cost = self.products[category][product] * quantity
            total_cost += item_cost

        # Calculate installment payment details
        if installments <= 0:
            raise ValueError("Installments must be greater than zero.")
        per_installment_cost = total_cost / installments

        return {
            "total_cost": round(total_cost, 2),
            "installments": installments,
            "per_installment_cost": round(per_installment_cost, 2)
        }


# Example usage of the FotopointStore
if __name__ == "__main__":
    store = FotopointStore()

    # List of items to purchase
    items_to_purchase = [
        {"category": "notebooks", "item": "Dell XPS 13", "quantity": 1},
        {"category": "smartwatches", "item": "Apple Watch Series 8", "quantity": 2},
        {"category": "gaming_peripherals", "item": "Logitech Mouse", "quantity": 3},
    ]

    # Number of installments
    installments = 3

    try:
        # Calculate the total cost and installment details
        result = store.calculate_total_cost(items_to_purchase, installments)
        print("Purchase Summary:")
        print(f"Total Cost: ${result['total_cost']}")
        print(f"Number of Installments: {result['installments']}")
        print(f"Cost per Installment: ${result['per_installment_cost']}")
    except ValueError as e:
        print(f"Error: {e}")
```
