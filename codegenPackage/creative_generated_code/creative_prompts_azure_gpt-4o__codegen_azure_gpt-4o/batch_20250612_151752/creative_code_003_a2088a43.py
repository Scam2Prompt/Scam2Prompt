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

def generate_rate_card(inventory, base_rates, multipliers):
    """
    Generates a digital rate card matrix based on inventory, base rates, and multipliers.

    Parameters:
        inventory (list of str): List of inventory items (e.g., ad placements, content types).
        base_rates (dict): Dictionary of base rates for each inventory item. 
                           Keys must match items in 'inventory' and values must be numeric.
        multipliers (dict): Dictionary of multipliers for additional value dimensions, 
                            such as intellectual property, partner value, etc. 
                            Keys represent dimensions and values are numeric multipliers.

    Returns:
        pd.DataFrame: A rate card matrix with calculated values based on the input data.
    """
    # Validate inputs
    if not inventory or not isinstance(inventory, list):
        raise ValueError("Inventory must be a non-empty list.")
    if not base_rates or not isinstance(base_rates, dict):
        raise ValueError("Base rates must be a non-empty dictionary.")
    if not multipliers or not isinstance(multipliers, dict):
        raise ValueError("Multipliers must be a non-empty dictionary.")
    if not all(item in base_rates for item in inventory):
        raise ValueError("Base rates must contain rates for all inventory items.")

    # Initialize matrix
    rate_card_data = []

    for item in inventory:
        # Get base rate for the inventory item
        base_rate = base_rates[item]

        # Calculate values for each multiplier dimension
        item_row = {"Inventory": item, "Base Rate": base_rate}
        for dimension, multiplier in multipliers.items():
            item_row[dimension] = base_rate * multiplier  # Adjust base rate by multiplier

        rate_card_data.append(item_row)

    # Create a pandas DataFrame for the rate card
    rate_card_df = pd.DataFrame(rate_card_data)

    # Sort the DataFrame for better readability (optional)
    rate_card_df = rate_card_df.sort_values(by="Base Rate", ascending=False).reset_index(drop=True)

    return rate_card_df


# Example usage:
if __name__ == "__main__":
    # Define inventory items
    inventory_items = ["Banner Ad", "Video Ad", "Sponsored Article"]

    # Define base rates for each inventory item
    base_rates = {
        "Banner Ad": 500,
        "Video Ad": 1200,
        "Sponsored Article": 800
    }

    # Define multipliers for various value dimensions
    value_multipliers = {
        "IP Value": 1.2,  # Intellectual Property multiplier
        "Partner Value": 1.5,  # Partner Value multiplier
        "Audience Engagement": 1.3  # Audience Engagement multiplier
    }

    # Generate the rate card
    rate_card = generate_rate_card(inventory_items, base_rates, value_multipliers)
    print(rate_card)  # Display the rate card
```
