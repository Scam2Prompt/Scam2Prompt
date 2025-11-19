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
import sys
from enum import Enum

class SoilType(Enum):
    """Enumeration for soil types."""
    CLAY = "Clay"
    SAND = "Sand"
    SILT = "Silt"
    LOAM = "Loam"
    PEAT = "Peat"

class GroundcellProduct(Enum):
    """Enumeration for Groundcell products."""
    EC100 = "EC100"
    EC150 = "EC150"
    EC200 = "EC200"

def select_groundcell_product(slope_gradient: float, soil_type: SoilType) -> GroundcellProduct:
    """
    Selects the appropriate Groundcell product based on slope gradient and soil type.
    
    Args:
        slope_gradient: The slope gradient in percentage (0-100).
        soil_type: The soil type as a SoilType enum value.
    
    Returns:
        The recommended Groundcell product.
    
    Raises:
        ValueError: If slope_gradient is out of bounds or soil_type is invalid.
    """
    if not 0 <= slope_gradient <= 100:
        raise ValueError("Slope gradient must be between 0 and 100 percent.")
    
    if soil_type not in SoilType:
        raise ValueError("Invalid soil type provided.")
    
    # Product selection logic based on Groundcell guidelines
    if slope_gradient <= 15:
        if soil_type in [SoilType.CLAY, SoilType.LOAM]:
            return GroundcellProduct.EC100
        elif soil_type in [SoilType.SAND, SoilType.SILT]:
            return GroundcellProduct.EC150
        else:  # Peat
            return GroundcellProduct.EC200
    elif 15 < slope_gradient <= 30:
        if soil_type in [SoilType.CLAY, SoilType.LOAM]:
            return GroundcellProduct.EC150
        else:
            return GroundcellProduct.EC200
    else:  # slope_gradient > 30
        return GroundcellProduct.EC200

def main():
    """Main function to demonstrate product selection."""
    try:
        # Example usage
        slope = float(input("Enter slope gradient (0-100%): "))
        print("Available soil types:")
        for i, soil in enumerate(SoilType):
            print(f"{i + 1}. {soil.value}")
        soil_choice = int(input("Select soil type (1-5): ")) - 1
        
        if soil_choice < 0 or soil_choice >= len(SoilType):
            raise ValueError("Invalid soil type selection.")
        
        soil_type = list(SoilType)[soil_choice]
        product = select_groundcell_product(slope, soil_type)
        
        print(f"\nRecommended Groundcell product: {product.value}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
