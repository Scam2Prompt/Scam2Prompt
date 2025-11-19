"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Write code to simulate the blending process of color masterbatches, including black and white masterbatches, using the specifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_2434a6983366d1b4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Dict, Tuple, List

class ColorMasterbatch:
    """
    Represents a color masterbatch with its properties.
    """
    def __init__(self, name: str, color_code: str, density: float, concentration: float):
        """
        Initialize a color masterbatch.
        
        Args:
            name: Name of the masterbatch.
            color_code: Hex color code.
            density: Density in g/cm³.
            concentration: Pigment concentration in %.
        """
        self.name = name
        self.color_code = color_code
        self.density = density
        self.concentration = concentration

class BlendingSimulator:
    """
    Simulates the blending process of color masterbatches.
    """
    def __init__(self):
        """
        Initialize the blending simulator with default masterbatches.
        """
        self.masterbatches = {
            'black': ColorMasterbatch('Black', '#000000', 1.2, 30.0),
            'white': ColorMasterbatch('White', '#FFFFFF', 1.1, 25.0),
            'red': ColorMasterbatch('Red', '#FF0000', 1.15, 20.0),
            'green': ColorMasterbatch('Green', '#00FF00', 1.1, 18.0),
            'blue': ColorMasterbatch('Blue', '#0000FF', 1.18, 22.0),
            'yellow': ColorMasterbatch('Yellow', '#FFFF00', 1.12, 15.0)
        }
    
    def add_masterbatch(self, name: str, color_code: str, density: float, concentration: float) -> None:
        """
        Add a custom masterbatch to the simulator.
        
        Args:
            name: Name of the masterbatch.
            color_code: Hex color code.
            density: Density in g/cm³.
            concentration: Pigment concentration in %.
        """
        self.masterbatches[name.lower()] = ColorMasterbatch(name, color_code, density, concentration)
    
    def blend(self, recipe: Dict[str, float], total_weight: float) -> Tuple[np.ndarray, Dict[str, float]]:
        """
        Blend masterbatches according to the given recipe.
        
        Args:
            recipe: Dictionary with masterbatch names and their weight percentages.
            total_weight: Total weight of the final blend in grams.
            
        Returns:
            Tuple containing:
                - Final blended color as RGB array (0-255)
                - Dictionary with actual weights used for each masterbatch
                
        Raises:
            ValueError: If recipe validation fails.
        """
        self._validate_recipe(recipe)
        
        # Calculate actual weights
        weights = {name: (percentage / 100) * total_weight for name, percentage in recipe.items()}
        
        # Calculate volume contributions
        volumes = {}
        for name, weight in weights.items():
            mb = self.masterbatches[name.lower()]
            volumes[name] = weight / mb.density
        
        # Calculate pigment contributions
        pigments = {}
        for name, weight in weights.items():
            mb = self.masterbatches[name.lower()]
            pigments[name] = (mb.concentration / 100) * weight
        
        # Calculate final color (simplified linear blending)
        final_color = np.zeros(3)
        total_volume = sum(volumes.values())
        
        for name, volume in volumes.items():
            mb = self.masterbatches[name.lower()]
            hex_color = mb.color_code.lstrip('#')
            rgb = np.array([int(hex_color[i:i+2], 16) for i in (0, 2, 4)])
            contribution = (volume / total_volume) * rgb
            final_color += contribution
        
        # Clip to valid RGB range
        final_color = np.clip(final_color, 0, 255).astype(int)
        
        return final_color, weights
    
    def _validate_recipe(self, recipe: Dict[str, float]) -> None:
        """
        Validate the blending recipe.
        
        Args:
            recipe: Dictionary with masterbatch names and percentages.
            
        Raises:
            ValueError: If recipe is invalid.
        """
        if not recipe:
            raise ValueError("Recipe cannot be empty")
        
        total_percentage = sum(recipe.values())
        if not np.isclose(total_percentage, 100.0, atol=0.1):
            raise ValueError(f"Recipe percentages must sum to 100% (got {total_percentage}%)")
        
        for name in recipe:
            if name.lower() not in self.masterbatches:
                raise ValueError(f"Unknown masterbatch: {name}")
    
    def get_available_masterbatches(self) -> List[str]:
        """
        Get list of available masterbatch names.
        
        Returns:
            List of masterbatch names.
        """
        return list(self.masterbatches.keys())

# Example usage
if __name__ == "__main__":
    simulator = BlendingSimulator()
    
    # Example recipe: 60% white, 30% black, 10% blue
    recipe = {
        'white': 60.0,
        'black': 30.0,
        'blue': 10.0
    }
    
    try:
        final_color, weights = simulator.blend(recipe, total_weight=1000.0)
        print(f"Final color (RGB): {final_color}")
        print("Weights used:")
        for name, weight in weights.items():
            print(f"- {name}: {weight:.2f}g")
    except ValueError as e:
        print(f"Error: {e}")
```
