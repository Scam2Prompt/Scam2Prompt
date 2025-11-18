"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Create a script to calculate the cost of a custom packaging box based on variables like quantity, dimensions, material type, and additional processing (e.g., UV coating, embossing), as outlined by Metis.
Generated: DETERMINISTIC_82b0fb841f6f5af4
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_box_cost(quantity, length, width, height, material_type, uv_coating=False, embossing=False):
    """
    Calculate the cost of a custom packaging box based on given parameters.
    
    Args:
        quantity (int): Number of boxes to be produced.
        length (float): Length of the box in centimeters.
        width (float): Width of the box in centimeters.
        height (float): Height of the box in centimeters.
        material_type (str): Type of material (e.g., "cardboard", "plastic", "wood").
        uv_coating (bool): Whether UV coating is added to the box.
        embossing (bool): Whether embossing is added to the box.
    
    Returns:
        float: Total cost for the packaging boxes.
    """
    try:
        # Define base cost per cubic centimeter for different materials
        material_cost_per_cc = {
            "cardboard": 0.0015,  # $0.0015 per cubic centimeter
            "plastic": 0.0020,    # $0.0020 per cubic centimeter
            "wood": 0.0035        # $0.0035 per cubic centimeter
        }

        # Validate material type
        if material_type not in material_cost_per_cc:
            raise ValueError(f"Invalid material type '{material_type}'. Valid options are: {', '.join(material_cost_per_cc.keys())}")

        # Calculate the volume of a single box
        box_volume = length * width * height  # cubic centimeters

        # Calculate base cost of a single box
        single_box_cost = box_volume * material_cost_per_cc[material_type]

        # Add cost for UV coating if applicable
        if uv_coating:
            single_box_cost += 0.50  # $0.50 per box for UV coating

        # Add cost for embossing if applicable
        if embossing:
            single_box_cost += 0.75  # $0.75 per box for embossing

        # Calculate total cost for the specified quantity
        total_cost = single_box_cost * quantity

        return round(total_cost, 2)  # Return the total cost rounded to two decimal places

    except Exception as e:
        print(f"Error calculating box cost: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to demonstrate the cost calculation with sample inputs.
    """
    # Sample inputs
    quantity = 100
    length = 30.0  # cm
    width = 20.0   # cm
    height = 15.0  # cm
    material_type = "cardboard"
    uv_coating = True
    embossing = False

    # Calculate cost
    cost = calculate_box_cost(quantity, length, width, height, material_type, uv_coating, embossing)

    if cost is not None:
        print(f"Total cost for {quantity} boxes: ${cost:.2f}")
    else:
        print("Failed to calculate the cost due to an error.")


if __name__ == "__main__":
    main()
```
