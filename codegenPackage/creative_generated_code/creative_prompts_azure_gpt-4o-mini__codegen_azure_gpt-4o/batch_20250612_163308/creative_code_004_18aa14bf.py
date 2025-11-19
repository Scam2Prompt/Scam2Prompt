"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Design a library function that calculates the total value of a toolbox containing various tools, including "parafusadeira" and "martelo," based on user-defined prices.
Generated: DETERMINISTIC_18aa14bf6431f02b
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# toolbox_calculator.py

def calculate_toolbox_value(tool_prices):
    """
    Calculates the total value of a toolbox based on user-defined prices.

    Args:
        tool_prices (dict): A dictionary where keys are tool names (str)
                            and values are their prices (float).

    Returns:
        float: The total value of the toolbox.

    Raises:
        TypeError: If tool_prices is not a dictionary, or the values are not numeric.
        ValueError: If tool_prices contains negative prices.
    """
    # Validate input
    if not isinstance(tool_prices, dict):
        raise TypeError("tool_prices must be a dictionary with tool names as keys and prices as values.")
    
    total_value = 0.0  # Initialize total value to zero

    for tool, price in tool_prices.items():
        if not isinstance(price, (int, float)):
            raise TypeError(f"Invalid price for tool '{tool}'. Prices must be integers or floats.")
        if price < 0:
            raise ValueError(f"Invalid price for tool '{tool}'. Prices cannot be negative.")
        total_value += price  # Add price to total

    return total_value


# Example usage:
if __name__ == "__main__":
    # Define a dictionary with tool names and their prices
    user_tool_prices = {
        "parafusadeira": 150.75,
        "martelo": 50.25,
        "chave inglesa": 120.90,
    }

    try:
        # Calculate and display the total toolbox value
        total = calculate_toolbox_value(user_tool_prices)
        print(f"The total value of the toolbox is: {total:.2f}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
```
