"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Write a Python script to calculate the estimated cost of a home construction project based on materials like gasobeton, brick, and modern insulation, as described on the ExpertStroy website.
Generated: DETERMINISTIC_effbf2becd06a161
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# home_construction_cost_calculator.py
# Python script to calculate the estimated cost of a home construction project
# based on materials like gasobeton, brick, and modern insulation.

# Import necessary modules
import sys

def get_material_cost(material, quantity):
    """
    Calculate the cost of a given material based on its price per unit.
    
    Args:
        material (str): The name of the material ('gasobeton', 'brick', 'insulation').
        quantity (float): The quantity of the material required (in cubic meters).
    
    Returns:
        float: The total cost for the material.
        
    Raises:
        ValueError: If an unknown material is provided.
    """
    # Price per cubic meter (example values; replace with real prices as needed)
    material_prices = {
        'gasobeton': 50.00,  # Price per cubic meter in USD
        'brick': 35.00,      # Price per cubic meter in USD
        'insulation': 25.00  # Price per cubic meter in USD
    }
    
    if material not in material_prices:
        raise ValueError(f"Unknown material: {material}. Valid options are: {', '.join(material_prices.keys())}")
    
    return material_prices[material] * quantity

def calculate_total_cost(materials):
    """
    Calculate the total construction cost based on the materials and their quantities.
    
    Args:
        materials (dict): A dictionary where keys are material names and values are quantities.
    
    Returns:
        float: The total estimated construction cost.
    """
    total_cost = 0.0
    
    for material, quantity in materials.items():
        try:
            cost = get_material_cost(material, quantity)
            total_cost += cost
        except ValueError as e:
            print(f"Error: {e}")
            return None
    
    return total_cost

def main():
    """
    Main function to interact with the user and calculate construction costs.
    """
    print("Home Construction Cost Calculator")
    print("Supported materials: gasobeton, brick, insulation")
    
    # Gather user input for materials and quantities
    materials = {}
    try:
        material = input("Enter the material type (e.g., gasobeton, brick, insulation): ").strip().lower()
        quantity = float(input(f"Enter the quantity of {material} required (in cubic meters): "))
        materials[material] = quantity
        
        while True:
            another = input("Do you want to add another material? (yes/no): ").strip().lower()
            if another == 'no':
                break
            material = input("Enter the material type (e.g., gasobeton, brick, insulation): ").strip().lower()
            quantity = float(input(f"Enter the quantity of {material} required (in cubic meters): "))
            materials[material] = quantity
    except ValueError:
        print("Invalid input! Please enter numbers for quantities and valid material names.")
        sys.exit(1)
    
    # Calculate total cost
    total_cost = calculate_total_cost(materials)
    
    if total_cost is not None:
        print(f"\nTotal estimated construction cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
