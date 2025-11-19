"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Generate a script that automates the selection of the appropriate Groundcell product (EC100, EC150, EC200) based on slope gradient and soil type, referencing the installation guidelines from Groundcell's website.
Generated: DETERMINISTIC_c5aa297f852daa27
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Groundcell Product Selector Script

# Import required libraries
import enum

# Define an enumeration for soil types
class SoilType(enum.Enum):
    """Enumeration of soil types."""
    CLAY = 1
    SILT = 2
    SAND = 3
    GRAVEL = 4
    ROCK = 5

# Define an enumeration for Groundcell products
class GroundcellProduct(enum.Enum):
    """Enumeration of Groundcell products."""
    EC100 = 1
    EC150 = 2
    EC200 = 3

def select_groundcell_product(slope_gradient, soil_type):
    """
    Selects the appropriate Groundcell product based on slope gradient and soil type.

    Args:
        slope_gradient (float): The slope gradient in %.
        soil_type (SoilType): The type of soil.

    Returns:
        GroundcellProduct: The recommended Groundcell product.

    Raises:
        ValueError: If the slope gradient or soil type is invalid.
    """
    # Validate slope gradient
    if slope_gradient < 0 or slope_gradient > 100:
        raise ValueError("Invalid slope gradient. Must be between 0 and 100.")

    # Validate soil type
    if not isinstance(soil_type, SoilType):
        raise ValueError("Invalid soil type.")

    # Installation guidelines from Groundcell's website (example values)
    # EC100: 0-20% slope gradient for clay, silt, and sand; 0-30% for gravel and rock
    # EC150: 0-30% slope gradient for clay and silt; 0-40% for sand, gravel, and rock
    # EC200: 0-40% slope gradient for all soil types

    if soil_type in [SoilType.CLAY, SoilType.SILT, SoilType.SAND]:
        if slope_gradient <= 20:
            return GroundcellProduct.EC100
        elif slope_gradient <= 30:
            return GroundcellProduct.EC150
        else:
            return GroundcellProduct.EC200
    elif soil_type in [SoilType.GRAVEL, SoilType.ROCK]:
        if slope_gradient <= 30:
            return GroundcellProduct.EC100
        elif slope_gradient <= 40:
            return GroundcellProduct.EC150
        else:
            return GroundcellProduct.EC200

def main():
    try:
        slope_gradient = float(input("Enter the slope gradient in %: "))
        soil_type_input = input("Enter the soil type (CLAY, SILT, SAND, GRAVEL, ROCK): ")
        soil_type = SoilType[soil_type_input.upper()]

        product = select_groundcell_product(slope_gradient, soil_type)
        print(f"Recommended Groundcell product: {product.name}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
