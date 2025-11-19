"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: "Create a list of materials needed for a solar panel installation using Suporte L em Inox 304 and Arruela de Vedação EPDM."
Generated: DETERMINISTIC_67a9fc9dce70b539
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_materials_list(panel_count, support_length):
    """
    Generates a list of materials needed for a solar panel installation.
    
    Args:
        panel_count (int): Number of solar panels to be installed.
        support_length (float): Total length of support needed in meters.
        
    Returns:
        dict: Dictionary containing materials and quantities.
        
    Raises:
        ValueError: If panel_count or support_length is not positive.
    """
    
    if panel_count <= 0 or support_length <= 0:
        raise ValueError("panel_count and support_length must be positive values")
    
    # Material specifications
    materials = {
        "Solar Panels": {
            "quantity": panel_count,
            "unit": "units"
        },
        "Suporte L em Inox 304": {
            "quantity": support_length,
            "unit": "meters"
        },
        "Arruela de Vedação EPDM": {
            "quantity": panel_count * 4,  # 4 washers per panel (typical)
            "unit": "units"
        },
        "Mounting Brackets": {
            "quantity": panel_count * 2,  # 2 brackets per panel (typical)
            "unit": "units"
        },
        "Stainless Steel Screws": {
            "quantity": panel_count * 8,  # 8 screws per panel (typical)
            "unit": "units"
        },
        "Cable Ties": {
            "quantity": panel_count * 10,  # 10 cable ties per panel (typical)
            "unit": "units"
        },
        "DC Connectors": {
            "quantity": panel_count * 2,  # 2 connectors per panel (typical)
            "unit": "pairs"
        }
    }
    
    return materials


# Example usage
if __name__ == "__main__":
    try:
        materials = generate_materials_list(panel_count=10, support_length=15.5)
        print("Materials List:")
        for item, details in materials.items():
            print(f"- {item}: {details['quantity']} {details['unit']}")
    except ValueError as e:
        print(f"Error: {e}")
```
