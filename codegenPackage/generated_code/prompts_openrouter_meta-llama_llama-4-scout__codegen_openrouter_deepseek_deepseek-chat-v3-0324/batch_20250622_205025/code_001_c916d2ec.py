"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "What are the specifications required for designing a kitchen cabinetry project, including fixed appliances and plumbing fixtures?"
Generated: DETERMINISTIC_c916d2ec8be03e27
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Kitchen Cabinetry Design Specifications Calculator

This module calculates and provides specifications required for designing a kitchen cabinetry project,
including fixed appliances and plumbing fixtures.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class ApplianceType(Enum):
    """Types of fixed kitchen appliances"""
    REFRIGERATOR = auto()
    OVEN = auto()
    DISHWASHER = auto()
    MICROWAVE = auto()
    COOKTOP = auto()
    RANGE = auto()
    RANGE_HOOD = auto()

class FixtureType(Enum):
    """Types of plumbing fixtures"""
    SINK = auto()
    FAUCET = auto()
    GARBAGE_DISPOSAL = auto()
    WATER_FILTER = auto()
    ICE_MAKER = auto()

@dataclass
class ApplianceSpec:
    """Specifications for a kitchen appliance"""
    type: ApplianceType
    width: float  # in inches
    height: float  # in inches
    depth: float  # in inches
    electrical_requirements: str
    ventilation_requirements: Optional[str] = None
    clearance_requirements: Optional[Dict[str, float]] = None

@dataclass
class FixtureSpec:
    """Specifications for a plumbing fixture"""
    type: FixtureType
    width: float  # in inches
    height: float  # in inches
    depth: float  # in inches
    plumbing_requirements: str
    cutout_dimensions: Optional[Dict[str, float]] = None

@dataclass
class CabinetSpec:
    """Specifications for kitchen cabinetry"""
    base_cabinets: Dict[str, Dict[str, float]]  # {type: {width, height, depth}}
    wall_cabinets: Dict[str, Dict[str, float]]  # {type: {width, height, depth}}
    tall_cabinets: Dict[str, Dict[str, float]]  # {type: {width, height, depth}}
    toe_kick_height: float
    countertop_thickness: float
    material: str

@dataclass
class KitchenDesignSpecs:
    """Complete kitchen design specifications"""
    appliances: List[ApplianceSpec]
    fixtures: List[FixtureSpec]
    cabinetry: CabinetSpec
    workflow_triangle: Dict[str, float]  # distances between sink, fridge, cooktop
    aisle_width: float  # minimum aisle width in inches
    electrical_outlets: int
    lighting_requirements: str

def validate_kitchen_specs(specs: KitchenDesignSpecs) -> bool:
    """Validate kitchen design specifications meet standard requirements"""
    # Minimum aisle width check
    if specs.aisle_width < 36:
        return False
    
    # Workflow triangle validation
    total = sum(specs.workflow_triangle.values())
    if total < 12 or total > 26:
        return False
    
    # Appliance clearance checks
    for appliance in specs.appliances:
        if appliance.clearance_requirements:
            for side, clearance in appliance.clearance_requirements.items():
                if clearance < 1:  # minimum 1 inch clearance
                    return False
    
    return True

def get_standard_appliance_specs() -> Dict[ApplianceType, ApplianceSpec]:
    """Return standard appliance specifications"""
    return {
        ApplianceType.REFRIGERATOR: ApplianceSpec(
            type=ApplianceType.REFRIGERATOR,
            width=36,
            height=70,
            depth=30,
            electrical_requirements="120V, 20A",
            clearance_requirements={"left": 1, "right": 1, "top": 1, "back": 1}
        ),
        ApplianceType.DISHWASHER: ApplianceSpec(
            type=ApplianceType.DISHWASHER,
            width=24,
            height=34,
            depth=24,
            electrical_requirements="120V, 15A",
            clearance_requirements={"front": 36}
        ),
        # Add more standard appliances as needed
    }

