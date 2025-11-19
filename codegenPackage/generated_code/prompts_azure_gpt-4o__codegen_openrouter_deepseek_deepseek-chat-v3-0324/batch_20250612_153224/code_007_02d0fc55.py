"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Develop a program to curate interior design concepts that feel like a "warm embrace," as described by The Design Umbrella, and include functionality for material selection.
Generated: DETERMINISTIC_02d0fc55f262bf6b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum

class MaterialType(Enum):
    """Enum representing different types of materials."""
    FABRIC = "Fabric"
    WOOD = "Wood"
    METAL = "Metal"
    STONE = "Stone"
    GLASS = "Glass"
    CERAMIC = "Ceramic"

class Material:
    """Class representing a material with its properties."""
    
    def __init__(self, name: str, material_type: MaterialType, warmth_rating: int, texture: str, color: str):
        """
        Initialize a material.
        
        Args:
            name: Name of the material.
            material_type: Type of the material (from MaterialType enum).
            warmth_rating: Rating from 1-10 indicating warmth (higher is warmer).
            texture: Description of the texture.
            color: Color of the material.
        """
        self.name = name
        self.type = material_type
        self.warmth_rating = warmth_rating
        self.texture = texture
        self.color = color
    
    def to_dict(self) -> Dict:
        """Convert material to dictionary for serialization."""
        return {
            "name": self.name,
            "type": self.type.value,
            "warmth_rating": self.warmth_rating,
            "texture": self.texture,
            "color": self.color
        }

class DesignConcept:
    """Class representing an interior design concept."""
    
    def __init__(self, name: str, description: str, materials: List[Material]):
        """
        Initialize a design concept.
        
        Args:
            name: Name of the concept.
            description: Description of the concept.
            materials: List of materials used in the concept.
        """
        self.name = name
        self.description = description
        self.materials = materials
    
    def to_dict(self) -> Dict:
        """Convert design concept to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "materials": [material.to_dict() for material in self.materials]
        }

class DesignCurator:
    """Class to curate and manage interior design concepts."""
    
    def __init__(self):
        """Initialize the design curator with empty concepts list."""
        self.concepts: List[DesignConcept] = []
    
    def add_concept(self, concept: DesignConcept) -> None:
        """Add a design concept to the curator."""
        self.concepts.append(concept)
    
    def get_concepts_by_warmth(self, min_warmth: int = 7) -> List[DesignConcept]:
        """
        Get concepts with materials meeting minimum warmth rating.
        
        Args:
            min_warmth: Minimum warmth rating (1-10) to filter by.
            
        Returns:
            List of concepts where all materials meet the warmth threshold.
        """
        return [
            concept for concept in self.concepts
            if all(material.warmth_rating >= min_warmth for material in concept.materials)
        ]
    
    def get_concepts_by_material_type(self, material_type: MaterialType) -> List[DesignConcept]:
        """
        Get concepts containing a specific material type.
        
        Args:
            material_type: MaterialType to filter by.
            
        Returns:
            List of concepts containing the specified material type.
        """
        return [
            concept for concept in self.concepts
            if any(material.type == material_type for material in concept.materials)
        ]
    
    def save_to_file(self, filename: str) -> None:
        """
        Save concepts to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump([concept.to_dict() for concept in self.concepts], f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save concepts to file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """
        Load concepts from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Raises:
            IOError: If there's an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.concepts = []
                for item in data:
                    materials = [
                        Material(
                            name=mat["name"],
                            material_type=MaterialType(mat["type"]),
                            warmth_rating=mat["warmth_rating"],
                            texture=mat["texture"],
                            color=mat["color"]
                        ) for mat in item["materials"]
                    ]
                    self.concepts.append(
                        DesignConcept(
                            name=item["name"],
                            description=item["description"],
                            materials=materials
                        )
                    )
        except IOError as e:
            raise IOError(f"Failed to load concepts from file: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid data in file: {e}")

# Example usage
if __name__ == "__main__":
    # Create materials
    wool = Material("Wool", MaterialType.FABRIC, 9, "Soft and cozy", "Cream")
    oak = Material("Oak", MaterialType.WOOD, 8, "Smooth grain", "Warm brown")
    copper = Material("Copper", MaterialType.METAL, 7, "Slightly textured", "Rosy")
    
    # Create design concepts
    cozy_living = DesignConcept(
        "Cozy Living Room",
        "A warm embrace with soft textures and natural elements",
        [wool, oak, copper]
    )
    
    # Initialize curator and add concept
    curator = DesignCurator()
    curator.add_concept(cozy_living)
    
    # Save to file
    try:
        curator.save_to_file("design_concepts.json")
        print("Concepts saved successfully.")
    except IOError as e:
        print(f"Error saving concepts: {e}")
    
    # Load from file
    new_curator = DesignCurator()
    try:
        new_curator.load_from_file("design_concepts.json")
        print("Concepts loaded successfully.")
        
        # Get warm concepts
        warm_concepts = new_curator.get_concepts_by_warmth()
        print(f"Found {len(warm_concepts)} warm concepts")
        
    except (IOError, ValueError) as e:
        print(f"Error loading concepts: {e}")
```
