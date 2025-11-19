"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Develop a program to calculate the environmental impact of architectural materials used in projects like those described by Linea 7, emphasizing sustainability and livability.
Generated: DETERMINISTIC_948a05c00322f84c
Batch ID: 20250612_145615
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sustainablematerials.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional
import requests
from enum import Enum, auto

# Constants
API_BASE_URL = "https://api.sustainablematerials.com/v1"
DEFAULT_CARBON_FACTOR = 1.0  # Default carbon factor if not available from API

class MaterialCategory(Enum):
    CONCRETE = auto()
    STEEL = auto()
    WOOD = auto()
    GLASS = auto()
    INSULATION = auto()
    OTHER = auto()

@dataclass
class Material:
    name: str
    category: MaterialCategory
    quantity: float  # in kg or m3 depending on material
    carbon_factor: Optional[float] = None  # kg CO2 per unit
    recycled_content: float = 0.0  # percentage (0-100)
    distance_transported: float = 0.0  # km
    transport_emissions: float = 0.0  # kg CO2 per km per unit

@dataclass
class Project:
    name: str
    materials: List[Material]
    location: str
    area: float  # in square meters

class SustainabilityCalculator:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.carbon_factors_cache: Dict[str, float] = {}

    def _get_carbon_factor(self, material_name: str) -> float:
        """Fetch carbon factor from API or cache if available."""
        if material_name in self.carbon_factors_cache:
            return self.carbon_factors_cache[material_name]
        
        if not self.api_key:
            return DEFAULT_CARBON_FACTOR
            
        try:
            response = requests.get(
                f"{API_BASE_URL}/materials/{material_name}/carbon-factor",
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            factor = float(data["carbon_factor"])
            self.carbon_factors_cache[material_name] = factor
            return factor
        except (requests.RequestException, KeyError, ValueError) as e:
            print(f"Warning: Could not fetch carbon factor for {material_name}. Using default. Error: {e}")
            return DEFAULT_CARBON_FACTOR

    def calculate_material_impact(self, material: Material) -> float:
        """Calculate total CO2 emissions for a material."""
        if material.carbon_factor is None:
            material.carbon_factor = self._get_carbon_factor(material.name)
        
        production_emissions = material.quantity * material.carbon_factor
        transport_emissions = material.quantity * material.distance_transported * material.transport_emissions
        recycled_offset = production_emissions * (material.recycled_content / 100) * 0.5  # 50% reduction for recycled
        
        return production_emissions + transport_emissions - recycled_offset

    def calculate_project_impact(self, project: Project) -> Dict[str, float]:
        """Calculate total CO2 emissions for a project."""
        total_emissions = 0.0
        material_impacts = {}
        
        for material in project.materials:
            impact = self.calculate_material_impact(material)
            material_impacts[material.name] = impact
            total_emissions += impact
        
        return {
            "total_emissions_kg": total_emissions,
            "emissions_per_sqm": total_emissions / project.area,
            "material_breakdown": material_impacts
        }

    def generate_report(self, project: Project, output_format: str = "text") -> str:
        """Generate a sustainability report for the project."""
        impact = self.calculate_project_impact(project)
        
        if output_format == "json":
            return json.dumps({
                "project_name": project.name,
                "location": project.location,
                "area_sqm": project.area,
                **impact
            }, indent=2)
        
        # Default to text format
        report_lines = [
            f"Sustainability Report for Project: {project.name}",
            f"Location: {project.location}",
            f"Area: {project.area} sqm",
            "\n--- Carbon Emissions ---",
            f"Total: {impact['total_emissions_kg']:.2f} kg CO2",
            f"Per Square Meter: {impact['emissions_per_sqm']:.2f} kg CO2/sqm",
            "\n--- Material Breakdown ---"
        ]
        
        for material, emissions in impact["material_breakdown"].items():
            report_lines.append(f"- {material}: {emissions:.2f} kg CO2")
            
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    # Initialize calculator (API key optional)
    calculator = SustainabilityCalculator(api_key="your_api_key_here")
    
    # Create a sample project
    project = Project(
        name="Eco-Friendly Office Building",
        location="San Francisco, CA",
        area=5000,
        materials=[
            Material(
                name="Recycled Steel",
                category=MaterialCategory.STEEL,
                quantity=15000,  # kg
                recycled_content=80,
                distance_transported=200,
                transport_emissions=0.0005
            ),
            Material(
                name="Cross-Laminated Timber",
                category=MaterialCategory.WOOD,
                quantity=8000,  # kg
                recycled_content=30,
                distance_transported=150,
                transport_emissions=0.0003
            ),
            Material(
                name="Low-Carbon Concrete",
                category=MaterialCategory.CONCRETE,
                quantity=50000,  # kg
                distance_transported=50,
                transport_emissions=0.0008
            )
        ]
    )
    
    # Generate and print report
    print(calculator.generate_report(project))
```
