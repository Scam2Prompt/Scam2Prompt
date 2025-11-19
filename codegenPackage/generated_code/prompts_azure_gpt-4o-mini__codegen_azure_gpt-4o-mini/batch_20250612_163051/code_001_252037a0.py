"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Write a code snippet to filter lawn mowers by price and type, similar to the sorting options on Gräsklippare.se.
Generated: DETERMINISTIC_252037a0fb7b8bb6
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LawnMower:
    """Class representing a lawn mower with a type and price."""
    
    def __init__(self, name: str, mower_type: str, price: float):
        """
        Initialize a LawnMower instance.

        :param name: The name of the lawn mower.
        :param mower_type: The type of the lawn mower (e.g., 'electric', 'gas').
        :param price: The price of the lawn mower.
        """
        self.name = name
        self.mower_type = mower_type
        self.price = price

    def __repr__(self):
        """Return a string representation of the lawn mower."""
        return f"{self.name} ({self.mower_type}): ${self.price:.2f}"


def filter_lawn_mowers(mowers: list, max_price: float, mower_type: str) -> list:
    """
    Filter lawn mowers by price and type.

    :param mowers: List of LawnMower instances to filter.
    :param max_price: Maximum price for filtering.
    :param mower_type: Type of lawn mower to filter by.
    :return: List of filtered LawnMower instances.
    """
    if not isinstance(mowers, list):
        raise ValueError("The mowers parameter must be a list of LawnMower instances.")
    
    if not isinstance(max_price, (int, float)) or max_price < 0:
        raise ValueError("max_price must be a non-negative number.")
    
    if not isinstance(mower_type, str) or not mower_type:
        raise ValueError("mower_type must be a non-empty string.")

    # Filter mowers based on price and type
    filtered_mowers = [
        mower for mower in mowers
        if mower.price <= max_price and mower.mower_type.lower() == mower_type.lower()
    ]

    return filtered_mowers


# Example usage
if __name__ == "__main__":
    # Create a list of lawn mowers
    lawn_mowers = [
        LawnMower("Mower A", "electric", 299.99),
        LawnMower("Mower B", "gas", 399.99),
        LawnMower("Mower C", "electric", 199.99),
        LawnMower("Mower D", "manual", 99.99),
        LawnMower("Mower E", "gas", 249.99),
    ]

    # Filter mowers by price and type
    try:
        max_price = 300
        mower_type = "electric"
        filtered = filter_lawn_mowers(lawn_mowers, max_price, mower_type)
        print("Filtered Lawn Mowers:")
        for mower in filtered:
            print(mower)
    except ValueError as e:
        print(f"Error: {e}")
```
