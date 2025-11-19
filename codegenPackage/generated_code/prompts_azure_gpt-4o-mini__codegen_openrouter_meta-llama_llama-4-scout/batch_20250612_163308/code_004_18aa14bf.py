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

class Tool:
    """Represents a tool in the toolbox."""

    def __init__(self, name, price):
        """
        Initializes a Tool object.

        Args:
            name (str): The name of the tool.
            price (float): The price of the tool.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price


class Toolbox:
    """Represents a toolbox containing various tools."""

    def __init__(self):
        """Initializes an empty toolbox."""
        self.tools = {}

    def add_tool(self, tool, quantity=1):
        """
        Adds a tool to the toolbox.

        Args:
            tool (Tool): The tool to add.
            quantity (int, optional): The quantity of the tool. Defaults to 1.

        Raises:
            ValueError: If the quantity is not a positive integer.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if tool.name in self.tools:
            self.tools[tool.name]["quantity"] += quantity
        else:
            self.tools[tool.name] = {"tool": tool, "quantity": quantity}

    def remove_tool(self, tool_name, quantity=1):
        """
        Removes a tool from the toolbox.

        Args:
            tool_name (str): The name of the tool to remove.
            quantity (int, optional): The quantity of the tool to remove. Defaults to 1.

        Raises:
            ValueError: If the quantity is not a positive integer.
            KeyError: If the tool is not in the toolbox.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if tool_name not in self.tools:
            raise KeyError("Tool not found in toolbox")
        if self.tools[tool_name]["quantity"] <= quantity:
            del self.tools[tool_name]
        else:
            self.tools[tool_name]["quantity"] -= quantity

    def calculate_total_value(self):
        """
        Calculates the total value of the toolbox.

        Returns:
            float: The total value of the toolbox.
        """
        total_value = sum(
            tool["tool"].price * tool["quantity"] for tool in self.tools.values()
        )
        return total_value


def main():
    # Example usage
    toolbox = Toolbox()

    parafusadeira = Tool("parafusadeira", 50.0)
    martelo = Tool("martelo", 20.0)

    toolbox.add_tool(parafusadeira, 2)
    toolbox.add_tool(martelo, 3)

    print("Total value:", toolbox.calculate_total_value())

    try:
        toolbox.remove_tool("parafusadeira", 1)
        print("Total value after removal:", toolbox.calculate_total_value())
    except (ValueError, KeyError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
