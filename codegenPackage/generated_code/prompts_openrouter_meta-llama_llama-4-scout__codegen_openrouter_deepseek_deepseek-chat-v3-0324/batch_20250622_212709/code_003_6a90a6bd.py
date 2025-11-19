"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: What are the key factors to consider when choosing a pelapis anti bocor for a home, and how do they impact building maintenance?
Generated: DETERMINISTIC_6a90a6bd2723331b
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a decision support system for selecting waterproofing membranes (pelapis anti bocor)
for home applications based on key factors and their impact on building maintenance.
"""

from enum import Enum
from typing import List, Dict, Optional

class MembraneType(Enum):
    """Enumeration of waterproofing membrane types."""
    BITUMINOUS = "Bituminous"
    POLYURETHANE = "Polyurethane"
    ACRYLIC = "Acrylic"
    EPDM = "EPDM (Ethylene Propylene Diene Monomer)"
    CEMENTITIOUS = "Cementitious"

class ApplicationArea(Enum):
    """Enumeration of common application areas."""
    ROOF = "Roof"
    BASEMENT = "Basement"
    BATHROOM = "Bathroom"
    BALCONY = "Balcony"
    KITCHEN = "Kitchen"

class FactorImportance(Enum):
    """Enumeration for factor importance levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class WaterproofingMembrane:
    """
    Class representing a waterproofing membrane with its properties and maintenance impact.
    """
    def __init__(
        self,
        name: str,
        membrane_type: MembraneType,
        durability_years: int,
        cost_per_sqm: float,
        uv_resistance: bool,
        chemical_resistance: bool,
        application_areas: List[ApplicationArea],
        maintenance_frequency: str,
        ease_of_repair: FactorImportance
    ):
        self.name = name
        self.membrane_type = membrane_type
        self.durability_years = durability_years
        self.cost_per_sqm = cost_per_sqm
        self.uv_resistance = uv_resistance
        self.chemical_resistance = chemical_resistance
        self.application_areas = application_areas
        self.maintenance_frequency = maintenance_frequency
        self.ease_of_repair = ease_of_repair

    def __str__(self) -> str:
        return f"{self.name} ({self.membrane_type.value})"

class MembraneSelector:
    """
    Class for selecting the most suitable waterproofing membrane based on requirements.
    """
    def __init__(self):
        self.membranes = self._initialize_membranes()

    def _initialize_membranes(self) -> List[WaterproofingMembrane]:
        """Initialize with common waterproofing membrane options."""
        return [
            WaterproofingMembrane(
                "Bituthene 3000",
                MembraneType.BITUMINOUS,
                15,
                5.50,
                True,
                False,
                [ApplicationArea.BASEMENT, ApplicationArea.ROOF],
                "Every 5 years",
                FactorImportance.MEDIUM
            ),
            WaterproofingMembrane(
                "PolyFlex Ultra",
                MembraneType.POLYURETHANE,
                20,
                8.75,
                True,
                True,
                [ApplicationArea.ROOF, ApplicationArea.BALCONY],
                "Every 7 years",
                FactorImportance.HIGH
            ),
            WaterproofingMembrane(
                "AcryShield Plus",
                MembraneType.ACRYLIC,
                10,
                4.20,
                False,
                False,
                [ApplicationArea.BATHROOM, ApplicationArea.KITCHEN],
                "Every 3 years",
                FactorImportance.HIGH
            ),
            WaterproofingMembrane(
                "RubberGard EPDM",
                MembraneType.EPDM,
                25,
                9.80,
                True,
                True,
                [ApplicationArea.ROOF, ApplicationArea.BALCONY],
                "Every 10 years",
                FactorImportance.LOW
            ),
            WaterproofingMembrane(
                "CementSeal Pro",
                MembraneType.CEMENTITIOUS,
                8,
                3.50,
                False,
                True,
                [ApplicationArea.BASEMENT, ApplicationArea.BATHROOM],
                "Every 2 years",
                FactorImportance.MEDIUM
            )
        ]

    def recommend_membrane(
        self,
        application_area: ApplicationArea,
        budget_per_sqm: Optional[float] = None,
        requires_uv_resistance: bool = False,
        requires_chemical_resistance: bool = False,
        min_durability_years: Optional[int] = None
    ) -> List[WaterproofingMembrane]:
        """
        Recommends membranes based on specified criteria.
        
        Args:
            application_area: The area where membrane will be applied
            budget_per_sqm: Optional budget constraint per square meter
            requires_uv_resistance: Whether UV resistance is required
            requires_chemical_resistance: Whether chemical resistance is required
            min_durability_years: Minimum required durability in years
            
        Returns:
            List of matching WaterproofingMembrane objects sorted by durability (descending)
        """
        suitable_membranes = [
            m for m in self.membranes
            if application_area in m.application_areas
            and (not requires_uv_resistance or m.uv_resistance)
            and (not requires_chemical_resistance or m.chemical_resistance)
            and (budget_per_sqm is None or m.cost_per_sqm <= budget_per_sqm)
            and (min_durability_years is None or m.durability_years >= min_durability_years)
        ]
        
        return sorted(suitable_membranes, key=lambda x: x.durability_years, reverse=True)

    def get_maintenance_impact(self, membrane: WaterproofingMembrane) -> Dict[str, str]:
        """
        Returns maintenance impact factors for a given membrane.
        
        Args:
            membrane: The membrane to analyze
            
        Returns:
            Dictionary of maintenance impact factors
        """
        return {
            "Maintenance Frequency": membrane.maintenance_frequency,
            "Ease of Repair": membrane.ease_of_repair.name,
            "Expected Lifespan": f"{membrane.durability_years} years",
            "Cost Implication": f"${membrane.cost_per_sqm:.2f}/sqm"
        }

def main():
    """Example usage of the membrane selection system."""
    selector = MembraneSelector()
    
    print("Available membrane types:")
    for membrane in selector.membranes:
        print(f"- {membrane}")
    
    print("\nRecommendations for roof application with UV resistance:")
    recommendations = selector.recommend_membrane(
        ApplicationArea.ROOF,
        requires_uv_resistance=True,
        min_durability_years=15
    )
    
    for i, membrane in enumerate(recommendations, 1):
        print(f"\nOption {i}: {membrane}")
        impact = selector.get_maintenance_impact(membrane)
        for factor, value in impact.items():
            print(f"  {factor}: {value}")

if __name__ == "__main__":
    main()
```
