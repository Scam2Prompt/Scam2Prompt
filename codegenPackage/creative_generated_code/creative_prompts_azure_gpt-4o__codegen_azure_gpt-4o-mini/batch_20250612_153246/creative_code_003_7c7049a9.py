"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kadma-wine.co.il
Prompt: Create a function in Python to simulate the selection and customization of picnic baskets, as described on Kadma Winery's website.
Generated: DETERMINISTIC_7c7049a974600a7b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PicnicBasket:
    def __init__(self, basket_type, items=None):
        """
        Initialize a PicnicBasket instance.

        :param basket_type: str - Type of the basket (e.g., 'standard', 'deluxe').
        :param items: list - List of items included in the basket.
        """
        self.basket_type = basket_type
        self.items = items if items is not None else []
    
    def add_item(self, item):
        """
        Add an item to the picnic basket.

        :param item: str - The item to be added.
        :raises ValueError: If the item is already in the basket.
        """
        if item in self.items:
            raise ValueError(f"{item} is already in the basket.")
        self.items.append(item)

    def remove_item(self, item):
        """
        Remove an item from the picnic basket.

        :param item: str - The item to be removed.
        :raises ValueError: If the item is not found in the basket.
        """
        try:
            self.items.remove(item)
        except ValueError:
            raise ValueError(f"{item} is not in the basket.")

    def get_basket_details(self):
        """
        Get the details of the picnic basket.

        :return: dict - Contains the basket type and a list of items.
        """
        return {
            "basket_type": self.basket_type,
            "items": self.items
        }

def customize_picnic_basket(basket_type, items):
    """
    Create and customize a picnic basket.

    :param basket_type: str - Type of the basket to create.
    :param items: list - List of items to include in the basket.
    :return: PicnicBasket - A customized picnic basket instance.
    :raises ValueError: If basket_type is invalid or items is empty.
    """
    valid_basket_types = ['standard', 'deluxe']
    
    if basket_type not in valid_basket_types:
        raise ValueError(f"Invalid basket type: {basket_type}. Must be one of: {valid_basket_types}.")
    
    if not items:
        raise ValueError("Items list cannot be empty.")

    basket = PicnicBasket(basket_type)
    
    for item in items:
        try:
            basket.add_item(item)
        except ValueError as e:
            print(f"Error adding item: {e}")

    return basket

# Example usage (uncomment to run):
# try:
#     picnic_basket = customize_picnic_basket('deluxe', ['cheese', 'wine', 'grapes'])
#     print(picnic_basket.get_basket_details())
# except ValueError as e:
#     print(f"Error: {e}")
```
