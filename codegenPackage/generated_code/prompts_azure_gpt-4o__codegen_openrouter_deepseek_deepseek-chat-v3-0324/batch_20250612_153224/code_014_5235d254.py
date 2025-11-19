"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write code to simulate the construction of tennis courts with security features and top-tier materials, inspired by C&M Pinnacle's Goldfields Tennis Court project.
Generated: DETERMINISTIC_5235d25427f7aba2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import random
import time

class MaterialGrade(enum.Enum):
    """Enum representing different material grades for tennis court construction."""
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PINNACLE = "Pinnacle (Top-tier)"

class SecurityFeature(enum.Enum):
    """Enum representing different security features for tennis courts."""
    SURVEILLANCE_CAMERAS = "Surveillance Cameras"
    MOTION_SENSORS = "Motion Sensors"
    ACCESS_CONTROL = "Access Control System"
    LIGHTING = "Perimeter Lighting"
    FENCING = "High-Security Fencing"

@dataclass
class CourtSpecifications:
    """Data class representing specifications for a tennis court."""
    length: float  # in meters
    width: float   # in meters
    surface_type: str
    material_grade: MaterialGrade
    security_features: List[SecurityFeature]
    has_lighting: bool
    has_spectator_seating: bool

class TennisCourtBuilder:
    """Class to simulate the construction of tennis courts with security features."""
    
    def __init__(self):
        self.available_materials = {
            MaterialGrade.STANDARD: {"asphalt": 50, "concrete": 60, "acrylic": 70},
            MaterialGrade.PREMIUM: {"porous_acrylic": 90, "artificial_grass": 85},
            MaterialGrade.PINNACLE: {"hybrid_clay": 120, "premium_grass": 150}
        }
        
        self.construction_steps = [
            "Site Preparation",
            "Base Construction",
            "Surface Layering",
            "Line Marking",
            "Net Installation",
            "Security Installation",
            "Final Inspection"
        ]
    
    def validate_specifications(self, specs: CourtSpecifications) -> bool:
        """Validate court specifications."""
        if specs.length <= 0 or specs.width <= 0:
            raise ValueError("Court dimensions must be positive numbers")
        if specs.surface_type not in self._get_available_surfaces(specs.material_grade):
            raise ValueError(f"Invalid surface type for {specs.material_grade.value} grade")
        return True
    
    def _get_available_surfaces(self, grade: MaterialGrade) -> List[str]:
        """Get available surfaces for a material grade."""
        return list(self.available_materials[grade].keys())
    
    def _calculate_construction_time(self, specs: CourtSpecifications) -> int:
        """Estimate construction time in days based on specifications."""
        base_time = 10  # base days
        time_factor = {
            MaterialGrade.STANDARD: 1.0,
            MaterialGrade.PREMIUM: 1.2,
            MaterialGrade.PINNACLE: 1.5
        }
        security_factor = 1 + (len(specs.security_features) * 0.1)
        return int(base_time * time_factor[specs.material_grade] * security_factor)
    
    def _calculate_cost(self, specs: CourtSpecifications) -> float:
        """Calculate estimated cost based on specifications."""
        base_cost = self.available_materials[specs.material_grade][specs.surface_type]
        area = specs.length * specs.width
        security_cost = len(specs.security_features) * 500
        lighting_cost = 1000 if specs.has_lighting else 0
        seating_cost = 2000 if specs.has_spectator_seating else 0
        return (base_cost * area) + security_cost + lighting_cost + seating_cost
    
    def construct_court(self, specs: CourtSpecifications) -> Dict:
        """Simulate the construction of a tennis court."""
        try:
            self.validate_specifications(specs)
            
            print(f"\nStarting construction of {specs.material_grade.value} tennis court...")
            print(f"Surface: {specs.surface_type}, Dimensions: {specs.length}m x {specs.width}m")
            
            construction_time = self._calculate_construction_time(specs)
            total_cost = self._calculate_cost(specs)
            
            # Simulate construction steps
            for step in self.construction_steps:
                time.sleep(0.5)  # Simulate time taken for each step
                print(f" - {step}... [COMPLETED]")
            
            print("\nConstruction completed successfully!")
            print(f"Total construction time: {construction_time} days")
            print(f"Estimated cost: ${total_cost:,.2f}")
            
            return {
                "status": "success",
                "construction_time_days": construction_time,
                "estimated_cost": total_cost,
                "specifications": specs
            }
        except Exception as e:
            print(f"\nConstruction failed: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }

def generate_sample_court() -> CourtSpecifications:
    """Generate a sample court specification inspired by C&M Pinnacle's Goldfields project."""
    return CourtSpecifications(
        length=23.77,  # Standard tennis court length
        width=10.97,   # Standard tennis court width (singles)
        surface_type="hybrid_clay",
        material_grade=MaterialGrade.PINNACLE,
        security_features=[
            SecurityFeature.SURVEILLANCE_CAMERAS,
            SecurityFeature.ACCESS_CONTROL,
            SecurityFeature.FENCING,
            SecurityFeature.LIGHTING
        ],
        has_lighting=True,
        has_spectator_seating=True
    )

if __name__ == "__main__":
    builder = TennisCourtBuilder()
    
    # Build a sample premium court
    sample_specs = generate_sample_court()
    construction_result = builder.construct_court(sample_specs)
```
