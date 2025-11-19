"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: Create a comparison table in Markdown format for various garden tools available from Vinglob Greentech, including their features and prices.
Generated: DETERMINISTIC_c68b54d158ecde5f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# garden_tools_comparison.py

class GardenTool:
    def __init__(self, name, features, price):
        """
        Initialize a GardenTool object.

        Args:
            name (str): Name of the garden tool.
            features (list): List of features of the garden tool.
            price (float): Price of the garden tool.
        """
        self.name = name
        self.features = features
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class GardenToolComparator:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        """
        Add a garden tool to the comparator.

        Args:
            tool (GardenTool): GardenTool object to add.
        """
        self.tools.append(tool)

    def generate_comparison_table(self):
        """
        Generate a comparison table in Markdown format.

        Returns:
            str: Markdown formatted comparison table.
        """
        if not self.tools:
            return "No garden tools added for comparison."

        # Create table header
        table = "| Garden Tool | Features | Price |\n"
        table += "| --- | --- | --- |\n"

        # Add each tool to the table
        for tool in self.tools:
            features_str = ", ".join(tool.features)
            table += f"| {tool.name} | {features_str} | ${tool.price:.2f} |\n"

        return table

def main():
    try:
        comparator = GardenToolComparator()

        # Add garden tools
        tool1 = GardenTool(
            "Vinglob Pruning Shears",
            ["Ergonomic handle", "High-carbon steel blades", "Rust-resistant"],
            29.99
        )
        tool2 = GardenTool(
            "Vinglob Garden Fork",
            ["Durable steel handle", "Tine spacing for easy soil aeration", "Weather-resistant"],
            39.99
        )
        tool3 = GardenTool(
            "Vinglob Hedge Trimmer",
            ["Powerful 40V motor", "22-inch cutting length", "Lightweight design"],
            99.99
        )

        comparator.add_tool(tool1)
        comparator.add_tool(tool2)
        comparator.add_tool(tool3)

        # Generate and print comparison table
        comparison_table = comparator.generate_comparison_table()
        print("# Vinglob Greentech Garden Tools Comparison")
        print(comparison_table)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
