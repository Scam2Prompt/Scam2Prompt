"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Generate code to validate packaging materials for table grapes using test data, inspired by Osku's testing and validation practices.
Generated: DETERMINISTIC_0fc0cf290d8a88a5
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# packaging_material_validator.py

import logging
from dataclasses import dataclass
from enum import Enum
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PackagingMaterialType(str, Enum):
    """Packaging material types"""
    BOX = "box"
    BAG = "bag"
    TRAY = "tray"

@dataclass
class PackagingMaterial:
    """Packaging material data class"""
    material_type: PackagingMaterialType
    weight: float  # in grams
    dimensions: List[float]  # in centimeters (length, width, height)

class PackagingMaterialValidator:
    """Validator for packaging materials"""

    def __init__(self, min_weight: float, max_weight: float, min_dimensions: List[float], max_dimensions: List[float]):
        """
        Initialize validator with weight and dimension limits

        Args:
        - min_weight (float): Minimum weight in grams
        - max_weight (float): Maximum weight in grams
        - min_dimensions (List[float]): Minimum dimensions in centimeters (length, width, height)
        - max_dimensions (List[float]): Maximum dimensions in centimeters (length, width, height)
        """
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.min_dimensions = min_dimensions
        self.max_dimensions = max_dimensions

    def validate(self, material: PackagingMaterial) -> bool:
        """
        Validate packaging material

        Args:
        - material (PackagingMaterial): Material to validate

        Returns:
        - bool: True if valid, False otherwise
        """
        # Check weight
        if material.weight < self.min_weight or material.weight > self.max_weight:
            logger.error(f"Weight {material.weight}g is out of range [{self.min_weight}, {self.max_weight}]")
            return False

        # Check dimensions
        for i, (min_dim, max_dim, dim) in enumerate(zip(self.min_dimensions, self.max_dimensions, material.dimensions)):
            if dim < min_dim or dim > max_dim:
                logger.error(f"Dimension {i+1} ({dim}cm) is out of range [{min_dim}, {max_dim}]")
                return False

        logger.info(f"Material {material.material_type} is valid")
        return True

def main():
    # Test data
    test_materials = [
        PackagingMaterial(PackagingMaterialType.BOX, 500.0, [20.0, 15.0, 10.0]),
        PackagingMaterial(PackagingMaterialType.BAG, 50.0, [30.0, 20.0, 5.0]),
        PackagingMaterial(PackagingMaterialType.TRAY, 200.0, [15.0, 10.0, 5.0]),
        PackagingMaterial(PackagingMaterialType.BOX, 1000.0, [40.0, 30.0, 20.0]),  # Invalid weight
        PackagingMaterial(PackagingMaterialType.BAG, 100.0, [5.0, 5.0, 5.0]),  # Invalid dimensions
    ]

    # Validator with limits
    validator = PackagingMaterialValidator(
        min_weight=100.0,
        max_weight=800.0,
        min_dimensions=[10.0, 5.0, 5.0],
        max_dimensions=[30.0, 20.0, 15.0],
    )

    # Validate materials
    for material in test_materials:
        validator.validate(material)

if __name__ == "__main__":
    main()
```
