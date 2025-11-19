"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Create a function that generates sustainable product designs inspired by Linea 7’s approach, focusing on durability, functionality, and end-user experience.
Generated: DETERMINISTIC_e164909f81acdbe4
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional
from enum import Enum, auto

class MaterialType(Enum):
    """Enumeration of sustainable material types."""
    RECYCLED_PLASTIC = auto()
    BAMBOO = auto()
    ORGANIC_COTTON = auto()
    RECLAIMED_WOOD = auto()
    CORK = auto()
    HEMP = auto()

class DesignFeature(Enum):
    """Enumeration of design features focusing on sustainability."""
    MODULAR = auto()
    REPAIRABLE = auto()
    MULTI_FUNCTIONAL = auto()
    ENERGY_EFFICIENT = auto()
    BIODEGRADABLE = auto()
    MINIMAL_WASTE = auto()

class ProductDesign:
    """Class representing a sustainable product design."""
    
    def __init__(
        self,
        name: str,
        materials: List[MaterialType],
        features: List[DesignFeature],
        durability_score: int,
        functionality_score: int,
        user_experience_score: int
    ):
        """Initialize a product design with given attributes.
        
        Args:
            name: Name of the product design.
            materials: List of sustainable materials used.
            features: List of design features.
            durability_score: Score (1-10) for durability.
            functionality_score: Score (1-10) for functionality.
            user_experience_score: Score (1-10) for user experience.
        """
        self.name = name
        self.materials = materials
        self.features = features
        self.durability_score = durability_score
        self.functionality_score = functionality_score
        self.user_experience_score = user_experience_score
    
    def __str__(self) -> str:
        """Return a string representation of the product design."""
        return (
            f"Product: {self.name}\n"
            f"Materials: {', '.join([mat.name for mat in self.materials])}\n"
            f"Features: {', '.join([feat.name for feat in self.features])}\n"
            f"Durability: {self.durability_score}/10\n"
            f"Functionality: {self.functionality_score}/10\n"
            f"User Experience: {self.user_experience_score}/10"
        )

def generate_sustainable_design(product_name: str) -> ProductDesign:
    """Generate a sustainable product design inspired by Linea 7's approach.
    
    Args:
        product_name: Name of the product to generate design for.
    
    Returns:
        A ProductDesign object with sustainable attributes.
    """
    # Randomly select 2-3 sustainable materials
    materials = random.sample(
        list(MaterialType),
        k=random.randint(2, 3)
    )
    
    # Randomly select 3-4 design features
    features = random.sample(
        list(DesignFeature),
        k=random.randint(3, 4)
    )
    
    # Generate scores with emphasis on durability and functionality
    durability_score = random.randint(7, 10)
    functionality_score = random.randint(7, 10)
    user_experience_score = random.randint(6, 10)
    
    return ProductDesign(
        name=product_name,
        materials=materials,
        features=features,
        durability_score=durability_score,
        functionality_score=functionality_score,
        user_experience_score=user_experience_score
    )

def validate_design(design: ProductDesign) -> bool:
    """Validate if the design meets sustainability criteria.
    
    Args:
        design: ProductDesign object to validate.
    
    Returns:
        bool: True if design meets criteria, False otherwise.
    """
    # Minimum criteria for a sustainable design
    if (design.durability_score < 7 or
        design.functionality_score < 7 or
        design.user_experience_score < 6 or
        len(design.materials) < 2 or
        len(design.features) < 3):
        return False
    return True

def generate_valid_design(product_name: str, max_attempts: int = 10) -> Optional[ProductDesign]:
    """Generate a valid sustainable design within maximum attempts.
    
    Args:
        product_name: Name of the product to generate design for.
        max_attempts: Maximum number of attempts to generate a valid design.
    
    Returns:
        A valid ProductDesign or None if max_attempts reached.
    """
    for _ in range(max_attempts):
        design = generate_sustainable_design(product_name)
        if validate_design(design):
            return design
    return None

# Example usage
if __name__ == "__main__":
    product_name = "Eco-Friendly Chair"
    design = generate_valid_design(product_name)
    
    if design:
        print("Generated Sustainable Product Design:")
        print(design)
    else:
        print("Failed to generate a valid sustainable design after maximum attempts.")
```
