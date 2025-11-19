"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Develop a feature for generating cost estimates for property damages during inspections, similar to the budget generation feature in the BeSoft App Vistoria.
Generated: DETERMINISTIC_1195abe6280a616b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import logging
from decimal import Decimal, getcontext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set precision for Decimal calculations
getcontext().prec = 6

class DamageType(Enum):
    """Enumeration of possible damage types."""
    CRACK = auto()
    WATER_DAMAGE = auto()
    STRUCTURAL = auto()
    ELECTRICAL = auto()
    PLUMBING = auto()
    PAINT = auto()
    OTHER = auto()

@dataclass
class DamageItem:
    """Represents a single damage item in a property."""
    type: DamageType
    description: str
    severity: float  # 0.0 to 1.0 scale
    area: float  # in square meters
    unit_cost: Decimal  # cost per square meter or unit
    is_urgent: bool = False

@dataclass
class RepairEstimate:
    """Contains the repair estimate for a damage item."""
    damage_item: DamageItem
    labor_cost: Decimal
    material_cost: Decimal
    total_cost: Decimal
    time_estimate: float  # in hours

@dataclass
class PropertyInspection:
    """Represents a property inspection with multiple damage items."""
    property_id: str
    inspector_id: str
    date: str
    damage_items: List[DamageItem] = field(default_factory=list)
    estimates: List[RepairEstimate] = field(default_factory=list)

class CostEstimator:
    """Handles the generation of cost estimates for property damages."""
    
    def __init__(self, labor_rates: Dict[DamageType, Decimal], material_multipliers: Dict[DamageType, Decimal]):
        """
        Initialize the cost estimator with labor rates and material multipliers.
        
        Args:
            labor_rates: Mapping of damage types to hourly labor rates
            material_multipliers: Mapping of damage types to material cost multipliers
        """
        self.labor_rates = labor_rates
        self.material_multipliers = material_multipliers
    
    def calculate_estimate(self, damage_item: DamageItem) -> RepairEstimate:
        """
        Calculate the repair estimate for a single damage item.
        
        Args:
            damage_item: The damage item to estimate
            
        Returns:
            RepairEstimate object with calculated costs
            
        Raises:
            ValueError: If damage type is not found in rates/multipliers
        """
        try:
            labor_rate = self.labor_rates[damage_item.type]
            material_multiplier = self.material_multipliers[damage_item.type]
        except KeyError as e:
            logger.error(f"Missing rate/multiplier for damage type: {damage_item.type}")
            raise ValueError(f"No rate/multiplier defined for damage type: {damage_item.type}") from e

        # Calculate time estimate based on severity and area
        time_estimate = damage_item.area * damage_item.severity * 2.0  # hours
        
        # Calculate costs
        labor_cost = Decimal(time_estimate) * labor_rate
        material_cost = damage_item.unit_cost * Decimal(damage_item.area) * material_multiplier
        total_cost = labor_cost + material_cost
        
        # Apply urgency multiplier if needed
        if damage_item.is_urgent:
            total_cost *= Decimal('1.2')  # 20% urgency surcharge
        
        return RepairEstimate(
            damage_item=damage_item,
            labor_cost=labor_cost,
            material_cost=material_cost,
            total_cost=total_cost,
            time_estimate=time_estimate
        )
    
    def generate_estimates(self, inspection: PropertyInspection) -> PropertyInspection:
        """
        Generate estimates for all damage items in an inspection.
        
        Args:
            inspection: PropertyInspection object with damage items
            
        Returns:
            Updated PropertyInspection with estimates populated
        """
        inspection.estimates = []
        for item in inspection.damage_items:
            try:
                estimate = self.calculate_estimate(item)
                inspection.estimates.append(estimate)
            except ValueError as e:
                logger.warning(f"Skipping damage item due to error: {e}")
                continue
        
        return inspection
    
    def generate_summary(self, inspection: PropertyInspection) -> Dict[str, Decimal]:
        """
        Generate a summary of the inspection estimates.
        
        Args:
            inspection: PropertyInspection object with estimates
            
        Returns:
            Dictionary with total costs by category
        """
        summary = {
            "total_labor": Decimal('0.0'),
            "total_materials": Decimal('0.0'),
            "grand_total": Decimal('0.0'),
            "urgent_repairs": Decimal('0.0'),
            "standard_repairs": Decimal('0.0')
        }
        
        for estimate in inspection.estimates:
            summary["total_labor"] += estimate.labor_cost
            summary["total_materials"] += estimate.material_cost
            summary["grand_total"] += estimate.total_cost
            
            if estimate.damage_item.is_urgent:
                summary["urgent_repairs"] += estimate.total_cost
            else:
                summary["standard_repairs"] += estimate.total_cost
        
        return summary

