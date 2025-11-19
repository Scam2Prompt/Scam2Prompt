"""
Generated Code Metadata:
========================
Original URL: https://watpac.in
Prompt: Write a Python function that calculates the total cost of purchasing various Watpac waterproofing chemicals, including GST for products like cement additives and water sealers.
Generated: DETERMINISTIC_017d524420d123d5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Chemical:
    """
    A class to represent a chemical product with its price and GST rate.
    """
    def __init__(self, name: str, price: float, gst_rate: float = 0.10):
        """
        Initializes a new Chemical instance.

        :param name: The name of the chemical product.
        :param price: The price of the chemical product (excluding GST).
        :param gst_rate: The GST rate applicable to the product (default is 10%).
        """
        self.name = name
        self.price = price
        self.gst_rate = gst_rate

    def total_cost(self) -> float:
        """
        Calculates the total cost of the chemical including GST.

        :return: Total cost including GST.
        """
        return self.price * (1 + self.gst_rate)


def calculate_total_cost(chemicals: list) -> float:
    """
    Calculates the total cost of purchasing various chemicals including GST.

    :param chemicals: A list of Chemical instances.
    :return: Total cost of all chemicals including GST.
    :raises ValueError: If the input list is empty or contains invalid items.
    """
    if not chemicals:
        raise ValueError("The list of chemicals cannot be empty.")

    total = 0.0
    for chemical in chemicals:
        if not isinstance(chemical, Chemical):
            raise ValueError("All items in the list must be instances of the Chemical class.")
        total += chemical.total_cost()
    
    return total


# Example usage
if __name__ == "__main__":
    try:
        # Create instances of Chemical
        cement_additive = Chemical(name="Cement Additive", price=50.0)
        water_sealer = Chemical(name="Water Sealer", price=75.0)

        # List of chemicals to purchase
        chemicals_to_purchase = [cement_additive, water_sealer]

        # Calculate total cost
        total_cost = calculate_total_cost(chemicals_to_purchase)
        print(f"Total cost of purchasing chemicals (including GST): ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
