"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "Write a Python code snippet to categorize construction tools for a company like Anhanguera Ferramentas."
Generated: DETERMINISTIC_f2b1a5b87da80060
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConstructionTool:
    """
    A class to represent a construction tool with its attributes.
    """
    def __init__(self, name: str, category: str, subcategory: str, price: float, quantity: int):
        """
        Initialize a construction tool with name, category, subcategory, price, and quantity.
        
        Args:
            name (str): Name of the tool
            category (str): Main category (e.g., 'Power Tools')
            subcategory (str): Subcategory (e.g., 'Drills')
            price (float): Price of the tool
            quantity (int): Available quantity in stock
        """
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Tool(name='{self.name}', category='{self.category}', subcategory='{self.subcategory}', price={self.price}, quantity={self.quantity})"


class ToolInventory:
    """
    A class to manage inventory of construction tools with categorization.
    """
    def __init__(self):
        self.tools = []
        self.categories = set()
        self.subcategories = {}

    def add_tool(self, tool: ConstructionTool):
        """
        Add a tool to the inventory and update category/subcategory mappings.
        
        Args:
            tool (ConstructionTool): Tool to be added
            
        Raises:
            ValueError: If tool is not a ConstructionTool instance
        """
        if not isinstance(tool, ConstructionTool):
            raise ValueError("Only ConstructionTool objects can be added to inventory")
            
        self.tools.append(tool)
        self.categories.add(tool.category)
        
        if tool.category not in self.subcategories:
            self.subcategories[tool.category] = set()
        self.subcategories[tool.category].add(tool.subcategory)

    def get_tools_by_category(self, category: str) -> list:
        """
        Get all tools in a specific category.
        
        Args:
            category (str): Category to filter by
            
        Returns:
            list: List of tools in the specified category
            
        Raises:
            ValueError: If category doesn't exist
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found in inventory")
            
        return [tool for tool in self.tools if tool.category == category]

    def get_tools_by_subcategory(self, category: str, subcategory: str) -> list:
        """
        Get all tools in a specific subcategory.
        
        Args:
            category (str): Parent category
            subcategory (str): Subcategory to filter by
            
        Returns:
            list: List of tools in the specified subcategory
            
        Raises:
            ValueError: If category or subcategory doesn't exist
        """
        if category not in self.subcategories:
            raise ValueError(f"Category '{category}' not found in inventory")
        if subcategory not in self.subcategories[category]:
            raise ValueError(f"Subcategory '{subcategory}' not found in category '{category}'")
            
        return [tool for tool in self.tools if tool.category == category and tool.subcategory == subcategory]

    def get_all_categories(self) -> list:
        """
        Get all available categories.
        
        Returns:
            list: Sorted list of all categories
        """
        return sorted(self.categories)

    def get_subcategories(self, category: str) -> list:
        """
        Get all subcategories for a given category.
        
        Args:
            category (str): Category to get subcategories for
            
        Returns:
            list: Sorted list of subcategories
            
        Raises:
            ValueError: If category doesn't exist
        """
        if category not in self.subcategories:
            raise ValueError(f"Category '{category}' not found in inventory")
            
        return sorted(self.subcategories[category])


# Example usage
if __name__ == "__main__":
    inventory = ToolInventory()
    
    # Adding sample tools
    inventory.add_tool(ConstructionTool("Hammer", "Hand Tools", "Hammers", 15.99, 50))
    inventory.add_tool(ConstructionTool("Screwdriver Set", "Hand Tools", "Screwdrivers", 24.99, 30))
    inventory.add_tool(ConstructionTool("Circular Saw", "Power Tools", "Saws", 129.99, 15))
    inventory.add_tool(ConstructionTool("Drill", "Power Tools", "Drills", 89.99, 25))
    inventory.add_tool(ConstructionTool("Measuring Tape", "Measuring Tools", "Tapes", 12.50, 40))
    
    # Display categories
    print("Available categories:", inventory.get_all_categories())
    
    # Display tools in a category
    power_tools = inventory.get_tools_by_category("Power Tools")
    print("\nPower Tools:")
    for tool in power_tools:
        print(f"- {tool.name} ({tool.subcategory}): ${tool.price}")
```
