"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generate-digital.com
Prompt: Create a function to generate a digital rate card that provides a value matrix for inventory, supporting discussions around intellectual property and partner value, based on Generate Digital's methodology.
Generated: DETERMINISTIC_a2088a43f2a280b1
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

def generate_rate_card(inventory_items, ip_values, partner_values):
    """
    Generates a digital rate card as a value matrix for inventory.
    
    Parameters:
        inventory_items (list of str): A list of inventory items.
        ip_values (dict): A dictionary mapping inventory items to their intellectual property values.
        partner_values (dict): A dictionary mapping inventory items to their partner values.
        
    Returns:
        pd.DataFrame: A DataFrame representing the digital rate card.
        
    Raises:
        ValueError: If any inventory item is not found in the IP or partner values.
    """
    
    # Validate inputs
    for item in inventory_items:
        if item not in ip_values:
            raise ValueError(f"Intellectual property value for '{item}' not found.")
        if item not in partner_values:
            raise ValueError(f"Partner value for '{item}' not found.")
    
    # Create a data structure to hold values
    data = {
        'Inventory Item': inventory_items,
        'Intellectual Property Value': [ip_values[item] for item in inventory_items],
        'Partner Value': [partner_values[item] for item in inventory_items]
    }
    
    # Create DataFrame
    rate_card_df = pd.DataFrame(data)
    
    # Compute a combined value for further analysis
    rate_card_df['Combined Value'] = rate_card_df['Intellectual Property Value'] + rate_card_df['Partner Value']
    
    # Set index to Inventory Item for better readability
    rate_card_df.set_index('Inventory Item', inplace=True)
    
    return rate_card_df

# Example usage
if __name__ == "__main__":
    inventory = ['Item A', 'Item B', 'Item C']
    intellectual_property_values = {
        'Item A': 1000,
        'Item B': 1500,
        'Item C': 2000
    }
    partner_values = {
        'Item A': 500,
        'Item B': 700,
        'Item C': 900
    }
    
    try:
        rate_card = generate_rate_card(inventory, intellectual_property_values, partner_values)
        print(rate_card)
    except ValueError as e:
        print(f"Error: {e}")
```
