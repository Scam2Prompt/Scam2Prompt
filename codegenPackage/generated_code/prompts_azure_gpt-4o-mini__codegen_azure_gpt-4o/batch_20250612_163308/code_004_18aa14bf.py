"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Design a library function that calculates the total value of a toolbox containing various tools, including "parafusadeira" and "martelo," based on user-defined prices.
Generated: DETERMINISTIC_18aa14bf6431f02b
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# toolbox_calculator.py

class ToolboxCalculator:
    """
    A class to calculate the total value of a toolbox containing various tools.
    """

    def __init__(self, tool_prices):
        """
        Initializes the ToolboxCalculator with user-defined prices for tools.

        :param tool_prices: A dictionary where keys are tool names (str) and values are their prices (float).
        """
        if not isinstance(tool_prices, dict):
            raise ValueError("tool_prices must be a dictionary.")
        self.tool_prices = tool_prices

    def calculate_total_value(self, toolbox):
        """
        Calculates the total value of the toolbox based on the tool prices.

        :param toolbox: A dictionary where keys are tool names (str) and values are quantities (int).
        :return: The total value of the toolbox (float).
        """
        if not isinstance(toolbox, dict):
            raise ValueError("toolbox must be a dictionary.")

        total_value = 0.0

        for tool, quantity in toolbox.items():
            if not isinstance(tool, str):
                raise ValueError(f"Tool name must be a string. Invalid tool: {tool}")
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError(f"Quantity must be a non-negative integer. Invalid quantity for {tool}: {quantity}")

            # Get the price of the tool, defaulting to 0 if the tool is not in the price list
            price = self.tool_prices.get(tool, 0.0)
            total_value += price * quantity

        return total_value


# Example usage:
if __name__ == "__main__":
    # Define user-defined prices for tools
    tool_prices = {
        "parafusadeira": 150.0,
        "martelo": 50.0,
        "chave inglesa": 75.0,
    }

    # Create an instance of ToolboxCalculator
    calculator = ToolboxCalculator(tool_prices)

    # Define the toolbox with quantities of tools
    toolbox = {
        "parafusadeira": 2,
        "martelo": 3,
        "chave inglesa": 1,
    }

    try:
        # Calculate the total value of the toolbox
        total_value = calculator.calculate_total_value(toolbox)
        print(f"The total value of the toolbox is: R$ {total_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
