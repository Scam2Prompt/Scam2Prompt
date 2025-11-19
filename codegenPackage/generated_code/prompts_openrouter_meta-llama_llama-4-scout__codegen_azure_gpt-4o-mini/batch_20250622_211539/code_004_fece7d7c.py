"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: "Generate a landscape design plan for a villa project with a focus on sustainability and environmental sensitivity, similar to Dens Haven's approach."
Generated: DETERMINISTIC_fece7d7c5110d723
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Plant:
    """Class representing a plant in the landscape design."""
    
    def __init__(self, name: str, water_needs: str, sunlight_needs: str, native: bool):
        self.name = name
        self.water_needs = water_needs
        self.sunlight_needs = sunlight_needs
        self.native = native

    def to_dict(self) -> Dict[str, Any]:
        """Convert the plant object to a dictionary."""
        return {
            "name": self.name,
            "water_needs": self.water_needs,
            "sunlight_needs": self.sunlight_needs,
            "native": self.native
        }

class LandscapeDesign:
    """Class representing a landscape design plan for a villa project."""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.plants: List[Plant] = []
        self.features: List[str] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the landscape design."""
        self.plants.append(plant)

    def add_feature(self, feature: str) -> None:
        """Add a sustainable feature to the landscape design."""
        self.features.append(feature)

    def generate_plan(self) -> Dict[str, Any]:
        """Generate the landscape design plan."""
        return {
            "project_name": self.project_name,
            "plants": [plant.to_dict() for plant in self.plants],
            "features": self.features
        }

    def save_plan(self, filename: str) -> None:
        """Save the landscape design plan to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan(), file, indent=4)
            print(f"Landscape design plan saved to {filename}.")
        except IOError as e:
            print(f"Error saving the plan: {e}")

# Example usage
if __name__ == "__main__":
    # Create a landscape design for a villa project
    design = LandscapeDesign("Sustainable Villa Project")

    # Add native plants to the design
    design.add_plant(Plant("Lavender", "Low", "Full Sun", True))
    design.add_plant(Plant("Coneflower", "Medium", "Full Sun", True))
    design.add_plant(Plant("Ferns", "High", "Shade", True))

    # Add sustainable features
    design.add_feature("Rainwater harvesting system")
    design.add_feature("Native plant garden")
    design.add_feature("Compost area")

    # Save the design plan to a file
    design.save_plan("landscape_design_plan.json")
```
