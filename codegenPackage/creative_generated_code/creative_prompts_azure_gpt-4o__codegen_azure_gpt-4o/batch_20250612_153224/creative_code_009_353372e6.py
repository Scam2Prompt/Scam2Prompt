"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Create a Python script to calculate the total weight of a bulk order of plexiglass sheets based on their thickness and dimensions, using the specifications provided by Bursa Pleksi Merkezi.
Generated: DETERMINISTIC_353372e6da89b89d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total weight of a bulk order of plexiglass sheets.

Plexiglass density: 1.19 g/cm³ (as per typical specifications from Bursa Pleksi Merkezi).

Formula:
Weight (grams) = Volume (cm³) * Density
Volume (cm³) = Length (cm) * Width (cm) * Thickness (cm)

This script accepts bulk order details (dimensions, thickness, and quantity of sheets)
and calculates the total weight in kilograms.
"""

def calculate_sheet_weight(length_cm, width_cm, thickness_cm):
    """
    Calculates the weight of a single plexiglass sheet based on its dimensions and thickness.

    Parameters:
    length_cm (float): Length of the sheet in cm.
    width_cm (float): Width of the sheet in cm.
    thickness_cm (float): Thickness of the sheet in cm.

    Returns:
    float: Weight of the sheet in grams.
    """
    try:
        # Plexiglass density in g/cm³
        density = 1.19
        # Calculate volume in cm³
        volume = length_cm * width_cm * thickness_cm
        # Calculate weight in grams
        weight_grams = volume * density
        return weight_grams
    except Exception as e:
        raise ValueError(f"Error calculating sheet weight: {e}")

def calculate_bulk_order_weight(order_list):
    """
    Calculates the total weight of a bulk order of plexiglass sheets.

    Parameters:
    order_list (list of dict): List of dictionaries where each dictionary contains:
        'length_cm' (float): Length of the sheet in cm.
        'width_cm' (float): Width of the sheet in cm.
        'thickness_cm' (float): Thickness of the sheet in cm.
        'quantity' (int): Number of sheets of this specification.

    Returns:
    float: Total weight of the bulk order in kilograms.
    """
    try:
        total_weight_grams = 0
        
        for order in order_list:
            # Validate order dictionary structure
            if not all(key in order for key in ('length_cm', 'width_cm', 'thickness_cm', 'quantity')):
                raise ValueError(f"Invalid order format: {order}")
            if order['quantity'] <= 0:
                raise ValueError(f"Quantity must be greater than 0: {order}")
            
            # Calculate weight for individual sheet and multiply by quantity
            sheet_weight = calculate_sheet_weight(
                length_cm=order['length_cm'],
                width_cm=order['width_cm'],
                thickness_cm=order['thickness_cm']
            )
            total_weight_grams += sheet_weight * order['quantity']
        
        # Convert total weight to kilograms
        total_weight_kg = total_weight_grams / 1000
        return total_weight_kg
    except Exception as e:
        raise ValueError(f"Error calculating bulk order weight: {e}")

if __name__ == "__main__":
    """
    Main entry point for the script. Collects user input and calculates the total weight of
    a bulk order.
    """
    try:
        # Example bulk order list for testing purposes
        # Replace these values with actual user input or data source
        bulk_order = [
            {"length_cm": 200, "width_cm": 100, "thickness_cm": 0.5, "quantity": 10},
            {"length_cm": 150, "width_cm": 75, "thickness_cm": 0.4, "quantity": 5},
            {"length_cm": 300, "width_cm": 100, "thickness_cm": 1.0, "quantity": 2}
        ]
        
        # Calculate total weight
        total_weight = calculate_bulk_order_weight(bulk_order)
        
        # Print the result
        print(f"Total weight of the bulk order: {total_weight:.2f} kg")
    except Exception as e:
        print(f"An error occurred: {e}")
```
