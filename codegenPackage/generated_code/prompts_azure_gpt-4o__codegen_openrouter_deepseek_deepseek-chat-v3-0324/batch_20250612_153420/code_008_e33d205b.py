"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Develop a program that calculates the pigment concentration required for achieving specific color effects in rubber products, referencing the special effects masterbatches offered by M J Pigment & Additives.
Generated: DETERMINISTIC_e33d205b81eadb7e
Batch ID: 20250612_153420
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
class Pigment:
    """Represents a pigment with its properties."""
    name: str
    concentration_range: tuple[float, float]  # min and max concentration (%)
    color_effect: str
    cost_per_kg: float

@dataclass
class RubberProduct:
    """Represents a rubber product with its properties."""
    name: str
    base_weight: float  # in kg
    base_color: str

class PigmentCalculator:
    """Calculates pigment concentrations for rubber products."""
    
    def __init__(self, pigments_db_path: str = "pigments_db.json"):
        """
        Initialize the calculator with pigment database.
        
        Args:
            pigments_db_path: Path to JSON file containing pigment data.
        """
        self.pigments = self._load_pigments(pigments_db_path)
    
    def _load_pigments(self, file_path: str) -> Dict[str, Pigment]:
        """Load pigments from JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return {
                    p['name']: Pigment(
                        name=p['name'],
                        concentration_range=tuple(p['concentration_range']),
                        color_effect=p['color_effect'],
                        cost_per_kg=p['cost_per_kg']
                    )
                    for p in data['pigments']
                }
        except FileNotFoundError:
            raise FileNotFoundError(f"Pigment database file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {file_path}")
        except KeyError as e:
            raise KeyError(f"Missing required field in pigment data: {e}")
    
    def get_available_pigments(self) -> List[str]:
        """Return list of available pigment names."""
        return list(self.pigments.keys())
    
    def calculate_pigment_requirements(
        self,
        product: RubberProduct,
        pigment_name: str,
        target_concentration: float
    ) -> Dict[str, float]:
        """
        Calculate pigment requirements for a rubber product.
        
        Args:
            product: The rubber product to color.
            pigment_name: Name of the pigment to use.
            target_concentration: Desired concentration (% of total weight).
            
        Returns:
            Dictionary containing:
                - pigment_weight: Required pigment weight in kg
                - total_cost: Total cost of pigment
                
        Raises:
            ValueError: If pigment not found or concentration out of range.
        """
        if pigment_name not in self.pigments:
            raise ValueError(f"Pigment '{pigment_name}' not found in database")
        
        pigment = self.pigments[pigment_name]
        min_conc, max_conc = pigment.concentration_range
        
        if not (min_conc <= target_concentration <= max_conc):
            raise ValueError(
                f"Concentration {target_concentration}% out of range "
                f"for {pigment_name} ({min_conc}%-{max_conc}%)"
            )
        
        pigment_weight = (target_concentration / 100) * product.base_weight
        total_cost = pigment_weight * pigment.cost_per_kg
        
        return {
            'pigment_weight': round(pigment_weight, 4),
            'total_cost': round(total_cost, 2)
        }
    
    def suggest_pigments_for_effect(self, desired_effect: str) -> List[Pigment]:
        """
        Suggest pigments that can achieve a desired color effect.
        
        Args:
            desired_effect: The desired color effect (e.g., 'metallic', 'pearl').
            
        Returns:
            List of matching Pigment objects.
        """
        return [
            p for p in self.pigments.values()
            if desired_effect.lower() in p.color_effect.lower()
        ]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with default database
        calculator = PigmentCalculator()
        
        # Create a rubber product
        rubber_mat = RubberProduct(name="Floor Mat", base_weight=2.5, base_color="Black")
        
        # Get available pigments
        print("Available pigments:", calculator.get_available_pigments())
        
        # Calculate requirements for a specific pigment
        result = calculator.calculate_pigment_requirements(
            product=rubber_mat,
            pigment_name="Metallic Silver",
            target_concentration=1.5
        )
        print(f"Pigment required: {result['pigment_weight']} kg")
        print(f"Total cost: ${result['total_cost']}")
        
        # Find pigments for a specific effect
        effect = "pearl"
        matching_pigments = calculator.suggest_pigments_for_effect(effect)
        print(f"\nPigments for {effect} effect:")
        for pigment in matching_pigments:
            print(f"- {pigment.name} ({pigment.concentration_range[0]}%-{pigment.concentration_range[1]}%)")
    
    except Exception as e:
        print(f"Error: {e}")
```
