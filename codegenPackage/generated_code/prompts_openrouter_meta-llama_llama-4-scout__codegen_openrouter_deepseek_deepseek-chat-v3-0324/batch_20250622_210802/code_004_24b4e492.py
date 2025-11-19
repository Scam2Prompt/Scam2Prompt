"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: "Generate a list of materials needed for a metal false ceiling installation, including lay-in metal ceiling and clip-in metal ceiling options."
Generated: DETERMINISTIC_24b4e492d28ef1c9
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_materials_list(ceiling_type):
    """
    Generates a list of materials needed for metal false ceiling installation.
    
    Args:
        ceiling_type (str): Type of ceiling ('lay_in' or 'clip_in')
    
    Returns:
        dict: Dictionary containing materials list and quantities
    
    Raises:
        ValueError: If ceiling_type is not 'lay_in' or 'clip_in'
    """
    common_materials = {
        'main_tees': {'description': 'Main support beams', 'unit': 'pieces'},
        'cross_tees': {'description': 'Secondary support beams', 'unit': 'pieces'},
        'wall_angles': {'description': 'Perimeter framing', 'unit': 'linear feet'},
        'hanger_wires': {'description': 'Suspension wires', 'unit': 'pieces'},
        'hanger_clips': {'description': 'Wire attachment clips', 'unit': 'pieces'},
        'fasteners': {'description': 'Screws and anchors', 'unit': 'pieces'},
        'ceiling_tiles': {'description': 'Metal ceiling panels', 'unit': 'pieces'}
    }
    
    if ceiling_type == 'lay_in':
        materials = {
            **common_materials,
            'tile_support_clips': {'description': 'Support clips for lay-in tiles', 'unit': 'pieces'},
            'reveal_moldings': {'description': 'Edge trim moldings', 'unit': 'linear feet'}
        }
    elif ceiling_type == 'clip_in':
        materials = {
            **common_materials,
            'clip_in_channels': {'description': 'Special channels for clip-in system', 'unit': 'linear feet'},
            'spring_clips': {'description': 'Retaining clips for panels', 'unit': 'pieces'}
        }
    else:
        raise ValueError("Invalid ceiling type. Must be 'lay_in' or 'clip_in'")
    
    return materials

def calculate_quantities(materials_list, area):
    """
    Calculates approximate quantities based on ceiling area.
    
    Args:
        materials_list (dict): Materials list from generate_materials_list()
        area (float): Ceiling area in square feet
    
    Returns:
        dict: Materials list with estimated quantities
    """
    quantities = materials_list.copy()
    
    # Main tees: 1 per 4 feet of width
    quantities['main_tees']['quantity'] = max(2, round(area ** 0.5 / 4))
    
    # Cross tees: 1 per 2 feet of length
    quantities['cross_tees']['quantity'] = max(2, round(area ** 0.5 / 2))
    
    # Wall angles: perimeter length
    perimeter = 4 * (area ** 0.5)
    quantities['wall_angles']['quantity'] = perimeter
    
    # Hanger wires: 1 per 4 sqft
    quantities['hanger_wires']['quantity'] = max(4, round(area / 4))
    
    # Hanger clips: same as hanger wires
    quantities['hanger_clips']['quantity'] = quantities['hanger_wires']['quantity']
    
    # Fasteners: 1 per 2 linear feet of perimeter
    quantities['fasteners']['quantity'] = round(perimeter / 2)
    
    # Ceiling tiles: based on panel size (assuming 2x2 ft panels)
    panel_area = 4  # 2x2 ft panels
    quantities['ceiling_tiles']['quantity'] = round(area / panel_area)
    
    # Type-specific calculations
    if 'tile_support_clips' in quantities:
        quantities['tile_support_clips']['quantity'] = quantities['ceiling_tiles']['quantity'] * 4
    
    if 'reveal_moldings' in quantities:
        quantities['reveal_moldings']['quantity'] = perimeter
    
    if 'clip_in_channels' in quantities:
        quantities['clip_in_channels']['quantity'] = quantities['main_tees']['quantity'] * (area ** 0.5)
    
    if 'spring_clips' in quantities:
        quantities['spring_clips']['quantity'] = quantities['ceiling_tiles']['quantity'] * 4
    
    return quantities

def print_materials_list(materials):
    """
    Prints formatted materials list with quantities.
    
    Args:
        materials (dict): Materials list with quantities
    """
    print("\nMaterials List:")
    print("----------------------------")
    for item, details in materials.items():
        print(f"{item.replace('_', ' ').title()}:")
        print(f"  Description: {details['description']}")
        print(f"  Quantity: {details.get('quantity', 'N/A')} {details['unit']}")
        print("----------------------------")

# Example usage
if __name__ == "__main__":
    try:
        ceiling_type = input("Enter ceiling type (lay_in or clip_in): ").lower()
        area = float(input("Enter ceiling area in square feet: "))
        
        materials = generate_materials_list(ceiling_type)
        materials_with_quantities = calculate_quantities(materials, area)
        print_materials_list(materials_with_quantities)
        
    except ValueError as e:
        print(f"Error: {e}")
```
