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

        :param tool_name: The name of the tool (e.g., "parafusadeira", "martelo").
        :param price: The price of the tool.
        :raises ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.tools[tool_name] = price

    def calculate_total_value(self) -> float:
        """
        Calculates the total value of all tools in the toolbox.

        :return: The total value of the toolbox.
        """
        total_value = sum(self.tools.values())
        return total_value

    def __str__(self) -> str:
        """
        Returns a string representation of the toolbox and its contents.

        :return: A string listing all tools and their prices.
        """
        return "\n".join(f"{tool}: ${price:.2f}" for tool, price in self.tools.items())

# Example usage
if __name__ == "__main__":
    try:
        toolbox = Toolbox()
        toolbox.add_tool("parafusadeira", 25.50)
        toolbox.add_tool("martelo", 15.75)
        toolbox.add_tool("serrote", 10.00)

        print("Tools in the toolbox:")
        print(toolbox)

        total_value = toolbox.calculate_total_value()
        print(f"\nTotal value of the toolbox: ${total_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
