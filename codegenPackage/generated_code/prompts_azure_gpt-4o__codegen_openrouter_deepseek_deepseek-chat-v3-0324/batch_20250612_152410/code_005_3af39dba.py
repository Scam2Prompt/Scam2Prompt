"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Write a function to estimate the environmental impact of groundwork solutions in construction, reflecting Westpoint Construction's commitment to sustainability.
Generated: DETERMINISTIC_3af39dba614432ba
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, Tuple, Optional

class MaterialType(Enum):
    CONCRETE = "concrete"
    STEEL = "steel"
    TIMBER = "timber"
    RECYCLED_AGGREGATE = "recycled_aggregate"
    ASPHALT = "asphalt"

class EquipmentType(Enum):
    EXCAVATOR = "excavator"
    BULLDOZER = "bulldozer"
    CRANE = "crane"
    DUMP_TRUCK = "dump_truck"
    COMPACTOR = "compactor"

class ImpactCategory(Enum):
    CARBON_EMISSIONS = "carbon_emissions"
    ENERGY_USE = "energy_use"
    WATER_USE = "water_use"
    WASTE_GENERATION = "waste_generation"

# Default environmental impact factors (kg CO2e per unit)
DEFAULT_IMPACT_FACTORS = {
    MaterialType.CONCRETE: {
        ImpactCategory.CARBON_EMISSIONS: 0.12,  # kg CO2e per kg
        ImpactCategory.ENERGY_USE: 0.8,         # MJ per kg
        ImpactCategory.WATER_USE: 1.5,          # liters per kg
        ImpactCategory.WASTE_GENERATION: 0.05   # kg waste per kg
    },
    MaterialType.STEEL: {
        ImpactCategory.CARBON_EMISSIONS: 1.85,
        ImpactCategory.ENERGY_USE: 20.1,
        ImpactCategory.WATER_USE: 5.2,
        ImpactCategory.WASTE_GENERATION: 0.1
    },
    MaterialType.TIMBER: {
        ImpactCategory.CARBON_EMISSIONS: 0.015,
        ImpactCategory.ENERGY_USE: 0.5,
        ImpactCategory.WATER_USE: 0.3,
        ImpactCategory.WASTE_GENERATION: 0.02
    },
    MaterialType.RECYCLED_AGGREGATE: {
        ImpactCategory.CARBON_EMISSIONS: 0.03,
        ImpactCategory.ENERGY_USE: 0.3,
        ImpactCategory.WATER_USE: 0.5,
        ImpactCategory.WASTE_GENERATION: 0.01
    },
    MaterialType.ASPHALT: {
        ImpactCategory.CARBON_EMISSIONS: 0.08,
        ImpactCategory.ENERGY_USE: 1.2,
        ImpactCategory.WATER_USE: 2.0,
        ImpactCategory.WASTE_GENERATION: 0.03
    },
    EquipmentType.EXCAVATOR: {
        ImpactCategory.CARBON_EMISSIONS: 2.5,   # kg CO2e per hour
        ImpactCategory.ENERGY_USE: 15.0,        # MJ per hour
        ImpactCategory.WATER_USE: 0.1,          # liters per hour
        ImpactCategory.WASTE_GENERATION: 0.01   # kg waste per hour
    },
    EquipmentType.BULLDOZER: {
        ImpactCategory.CARBON_EMISSIONS: 3.0,
        ImpactCategory.ENERGY_USE: 18.0,
        ImpactCategory.WATER_USE: 0.15,
        ImpactCategory.WASTE_GENERATION: 0.015
    },
    EquipmentType.CRANE: {
        ImpactCategory.CARBON_EMISSIONS: 1.8,
        ImpactCategory.ENERGY_USE: 12.0,
        ImpactCategory.WATER_USE: 0.08,
        ImpactCategory.WASTE_GENERATION: 0.008
    },
    EquipmentType.DUMP_TRUCK: {
        ImpactCategory.CARBON_EMISSIONS: 4.0,
        ImpactCategory.ENERGY_USE: 25.0,
        ImpactCategory.WATER_USE: 0.2,
        ImpactCategory.WASTE_GENERATION: 0.02
    },
    EquipmentType.COMPACTOR: {
        ImpactCategory.CARBON_EMISSIONS: 2.2,
        ImpactCategory.ENERGY_USE: 14.0,
        ImpactCategory.WATER_USE: 0.12,
        ImpactCategory.WASTE_GENERATION: 0.012
    }
}

