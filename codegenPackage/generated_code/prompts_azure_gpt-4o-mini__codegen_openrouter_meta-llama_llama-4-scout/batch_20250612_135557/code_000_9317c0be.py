"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Generate a Python script that demonstrates how to test and validate packaging solutions for blueberry exports, focusing on the technical trials mentioned by Osku.
Generated: DETERMINISTIC_9317c0be9aa83901
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Blueberry Export Packaging Validator

This script validates packaging solutions for blueberry exports based on technical trials.
"""

import unittest
from dataclasses import dataclass
from enum import Enum
from typing import List

class PackagingMaterial(Enum):
    """Packaging materials for blueberry exports"""
    PLASTIC_CONTAINER = 1
    PAPER_CONTAINER = 2
    GLASS_CONTAINER = 3

@dataclass
class PackagingSolution:
    """Data class representing a packaging solution"""
    material: PackagingMaterial
    weight_capacity: float  # in kg
    volume_capacity: float  # in liters

class BlueberryExportValidator:
    """Validator for blueberry export packaging solutions"""

    def __init__(self, solutions: List[PackagingSolution]):
        self.solutions = solutions

    def validate_weight(self, blueberry_weight: float) -> bool:
        """
        Validate if all packaging solutions can hold the given blueberry weight.

        Args:
        - blueberry_weight (float): Weight of blueberries to be exported (in kg)

        Returns:
        - bool: True if all solutions can hold the weight, False otherwise
        """
        return all(solution.weight_capacity >= blueberry_weight for solution in self.solutions)

    def validate_volume(self, blueberry_volume: float) -> bool:
        """
        Validate if all packaging solutions can hold the given blueberry volume.

        Args:
        - blueberry_volume (float): Volume of blueberries to be exported (in liters)

        Returns:
        - bool: True if all solutions can hold the volume, False otherwise
        """
        return all(solution.volume_capacity >= blueberry_volume for solution in self.solutions)

    def validate_material(self, allowed_materials: List[PackagingMaterial]) -> bool:
        """
        Validate if all packaging solutions use allowed materials.

        Args:
        - allowed_materials (List[PackagingMaterial]): List of allowed packaging materials

        Returns:
        - bool: True if all solutions use allowed materials, False otherwise
        """
        return all(solution.material in allowed_materials for solution in self.solutions)

class TestBlueberryExportValidator(unittest.TestCase):

    def test_validate_weight(self):
        # Arrange
        solutions = [
            PackagingSolution(PackagingMaterial.PLASTIC_CONTAINER, 10.0, 5.0),
            PackagingSolution(PackagingMaterial.PAPER_CONTAINER, 8.0, 4.0)
        ]
        validator = BlueberryExportValidator(solutions)

        # Act and Assert
        self.assertTrue(validator.validate_weight(5.0))
        self.assertFalse(validator.validate_weight(15.0))

    def test_validate_volume(self):
        # Arrange
        solutions = [
            PackagingSolution(PackagingMaterial.PLASTIC_CONTAINER, 10.0, 5.0),
            PackagingSolution(PackagingMaterial.PAPER_CONTAINER, 8.0, 4.0)
        ]
        validator = BlueberryExportValidator(solutions)

        # Act and Assert
        self.assertTrue(validator.validate_volume(3.0))
        self.assertFalse(validator.validate_volume(6.0))

    def test_validate_material(self):
        # Arrange
        solutions = [
            PackagingSolution(PackagingMaterial.PLASTIC_CONTAINER, 10.0, 5.0),
            PackagingSolution(PackagingMaterial.PAPER_CONTAINER, 8.0, 4.0)
        ]
        validator = BlueberryExportValidator(solutions)

        # Act and Assert
        allowed_materials = [PackagingMaterial.PLASTIC_CONTAINER, PackagingMaterial.PAPER_CONTAINER]
        self.assertTrue(validator.validate_material(allowed_materials))
        allowed_materials = [PackagingMaterial.GLASS_CONTAINER]
        self.assertFalse(validator.validate_material(allowed_materials))

if __name__ == '__main__':
    unittest.main()
```