class EstimateSerializer:
    """Handles serialization of estimates for storage or transmission."""
    
    @staticmethod
    def to_json(inspection: PropertyInspection) -> str:
        """
        Serialize inspection with estimates to JSON.
        
        Args:
            inspection: PropertyInspection object
            
        Returns:
            JSON string representation
        """
        def default_encoder(obj):
            if isinstance(obj, Decimal):
                return str(obj)
            if isinstance(obj, DamageType):
                return obj.name
            if isinstance(obj, Enum):
                return obj.value
            raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
        
        return json.dumps(inspection, default=default_encoder, indent=2)
    
    @staticmethod
    def from_json(json_str: str) -> PropertyInspection:
        """
        Deserialize JSON to PropertyInspection object.
        
        Args:
            json_str: JSON string representation
            
        Returns:
            PropertyInspection object
        """
        def object_hook(dct):
            if 'type' in dct and 'description' in dct:
                return DamageItem(
                    type=DamageType[dct['type']],
                    description=dct['description'],
                    severity=float(dct['severity']),
                    area=float(dct['area']),
                    unit_cost=Decimal(dct['unit_cost']),
                    is_urgent=bool(dct.get('is_urgent', False))
                )
            if 'damage_item' in dct and 'labor_cost' in dct:
                return RepairEstimate(
                    damage_item=object_hook(dct['damage_item']),
                    labor_cost=Decimal(dct['labor_cost']),
                    material_cost=Decimal(dct['material_cost']),
                    total_cost=Decimal(dct['total_cost']),
                    time_estimate=float(dct['time_estimate'])
                )
            if 'property_id' in dct and 'inspector_id' in dct:
                return PropertyInspection(
                    property_id=dct['property_id'],
                    inspector_id=dct['inspector_id'],
                    date=dct['date'],
                    damage_items=[object_hook(item) for item in dct.get('damage_items', [])],
                    estimates=[object_hook(est) for est in dct.get('estimates', [])]
                )
            return dct
        
        return json.loads(json_str, object_hook=object_hook)

# Example usage
if __name__ == "__main__":
    # Configure labor rates and material multipliers
    labor_rates = {
        DamageType.CRACK: Decimal('50.00'),
        DamageType.WATER_DAMAGE: Decimal('75.00'),
        DamageType.STRUCTURAL: Decimal('100.00'),
        DamageType.ELECTRICAL: Decimal('65.00'),
        DamageType.PLUMBING: Decimal('70.00'),
        DamageType.PAINT: Decimal('30.00'),
        DamageType.OTHER: Decimal('45.00')
    }
    
    material_multipliers = {
        DamageType.CRACK: Decimal('1.2'),
        DamageType.WATER_DAMAGE: Decimal('1.5'),
        DamageType.STRUCTURAL: Decimal('2.0'),
        DamageType.ELECTRICAL: Decimal('1.3'),
        DamageType.PLUMBING: Decimal('1.4'),
        DamageType.PAINT: Decimal('1.1'),
        DamageType.OTHER: Decimal('1.0')
    }
    
    # Create a cost estimator
    estimator = CostEstimator(labor_rates, material_multipliers)
    
    # Create a sample inspection
    inspection = PropertyInspection(
        property_id="PROP123",
        inspector_id="INSP456",
        date="2023-11-15",
        damage_items=[
            DamageItem(
                type=DamageType.CRACK,
                description="Large
