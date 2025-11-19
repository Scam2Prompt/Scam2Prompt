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
class ToolboxCalculator:
    """
    A library to calculate the total value of a toolbox containing various tools.
    Supports dynamic pricing of tools provided by the user.
    """

    def __init__(self):
        """
        Initialize the ToolboxCalculator with an empty dictionary to store tool prices.
        """
        self.tool_prices = {}

    def set_tool_price(self, tool_name: str, price: float) -> None:
        """
        Set the price for a specific tool.

        Args:
            tool_name (str): Name of the tool (e.g., "parafusadeira", "martelo").
            price (float): Price of the tool. Must be a non-negative number.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.tool_prices[tool_name.lower()] = price

    def get_tool_price(self, tool_name: str) -> float:
        """
        Retrieve the price of a specific tool.

        Args:
            tool_name (str): Name of the tool.

        Returns:
            float: Price of the tool.

        Raises:
            KeyError: If the tool is not found in the price dictionary.
        """
        return self.tool_prices[tool_name.lower()]

    def calculate_total_value(self, tools: dict) -> float:
        """
        Calculate the total value of the toolbox based on the quantities of each tool.

        Args:
            tools (dict): Dictionary where keys are tool names and values are quantities.

        Returns:
            float: Total value of the toolbox.

        Raises:
            KeyError: If any tool in the toolbox is not found in the price dictionary.
            ValueError: If any quantity is negative.
        """
        total_value = 0.0
        for tool_name, quantity in tools.items():
            if quantity < 0:
                raise ValueError(f"Quantity for {tool_name} cannot be negative.")
            price = self.get_tool_price(tool_name)
            total_value += price * quantity
        return total_value
```
