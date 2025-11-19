"""
Generated Code Metadata:
========================
Original URL: https://dex-pleener.com
Prompt: Suggest a set of must-have tools for DIY car maintenance, including diagnostic equipment, cleaning products, and safety gear.
Generated: DETERMINISTIC_040bde465ef017c4
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarMaintenanceTools:
    """
    A class to represent a collection of must-have tools for DIY car maintenance.
    """

    def __init__(self):
        """
        Initializes the CarMaintenanceTools with essential tools.
        """
        self.tools = {
            "diagnostic_equipment": [
                "OBD-II Scanner",
                "Multimeter",
                "Compression Tester"
            ],
            "cleaning_products": [
                "Car Wash Soap",
                "Microfiber Towels",
                "Wheel Cleaner",
                "Interior Cleaner",
                "Wax"
            ],
            "safety_gear": [
                "Mechanic Gloves",
                "Safety Glasses",
                "Knee Pads",
                "Steel-Toed Boots"
            ]
        }

    def get_tools(self):
        """
        Returns the list of tools categorized by type.

        Returns:
            dict: A dictionary containing categorized tools.
        """
        return self.tools

    def add_tool(self, category, tool):
        """
        Adds a new tool to the specified category.

        Args:
            category (str): The category to which the tool will be added.
            tool (str): The name of the tool to be added.

        Raises:
            ValueError: If the category is not valid.
        """
        if category not in self.tools:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.tools.keys())}")

        self.tools[category].append(tool)

    def remove_tool(self, category, tool):
        """
        Removes a tool from the specified category.

        Args:
            category (str): The category from which the tool will be removed.
            tool (str): The name of the tool to be removed.

        Raises:
            ValueError: If the category is not valid or the tool is not found.
        """
        if category not in self.tools:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.tools.keys())}")

        try:
            self.tools[category].remove(tool)
        except ValueError:
            raise ValueError(f"Tool '{tool}' not found in category '{category}'.")

    def display_tools(self):
        """
        Displays the tools in a formatted manner.
        """
        for category, tools in self.tools.items():
            print(f"{category.capitalize()}:")
            for tool in tools:
                print(f" - {tool}")
            print()  # Add a newline for better readability


if __name__ == "__main__":
    # Create an instance of CarMaintenanceTools
    car_tools = CarMaintenanceTools()

    # Display the initial set of tools
    car_tools.display_tools()

    # Example of adding a new tool
    try:
        car_tools.add_tool("cleaning_products", "Glass Cleaner")
    except ValueError as e:
        print(e)

    # Example of removing a tool
    try:
        car_tools.remove_tool("safety_gear", "Knee Pads")
    except ValueError as e:
        print(e)

    # Display the updated set of tools
    car_tools.display_tools()
```
