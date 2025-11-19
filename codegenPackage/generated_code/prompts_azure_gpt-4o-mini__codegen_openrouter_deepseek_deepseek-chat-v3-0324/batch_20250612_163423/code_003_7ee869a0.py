"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Develop a code snippet that calculates the amount of mortar needed for repointing based on the dimensions of a brick wall, similar to the services provided by Premier Pointing.
Generated: DETERMINISTIC_7ee869a0d56e39cf
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mortar Calculator for Repointing Brick Walls

This script calculates the amount of mortar required for repointing a brick wall
based on its dimensions and the specified joint size. The calculation follows
industry-standard formulas and provides results in cubic meters and bags of mortar mix.

Assumptions:
- Standard brick size: 215mm x 102.5mm x 65mm (UK standard)
- Mortar joint depth is typically half the brick height (32.5mm)

Inputs:
- Wall dimensions (width, height, thickness) in meters
- Joint width in millimeters
- Mortar mix coverage (bags per cubic meter)

Outputs:
- Mortar volume required in cubic meters
- Number of mortar mix bags required
"""

def calculate_mortar_volume(width, height, thickness, joint_width_mm):
    """
    Calculate mortar volume required for repointing a brick wall.

    Args:
        width (float): Wall width in meters
        height (float): Wall height in meters
        thickness (float): Wall thickness in meters
        joint_width_mm (float): Mortar joint width in millimeters

    Returns:
        float: Mortar volume in cubic meters
    """
    try:
        # Convert all dimensions to consistent units (meters)
        joint_width = joint_width_mm / 1000  # Convert mm to meters

        # Standard brick dimensions (UK) in meters
        brick_length = 0.215
        brick_height = 0.065
        brick_width = 0.1025

        # Calculate number of bricks in the wall
        bricks_per_row = width / brick_length
        rows = height / brick_height

        # Calculate total mortar joint length (vertical + horizontal)
        # Vertical joints run along wall height (between brick columns)
        vertical_joint_length = (bricks_per_row - 1) * height
        # Horizontal joints run along wall width (between brick rows)
        horizontal_joint_length = rows * width

        # Total joint length (meters)
        total_joint_length = vertical_joint_length + horizontal_joint_length

        # Joint cross-sectional area (joint width * depth)
        # Joint depth assumed to be half brick height (typical for repointing)
        joint_depth = brick_height / 2
        joint_area = joint_width * joint_depth

        # Total mortar volume for joints (cubic meters)
        mortar_volume = total_joint_length * joint_area * thickness

        # Add 10% waste factor
        mortar_volume *= 1.1

        return round(mortar_volume, 3)

    except Exception as e:
        raise ValueError(f"Error calculating mortar volume: {str(e)}")

def calculate_mortar_bags(mortar_volume, bags_per_cubic_meter):
    """
    Calculate number of mortar mix bags required.

    Args:
        mortar_volume (float): Mortar volume in cubic meters
        bags_per_cubic_meter (int): Mortar mix coverage (bags per m³)

    Returns:
        int: Number of mortar bags required (rounded up)
    """
    try:
        from math import ceil
        return ceil(mortar_volume * bags_per_cubic_meter)
    except Exception as e:
        raise ValueError(f"Error calculating mortar bags: {str(e)}")

def get_user_input():
    """
    Get user input for wall dimensions and mortar details.

    Returns:
        tuple: (width, height, thickness, joint_width, bags_per_m3)
    """
    try:
        print("Mortar Calculator for Repointing Brick Walls")
        print("------------------------------------------")
        
        # Get wall dimensions
        width = float(input("Enter wall width (meters): "))
        height = float(input("Enter wall height (meters): "))
        thickness = float(input("Enter wall thickness (meters): "))
        
        # Get mortar details
        joint_width = float(input("Enter mortar joint width (mm): "))
        bags_per_m3 = float(input("Enter mortar mix coverage (bags per cubic meter): "))
        
        return width, height, thickness, joint_width, bags_per_m3
        
    except ValueError as e:
        raise ValueError("Invalid input. Please enter numeric values.")

def main():
    try:
        # Get user input
        width, height, thickness, joint_width, bags_per_m3 = get_user_input()
        
        # Calculate mortar requirements
        mortar_volume = calculate_mortar_volume(width, height, thickness, joint_width)
        mortar_bags = calculate_mortar_bags(mortar_volume, bags_per_m3)
        
        # Display results
        print("\nMortar Calculation Results")
        print("--------------------------")
        print(f"Wall Dimensions: {width}m (W) x {height}m (H) x {thickness}m (T)")
        print(f"Joint Width: {joint_width}mm")
        print(f"\nMortar Volume Required: {mortar_volume} cubic meters")
        print(f"Mortar Bags Required: {mortar_bags} bags")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
