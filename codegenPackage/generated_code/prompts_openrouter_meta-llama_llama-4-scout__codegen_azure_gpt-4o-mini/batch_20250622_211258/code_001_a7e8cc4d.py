"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Generate a Python code snippet to categorize and filter lawn mowers based on their type (e.g., bensindriven, eldriven, robotgräsklippare) and price range.
Generated: DETERMINISTIC_a7e8cc4ddaa762a6
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LawnMower:
    """
    A class to represent a lawn mower.

    Attributes:
        type (str): The type of the lawn mower (e.g., 'bensindriven', 'eldriven', 'robotgräsklippare').
        price (float): The price of the lawn mower.
    """

    def __init__(self, mower_type: str, price: float):
        """
        Initializes a new instance of LawnMower.

        Args:
            mower_type (str): The type of the lawn mower.
            price (float): The price of the lawn mower.

        Raises:
            ValueError: If the price is negative or the type is invalid.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if mower_type not in ['bensindriven', 'eldriven', 'robotgräsklippare']:
            raise ValueError("Invalid mower type.")

        self.type = mower_type
        self.price = price


class LawnMowerCatalog:
    """
    A class to manage a catalog of lawn mowers.

    Attributes:
        mowers (list): A list of LawnMower instances.
    """

    def __init__(self):
        """Initializes the catalog with an empty list of mowers."""
        self.mowers = []

    def add_mower(self, mower: LawnMower):
        """
        Adds a lawn mower to the catalog.

        Args:
            mower (LawnMower): The lawn mower to add.
        """
        self.mowers.append(mower)

    def filter_mowers(self, mower_type: str, min_price: float, max_price: float):
        """
        Filters the lawn mowers based on type and price range.

        Args:
            mower_type (str): The type of lawn mower to filter by.
            min_price (float): The minimum price of the lawn mowers to include.
            max_price (float): The maximum price of the lawn mowers to include.

        Returns:
            list: A list of lawn mowers that match the criteria.
        """
        if min_price < 0 or max_price < 0:
            raise ValueError("Price range cannot be negative.")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")

        filtered_mowers = [
            mower for mower in self.mowers
            if mower.type == mower_type and min_price <= mower.price <= max_price
        ]
        return filtered_mowers


# Example usage
if __name__ == "__main__":
    try:
        catalog = LawnMowerCatalog()
        catalog.add_mower(LawnMower('bensindriven', 3000))
        catalog.add_mower(LawnMower('eldriven', 1500))
        catalog.add_mower(LawnMower('robotgräsklippare', 5000))

        # Filter mowers of type 'eldriven' with price between 1000 and 2000
        filtered = catalog.filter_mowers('eldriven', 1000, 2000)
        for mower in filtered:
            print(f"Type: {mower.type}, Price: {mower.price}")

    except ValueError as e:
        print(f"Error: {e}")
```
