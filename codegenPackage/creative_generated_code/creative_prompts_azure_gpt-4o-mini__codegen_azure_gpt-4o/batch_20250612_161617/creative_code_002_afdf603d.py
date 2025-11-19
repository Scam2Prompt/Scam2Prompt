"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Write a Python script that simulates the estimation of costs for custom printed packaging based on the unique features highlighted on the Metis website.
Generated: DETERMINISTIC_afdf603dd2509f4d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def estimate_packaging_cost(dimensions, material, printing_color_count, quantity):
    """
    Estimate the cost of custom printed packaging.
    
    Args:
        dimensions (tuple): Dimensions of the packaging in format (length, width, height) in cm.
        material (str): Type of material ('cardboard', 'plastic', 'kraft').
        printing_color_count (int): Number of colors used in printing.
        quantity (int): Number of units to produce.
        
    Returns:
        float: Estimated total cost in USD.
    """
    
    try:
        # Validate inputs
        if not isinstance(dimensions, tuple) or len(dimensions) != 3:
            raise ValueError("Dimensions must be a tuple of three values: (length, width, height).")
        if material not in ['cardboard', 'plastic', 'kraft']:
            raise ValueError("Material must be one of: 'cardboard', 'plastic', 'kraft'.")
        if not isinstance(printing_color_count, int) or printing_color_count < 0:
            raise ValueError("Printing color count must be a non-negative integer.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Base cost factors
        material_cost = {
            'cardboard': 0.5,  # cost per cubic cm
            'plastic': 0.8,
            'kraft': 0.6
        }
        
        # Calculate volume (in cubic cm)
        length, width, height = dimensions
        volume = length * width * height
        
        # Calculate material cost
        base_material_cost = volume * material_cost[material]
        
        # Printing cost based on number of colors
        printing_cost_per_unit = 0.1 * printing_color_count
        
        # Quantity discounts
        if quantity >= 1000:
            discount = 0.15  # 15% discount for bulk orders
        elif quantity >= 500:
            discount = 0.10  # 10% discount
        elif quantity >= 100:
            discount = 0.05  # 5% discount
        else:
            discount = 0.0  # No discount
        
        # Calculate total cost
        total_cost = (base_material_cost + printing_cost_per_unit) * quantity
        total_cost -= total_cost * discount
        
        return round(total_cost, 2)

    except Exception as e:
        print(f"Error in cost estimation: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and simulate cost estimation.
    """
    print("Welcome to the Custom Packaging Cost Estimator!")
    
    try:
        # Gather user inputs
        length = float(input("Enter the length of the packaging (in cm): "))
        width = float(input("Enter the width of the packaging (in cm): "))
        height = float(input("Enter the height of the packaging (in cm): "))
        dimensions = (length, width, height)
        
        material = input("Enter the material ('cardboard', 'plastic', 'kraft'): ").strip().lower()
        printing_color_count = int(input("Enter the number of printing colors: "))
        quantity = int(input("Enter the quantity of units to produce: "))
        
        # Estimate cost
        estimated_cost = estimate_packaging_cost(dimensions, material, printing_color_count, quantity)
        
        if estimated_cost is not None:
            print(f"Estimated total cost: ${estimated_cost:.2f}")
        else:
            print("Failed to estimate cost due to invalid inputs.")
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