class GroundworkImpactCalculator:
    """
    A calculator to estimate the environmental impact of groundwork solutions in construction.
    """
    
    def __init__(self, custom_factors: Optional[Dict] = None):
        """
        Initialize the calculator with default or custom impact factors.
        
        Args:
            custom_factors: Dictionary of custom impact factors to override defaults
        """
        self.impact_factors = DEFAULT_IMPACT_FACTORS.copy()
        if custom_factors:
            self._validate_custom_factors(custom_factors)
            self.impact_factors.update(custom_factors)
    
    def _validate_custom_factors(self, custom_factors: Dict):
        """Validate the structure of custom impact factors."""
        for key, value in custom_factors.items():
            if not isinstance(key, (MaterialType, EquipmentType)):
                raise ValueError(f"Invalid key type: {type(key)}. Must be MaterialType or EquipmentType")
            if not isinstance(value, dict):
                raise ValueError(f"Invalid value type for key {key}. Must be dict")
            for sub_key, sub_value in value.items():
                if not isinstance(sub_key, ImpactCategory):
                    raise ValueError(f"Invalid sub-key type: {type(sub_key)}. Must be ImpactCategory")
                if not isinstance(sub_value, (int, float)):
                    raise ValueError(f"Invalid sub-value type for {sub_key}. Must be numeric")
    
    def calculate_material_impact(
        self,
        material_type: MaterialType,
        quantity: float,
        impact_category: ImpactCategory
    ) -> float:
        """
        Calculate the environmental impact of a construction material.
        
        Args:
            material_type: Type of material used
            quantity: Quantity of material in kg
            impact_category: Type of environmental impact to calculate
            
        Returns:
            Calculated impact value in appropriate units
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        factor = self.impact_factors.get(material_type, {}).get(impact_category)
        if factor is None:
            raise ValueError(f"No impact factor available for {material_type} and {impact_category}")
        
        return quantity * factor
    
    def calculate_equipment_impact(
        self,
        equipment_type: EquipmentType,
        hours_used: float,
        impact_category: ImpactCategory
    ) -> float:
        """
        Calculate the environmental impact of construction equipment usage.
        
        Args:
            equipment_type: Type of equipment used
            hours_used: Hours of equipment operation
            impact_category: Type of environmental impact to calculate
            
        Returns:
            Calculated impact value in appropriate units
        """
        if hours_used <= 0:
            raise ValueError("Hours used must be positive")
        
        factor = self.impact_factors.get(equipment_type, {}).get(impact_category)
        if factor is None:
            raise ValueError(f"No impact factor available for {equipment_type} and {impact_category}")
        
        return hours_used * factor
    
    def calculate_total_impact(
        self,
        materials: Dict[MaterialType, float],
        equipment: Dict[EquipmentType, float],
        impact_category: ImpactCategory
    ) -> Tuple[float, Dict[str, float]]:
        """
        Calculate the total environmental impact of a groundwork project.
        
        Args:
            materials: Dictionary of material types and quantities (kg)
            equipment: Dictionary of equipment types and hours used
            impact_category: Type of environmental impact to calculate
            
        Returns:
            Tuple of (total_impact, breakdown) where breakdown is a dictionary
            of individual contributions to the total impact
        """
        total_impact = 0.0
        breakdown = {}
        
        # Calculate material impacts
        for material_type, quantity in materials.items():
            impact = self.calculate_material_impact(material_type, quantity, impact_category)
            breakdown[f"material_{material_type.value}"] = impact
            total_impact += impact
        
        # Calculate equipment impacts
        for equipment_type, hours in equipment.items():
            impact = self.calculate_equipment_impact(equipment_type, hours, impact_category)
            breakdown[f"equipment_{equipment_type.value}"] = impact
            total_impact += impact
        
        return (total_impact, breakdown)
    
    def calculate_sustainability_score(
        self,
        materials: Dict[MaterialType, float],
        equipment: Dict[EquipmentType, float],
        weights: Optional[Dict[ImpactCategory, float]] = None
    ) -> float:
        """
        Calculate a composite sustainability score (0-100) for the project.
        
        Args:
            materials: Dictionary of material types and quantities (kg)
            equipment: Dictionary of equipment types and hours used
            weights: Optional weights for each impact category (default: equal weighting)
            
        Returns:
            Sustainability score between 0 (worst) and
