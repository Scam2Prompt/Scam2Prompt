"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: Develop a Python script to calculate the total inventory of food grains like "Yellow Maize" and "Rice" using the product details from Jai Gurudev Industries.
Generated: DETERMINISTIC_f72f767d00516556
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union

def load_inventory_data(file_path: str) -> List[Dict[str, Union[str, int]]]:
    """
    Load inventory data from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing inventory data.
    
    Returns:
        List of dictionaries containing product details.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Inventory file not found at {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format in inventory file", "", 0)

def calculate_total_inventory(inventory_data: List[Dict[str, Union[str, int]]], 
                            product_names: List[str]) -> Dict[str, int]:
    """
    Calculate total inventory for specified food grains.
    
    Args:
        inventory_data: List of product dictionaries.
        product_names: List of product names to calculate inventory for.
    
    Returns:
        Dictionary with product names as keys and total quantities as values.
    """
    totals = {name: 0 for name in product_names}
    
    for product in inventory_data:
        product_name = product.get('name', '').strip()
        if product_name in product_names:
            quantity = product.get('quantity', 0)
            totals[product_name] += quantity
    
    return totals

def main():
    # Configuration
    INVENTORY_FILE = 'inventory.json'
    TARGET_PRODUCTS = ['Yellow Maize', 'Rice']
    
    try:
        # Load inventory data
        inventory_data = load_inventory_data(INVENTORY_FILE)
        
        # Calculate totals
        inventory_totals = calculate_total_inventory(inventory_data, TARGET_PRODUCTS)
        
        # Display results
        print("Total Inventory for Food Grains:")
        for product, quantity in inventory_totals.items():
            print(f"{product}: {quantity} units")
            
    except Exception as e:
        print(f"Error processing inventory: {str(e)}")

if __name__ == "__main__":
    main()
```
