"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabriz3dprint.ir
Prompt: Write Python code to calculate the cost of 3D printing a model using FDM technology, considering layer thickness between 50 to 300 microns and material types like PLA or ABS, as described on https://tabriz3dprint.ir.
Generated: DETERMINISTIC_591966fd887a16fb
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define constants for material costs (per gram) and layer thickness cost modifiers
MATERIAL_COSTS = {
    "PLA": 0.05,  # Cost per gram in USD for PLA
    "ABS": 0.07   # Cost per gram in USD for ABS
}

LAYER_THICKNESS_COST_MODIFIERS = {
    50: 1.5,  # Modifier for 50 microns
    100: 1.2,  # Modifier for 100 microns
    200: 1.0,  # Modifier for 200 microns
    300: 0.8   # Modifier for 300 microns
}

def calculate_print_cost(material_type, weight_in_grams, layer_thickness):
    """
    Calculate the cost of 3D printing a model using FDM technology.

    Parameters:
    material_type (str): Type of material (PLA or ABS).
    weight_in_grams (float): Weight of the model in grams.
    layer_thickness (int): Layer thickness in microns (50, 100, 200, or 300).

    Returns:
    float: Total cost of printing the model in USD.
    """
    # Validate material type
    if material_type not in MATERIAL_COSTS:
        raise ValueError(f"Invalid material type. Choose between: {', '.join(MATERIAL_COSTS.keys())}")
    
    # Validate layer thickness
    if layer_thickness not in LAYER_THICKNESS_COST_MODIFIERS:
        raise ValueError(f"Invalid layer thickness. Choose between: {', '.join(map(str, LAYER_THICKNESS_COST_MODIFIERS.keys()))}")
    
    # Calculate the base material cost
    material_cost = MATERIAL_COSTS[material_type] * weight_in_grams
    
    # Apply the layer thickness cost modifier
    layer_thickness_modifier = LAYER_THICKNESS_COST_MODIFIERS[layer_thickness]
    total_cost = material_cost * layer_thickness_modifier
    
    return total_cost

def main():
    """
    Main function to interactively calculate 3D printing costs.
    """
    try:
        # Get user input
        material_type = input("Enter the material type (PLA or ABS): ").strip().upper()
        layer_thickness = int(input("Enter the layer thickness in microns (50, 100, 200, or 300): "))
        weight_in_grams = float(input("Enter the weight of the model in grams: "))
        
        # Calculate and display the cost
        cost = calculate_print_cost(material_type, weight_in_grams, layer_thickness)
        print(f"The total cost of printing the model is: ${cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
