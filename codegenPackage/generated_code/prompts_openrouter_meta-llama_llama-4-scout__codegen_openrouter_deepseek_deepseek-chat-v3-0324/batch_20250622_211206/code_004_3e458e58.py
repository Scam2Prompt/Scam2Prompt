"""
Generated Code Metadata:
========================
Original URL: https://1inchclub.xyz
Prompt: Develop a simple material creation algorithm inspired by the AI that created 41 new materials in 17 days, as reported on KlimaDAO.
Generated: DETERMINISTIC_3e458e5825f6b9be
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Element:
    """Represents a chemical element with its properties."""
    symbol: str
    atomic_number: int
    electronegativity: float
    atomic_radius: float
    valence_electrons: int

@dataclass
class Material:
    """Represents a material composed of elements with a specific composition."""
    elements: List[Tuple[Element, float]]  # (Element, percentage)
    formation_energy: float
    stability_score: float

class MaterialGenerator:
    """Generates new materials based on element combinations and stability criteria."""
    
    def __init__(self, elements_db_path: str = 'elements.json'):
        """
        Initialize the generator with a database of elements.
        
        Args:
            elements_db_path: Path to JSON file containing element data.
        """
        self.elements = self._load_elements(elements_db_path)
        self.used_combinations = set()  # Track tried combinations to avoid duplicates
        
    def _load_elements(self, file_path: str) -> List[Element]:
        """Load elements from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                elements_data = json.load(f)
            return [Element(**data) for data in elements_data]
        except FileNotFoundError:
            logger.error(f"Elements database not found at {file_path}")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in elements database")
            raise
        except Exception as e:
            logger.error(f"Error loading elements: {str(e)}")
            raise
    
    def _calculate_stability(self, material: Material) -> float:
        """
        Calculate a stability score for the material based on:
        - Electronegativity differences
        - Valence electron compatibility
        - Atomic radius ratios
        
        Returns:
            A stability score between 0 (unstable) and 1 (stable)
        """
        if len(material.elements) == 1:
            return 1.0  # Pure elements are considered stable
            
        total_score = 0.0
        pairs = [(a, b) for idx, a in enumerate(material.elements) for b in material.elements[idx+1:]]
        
        for (el1, perc1), (el2, perc2) in pairs:
            # Electronegativity difference (smaller is better)
            en_diff = abs(el1.electronegativity - el2.electronegativity)
            en_score = np.exp(-en_diff)
            
            # Valence compatibility (sum should be 8 for optimal stability)
            valence_sum = el1.valence_electrons + el2.valence_electrons
            valence_score = 1 - abs(valence_sum - 8)/8
            
            # Atomic radius ratio (should be close to 1)
            radius_ratio = max(el1.atomic_radius, el2.atomic_radius) / min(el1.atomic_radius, el2.atomic_radius)
            radius_score = np.exp(-abs(radius_ratio - 1))
            
            # Weighted average of scores
            pair_score = (en_score * 0.4 + valence_score * 0.3 + radius_score * 0.3)
            total_score += pair_score * (perc1 + perc2)/2
            
        return total_score / len(pairs) if pairs else 0.0
    
    def _generate_composition(self, num_elements: int) -> List[Tuple[Element, float]]:
        """
        Generate a random composition of elements.
        
        Args:
            num_elements: Number of elements in the composition
            
        Returns:
            List of (Element, percentage) tuples that sum to 100%
        """
        selected = random.sample(self.elements, num_elements)
        percentages = np.random.dirichlet(np.ones(num_elements), size=1)[0] * 100
        return list(zip(selected, percentages))
    
    def generate_materials(self, 
                          num_materials: int = 10, 
                          max_elements: int = 3,
                          min_stability: float = 0.7) -> List[Material]:
        """
        Generate new materials meeting stability criteria.
        
        Args:
            num_materials: Number of materials to generate
            max_elements: Maximum number of elements per material
            min_stability: Minimum stability score required
            
        Returns:
            List of generated Material objects
        """
        materials = []
        attempts = 0
        max_attempts = num_materials * 10  # Prevent infinite loops
        
        while len(materials) < num_materials and attempts < max_attempts:
            attempts += 1
            num_elements = random.randint(1, max_elements)
            composition = self._generate_composition(num_elements)
            
            # Create a unique key for this combination
            combo_key = tuple(sorted((el.symbol for el, _ in composition)))
            if combo_key in self.used_combinations:
                continue
                
            self.used_combinations.add(combo_key)
            
            # Create material and calculate properties
            material = Material(
                elements=composition,
                formation_energy=random.uniform(-5.0, 5.0),  # Placeholder for actual calculation
                stability_score=0.0
            )
            
            material.stability_score = self._calculate_stability(material)
            
            if material.stability_score >= min_stability:
                materials.append(material)
                logger.info(f"Generated material {len(materials)}/{num_materials}")
                
        if len(materials) < num_materials:
            logger.warning(f"Only generated {len(materials)} materials meeting criteria")
            
        return materials

# Example usage
if __name__ == "__main__":
    try:
        generator = MaterialGenerator()
        new_materials = generator.generate_materials(num_materials=5)
        
        # Print results
        for i, material in enumerate(new_materials, 1):
            elements = ", ".join(f"{el.symbol} ({perc:.1f}%)" for el, perc in material.elements)
            print(f"Material {i}: {elements}")
            print(f"Stability: {material.stability_score:.2f}, Formation Energy: {material.formation_energy:.2f} eV")
            print()
            
    except Exception as e:
        logger.error(f"Error in material generation: {str(e)}")
```
