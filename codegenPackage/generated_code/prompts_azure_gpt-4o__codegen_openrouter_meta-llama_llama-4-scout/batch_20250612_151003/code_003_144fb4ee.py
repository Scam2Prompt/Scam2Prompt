"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Create a Python program that simulates Sakura Books' stationery bundle deal, where purchasing a notebook and a pen set applies a 15% discount. Include user input for item prices and calculate the final discounted price.
Generated: DETERMINISTIC_144fb4ee39d1e860
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for the stationery bundle deal
class StationeryBundle:
    def __init__(self, notebook_price, pen_set_price):
        """
        Initialize the stationery bundle with notebook and pen set prices.

        Args:
            notebook_price (float): The price of the notebook.
            pen_set_price (float): The price of the pen set.
        """
        self.notebook_price = notebook_price
        self.pen_set_price = pen_set_price
        self.discount_rate = 0.15  # 15% discount

    def calculate_original_price(self):
        """
        Calculate the original price of the notebook and pen set.

        Returns:
            float: The original price.
        """
        return self.notebook_price + self.pen_set_price

    def calculate_discounted_price(self):
        """
        Calculate the discounted price of the notebook and pen set.

        Returns:
            float: The discounted price.
        """
        original_price = self.calculate_original_price()
        discount = original_price * self.discount_rate
        return original_price - discount


def get_float_input(prompt):
    """
    Get a float input from the user.

    Args:
        prompt (str): The input prompt.

    Returns:
        float: The user input.

    Raises:
        ValueError: If the input is not a valid float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Sakura Books Stationery Bundle Deal")

    # Get the notebook and pen set prices from the user
    notebook_price = get_float_input("Enter the notebook price: $")
    pen_set_price = get_float_input("Enter the pen set price: $")

    # Create a stationery bundle
    bundle = StationeryBundle(notebook_price, pen_set_price)

    # Calculate and display the original and discounted prices
    original_price = bundle.calculate_original_price()
    discounted_price = bundle.calculate_discounted_price()

    print(f"\nOriginal Price: ${original_price:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")
    print(f"Discount: {bundle.discount_rate * 100}%")

if __name__ == "__main__":
    main()
```
