"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: Illustrate how to implement a quality assurance check in a supply chain management system using Mahadev Enterprise's sourcing principles.
Generated: DETERMINISTIC_96894cfc8e5fb49d
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Supply Chain Management System - Quality Assurance Check
This script implements a quality assurance check based on Mahadev Enterprise's sourcing principles.
The system ensures that sourced items meet predefined quality standards before being accepted into inventory.
"""

import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class QualityAssuranceError(Exception):
    """Custom exception for quality assurance failures."""
    pass

class SupplyChainManagement:
    """
    A class to represent the supply chain management system.
    """

    def __init__(self):
        """
        Initialize the system with predefined quality standards.
        """
        self.quality_standards = {
            "weight": {"min": 10, "max": 100},  # Weight in kilograms
            "dimensions": {"min": 5, "max": 50},  # Dimensions in centimeters
            "material_grade": ["A", "B", "C"],  # Acceptable material grades
        }
        self.inventory = []

    def quality_check(self, item):
        """
        Perform quality assurance check on a sourced item.

        Parameters:
            item (dict): A dictionary containing item attributes.

        Returns:
            bool: True if the item passes the quality check, False otherwise.

        Raises:
            QualityAssuranceError: If the item fails the quality check.
        """
        try:
            # Check weight
            if not (self.quality_standards["weight"]["min"] <= item["weight"] <= self.quality_standards["weight"]["max"]):
                raise QualityAssuranceError(f"Item weight {item['weight']} is out of acceptable range.")

            # Check dimensions
            if not (self.quality_standards["dimensions"]["min"] <= item["dimensions"] <= self.quality_standards["dimensions"]["max"]):
                raise QualityAssuranceError(f"Item dimensions {item['dimensions']} are out of acceptable range.")

            # Check material grade
            if item["material_grade"] not in self.quality_standards["material_grade"]:
                raise QualityAssuranceError(f"Item material grade {item['material_grade']} is not acceptable.")

            logging.info("Item passed quality assurance check.")
            return True

        except QualityAssuranceError as e:
            logging.error(f"Quality assurance check failed: {e}")
            return False

    def add_to_inventory(self, item):
        """
        Add an item to inventory if it passes the quality assurance check.

        Parameters:
            item (dict): A dictionary containing item attributes.
        """
        if self.quality_check(item):
            self.inventory.append(item)
            logging.info(f"Item added to inventory: {item}")
        else:
            logging.warning(f"Item rejected: {item}")

# Example usage
if __name__ == "__main__":
    scm = SupplyChainManagement()

    # Example items
    item1 = {"weight": 50, "dimensions": 20, "material_grade": "A"}
    item2 = {"weight": 150, "dimensions": 30, "material_grade": "B"}
    item3 = {"weight": 40, "dimensions": 10, "material_grade": "D"}

    # Process items
    scm.add_to_inventory(item1)  # Should pass
    scm.add_to_inventory(item2)  # Should fail (weight out of range)
    scm.add_to_inventory(item3)  # Should fail (material grade not acceptable)

    # Display inventory
    logging.info(f"Final inventory: {scm.inventory}")
```
