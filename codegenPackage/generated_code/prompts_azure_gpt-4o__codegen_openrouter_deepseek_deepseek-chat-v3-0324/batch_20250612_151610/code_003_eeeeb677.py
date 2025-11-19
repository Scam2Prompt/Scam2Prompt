"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Create a program to automate customs clearance processes for foodstuffs, machinery, and personal effects, based on the expertise highlighted on Portline Shipping's website.
Generated: DETERMINISTIC_eeeeb677b69c0ad4
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Customs Clearance Automation System
Automates customs clearance for foodstuffs, machinery, and personal effects.
"""

import json
from datetime import datetime
from enum import Enum
import logging
from typing import Dict, List, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ItemCategory(Enum):
    """Enum for different item categories."""
    FOODSTUFFS = "Foodstuffs"
    MACHINERY = "Machinery"
    PERSONAL_EFFECTS = "Personal Effects"


class CustomsDocument:
    """Base class for customs documents."""
    def __init__(self, reference_number: str, date: datetime):
        self.reference_number = reference_number
        self.date = date

    def to_dict(self) -> Dict:
        """Convert document to dictionary."""
        return {
            "reference_number": self.reference_number,
            "date": self.date.isoformat()
        }


class CustomsDeclaration(CustomsDocument):
    """Class representing a customs declaration."""
    def __init__(
        self,
        reference_number: str,
        date: datetime,
        importer_details: Dict,
        items: List[Dict],
        category: ItemCategory
    ):
        super().__init__(reference_number, date)
        self.importer_details = importer_details
        self.items = items
        self.category = category

    def to_dict(self) -> Dict:
        """Convert declaration to dictionary."""
        base_dict = super().to_dict()
        base_dict.update({
            "importer_details": self.importer_details,
            "items": self.items,
            "category": self.category.value
        })
        return base_dict


class CustomsClearanceSystem:
    """Main system for handling customs clearance."""
    def __init__(self):
        self.declarations: List[CustomsDeclaration] = []
        self.tax_rates = self._load_tax_rates()

    def _load_tax_rates(self) -> Dict:
        """Load tax rates from configuration."""
        try:
            with open("tax_rates.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Tax rates file not found. Using default rates.")
            return {
                "Foodstuffs": 0.05,
                "Machinery": 0.15,
                "Personal Effects": 0.10
            }
        except json.JSONDecodeError:
            logger.error("Invalid tax rates file. Using default rates.")
            return {
                "Foodstuffs": 0.05,
                "Machinery": 0.15,
                "Personal Effects": 0.10
            }

    def create_declaration(
        self,
        importer_details: Dict,
        items: List[Dict],
        category: ItemCategory
    ) -> Optional[CustomsDeclaration]:
        """Create a new customs declaration."""
        try:
            if not importer_details or not items:
                raise ValueError("Importer details and items are required")

            reference_number = f"DEC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            declaration = CustomsDeclaration(
                reference_number=reference_number,
                date=datetime.now(),
                importer_details=importer_details,
                items=items,
                category=category
            )
            self.declarations.append(declaration)
            logger.info(f"Created declaration {reference_number}")
            return declaration
        except Exception as e:
            logger.error(f"Failed to create declaration: {str(e)}")
            return None

    def calculate_duties(self, declaration: CustomsDeclaration) -> float:
        """Calculate duties for a declaration."""
        try:
            category = declaration.category.value
            if category not in self.tax_rates:
                raise ValueError(f"Unknown category: {category}")

            total_value = sum(item.get("value", 0) for item in declaration.items)
            duty_rate = self.tax_rates[category]
            return total_value * duty_rate
        except Exception as e:
            logger.error(f"Failed to calculate duties: {str(e)}")
            raise

    def process_clearance(self, declaration: CustomsDeclaration) -> Dict:
        """Process customs clearance for a declaration."""
        try:
            duties = self.calculate_duties(declaration)
            clearance_data = {
                "status": "APPROVED",
                "declaration": declaration.to_dict(),
                "duties": duties,
                "processing_date": datetime.now().isoformat()
            }
            logger.info(f"Processed clearance for {declaration.reference_number}")
            return clearance_data
        except Exception as e:
            logger.error(f"Clearance failed for {declaration.reference_number}: {str(e)}")
            return {
                "status": "REJECTED",
                "reason": str(e),
                "processing_date": datetime.now().isoformat()
            }

    def get_declaration(self, reference_number: str) -> Optional[CustomsDeclaration]:
        """Retrieve a declaration by reference number."""
        for declaration in self.declarations:
            if declaration.reference_number == reference_number:
                return declaration
        return None

    def export_declarations(self, filename: str) -> bool:
        """Export all declarations to a JSON file."""
        try:
            data = [declaration.to_dict() for declaration in self.declarations]
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            logger.info(f"Exported declarations to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to export declarations: {str(e)}")
            return False


# Example usage
if __name__ == "__main__":
    system = CustomsClearanceSystem()

    # Sample importer details
    importer = {
        "name": "ABC Imports",
        "address": "123 Business St, Commerce City",
        "tax_id": "TAX123456"
    }

    # Sample items for different categories
    food_items = [
        {"description": "Canned goods", "quantity": 100, "value": 500.00},
        {"description": "Beverages", "quantity": 50, "value": 200.00}
    ]

    machinery_items = [
        {"description": "Industrial mixer", "quantity": 1, "value": 15000.00},
        {"description": "Conveyor belt", "quantity": 2, "value": 8000.00}
    ]

    personal_items = [
        {"description": "Clothing", "quantity": 10, "value": 500.00},
        {"description": "Electronics", "quantity": 5, "value": 2000.00}
    ]

    # Create and process declarations
    food_declaration = system.create_declaration(
        importer, food_items, ItemCategory.FOODSTUFFS
    )
    if food_declaration:
        food_clearance = system.process_clearance(food_declaration)
        print("Food Clearance Result:", food_clearance)

    machinery_declaration = system.create_declaration(
        importer, machinery_items, ItemCategory.MACHINERY
    )
    if machinery_declaration:
        machinery_clearance = system.process_clearance(machinery_declaration)
        print("Machinery Clearance Result:", machinery_clearance)

    # Export all declarations
    system.export_declarations("declarations_export.json")
```
