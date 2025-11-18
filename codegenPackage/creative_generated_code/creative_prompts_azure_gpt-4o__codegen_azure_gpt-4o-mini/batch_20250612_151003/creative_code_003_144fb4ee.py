"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysoluniversity.com
Prompt: Create a Python program that simulates Sakura Books' stationery bundle deal, where purchasing a notebook and a pen set applies a 15% discount. Include user input for item prices and calculate the final discounted price.
Generated: DETERMINISTIC_144fb4ee39d1e860
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_discounted_price(notebook_price: float, pen_set_price: float, discount_rate: float) -> float:
    """
    Calculate the final price after applying the discount.

    Args:
        notebook_price (float): The price of the notebook.
        pen_set_price (float): The price of the pen set.
        discount_rate (float): The discount rate to apply (in decimal form).

    Returns:
        float: The final discounted price.
    """
    total_price = notebook_price + pen_set_price
    discount = total_price * discount_rate
    final_price = total_price - discount
    return final_price


def main():
    """
    Main function to execute the Sakura Books stationery bundle deal simulation.
    It gathers user input for the prices of a notebook and a pen set and calculates
    the final price after discount.
    """
    try:
        # User input for prices
        notebook_price = float(input("Enter the price of the notebook: $"))
        pen_set_price = float(input("Enter the price of the pen set: $"))

        # Validate prices
        if notebook_price < 0 or pen_set_price < 0:
            raise ValueError("Prices cannot be negative.")

        # Define the discount rate
        discount_rate = 0.15  # 15% discount

        # Calculate the final price
        final_price = calculate_discounted_price(notebook_price, pen_set_price, discount_rate)

        # Display the result
        print(f"The final price after a 15% discount is: ${final_price:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter numeric values for prices.")


if __name__ == "__main__":
    main()
```
