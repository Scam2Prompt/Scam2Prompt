"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Write a script to automate the addition of new items to an artist's online sales collection, adhering to the pricing structure described in the VIP Management plans.
Generated: DETERMINISTIC_47ebf59638cfc3ad
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Constants for VIP Management pricing plans
PRICING_PLANS = {
    "standard": 1.0,  # No price increase
    "silver": 1.2,    # 20% price increase
    "gold": 1.5,      # 50% price increase
}

# Path to the inventory file
INVENTORY_FILE = "inventory.json"

def load_inventory(file_path):
    """
    Load the inventory from a JSON file.

    :param file_path: Path to the inventory file.
    :return: Inventory data as a dictionary.
    """
    if not os.path.exists(file_path):
        # Return an empty dictionary if the file doesn't exist
        return {}
    
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading inventory: {e}")
        return {}

def save_inventory(file_path, inventory):
    """
    Save the inventory data to a JSON file.

    :param file_path: Path to the inventory file.
    :param inventory: Inventory data as a dictionary.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(inventory, file, indent=4)
    except IOError as e:
        print(f"Error saving inventory: {e}")

def add_item_to_inventory(name, base_price, plan, inventory):
    """
    Add a new item to the inventory.

    :param name: Name of the item.
    :param base_price: Base price of the item.
    :param plan: VIP pricing plan ("standard", "silver", or "gold").
    :param inventory: Inventory dictionary.
    :return: Updated inventory.
    """
    if plan not in PRICING_PLANS:
        raise ValueError(f"Invalid pricing plan: {plan}")
    
    # Calculate the price according to the selected pricing plan
    adjusted_price = round(base_price * PRICING_PLANS[plan], 2)
    
    # Add the item to the inventory
    inventory[name] = {
        "base_price": base_price,
        "adjusted_price": adjusted_price,
        "plan": plan
    }
    
    return inventory

def main():
    print("Welcome to the Artist's Online Sales Collection Manager!")
    
    inventory = load_inventory(INVENTORY_FILE)
    
    while True:
        try:
            # Gather item details from the user
            name = input("Enter the name of the item (or 'exit' to quit): ").strip()
            if name.lower() == 'exit':
                break
            
            base_price = float(input("Enter the base price of the item: ").strip())
            plan = input("Enter the VIP plan ('standard', 'silver', 'gold'): ").strip().lower()
            
            # Update inventory
            inventory = add_item_to_inventory(name, base_price, plan, inventory)
            print(f"Item '{name}' added successfully!")
        
        except ValueError as e:
            print(f"Error: {e}")
        
        # Save the updated inventory
        save_inventory(INVENTORY_FILE, inventory)
    
    print("Exiting the manager. Goodbye!")

if __name__ == "__main__":
    main()
```
