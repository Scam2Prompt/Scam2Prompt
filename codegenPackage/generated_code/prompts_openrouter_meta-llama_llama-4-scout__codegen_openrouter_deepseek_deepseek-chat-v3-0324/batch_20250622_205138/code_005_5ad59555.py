"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: "Develop a Python program to analyze the specifications of tractor pulling sleds, like the measurements and plans for mini sleds discussed on jobbo.com.au, and provide recommendations for modifications."
Generated: DETERMINISTIC_5ad595551a8611de
Batch ID: 20250622_205138
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
from typing import List, Optional, Dict
import math

@dataclass
class SledComponent:
    """Represents a component of a tractor pulling sled."""
    name: str
    length: float  # in meters
    width: float   # in meters
    weight: float  # in kilograms
    material: str
    notes: Optional[str] = None

@dataclass
class SledDesign:
    """Represents a complete tractor pulling sled design."""
    name: str
    components: List[SledComponent]
    total_weight: float
    total_length: float
    total_width: float
    max_speed: float  # in km/h
    notes: Optional[str] = None

class SledAnalyzer:
    """Analyzes tractor pulling sled designs and provides recommendations."""
    
    def __init__(self):
        self.designs: Dict[str, SledDesign] = {}
        self.material_properties = {
            'steel': {'density': 7850, 'strength': 400},
            'aluminum': {'density': 2700, 'strength': 310},
            'carbon_fiber': {'density': 1600, 'strength': 500}
        }
    
    def load_design_from_file(self, file_path: str) -> SledDesign:
        """Load a sled design from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                components = [
                    SledComponent(**component) for component in data['components']
                ]
                design = SledDesign(
                    name=data['name'],
                    components=components,
                    total_weight=data['total_weight'],
                    total_length=data['total_length'],
                    total_width=data['total_width'],
                    max_speed=data['max_speed'],
                    notes=data.get('notes')
                )
                self.designs[design.name] = design
                return design
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {file_path}")
        except KeyError as e:
            raise ValueError(f"Missing required field in JSON: {e}")
    
    def calculate_design_metrics(self, design: SledDesign) -> Dict[str, float]:
        """Calculate various metrics for a sled design."""
        metrics = {
            'weight_distribution': {},
            'strength_to_weight_ratio': 0,
            'aerodynamic_factor': 0
        }
        
        total_weight = 0
        for component in design.components:
            metrics['weight_distribution'][component.name] = (
                component.weight / design.total_weight * 100
            )
            material_strength = self.material_properties.get(
                component.material, {}
            ).get('strength', 0)
            metrics['strength_to_weight_ratio'] += (
                material_strength / component.weight if component.weight > 0 else 0
            )
            total_weight += component.weight
        
        # Normalize strength to weight ratio
        metrics['strength_to_weight_ratio'] /= len(design.components)
        
        # Simple aerodynamic factor calculation
        frontal_area = design.total_width * design.total_length
        metrics['aerodynamic_factor'] = (
            design.max_speed ** 2 * frontal_area * 0.5
        )
        
        return metrics
    
    def generate_recommendations(self, design: SledDesign) -> List[str]:
        """Generate recommendations for improving a sled design."""
        recommendations = []
        metrics = self.calculate_design_metrics(design)
        
        # Weight distribution analysis
        for comp_name, percent in metrics['weight_distribution'].items():
            if percent > 30:
                recommendations.append(
                    f"Consider redistributing weight from {comp_name} "
                    f"(currently {percent:.1f}% of total weight)"
                )
        
        # Material recommendations
        for component in design.components:
            if component.material == 'steel' and component.weight > 50:
                recommendations.append(
                    f"Consider replacing {component.name} with aluminum "
                    "or carbon fiber to reduce weight"
                )
        
        # Aerodynamic improvements
        if metrics['aerodynamic_factor'] > 5000:
            recommendations.append(
                "Consider aerodynamic improvements to reduce drag at high speeds"
            )
        
        # General recommendations
        if design.total_weight > 1000:
            recommendations.append(
                "The sled may be too heavy for smaller tractors, "
                "consider weight reduction"
            )
        
        return recommendations
    
    def compare_designs(self, design1: SledDesign, design2: SledDesign) -> Dict[str, str]:
        """Compare two sled designs and highlight differences."""
        comparison = {}
        metrics1 = self.calculate_design_metrics(design1)
        metrics2 = self.calculate_design_metrics(design2)
        
        comparison['weight'] = (
            f"Design {design1.name}: {design1.total_weight} kg vs "
            f"Design {design2.name}: {design2.total_weight} kg"
        )
        
        comparison['aerodynamics'] = (
            f"Design {design1.name} aerodynamic factor: {metrics1['aerodynamic_factor']:.1f} vs "
            f"Design {design2.name}: {metrics2['aerodynamic_factor']:.1f}"
        )
        
        comparison['strength_to_weight'] = (
            f"Design {design1.name} strength-to-weight: {metrics1['strength_to_weight_ratio']:.1f} vs "
            f"Design {design2.name}: {metrics2['strength_to_weight_ratio']:.1f}"
        )
        
        return comparison
    
    def save_recommendations(self, recommendations: List[str], file_path: str):
        """Save recommendations to a text file."""
        try:
            with open(file_path, 'w') as f:
                f.write("Tractor Pulling Sled Recommendations:\n")
                f.write("=" * 50 + "\n")
                for i, rec in enumerate(recommendations, 1):
                    f.write(f"{i}. {rec}\n")
        except IOError as e:
            raise ValueError(f"Error writing to file: {e}")

# Example usage
if __name__ == "__main__":
    analyzer = SledAnalyzer()
    
    try:
        # Load a design
        design = analyzer.load_design_from_file("sled_design.json")
        
        # Analyze and get recommendations
        recommendations = analyzer.generate_recommendations(design)
        
        # Print recommendations
        print("Recommendations for design:", design.name)
        for rec in recommendations:
            print("-", rec)
        
        # Save recommendations to file
        analyzer.save_recommendations(recommendations, "sled_recommendations.txt")
        
    except ValueError as e:
        print(f"Error: {e}")
```
