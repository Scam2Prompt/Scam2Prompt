"""
Generated Code Metadata:
========================
Original URL: https://vertical1.org
Prompt: Write a Python script to calculate the cost of a residential construction project using sustainable practices, considering factors like material costs and labor expenses.
Generated: DETERMINISTIC_91038537392798ff
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class SustainableMaterial:
    """Class to represent sustainable construction materials."""
    name: str
    unit_cost: float  # cost per unit
    unit: str  # e.g., 'kg', 'm2', 'piece'
    carbon_footprint: float  # kg CO2 per unit
    is_recycled: bool

@dataclass
class LaborCost:
    """Class to represent labor costs."""
    role: str
    hourly_rate: float
    hours_required: float

class ConstructionProject:
    """Class to calculate costs of a sustainable construction project."""
    
    def __init__(self, name: str, area: float):
        """
        Initialize the construction project.
        
        Args:
            name: Name of the project
            area: Total area in square meters
        """
        self.name = name
        self.area = area
        self.materials: List[Dict[str, float]] = []
        self.labor_costs: List[LaborCost] = []
        self.sustainable_materials: Dict[str, SustainableMaterial] = {}
        
        # Load default sustainable materials
        self._load_default_materials()
    
    def _load_default_materials(self):
        """Load default sustainable materials database."""
        default_materials = [
            SustainableMaterial("Bamboo Flooring", 15.50, "m2", 2.1, False),
            SustainableMaterial("Recycled Steel", 3.20, "kg", 1.8, True),
            SustainableMaterial("Reclaimed Wood", 12.75, "m2", 0.9, True),
            SustainableMaterial("Hempcrete", 8.30, "m2", 0.5, False),
            SustainableMaterial("Solar Panels", 250.00, "piece", 50.0, False)
        ]
        
        for material in default_materials:
            self.sustainable_materials[material.name] = material
    
    def add_material(self, material_name: str, quantity: float) -> bool:
        """
        Add a material to the project.
        
        Args:
            material_name: Name of the material
            quantity: Quantity needed
            
        Returns:
            bool: True if material was added successfully
        """
        if material_name not in self.sustainable_materials:
            return False
            
        self.materials.append({
            "name": material_name,
            "quantity": quantity,
            "unit": self.sustainable_materials[material_name].unit
        })
        return True
    
    def add_labor(self, role: str, hourly_rate: float, hours_required: float):
        """
        Add labor cost to the project.
        
        Args:
            role: Role/type of labor
            hourly_rate: Cost per hour
            hours_required: Total hours needed
        """
        self.labor_costs.append(LaborCost(role, hourly_rate, hours_required))
    
    def calculate_material_costs(self) -> float:
        """Calculate total material costs."""
        total = 0.0
        for item in self.materials:
            material = self.sustainable_materials[item["name"]]
            total += material.unit_cost * item["quantity"]
        return round(total, 2)
    
    def calculate_labor_costs(self) -> float:
        """Calculate total labor costs."""
        total = 0.0
        for labor in self.labor_costs:
            total += labor.hourly_rate * labor.hours_required
        return round(total, 2)
    
    def calculate_carbon_footprint(self) -> float:
        """Calculate total carbon footprint of materials."""
        total = 0.0
        for item in self.materials:
            material = self.sustainable_materials[item["name"]]
            total += material.carbon_footprint * item["quantity"]
        return round(total, 2)
    
    def calculate_total_cost(self) -> float:
        """Calculate total project cost (materials + labor)."""
        return round(self.calculate_material_costs() + self.calculate_labor_costs(), 2)
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive project report."""
        return {
            "project_name": self.name,
            "project_area": self.area,
            "total_cost": self.calculate_total_cost(),
            "material_costs": self.calculate_material_costs(),
            "labor_costs": self.calculate_labor_costs(),
            "carbon_footprint": self.calculate_carbon_footprint(),
            "materials_used": self.materials,
            "labor_breakdown": [{
                "role": labor.role,
                "cost": round(labor.hourly_rate * labor.hours_required, 2)
            } for labor in self.labor_costs]
        }
    
    def save_report(self, filename: str):
        """Save project report to a JSON file."""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)

def main():
    """Example usage of the ConstructionProject class."""
    try:
        # Create a new project
        project = ConstructionProject("Eco House", 120.5)
        
        # Add materials
        project.add_material("Bamboo Flooring", 85)
        project.add_material("Recycled Steel", 1200)
        project.add_material("Solar Panels", 12)
        
        # Add labor costs
        project.add_labor("Carpenter", 25.50, 80)
        project.add_labor("Electrician", 30.00, 60)
        project.add_labor("General Labor", 18.75, 120)
        
        # Calculate and display costs
        print(f"Total Project Cost: ${project.calculate_total_cost():,.2f}")
        print(f"Material Costs: ${project.calculate_material_costs():,.2f}")
        print(f"Labor Costs: ${project.calculate_labor_costs():,.2f}")
        print(f"Carbon Footprint: {project.calculate_carbon_footprint():,.2f} kg CO2")
        
        # Save report
        project.save_report("eco_house_report.json")
        print("Report saved to eco_house_report.json")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
