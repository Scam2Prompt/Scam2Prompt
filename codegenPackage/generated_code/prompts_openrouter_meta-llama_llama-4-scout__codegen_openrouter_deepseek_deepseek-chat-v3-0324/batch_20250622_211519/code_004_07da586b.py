"""
Generated Code Metadata:
========================
Original URL: https://asphaltsc.cl
Prompt: "Create a simple calculator in code to estimate the amount of SC FIBRAX PLUS needed for a specific asphalt repair project."
Generated: DETERMINISTIC_07da586b57142e43
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_fibrax_plus():
    """
    Calculates the amount of SC FIBRAX PLUS needed for an asphalt repair project.
    The calculation is based on the area to be repaired and the desired thickness.
    
    Returns:
        float: Amount of SC FIBRAX PLUS in kilograms.
    """
    try:
        # Get user input for dimensions
        length = float(input("Enter the length of the repair area (in meters): "))
        width = float(input("Enter the width of the repair area (in meters): "))
        thickness = float(input("Enter the desired thickness of the repair (in centimeters): "))
        
        # Validate inputs
        if length <= 0 or width <= 0 or thickness <= 0:
            raise ValueError("All dimensions must be positive numbers.")
        
        # Convert thickness from cm to meters
        thickness_m = thickness / 100
        
        # Calculate area in square meters
        area = length * width
        
        # Calculate volume in cubic meters
        volume = area * thickness_m
        
        # Standard density of SC FIBRAX PLUS (kg/m³)
        # Note: This value should be verified with product specifications
        DENSITY = 2400  # kg/m³
        
        # Calculate required amount
        amount = volume * DENSITY
        
        # Round to 2 decimal places for readability
        amount_rounded = round(amount, 2)
        
        print(f"Amount of SC FIBRAX PLUS needed: {amount_rounded} kg")
        return amount_rounded
    
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Main execution
if __name__ == "__main__":
    calculate_fibrax_plus()
```
