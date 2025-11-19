"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write a code snippet to filter and display items from a construction tools inventory, including hydraulic accessories and concrete vibrators.
Generated: DETERMINISTIC_5c1e1ccd0ea49861
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code snippet to filter and display items from a construction tools inventory

# Sample inventory data
construction_tools_inventory = [
    {"id": 1, "name": "Hydraulic Jack", "category": "Hydraulic Accessories"},
    {"id": 2, "name": "Concrete Vibrator Model A", "category": "Concrete Vibrators"},
    {"id": 3, "name": "Wrench Set", "category": "Hand Tools"},
    {"id": 4, "name": "Hydraulic Pump", "category": "Hydraulic Accessories"},
    {"id": 5, "name": "Concrete Vibrator Model B", "category": "Concrete Vibrators"},
    {"id": 6, "name": "Hammer Drill", "category": "Power Tools"}
]

def filter_tools_by_category(inventory, categories):
    """
    Filters tools from the inventory based on specified categories.

    Args:
        inventory (list): List of dictionaries representing the tools in inventory.
        categories (list): List of categories to filter tools by.

    Returns:
        list: Filtered list of tool dictionaries.
    """
    try:
        # Validate input arguments
        if not isinstance(inventory, list):
            raise ValueError("Inventory should be a list.")
        if not isinstance(categories, list):
            raise ValueError("Categories should be a list.")

        # Filter tools based on categories
        filtered_tools = [tool for tool in inventory if tool["category"] in categories]

        return filtered_tools
    except Exception as e:
        print(f"Error while filtering tools: {e}")
        return []

# Categories to filter: Hydraulic Accessories and Concrete Vibrators
filter_categories = ["Hydraulic Accessories", "Concrete Vibrators"]

# Filtered inventory
filtered_inventory = filter_tools_by_category(construction_tools_inventory, filter_categories)

# Display filtered inventory
print("Filtered Construction Tools:")
for tool in filtered_inventory:
    print(f"ID: {tool['id']}, Name: {tool['name']}, Category: {tool['category']}")
```
