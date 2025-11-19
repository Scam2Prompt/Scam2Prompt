"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: "Create a specification sheet for a gypsum board partition system for an IT building."
Generated: DETERMINISTIC_4d4df78cfe4a09df
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gypsum Board Partition System Specification Sheet Generator for IT Buildings

This script generates a detailed specification sheet for gypsum board partition systems
tailored for IT buildings, considering acoustic, fire, and structural requirements.
"""

import json
from datetime import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class PartitionLayer:
    """Represents a single layer in the partition system"""
    material: str
    thickness_mm: float
    purpose: str
    fire_rating_min: Optional[int] = None
    stc_rating: Optional[int] = None

@dataclass
class PartitionSystem:
    """Represents a complete partition system specification"""
    system_name: str
    description: str
    layers: List[PartitionLayer]
    total_thickness_mm: float
    fire_rating_hrs: float
    stc_rating: int
    installation_guidelines: str
    compatible_accessories: List[str]
    manufacturer: str
    code_compliance: List[str]

class SpecificationGenerator:
    """Generates specification sheets for partition systems"""
    
    def __init__(self):
        self.template = {
            "header": {
                "project": "IT Building Partition System",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "prepared_by": "Architectural Specifications Team",
                "version": "1.0"
            },
            "systems": []
        }
    
    def add_system(self, system: PartitionSystem) -> None:
        """Add a partition system to the specification sheet"""
        system_data = {
            "system_name": system.system_name,
            "description": system.description,
            "total_thickness_mm": system.total_thickness_mm,
            "fire_rating_hrs": system.fire_rating_hrs,
            "stc_rating": system.stc_rating,
            "installation_guidelines": system.installation_guidelines,
            "compatible_accessories": system.compatible_accessories,
            "manufacturer": system.manufacturer,
            "code_compliance": system.code_compliance,
            "layers": [
                {
                    "material": layer.material,
                    "thickness_mm": layer.thickness_mm,
                    "purpose": layer.purpose,
                    "fire_rating_min": layer.fire_rating_min,
                    "stc_rating": layer.stc_rating
                } for layer in system.layers
            ]
        }
        self.template["systems"].append(system_data)
    
    def generate_spec_sheet(self, output_format: str = "json") -> str:
        """
        Generate the specification sheet in the requested format
        Supported formats: json, pretty_json
        """
        if output_format == "json":
            return json.dumps(self.template)
        elif output_format == "pretty_json":
            return json.dumps(self.template, indent=2)
        else:
            raise ValueError(f"Unsupported output format: {output_format}")

def create_it_building_systems() -> List[PartitionSystem]:
    """Create standard partition systems for IT buildings"""
    
    # Standard acoustic partition system
    acoustic_system = PartitionSystem(
        system_name="IT-A1 Acoustic Partition",
        description="High-performance acoustic partition for IT server rooms and offices",
        layers=[
            PartitionLayer(
                material="15mm Type X Gypsum Board",
                thickness_mm=15,
                purpose="Face layer",
                fire_rating_min=60,
                stc_rating=52
            ),
            PartitionLayer(
                material="50mm Acoustic Mineral Wool",
                thickness_mm=50,
                purpose="Sound insulation",
                stc_rating=45
            ),
            PartitionLayer(
                material="15mm Type X Gypsum Board",
                thickness_mm=15,
                purpose="Face layer",
                fire_rating_min=60,
                stc_rating=52
            )
        ],
        total_thickness_mm=80,
        fire_rating_hrs=2,
        stc_rating=55,
        installation_guidelines="Install on 92mm metal studs at 600mm centers",
        compatible_accessories=[
            "Acoustic sealant",
            "Resilient channels",
            "Soundproof door kits"
        ],
        manufacturer="GypsumTech Inc.",
        code_compliance=["ASTM C1396", "UL Design U419", "IBC Section 2507"]
    )
    
    # Fire-rated partition system
    fire_system = PartitionSystem(
        system_name="IT-F1 Fire Partition",
        description="2-hour fire-rated partition for IT equipment rooms",
        layers=[
            PartitionLayer(
                material="16mm Fire-Shield Gypsum Board",
                thickness_mm=16,
                purpose="Face layer",
                fire_rating_min=120,
                stc_rating=48
            ),
            PartitionLayer(
                material="16mm Fire-Shield Gypsum Board",
                thickness_mm=16,
                purpose="Face layer",
                fire_rating_min=120,
                stc_rating=48
            )
        ],
        total_thickness_mm=32,
        fire_rating_hrs=2,
        stc_rating=50,
        installation_guidelines="Install on 64mm metal studs at 400mm centers",
        compatible_accessories=[
            "Fire-rated sealant",
            "Firestop systems",
            "Fire-rated door assemblies"
        ],
        manufacturer="FireSafe Partitions LLC",
        code_compliance=["ASTM E119", "UL Design U301", "NFPA 101"]
    )
    
    return [acoustic_system, fire_system]

def main():
    """Generate and output the specification sheet"""
    try:
        generator = SpecificationGenerator()
        systems = create_it_building_systems()
        
        for system in systems:
            generator.add_system(system)
        
        spec_sheet = generator.generate_spec_sheet(output_format="pretty_json")
        print(spec_sheet)
        
        # Optionally save to file
        with open("gypsum_partition_specs.json", "w") as f:
            f.write(spec_sheet)
            
    except Exception as e:
        print(f"Error generating specification sheet: {str(e)}")

if __name__ == "__main__":
    main()
```
