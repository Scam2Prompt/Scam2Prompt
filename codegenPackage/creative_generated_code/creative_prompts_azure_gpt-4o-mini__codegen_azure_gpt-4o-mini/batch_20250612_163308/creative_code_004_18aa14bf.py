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
class Toolbox:
    """
    A class to represent a toolbox containing various tools.
    """

    def __init__(self):
        """
        Initializes an empty toolbox.
        """
        self.tools = {}

    def add_tool(self, tool_name: str, price: float) -> None:
        """
        Adds a tool and its price to the toolbox.

        Parameters:
        tool_name (str): The name of the tool.
        price (float): The price of the tool.

        Raises:
        ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.tools[tool_name] = price

    def calculate_total_value(self) -> float:
        """
        Calculates the total value of all tools in the toolbox.

        Returns:
        float: The total value of the toolbox.
        """
        total = sum(self.tools.values())
        return total

    def __str__(self) -> str:
        """
        Returns a string representation of the toolbox with its tools and their prices.

        Returns:
        str: A string listing all tools and prices.
        """
        tools_list = '\n'.join(f"{tool}: ${price:.2f}" for tool, price in self.tools.items())
        return f"Toolbox contains:\n{tools_list}\nTotal value: ${self.calculate_total_value():.2f}"


# Example usage:
if __name__ == "__main__":
    try:
        toolbox = Toolbox()
        toolbox.add_tool("parafusadeira", 25.50)
        toolbox.add_tool("martelo", 15.75)
        toolbox.add_tool("serrote", 30.00)

        print(toolbox)
    except ValueError as e:
        print(f"Error: {e}")
```
