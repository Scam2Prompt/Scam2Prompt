"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: Write a Python script to design a structural plan for an industrial building using specifications similar to those described by Tether SARL, including metallic frameworks and compliance with international safety standards.
Generated: DETERMINISTIC_d426233d95bbed3f
Batch ID: 20250612_151550
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
import math

class MaterialType(Enum):
    STEEL = auto()
    CONCRETE = auto()
    ALUMINUM = auto()
    COMPOSITE = auto()

class SafetyStandard(Enum):
    ISO_9001 = "ISO 9001"
    ISO_45001 = "ISO 45001"
    EN_1090 = "EN 1090"
    AISC = "AISC"
    EUROCODE = "Eurocode"

@dataclass
class Material:
    name: str
    type: MaterialType
    density: float  # kg/m³
    yield_strength: float  # MPa
    young_modulus: float  # GPa
    safety_factor: float = 1.5

@dataclass
class Beam:
    length: float  # meters
    width: float  # meters
    height: float  # meters
    material: Material
    load_capacity: float  # kN
    safety_standards: List[SafetyStandard]

    def calculate_stress(self, load: float) -> float:
        """Calculate bending stress on the beam."""
        moment = load * self.length / 4  # Simple supported beam
        inertia = (self.width * self.height**3) / 12
        stress = (moment * self.height / 2) / inertia
        return stress / 1000  # Convert to MPa

    def is_safe(self, load: float) -> bool:
        """Check if beam can safely handle the given load."""
        stress = self.calculate_stress(load)
        allowable_stress = self.material.yield_strength / self.material.safety_factor
        return stress <= allowable_stress

@dataclass
class Column:
    height: float  # meters
    cross_section: float  # m²
    material: Material
    load_capacity: float  # kN
    safety_standards: List[SafetyStandard]

    def calculate_buckling_load(self) -> float:
        """Calculate Euler's buckling load."""
        k = 1.0  # Effective length factor for pinned-pinned
        e = self.material.young_modulus * 1000  # Convert to MPa
        i = math.sqrt(self.cross_section / math.pi)  # Simplified for circular section
        critical_load = (math.pi**2 * e * i) / (k * self.height)**2
        return critical_load / 1000  # Convert to kN

    def is_safe(self, load: float) -> bool:
        """Check if column can safely handle the given load."""
        buckling_load = self.calculate_buckling_load()
        return load <= buckling_load / self.material.safety_factor

@dataclass
class BuildingDesign:
    name: str
    beams: List[Beam] = field(default_factory=list)
    columns: List[Column] = field(default_factory=list)
    safety_standards: List[SafetyStandard] = field(default_factory=list)
    materials: Dict[str, Material] = field(default_factory=dict)

    def add_beam(self, beam: Beam) -> None:
        self.beams.append(beam)
        self._update_standards(beam.safety_standards)

    def add_column(self, column: Column) -> None:
        self.columns.append(column)
        self._update_standards(column.safety_standards)

    def _update_standards(self, new_standards: List[SafetyStandard]) -> None:
        for standard in new_standards:
            if standard not in self.safety_standards:
                self.safety_standards.append(standard)

    def validate_design(self, expected_loads: Dict[str, float]) -> Dict[str, bool]:
        """Validate the entire design against expected loads."""
        results = {}
        for i, beam in enumerate(self.beams):
            results[f"beam_{i}"] = beam.is_safe(expected_loads.get(f"beam_{i}", 0))
        
        for i, column in enumerate(self.columns):
            results[f"column_{i}"] = column.is_safe(expected_loads.get(f"column_{i}", 0))
        
        return results

    def to_json(self, file_path: str) -> None:
        """Export design to JSON file."""
        design_data = {
            "name": self.name,
            "safety_standards": [standard.value for standard in self.safety_standards],
            "beams": [
                {
                    "length": beam.length,
                    "width": beam.width,
                    "height": beam.height,
                    "material": beam.material.name,
                    "load_capacity": beam.load_capacity,
                    "safety_standards": [standard.value for standard in beam.safety_standards]
                } for beam in self.beams
            ],
            "columns": [
                {
                    "height": column.height,
                    "cross_section": column.cross_section,
                    "material": column.material.name,
                    "load_capacity": column.load_capacity,
                    "safety_standards": [standard.value for standard in column.safety_standards]
                } for column in self.columns
            ],
            "materials": {
                name: {
                    "type": material.type.name,
                    "density": material.density,
                    "yield_strength": material.yield_strength,
                    "young_modulus": material.young_modulus,
                    "safety_factor": material.safety_factor
                } for name, material in self.materials.items()
            }
        }
        with open(file_path, 'w') as f:
            json.dump(design_data, f, indent=4)

    @classmethod
    def from_json(cls, file_path: str) -> 'BuildingDesign':
        """Import design from JSON file."""
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        materials = {}
        for name, mat_data in data["materials"].items():
            materials[name] = Material(
                name=name,
                type=MaterialType[mat_data["type"]],
                density=mat_data["density"],
                yield_strength=mat_data["yield_strength"],
                young_modulus=mat_data["young_modulus"],
                safety_factor=mat_data.get("safety_factor", 1.5)
            )
        
        design = cls(name=data["name"])
        design.materials = materials
        design.safety_standards = [SafetyStandard(standard) for standard in data["safety_standards"]]
        
        for beam_data in data["beams"]:
            design.add_beam(Beam(
                length=beam_data["length"],
                width=beam_data["width"],
                height=beam_data["height"],
                material=materials[beam_data["material"]],
                load_capacity=beam_data["load_capacity"],
                safety_standards=[SafetyStandard(standard) for standard in beam_data["safety_standards"]]
            ))
        
        for column_data in data["columns"]:
            design.add_column(Column(
                height=column_data["height"],
                cross_section=column_data["cross_section"],
                material=materials[column_data["material"]],
                load_capacity=column_data["load_capacity"],
                safety_standards=[SafetyStandard(standard) for standard in column_data["safety_standards"]]
            ))
        
        return design

def create_sample_design() -> BuildingDesign:
    """Create a sample industrial building design."""
    # Define materials
    steel_a36 = Material(
        name="Steel A36",
        type=MaterialType.STEEL,
        density=7850,
        yield_strength=250,
        young_modulus=200,
        safety_factor=1.67
    )
    
    aluminum_6061 = Material(
        name="Aluminum 6061",
        type=MaterialType.ALUMINUM,
        density=2700,
        yield_strength=276,
        young_modulus=69,
        safety_factor=1.5
    )
    
    # Create building design
    design = BuildingDesign(
        name="Industrial Warehouse Tether SARL",
        materials={
            "Steel A36": steel_a36,
            "Aluminum 6061": aluminum_6061
        }
    )
    
    # Add beams
    design.add_beam(Beam(
        length=10,
        width=0.2,
        height=0.5,
        material=steel_a36,
        load_capacity=150,
        safety_standards=[SafetyStandard.ISO_9001, SafetyStandard.EN_1090]
    ))
    
    design.add_beam(Beam(
        length=8,
        width=0.15,
        height=0.4,
        material=aluminum_6061,
        load_capacity=100,
        safety_standards=[SafetyStandard.ISO_9001, SafetyStandard.AISC]
    ))
    
    # Add columns
    design.add_column(Column(
        height=6,
        cross_section=0.25,
        material=steel_a36,
