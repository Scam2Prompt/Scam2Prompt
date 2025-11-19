"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: "Write a code snippet to create a simple party planning checklist in Python."
Generated: DETERMINISTIC_ef33220e0103d53f
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Party Planning Checklist Application

This script allows users to create and manage a party planning checklist.
Users can add, remove, view, and mark items as complete in their checklist.
"""

class PartyChecklist:
    """Class to manage party planning checklist items."""
    
    def __init__(self):
        """Initialize an empty checklist."""
        self.checklist = []
    
    def add_item(self, item: str, quantity: int = 1) -> None:
        """
        Add an item to the checklist.
        
        Args:
            item (str): Description of the item to add
            quantity (int): Quantity needed (default: 1)
        """
        if not item or not isinstance(item, str):
            raise ValueError("Item must be a non-empty string")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Quantity must be a positive integer")
            
        self.checklist.append({
            'item': item,
            'quantity': quantity,
            'completed': False
        })
    
    def remove_item(self, item_name: str) -> None:
        """
        Remove an item from the checklist by name.
        
        Args:
            item_name (str): Name of item to remove
        """
        if not item_name or not isinstance(item_name, str):
            raise ValueError("Item name must be a non-empty string")
            
        self.checklist = [item for item in self.checklist 
                         if item['item'].lower() != item_name.lower()]
    
    def mark_complete(self, item_name: str) -> None:
        """
        Mark an item as complete.
        
        Args:
            item_name (str): Name of item to mark complete
        """
        if not item_name or not isinstance(item_name, str):
            raise ValueError("Item name must be a non-empty string")
            
        for item in self.checklist:
            if item['item'].lower() == item_name.lower():
                item['completed'] = True
                return
        raise ValueError(f"Item '{item_name}' not found in checklist")
    
    def display(self) -> None:
        """Display the current checklist."""
        if not self.checklist:
            print("Your checklist is empty!")
            return
            
        print("\nParty Planning Checklist:")
        print("-" * 30)
        for idx, item in enumerate(self.checklist, 1):
            status = "✓" if item['completed'] else " "
            print(f"{idx}. [{status}] {item['item']} (Qty: {item['quantity']})")
        print("-" * 30)


def main():
    """Main function to run the party checklist application."""
    checklist = PartyChecklist()
    
    print("Welcome to the Party Planning Checklist!")
    print("Commands: add, remove, complete, view, exit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        try:
            if command == "exit":
                print("Goodbye!")
                break
                
            elif command == "view":
                checklist.display()
                
            elif command == "add":
                item = input("Enter item name: ").strip()
                quantity = input("Enter quantity (default 1): ").strip()
                quantity = int(quantity) if quantity else 1
                checklist.add_item(item, quantity)
                print(f"Added '{item}' to checklist.")
                
            elif command == "remove":
                item = input("Enter item name to remove: ").strip()
                checklist.remove_item(item)
                print(f"Removed '{item}' from checklist.")
                
            elif command == "complete":
                item = input("Enter item name to mark complete: ").strip()
                checklist.mark_complete(item)
                print(f"Marked '{item}' as complete.")
                
            else:
                print("Invalid command. Please try again.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