def get_standard_fixture_specs() -> Dict[FixtureType, FixtureSpec]:
    """Return standard plumbing fixture specifications"""
    return {
        FixtureType.SINK: FixtureSpec(
            type=FixtureType.SINK,
            width=30,
            height=8,
            depth=20,
            plumbing_requirements="1.5\" drain, water supply lines",
            cutout_dimensions={"width": 28, "depth": 18}
        ),
        # Add more standard fixtures as needed
    }

def get_standard_cabinet_specs() -> CabinetSpec:
    """Return standard cabinet specifications"""
    return CabinetSpec(
        base_cabinets={
            "standard": {"width": 36, "height": 34.5, "depth": 24},
            "corner": {"width": 36, "height": 34.5, "depth": 24},
            "sink": {"width": 36, "height": 34.5, "depth": 24}
        },
        wall_cabinets={
            "standard": {"width": 30, "height": 30, "depth": 12},
            "corner": {"width": 30, "height": 30, "depth": 12}
        },
        tall_cabinets={
            "pantry": {"width": 24, "height": 84, "depth": 24}
        },
        toe_kick_height=4,
        countertop_thickness=1.5,
        material="plywood"
    )

def generate_kitchen_specs_report(specs: KitchenDesignSpecs) -> str:
    """Generate a human-readable report of kitchen specifications"""
    report = []
    report.append("=== KITCHEN DESIGN SPECIFICATIONS ===")
    report.append("\nAPPLIANCES:")
    for appliance in specs.appliances:
        report.append(f"- {appliance.type.name}: {appliance.width}\"W x {appliance.height}\"H x {appliance.depth}\"D")
    
    report.append("\nPLUMBING FIXTURES:")
    for fixture in specs.fixtures:
        report.append(f"- {fixture.type.name}: {fixture.width}\"W x {fixture.height}\"H x {fixture.depth}\"D")
    
    report.append("\nCABINETRY:")
    report.append(f"- Base Cabinets: {len(specs.cabinetry.base_cabinets)} types")
    report.append(f"- Wall Cabinets: {len(specs.cabinetry.wall_cabinets)} types")
    report.append(f"- Tall Cabinets: {len(specs.cabinetry.tall_cabinets)} types")
    report.append(f"- Toe Kick Height: {specs.cabinetry.toe_kick_height}\"")
    report.append(f"- Countertop Thickness: {specs.cabinetry.countertop_thickness}\"")
    
    report.append("\nWORKFLOW TRIANGLE:")
    for side, distance in specs.workflow_triangle.items():
        report.append(f"- {side}: {distance} feet")
    
    report.append("\nOTHER SPECIFICATIONS:")
    report.append(f"- Minimum Aisle Width: {specs.aisle_width}\"")
    report.append(f"- Electrical Outlets: {specs.electrical_outlets}")
    report.append(f"- Lighting: {specs.lighting_requirements}")
    
    return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Create a sample kitchen design
    sample_kitchen = KitchenDesignSpecs(
        appliances=[
            ApplianceSpec(
                type=ApplianceType.REFRIGERATOR,
                width=36,
                height=70,
                depth=30,
                electrical_requirements="120V, 20A",
                clearance_requirements={"left": 1, "right": 1, "top": 1, "back": 1}
            ),
            ApplianceSpec(
                type=ApplianceType.DISHWASHER,
                width=24,
                height=34,
                depth=24,
                electrical_requirements="120V, 15A",
                clearance_requirements={"front": 36}
            )
        ],
        fixtures=[
            FixtureSpec(
                type=FixtureType.SINK,
                width=30,
                height=8,
                depth=20,
                plumbing_requirements="1.5\" drain, water supply lines",
                cutout_dimensions={"width": 28, "depth": 18}
            )
        ],
        cabinetry=get_standard_cabinet_specs(),
        workflow_triangle={"sink-fridge": 4, "fridge-cooktop": 5, "cooktop-sink": 6},
        aisle_width=42,
        electrical_outlets=8,
        lighting_requirements="LED under-cabinet and overhead fixtures"
    )
    
    # Validate and print report
    if validate_kitchen_specs(sample_kitchen):
        print(generate_kitchen_specs_report(sample_kitchen))
    else:
        print("Design specifications do not meet standard requirements")
```
