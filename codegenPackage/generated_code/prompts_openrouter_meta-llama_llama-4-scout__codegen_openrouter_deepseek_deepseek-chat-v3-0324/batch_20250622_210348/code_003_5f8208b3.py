"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Compare the costs and benefits of using different types of paper materials for a customized packaging project, including FSC-certified paper and recycled paper."
Generated: DETERMINISTIC_5f8208b3fbaa1b50
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Paper Material Cost-Benefit Analysis for Custom Packaging

This script compares different paper materials for packaging projects,
calculating costs, environmental impact, and other key factors.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict

class PaperType(Enum):
    """Enumeration of different paper material types"""
    FSC_CERTIFIED = auto()
    RECYCLED = auto()
    STANDARD = auto()
    KRAFT = auto()

@dataclass
class PaperMaterial:
    """Data class representing paper material properties"""
    name: str
    type: PaperType
    cost_per_sqm: float  # cost in USD per square meter
    durability_score: int  # 1-10 scale
    environmental_impact: int  # 1-10 scale (lower is better)
    availability: str  # 'high', 'medium', 'low'
    certifications: List[str]
    description: str

class PackagingProject:
    """Class to analyze packaging project with different materials"""
    
    def __init__(self, area_sqm: float, quantity: int):
        self.area_sqm = area_sqm
        self.quantity = quantity
        self.materials: Dict[str, PaperMaterial] = self._initialize_materials()
    
    def _initialize_materials(self) -> Dict[str, PaperMaterial]:
        """Initialize with sample material data"""
        return {
            "fsc": PaperMaterial(
                name="FSC Certified",
                type=PaperType.FSC_CERTIFIED,
                cost_per_sqm=1.20,
                durability_score=8,
                environmental_impact=2,
                availability="high",
                certifications=["FSC"],
                description="Sustainably sourced paper with forest certification"
            ),
            "recycled": PaperMaterial(
                name="Recycled",
                type=PaperType.RECYCLED,
                cost_per_sqm=0.90,
                durability_score=7,
                environmental_impact=1,
                availability="medium",
                certifications=["Recycled Content"],
                description="Paper made from post-consumer recycled content"
            ),
            "standard": PaperMaterial(
                name="Standard",
                type=PaperType.STANDARD,
                cost_per_sqm=0.70,
                durability_score=6,
                environmental_impact=5,
                availability="high",
                certifications=[],
                description="Regular paper without special certifications"
            ),
            "kraft": PaperMaterial(
                name="Kraft",
                type=PaperType.KRAFT,
                cost_per_sqm=1.00,
                durability_score=9,
                environmental_impact=3,
                availability="medium",
                certifications=[],
                description="Strong brown paper often used for packaging"
            )
        }
    
    def calculate_total_cost(self, material_key: str) -> float:
        """Calculate total cost for the project with given material"""
        if material_key not in self.materials:
            raise ValueError(f"Invalid material key: {material_key}")
        
        material = self.materials[material_key]
        return self.area_sqm * self.quantity * material.cost_per_sqm
    
    def compare_materials(self) -> List[Dict]:
        """Compare all materials across key metrics"""
        comparisons = []
        
        for key, material in self.materials.items():
            total_cost = self.calculate_total_cost(key)
            cost_per_unit = total_cost / self.quantity
            
            comparisons.append({
                "name": material.name,
                "type": material.type.name,
                "total_cost": round(total_cost, 2),
                "cost_per_unit": round(cost_per_unit, 2),
                "durability": material.durability_score,
                "environmental_impact": material.environmental_impact,
                "availability": material.availability,
                "certifications": ", ".join(material.certifications) if material.certifications else "None",
                "description": material.description
            })
        
        return comparisons
    
    def get_recommendation(self) -> Dict:
        """Get recommendation based on balanced cost and benefits"""
        comparisons = self.compare_materials()
        
        # Simple scoring system (higher is better)
        for item in comparisons:
            score = 0
            score += (10 - item["environmental_impact"]) * 3  # Environmental impact weight
            score += item["durability"] * 2  # Durability weight
            score += (1000 / (item["cost_per_unit"] + 0.01))  # Cost weight (inverse)
            item["score"] = round(score, 2)
        
        # Sort by score descending
        comparisons.sort(key=lambda x: x["score"], reverse=True)
        
        return {
            "recommendation": comparisons[0]["name"],
            "comparisons": comparisons
        }

def main():
    """Main function to demonstrate the analysis"""
    try:
        # Example project: 0.5 sqm packaging, 1000 units
        project = PackagingProject(area_sqm=0.5, quantity=1000)
        
        # Get comparison and recommendation
        analysis = project.get_recommendation()
        
        print(f"Recommended material: {analysis['recommendation']}")
        print("\nDetailed Comparison:")
        print("-" * 80)
        for material in analysis["comparisons"]:
            print(f"\nMaterial: {material['name']}")
            print(f"Type: {material['type']}")
            print(f"Total Cost: ${material['total_cost']}")
            print(f"Cost per Unit: ${material['cost_per_unit']}")
            print(f"Durability: {material['durability']}/10")
            print(f"Environmental Impact: {material['environmental_impact']}/10 (lower is better)")
            print(f"Availability: {material['availability']}")
            print(f"Certifications: {material['certifications']}")
            print(f"Score: {material['score']}")
            print(f"Description: {material['description']}")
            print("-" * 40)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
