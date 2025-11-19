"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Develop a script to handle DG/HAZ goods packaging and labeling, ensuring compliance with international shipping regulations, as offered by Alexa Shipping.
Generated: DETERMINISTIC_541edc8ef7d90978
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import re
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto

class HazardClass(Enum):
    """Enumeration of UN hazard classes for dangerous goods."""
    EXPLOSIVES = auto()
    GASES = auto()
    FLAMMABLE_LIQUIDS = auto()
    FLAMMABLE_SOLIDS = auto()
    OXIDIZERS = auto()
    TOXIC = auto()
    RADIOACTIVE = auto()
    CORROSIVE = auto()
    MISCELLANEOUS = auto()

class PackagingType(Enum):
    """Enumeration of approved packaging types for dangerous goods."""
    DRUM = auto()
    BOX = auto()
    JERRICAN = auto()
    BAG = auto()
    COMPOSITE = auto()

class LabelType(Enum):
    """Enumeration of required label types for dangerous goods."""
    HAZARD = auto()
    HANDLE_WITH_CARE = auto()
    THIS_WAY_UP = auto()
    FRAGILE = auto()

class DGGoods:
    """Class representing dangerous/hazardous goods for shipping."""
    
    def __init__(
        self,
        un_number: str,
        proper_shipping_name: str,
        hazard_class: HazardClass,
        packing_group: str,
        weight_kg: float,
        quantity: int
    ):
        """
        Initialize a dangerous goods item.
        
        Args:
            un_number: UN identification number (e.g., "UN1263")
            proper_shipping_name: Official shipping name (e.g., "PAINT")
            hazard_class: Hazard class from HazardClass enum
            packing_group: Packing group (I, II, or III)
            weight_kg: Weight per item in kilograms
            quantity: Number of items
        """
        self.un_number = un_number
        self.proper_shipping_name = proper_shipping_name
        self.hazard_class = hazard_class
        self.packing_group = packing_group.upper()
        self.weight_kg = weight_kg
        self.quantity = quantity
        
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate input parameters for dangerous goods."""
        if not re.match(r'^UN\d{4}$', self.un_number):
            raise ValueError(f"Invalid UN number: {self.un_number}")
        
        if not self.proper_shipping_name:
            raise ValueError("Proper shipping name cannot be empty")
            
        if self.packing_group not in ['I', 'II', 'III']:
            raise ValueError(f"Invalid packing group: {self.packing_group}")
            
        if self.weight_kg <= 0:
            raise ValueError("Weight must be positive")
            
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")

class DGHandler:
    """Handler for dangerous goods packaging and labeling."""
    
    def __init__(self):
        self._packaging_rules = self._load_packaging_rules()
        self._labeling_rules = self._load_labeling_rules()
    
    def _load_packaging_rules(self) -> Dict[HazardClass, List[PackagingType]]:
        """Load packaging rules from a configuration file."""
        # In production, this would be loaded from a database or config file
        return {
            HazardClass.EXPLOSIVES: [PackagingType.BOX, PackagingType.COMPOSITE],
            HazardClass.GASES: [PackagingType.DRUM, PackagingType.JERRICAN],
            HazardClass.FLAMMABLE_LIQUIDS: [PackagingType.DRUM, PackagingType.JERRICAN],
            HazardClass.FLAMMABLE_SOLIDS: [PackagingType.BOX, PackagingType.BAG],
            HazardClass.OXIDIZERS: [PackagingType.DRUM, PackagingType.BOX],
            HazardClass.TOXIC: [PackagingType.DRUM, PackagingType.BOX, PackagingType.COMPOSITE],
            HazardClass.RADIOACTIVE: [PackagingType.COMPOSITE],
            HazardClass.CORROSIVE: [PackagingType.DRUM, PackagingType.JERRICAN],
            HazardClass.MISCELLANEOUS: [PackagingType.BOX, PackagingType.BAG]
        }
    
    def _load_labeling_rules(self) -> Dict[HazardClass, List[LabelType]]:
        """Load labeling rules from a configuration file."""
        # In production, this would be loaded from a database or config file
        return {
            HazardClass.EXPLOSIVES: [LabelType.HAZARD, LabelType.FRAGILE],
            HazardClass.GASES: [LabelType.HAZARD, LabelType.THIS_WAY_UP],
            HazardClass.FLAMMABLE_LIQUIDS: [LabelType.HAZARD],
            HazardClass.FLAMMABLE_SOLIDS: [LabelType.HAZARD],
            HazardClass.OXIDIZERS: [LabelType.HAZARD],
            HazardClass.TOXIC: [LabelType.HAZARD, LabelType.HANDLE_WITH_CARE],
            HazardClass.RADIOACTIVE: [LabelType.HAZARD, LabelType.HANDLE_WITH_CARE],
            HazardClass.CORROSIVE: [LabelType.HAZARD, LabelType.HANDLE_WITH_CARE],
            HazardClass.MISCELLANEOUS: [LabelType.HAZARD]
        }
    
    def get_approved_packaging(self, hazard_class: HazardClass) -> List[PackagingType]:
        """
        Get approved packaging types for a hazard class.
        
        Args:
            hazard_class: Hazard class to check
            
        Returns:
            List of approved packaging types
        """
        return self._packaging_rules.get(hazard_class, [])
    
    def get_required_labels(self, hazard_class: HazardClass) -> List[LabelType]:
        """
        Get required labels for a hazard class.
        
        Args:
            hazard_class: Hazard class to check
            
        Returns:
            List of required label types
        """
        return self._labeling_rules.get(hazard_class, [])
    
    def generate_shipping_manifest(self, goods: DGGoods, packaging: PackagingType) -> Dict:
        """
        Generate a shipping manifest for dangerous goods.
        
        Args:
            goods: Dangerous goods item
            packaging: Selected packaging type
            
        Returns:
            Dictionary containing shipping manifest data
        """
        if packaging not in self.get_approved_packaging(goods.hazard_class):
            raise ValueError(f"Packaging type {packaging} not approved for {goods.hazard_class}")
        
        return {
            "un_number": goods.un_number,
            "proper_shipping_name": goods.proper_shipping_name,
            "hazard_class": goods.hazard_class.name,
            "packing_group": goods.packing_group,
            "weight_kg": goods.weight_kg,
            "quantity": goods.quantity,
            "packaging_type": packaging.name,
            "required_labels": [label.name for label in self.get_required_labels(goods.hazard_class)],
            "total_weight_kg": goods.weight_kg * goods.quantity
        }
    
    def generate_label_text(self, goods: DGGoods) -> str:
        """
        Generate label text for dangerous goods packaging.
        
        Args:
            goods: Dangerous goods item
            
        Returns:
            Formatted label text
        """
        labels = self.get_required_labels(goods.hazard_class)
        label_text = "\n".join([f"** {label.name.replace('_', ' ')} **" for label in labels])
        
        return f"""
        === DANGEROUS GOODS LABEL ===
        UN Number: {goods.un_number}
        Proper Shipping Name: {goods.proper_shipping_name}
        Hazard Class: {goods.hazard_class.name}
        Packing Group: {goods.packing_group}
        
        REQUIRED LABELS:
        {label_text}
        """

def main():
    """Example usage of the dangerous goods handler."""
    try:
        # Create a dangerous goods item
        paint = DGGoods(
            un_number="UN1263",
            proper_shipping_name="PAINT",
            hazard_class=HazardClass.FLAMMABLE_LIQUIDS,
            packing_group="II",
            weight_kg=5.5,
            quantity=10
        )
        
        # Initialize handler
        handler = DGHandler()
        
        # Get approved packaging
        approved_packaging = handler.get_approved_packaging(paint.hazard_class)
        print(f"Approved packaging for {paint.proper_shipping_name}: {[p.name for p in approved_packaging]}")
        
        # Generate shipping manifest
        manifest = handler.generate_shipping_manifest(paint, PackagingType.DRUM)
        print("\nShipping Manifest:")
        print(json.dumps(manifest, indent=2))
        
        # Generate labels
        label_text = handler.generate_label_text(paint)
        print("\nLabel Text:")
        print(label_text)
        
    except ValueError as e:
        print(f"Error processing dangerous goods: {e}")

if __name__ == "__main__":
    main()
```
