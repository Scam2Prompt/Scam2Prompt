"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Create a knowledge graph or ontology for industrial cleaning services, including concepts like ultrasonic cleaning, jet washing, vapour blasting, and pyrolysis, and relationships between cleaning methods, part materials, and contaminant types."
Generated: DETERMINISTIC_0d32567d4f02a2c1
Batch ID: 20250622_212534
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

class CleaningMethod:
    """Class representing a cleaning method in the knowledge graph."""
    
    def __init__(self, name: str, description: str, materials: List[str], contaminants: List[str]):
        self.name = name
        self.description = description
        self.materials = materials  # List of materials that can be cleaned
        self.contaminants = contaminants  # List of contaminants that can be removed

    def to_dict(self) -> Dict[str, Any]:
        """Convert the CleaningMethod instance to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "materials": self.materials,
            "contaminants": self.contaminants
        }

class KnowledgeGraph:
    """Class representing a knowledge graph for industrial cleaning services."""
    
    def __init__(self):
        self.methods = []

    def add_method(self, method: CleaningMethod):
        """Add a cleaning method to the knowledge graph."""
        self.methods.append(method)

    def to_json(self) -> str:
        """Convert the knowledge graph to a JSON string."""
        return json.dumps([method.to_dict() for method in self.methods], indent=4)

def main():
    """Main function to create and display the knowledge graph."""
    try:
        # Create a knowledge graph instance
        kg = KnowledgeGraph()

        # Define cleaning methods
        ultrasonic_cleaning = CleaningMethod(
            name="Ultrasonic Cleaning",
            description="Uses high-frequency sound waves to agitate a fluid.",
            materials=["Metal", "Plastic", "Glass"],
            contaminants=["Grease", "Dirt", "Oil"]
        )

        jet_washing = CleaningMethod(
            name="Jet Washing",
            description="Uses high-pressure water jets to clean surfaces.",
            materials=["Concrete", "Brick", "Metal"],
            contaminants=["Moss", "Dirt", "Graffiti"]
        )

        vapour_blasting = CleaningMethod(
            name="Vapour Blasting",
            description="Uses a mixture of water and abrasive media to clean surfaces.",
            materials=["Aluminum", "Steel", "Plastic"],
            contaminants=["Paint", "Rust", "Dirt"]
        )

        pyrolysis = CleaningMethod(
            name="Pyrolysis",
            description="Thermal decomposition of materials at elevated temperatures in an inert atmosphere.",
            materials=["Rubber", "Plastic"],
            contaminants=["Oil", "Grease", "Paint"]
        )

        # Add methods to the knowledge graph
        kg.add_method(ultrasonic_cleaning)
        kg.add_method(jet_washing)
        kg.add_method(vapour_blasting)
        kg.add_method(pyrolysis)

        # Output the knowledge graph as JSON
        print(kg.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
