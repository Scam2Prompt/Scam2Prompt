"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a Python script to calculate the cost of custom glass installations, including options for tempered glass thickness (6mm to 25mm), types of glass (laminated, blindex), and additional features like stainless steel frames or roldanas.
Generated: DETERMINISTIC_f4d2863bb41c42ae
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the cost of custom glass installations.

Features:
1. Supports tempered glass thickness options (6mm to 25mm).
2. Types of glass: Laminated, Blindex.
3. Additional features: Stainless steel frames, Roldanas (rollers).
4. Error handling for invalid inputs.
"""

# Constants for pricing
GLASS_THICKNESS_PRICES = {
    6: 50,    # Price per square meter for 6mm tempered glass
    8: 70,    # Price per square meter for 8mm tempered glass
    10: 90,   # Price per square meter for 10mm tempered glass
    12: 110,  # Price per square meter for 12mm tempered glass
    15: 140,  # Price per square meter for 15mm tempered glass
    20: 180,  # Price per square meter for 20mm tempered glass
    25: 230   # Price per square meter for 25mm tempered glass
}

GLASS_TYPE_MULTIPLIERS = {
    'laminated': 1.2,  # 20% price increase for laminated glass
    'blindex': 1.5     # 50% price increase for Blindex glass
}

ADDITIONAL_FEATURES_COST = {
    'stainless_steel_frame': 100,  # Flat cost for stainless steel frames
    'roldanas': 50                # Flat cost for Roldanas (rollers)
}

# Function to calculate the cost
def calculate_glass_cost(area, thickness, glass_type, additional_features):
    """
    Calculate the cost of custom glass installation.

    Parameters:
        area (float): The area of the glass in square meters.
        thickness (int): The thickness of the glass in mm (6mm to 25mm).
        glass_type (str): The type of glass ('laminated' or 'blindex').
        additional_features (list): Additional features ['stainless_steel_frame', 'roldanas'].

    Returns:
        float: Total cost of the installation.
    """
    if thickness not in GLASS_THICKNESS_PRICES:
        raise ValueError(f"Invalid thickness: {thickness}. Must be between 6mm and 25mm.")

    if glass_type not in GLASS_TYPE_MULTIPLIERS:
        raise ValueError(f"Invalid glass type: {glass_type}. Must be 'laminated' or 'blindex'.")

    # Base price calculation
    base_price = GLASS_THICKNESS_PRICES[thickness] * area
    
    # Apply glass type multiplier
    type_multiplier = GLASS_TYPE_MULTIPLIERS[glass_type]
    total_price = base_price * type_multiplier

    # Add cost for additional features
    for feature in additional_features:
        if feature not in ADDITIONAL_FEATURES_COST:
            raise ValueError(f"Invalid feature: {feature}. Must be 'stainless_steel_frame' or 'roldanas'.")
        total_price += ADDITIONAL_FEATURES_COST[feature]

    return total_price

# Main function to interact with the user
def main():
    """
    Main function to gather user input and calculate the installation cost.
    """
    try:
        # Get user inputs
        area = float(input("Enter glass area in square meters: "))
        thickness = int(input("Enter glass thickness in mm (6, 8, 10, 12, 15, 20, 25): "))
        glass_type = input("Enter glass type ('laminated' or 'blindex'): ").lower()
        additional_features = input(
            "Enter additional features (comma-separated: 'stainless_steel_frame', 'roldanas'): "
        ).lower().split(',')

        # Remove whitespace and filter empty strings
        additional_features = [feature.strip() for feature in additional_features if feature.strip()]

        # Calculate cost
        total_cost = calculate_glass_cost(area, thickness, glass_type, additional_features)

        # Output the total cost
        print(f"\nTotal installation cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
