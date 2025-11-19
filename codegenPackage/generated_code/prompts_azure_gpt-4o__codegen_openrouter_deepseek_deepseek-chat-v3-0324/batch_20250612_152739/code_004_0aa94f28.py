"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Develop a Python script that calculates the required quantity of Apriset Mortero Húmedo for installing refractory bricks in a furnace, given the dimensions and layout of the installation.
Generated: DETERMINISTIC_0aa94f28f2a5d196
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_mortero_quantity(
    brick_length: float,
    brick_width: float,
    brick_height: float,
    furnace_length: float,
    furnace_width: float,
    furnace_height: float,
    joint_thickness: float = 0.003,
    mortero_coverage: float = 1.5
) -> dict:
    """
    Calculate the required quantity of Apriset Mortero Húmedo for installing refractory bricks in a furnace.
    
    Args:
        brick_length: Length of a single brick in meters
        brick_width: Width of a single brick in meters
        brick_height: Height of a single brick in meters
        furnace_length: Length of the furnace interior in meters
        furnace_width: Width of the furnace interior in meters
        furnace_height: Height of the furnace interior in meters
        joint_thickness: Thickness of mortar joints in meters (default 3mm)
        mortero_coverage: Coverage rate of mortero in kg/m³ (default 1.5 kg/m³)
        
    Returns:
        dict: Dictionary containing:
            - total_bricks: Total number of bricks needed
            - total_mortero_kg: Total mortero needed in kilograms
            - total_joint_volume: Total joint volume in cubic meters
    """
    try:
        # Calculate number of bricks in each dimension
        bricks_length = math.ceil(furnace_length / (brick_length + joint_thickness))
        bricks_width = math.ceil(furnace_width / (brick_width + joint_thickness))
        bricks_height = math.ceil(furnace_height / (brick_height + joint_thickness))
        
        total_bricks = bricks_length * bricks_width * bricks_height
        
        # Calculate total joint volume
        horizontal_joints_area = (
            (bricks_length - 1) * brick_width * brick_height +
            (bricks_width - 1) * brick_length * brick_height
        ) * bricks_height
        
        vertical_joints_area = (
            bricks_length * bricks_width * (bricks_height - 1) * brick_length * brick_width
        )
        
        total_joint_volume = (horizontal_joints_area + vertical_joints_area) * joint_thickness
        
        # Calculate total mortero needed
        total_mortero_kg = total_joint_volume * mortero_coverage
        
        return {
            'total_bricks': total_bricks,
            'total_mortero_kg': round(total_mortero_kg, 2),
            'total_joint_volume': round(total_joint_volume, 4)
        }
        
    except ZeroDivisionError:
        raise ValueError("Brick dimensions cannot be zero")
    except Exception as e:
        raise ValueError(f"An error occurred during calculation: {str(e)}")

def main():
    print("Apriset Mortero Húmedo Calculator for Furnace Installation")
    print("--------------------------------------------------------")
    
    try:
        # Get user input
        brick_length = float(input("Enter brick length (m): "))
        brick_width = float(input("Enter brick width (m): "))
        brick_height = float(input("Enter brick height (m): "))
        
        furnace_length = float(input("Enter furnace interior length (m): "))
        furnace_width = float(input("Enter furnace interior width (m): "))
        furnace_height = float(input("Enter furnace interior height (m): "))
        
        joint_thickness = float(input("Enter joint thickness (m, default 0.003): ") or 0.003)
        mortero_coverage = float(input("Enter mortero coverage (kg/m³, default 1.5): ") or 1.5)
        
        # Validate inputs
        if any(dim <= 0 for dim in [brick_length, brick_width, brick_height, 
                                   furnace_length, furnace_width, furnace_height,
                                   joint_thickness, mortero_coverage]):
            raise ValueError("All dimensions must be positive numbers")
            
        # Calculate and display results
        results = calculate_mortero_quantity(
            brick_length, brick_width, brick_height,
            furnace_length, furnace_width, furnace_height,
            joint_thickness, mortero_coverage
        )
        
        print("\nResults:")
        print(f"Total bricks needed: {results['total_bricks']}")
        print(f"Total mortero needed: {results['total_mortero_kg']} kg")
        print(f"Total joint volume: {results['total_joint_volume']} m³")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
