"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python script to manage an inventory of tools, including pliers, drills, hammers, screwdrivers, and toolboxes, with functionality to add, remove, and search for tools.
Generated: DETERMINISTIC_f8835e8ab4672049
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

# Import necessary modules for error handling and input validation
import sys

class ToolInventory:
    # Initialize the inventory as an empty dictionary
    def __init__(self):
        self.inventory = {}

    # Method to add a tool to the inventory
    def add_tool(self, tool_name, quantity):
        """
        Adds a tool to the inventory.
        
        Parameters:
            tool_name (str): Name of the tool.
            quantity (int): Number of tools to add.
        
        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if tool_name in self.inventory:
            self.inventory[tool_name] += quantity
        else:
            self.inventory[tool_name] = quantity
        print(f"Added {quantity} {tool_name}(s) to the inventory.")

    # Method to remove a tool from the inventory
    def remove_tool(self, tool_name, quantity):
        """
        Removes a tool from the inventory.
        
        Parameters:
            tool_name (str): Name of the tool.
            quantity (int): Number of tools to remove.
        
        Raises:
            ValueError: If quantity is not a positive integer or exceeds available stock.
            KeyError: If the tool does not exist in the inventory.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if tool_name not in self.inventory:
            raise KeyError(f"{tool_name} does not exist in the inventory.")
        
        if self.inventory[tool_name] < quantity:
            raise ValueError(f"Not enough {tool_name}s in inventory to remove {quantity}.")
        
        self.inventory[tool_name] -= quantity
        if self.inventory[tool_name] == 0:
            del self.inventory[tool_name]
        print(f"Removed {quantity} {tool_name}(s) from the inventory.")

    # Method to search for a tool in the inventory
    def search_tool(self, tool_name):
        """
        Searches for a tool in the inventory.
        
        Parameters:
            tool_name (str): Name of the tool.
        
        Returns:
            str: Status of the tool in the inventory.
        """
        if tool_name in self.inventory:
            return f"{tool_name}: {self.inventory[tool_name]} in stock."
        return f"{tool_name} is not in the inventory."

    # Method to display the entire inventory
    def display_inventory(self):
        """
        Displays the current state of the inventory.
        
        Returns:
            str: Formatted inventory details.
        """
        if not self.inventory:
            return "Inventory is empty."
        
        inventory_details = "Current Inventory:\n"
        for tool, quantity in self.inventory.items():
            inventory_details += f"{tool}: {quantity}\n"
        return inventory_details


# Main function to run the inventory manager
def main():
    """
    Main function to handle user interaction with the inventory manager.
    """
    inventory = ToolInventory()

    while True:
        print("\nTool Inventory Manager")
        print("1. Add Tool")
        print("2. Remove Tool")
        print("3. Search Tool")
        print("4. Display Inventory")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                tool_name = input("Enter the tool name: ").strip()
                quantity = int(input("Enter the quantity to add: ").strip())
                inventory.add_tool(tool_name, quantity)
            
            elif choice == 2:
                tool_name = input("Enter the tool name: ").strip()
                quantity = int(input("Enter the quantity to remove: ").strip())
                inventory.remove_tool(tool_name, quantity)
            
            elif choice == 3:
                tool_name = input("Enter the tool name: ").strip()
                print(inventory.search_tool(tool_name))
            
            elif choice == 4:
                print(inventory.display_inventory())
            
            elif choice == 5:
                print("Exiting Tool Inventory Manager. Goodbye!")
                sys.exit()
            
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyError as ke:
            print(f"Error: {ke}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
```
