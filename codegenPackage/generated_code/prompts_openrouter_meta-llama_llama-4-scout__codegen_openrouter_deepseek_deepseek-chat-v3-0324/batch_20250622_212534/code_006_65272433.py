"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Write a technical guide on specifying the level of cleanliness required for industrial parts, including factors like surface roughness, material type, and contaminant level, and using standards and regulations like ISO 9001:2015."
Generated: DETERMINISTIC_652724339362f8e2
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Industrial Parts Cleanliness Specification System

This module provides functionality to specify cleanliness requirements for industrial parts
based on factors like surface roughness, material type, contaminant level, and compliance
with standards like ISO 9001:2015.

Classes:
    CleanlinessSpecification: Main class for defining cleanliness requirements
    CleanlinessValidator: Class for validating parts against specifications
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Dict
import re

class MaterialType(Enum):
    """Enumeration of common industrial material types"""
    METAL = "Metal"
    PLASTIC = "Plastic"
    CERAMIC = "Ceramic"
    COMPOSITE = "Composite"
    RUBBER = "Rubber"

class ContaminantType(Enum):
    """Enumeration of common contaminant types"""
    PARTICULATE = "Particulate"
    OIL = "Oil"
    GREASE = "Grease"
    CHEMICAL = "Chemical"
    BIOFILM = "Biofilm"

class StandardType(Enum):
    """Enumeration of relevant standards"""
    ISO_9001_2015 = "ISO 9001:2015"
    ISO_16232 = "ISO 16232"
    VDA_19 = "VDA 19"
    SAE_AS4059 = "SAE AS4059"

@dataclass
class SurfaceRoughness:
    """Data class representing surface roughness parameters"""
    Ra: float  # Average roughness in micrometers
    Rz: float  # Maximum height of the profile
    Rq: Optional[float] = None  # Root mean square roughness

@dataclass
class ContaminantLevel:
    """Data class representing contaminant levels"""
    type: ContaminantType
    max_concentration: float  # Maximum allowed concentration in mg/m²
    particle_size: Optional[float] = None  # Maximum particle size in microns (if applicable)

@dataclass
class CleanlinessSpecification:
    """
    Class representing cleanliness requirements for industrial parts
    
    Attributes:
        part_number: Identifier for the part
        material: Material type from MaterialType enum
        surface_roughness: Surface roughness requirements
        contaminants: List of allowed contaminant levels
        applicable_standards: List of standards the part must comply with
        notes: Optional additional requirements or notes
    """
    part_number: str
    material: MaterialType
    surface_roughness: SurfaceRoughness
    contaminants: List[ContaminantLevel]
    applicable_standards: List[StandardType]
    notes: Optional[str] = None

    def validate_part_number(self) -> bool:
        """Validate the part number format"""
        pattern = r'^[A-Z]{2,4}\d{4,6}(-[A-Z]\d)?$'
        return re.match(pattern, self.part_number) is not None

class CleanlinessValidator:
    """Class for validating parts against cleanliness specifications"""
    
    def __init__(self, specification: CleanlinessSpecification):
        self.specification = specification
    
    def validate_material(self, actual_material: MaterialType) -> bool:
        """Validate material type matches specification"""
        return actual_material == self.specification.material
    
    def validate_surface_roughness(self, actual_roughness: SurfaceRoughness) -> Dict[str, bool]:
        """Validate surface roughness meets requirements"""
        results = {
            'Ra': actual_roughness.Ra <= self.specification.surface_roughness.Ra,
            'Rz': actual_roughness.Rz <= self.specification.surface_roughness.Rz
        }
        
        if self.specification.surface_roughness.Rq is not None:
            results['Rq'] = actual_roughness.Rq <= self.specification.surface_roughness.Rq
            
        return results
    
    def validate_contaminants(self, actual_contaminants: List[ContaminantLevel]) -> Dict[str, bool]:
        """Validate contaminant levels meet requirements"""
        results = {}
        
        for spec_contaminant in self.specification.contaminants:
            found = False
            for actual_contaminant in actual_contaminants:
                if actual_contaminant.type == spec_contaminant.type:
                    found = True
                    if actual_contaminant.max_concentration > spec_contaminant.max_concentration:
                        results[str(spec_contaminant.type)] = False
                    else:
                        results[str(spec_contaminant.type)] = True
                    break
            
            if not found:
                results[str(spec_contaminant.type)] = True  # No contaminant means it passes
        
        return results
    
    def check_iso_9001_compliance(self) -> bool:
        """Check if specification includes ISO 9001:2015 requirements"""
        return StandardType.ISO_9001_2015 in self.specification.applicable_standards
    
    def get_validation_report(self, actual_material: MaterialType, 
                            actual_roughness: SurfaceRoughness, 
                            actual_contaminants: List[ContaminantLevel]) -> Dict:
        """
        Generate comprehensive validation report
        
        Returns:
            Dictionary containing all validation results and overall status
        """
        report = {
            'part_number_valid': self.specification.validate_part_number(),
            'material_match': self.validate_material(actual_material),
            'surface_roughness': self.validate_surface_roughness(actual_roughness),
            'contaminants': self.validate_contaminants(actual_contaminants),
            'iso_9001_compliant': self.check_iso_9001_compliance(),
            'specification': str(self.specification)
        }
        
        # Calculate overall status
        all_checks = [
            report['part_number_valid'],
            report['material_match'],
            all(report['surface_roughness'].values()),
            all(report['contaminants'].values())
        ]
        
        if StandardType.ISO_9001_2015 in self.specification.applicable_standards:
            all_checks.append(report['iso_9001_compliant'])
        
        report['overall_status'] = all(all_checks)
        
        return report

# Example usage
if __name__ == "__main__":
    # Create a cleanliness specification
    spec = CleanlinessSpecification(
        part_number="ABC1234",
        material=MaterialType.METAL,
        surface_roughness=SurfaceRoughness(Ra=0.8, Rz=3.2),
        contaminants=[
            ContaminantLevel(type=ContaminantType.OIL, max_concentration=1.0),
            ContaminantLevel(type=ContaminantType.PARTICULATE, max_concentration=0.5, particle_size=25)
        ],
        applicable_standards=[StandardType.ISO_9001_2015, StandardType.ISO_16232],
        notes="Special handling required for oil contamination"
    )
    
    # Create validator
    validator = CleanlinessValidator(spec)
    
    # Test data
    test_material = MaterialType.METAL
    test_roughness = SurfaceRoughness(Ra=0.7, Rz=3.0, Rq=0.9)
    test_contaminants = [
        ContaminantLevel(type=ContaminantType.OIL, max_concentration=0.8),
        ContaminantLevel(type=ContaminantType.PARTICULATE, max_concentration=0.4, particle_size=20)
    ]
    
    # Generate validation report
    report = validator.get_validation_report(
        actual_material=test_material,
        actual_roughness=test_roughness,
        actual_contaminants=test_contaminants
    )
    
    print("Validation Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
```
