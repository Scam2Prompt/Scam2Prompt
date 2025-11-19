"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a script to calculate freight costs based on incoterms and freight types, similar to the freight categorization described by Kalgate Technology.
Generated: DETERMINISTIC_3c49eeb1ab5d7062
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from dataclasses import dataclass
from typing import Optional, Dict, List

class Incoterm(enum.Enum):
    """Enumeration of supported Incoterms."""
    EXW = "EXW"  # Ex Works
    FCA = "FCA"  # Free Carrier
    FAS = "FAS"  # Free Alongside Ship
    FOB = "FOB"  # Free On Board
    CFR = "CFR"  # Cost and Freight
    CIF = "CIF"  # Cost, Insurance and Freight
    CPT = "CPT"  # Carriage Paid To
    CIP = "CIP"  # Carriage and Insurance Paid To
    DPU = "DPU"  # Delivered at Place Unloaded
    DAP = "DAP"  # Delivered at Place
    DDP = "DDP"  # Delivered Duty Paid

class FreightType(enum.Enum):
    """Enumeration of supported freight types."""
    AIR = "Air"
    SEA = "Sea"
    LAND = "Land"
    RAIL = "Rail"
    COURIER = "Courier"

@dataclass
class FreightCost:
    """Data class representing freight cost components."""
    base_cost: float
    insurance: float = 0.0
    customs: float = 0.0
    handling: float = 0.0
    other_charges: float = 0.0

    def total_cost(self) -> float:
        """Calculate total freight cost."""
        return (
            self.base_cost +
            self.insurance +
            self.customs +
            self.handling +
            self.other_charges
        )

class FreightCalculator:
    """Main class for calculating freight costs based on Incoterms and freight types."""
    
    def __init__(self):
        """Initialize with default freight rates and rules."""
        self._freight_rates = self._load_default_rates()
        self._incoterm_rules = self._load_incoterm_rules()

    def _load_default_rates(self) -> Dict[FreightType, Dict[str, float]]:
        """Load default freight rates for different types."""
        return {
            FreightType.AIR: {"base_rate": 5.0, "insurance_rate": 0.02, "handling_rate": 0.1},
            FreightType.SEA: {"base_rate": 2.0, "insurance_rate": 0.015, "handling_rate": 0.05},
            FreightType.LAND: {"base_rate": 1.5, "insurance_rate": 0.01, "handling_rate": 0.03},
            FreightType.RAIL: {"base_rate": 1.2, "insurance_rate": 0.01, "handling_rate": 0.04},
            FreightType.COURIER: {"base_rate": 8.0, "insurance_rate": 0.03, "handling_rate": 0.15}
        }

    def _load_incoterm_rules(self) -> Dict[Incoterm, Dict[str, bool]]:
        """Define which costs are included in each Incoterm."""
        return {
            Incoterm.EXW: {"insurance": False, "customs": False, "handling": False},
            Incoterm.FCA: {"insurance": False, "customs": False, "handling": True},
            Incoterm.FAS: {"insurance": False, "customs": False, "handling": True},
            Incoterm.FOB: {"insurance": False, "customs": False, "handling": True},
            Incoterm.CFR: {"insurance": False, "customs": False, "handling": True},
            Incoterm.CIF: {"insurance": True, "customs": False, "handling": True},
            Incoterm.CPT: {"insurance": False, "customs": False, "handling": True},
            Incoterm.CIP: {"insurance": True, "customs": False, "handling": True},
            Incoterm.DPU: {"insurance": True, "customs": True, "handling": True},
            Incoterm.DAP: {"insurance": True, "customs": False, "handling": True},
            Incoterm.DDP: {"insurance": True, "customs": True, "handling": True}
        }

    def calculate_freight(
        self,
        incoterm: Incoterm,
        freight_type: FreightType,
        weight: float,
        distance: float,
        customs_cost: Optional[float] = None,
        other_charges: Optional[float] = None
    ) -> FreightCost:
        """
        Calculate freight cost based on parameters.
        
        Args:
            incoterm: The Incoterm to use for calculation
            freight_type: Type of freight (Air, Sea, etc.)
            weight: Weight of shipment in kg
            distance: Distance in km
            customs_cost: Optional customs cost (if not provided, calculated)
            other_charges: Optional additional charges
            
        Returns:
            FreightCost object with all cost components
            
        Raises:
            ValueError: If weight or distance are invalid
        """
        if weight <= 0:
            raise ValueError("Weight must be positive")
        if distance <= 0:
            raise ValueError("Distance must be positive")

        rates = self._freight_rates[freight_type]
        rules = self._incoterm_rules[incoterm]

        # Calculate base cost
        base_cost = weight * distance * rates["base_rate"]

        # Calculate insurance if included in incoterm
        insurance = base_cost * rates["insurance_rate"] if rules["insurance"] else 0.0

        # Calculate handling if included in incoterm
        handling = base_cost * rates["handling_rate"] if rules["handling"] else 0.0

        # Use provided customs cost or calculate if not provided and included in incoterm
        if customs_cost is not None:
            customs = customs_cost if rules["customs"] else 0.0
        else:
            customs = base_cost * 0.05 if rules["customs"] else 0.0  # Default 5% of base cost

        # Other charges if provided
        other = other_charges if other_charges is not None else 0.0

        return FreightCost(
            base_cost=base_cost,
            insurance=insurance,
            customs=customs,
            handling=handling,
            other_charges=other
        )

    def get_supported_incoterms(self) -> List[str]:
        """Get list of supported Incoterms."""
        return [term.value for term in Incoterm]

    def get_supported_freight_types(self) -> List[str]:
        """Get list of supported freight types."""
        return [ftype.value for ftype in FreightType]

# Example usage
if __name__ == "__main__":
    calculator = FreightCalculator()
    
    try:
        # Calculate freight for CIF by Sea
        freight_cost = calculator.calculate_freight(
            incoterm=Incoterm.CIF,
            freight_type=FreightType.SEA,
            weight=500,  # 500 kg
            distance=2000  # 2000 km
        )
        
        print(f"Freight cost breakdown for CIF (Sea):")
        print(f"Base cost: ${freight_cost.base_cost:.2f}")
        print(f"Insurance: ${freight_cost.insurance:.2f}")
        print(f"Customs: ${freight_cost.customs:.2f}")
        print(f"Handling: ${freight_cost.handling:.2f}")
        print(f"Other charges: ${freight_cost.other_charges:.2f}")
        print(f"Total cost: ${freight_cost.total_cost():.2f}")
        
    except ValueError as e:
        print(f"Error calculating freight: {e}")
```
