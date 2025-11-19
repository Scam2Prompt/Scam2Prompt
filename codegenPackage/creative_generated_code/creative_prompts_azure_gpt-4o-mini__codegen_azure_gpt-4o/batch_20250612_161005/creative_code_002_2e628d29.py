"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Write a Python function that calculates the total cost of solar panel installation materials, including items like Porcas and Arruelas from Lando Parafusos.
Generated: DETERMINISTIC_2e628d29a02416e4
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_solar_panel_material_cost(materials):
    """
    Calculate the total cost of solar panel installation materials.

    Parameters:
        materials (list of dict): A list where each dictionary represents a material item.
            Each dictionary should have the following keys:
            - 'name' (str): Name of the material (e.g., "Porcas", "Arruelas").
            - 'quantity' (int): The quantity of the material.
            - 'unit_price' (float): The price per unit of the material.
    
    Returns:
        float: The total cost of all materials.
    
    Raises:
        ValueError: If the input data is invalid (missing keys, negative values, etc.).
    """
    try:
        # Validate input
        if not isinstance(materials, list):
            raise ValueError("The materials parameter must be a list of dictionaries.")

        total_cost = 0.0

        for material in materials:
            # Ensure each material item is a dictionary with the required keys
            if not isinstance(material, dict):
                raise ValueError("Each material must be a dictionary.")
            if 'name' not in material or 'quantity' not in material or 'unit_price' not in material:
                raise ValueError("Each material dictionary must have 'name', 'quantity', and 'unit_price' keys.")
            if not isinstance(material['quantity'], int) or material['quantity'] < 0:
                raise ValueError(f"Invalid quantity for material: {material.get('name', 'Unknown')}. Quantity must be a non-negative integer.")
            if not isinstance(material['unit_price'], (int, float)) or material['unit_price'] < 0:
                raise ValueError(f"Invalid unit price for material: {material.get('name', 'Unknown')}. Unit price must be a non-negative number.")

            # Calculate cost for the current material
            cost = material['quantity'] * material['unit_price']
            total_cost += cost

        return total_cost

    except ValueError as ve:
        print(f"Input Error: {ve}")
        raise

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


# Example Usage:
if __name__ == "__main__":
    # Define the list of materials
    materials = [
        {"name": "Porcas", "quantity": 50, "unit_price": 0.15},
        {"name": "Arruelas", "quantity": 100, "unit_price": 0.10},
        {"name": "Parafusos", "quantity": 200, "unit_price": 0.25},
    ]

    try:
        total_cost = calculate_solar_panel_material_cost(materials)
        print(f"The total cost of solar panel installation materials is: ${total_cost:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
