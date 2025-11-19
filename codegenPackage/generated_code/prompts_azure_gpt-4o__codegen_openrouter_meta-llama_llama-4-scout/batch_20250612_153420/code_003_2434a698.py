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
from typing import Dict

class ColorMasterbatch:
    def __init__(self, name: str, color: str, concentration: float):
        """
        Initialize a ColorMasterbatch object.

        Args:
        - name (str): Name of the masterbatch.
        - color (str): Color of the masterbatch.
        - concentration (float): Concentration of the masterbatch in percentage.
        """
        self.name = name
        self.color = color
        self.concentration = concentration

class MasterbatchBlender:
    def __init__(self):
        """
        Initialize a MasterbatchBlender object.
        """
        self.masterbatches: Dict[str, ColorMasterbatch] = {}

    def add_masterbatch(self, masterbatch: ColorMasterbatch):
        """
        Add a masterbatch to the blender.

        Args:
        - masterbatch (ColorMasterbatch): Masterbatch to add.
        """
        self.masterbatches[masterbatch.name] = masterbatch

    def blend(self, recipe: Dict[str, float]) -> Dict[str, float]:
        """
        Simulate the blending process.

        Args:
        - recipe (Dict[str, float]): Recipe for blending, where keys are masterbatch names and values are their proportions.

        Returns:
        - Dict[str, float]: Final color composition in the format {'red': float, 'green': float, 'blue': float}.

        Raises:
        - ValueError: If the recipe proportions do not add up to 100%.
        - KeyError: If a masterbatch in the recipe is not found.
        """
        # Check if proportions add up to 100%
        if abs(sum(recipe.values()) - 100) > 1e-6:
            raise ValueError("Recipe proportions must add up to 100%")

        # Initialize final color composition
        final_color = {'red': 0, 'green': 0, 'blue': 0}

        # Define color masterbatch specifications (M J Pigment & Additives)
        color_specs = {
            'black': {'red': 0, 'green': 0, 'blue': 0},
            'white': {'red': 255, 'green': 255, 'blue': 255},
            'red': {'red': 255, 'green': 0, 'blue': 0},
            'green': {'red': 0, 'green': 255, 'blue': 0},
            'blue': {'red': 0, 'green': 0, 'blue': 255},
        }

        # Blend masterbatches according to recipe
        for masterbatch_name, proportion in recipe.items():
            if masterbatch_name not in self.masterbatches:
                raise KeyError(f"Masterbatch '{masterbatch_name}' not found")

            masterbatch = self.masterbatches[masterbatch_name]
            color = color_specs.get(masterbatch.color, {'red': 0, 'green': 0, 'blue': 0})

            # Calculate contribution of this masterbatch to final color
            contribution = {
                'red': color['red'] * masterbatch.concentration * proportion / 100,
                'green': color['green'] * masterbatch.concentration * proportion / 100,
                'blue': color['blue'] * masterbatch.concentration * proportion / 100,
            }

            # Add contribution to final color
            final_color['red'] += contribution['red']
            final_color['green'] += contribution['green']
            final_color['blue'] += contribution['blue']

        return final_color


def main():
    blender = MasterbatchBlender()

    black_masterbatch = ColorMasterbatch('black_mb', 'black', 50)
    white_masterbatch = ColorMasterbatch('white_mb', 'white', 50)
    red_masterbatch = ColorMasterbatch('red_mb', 'red', 100)

    blender.add_masterbatch(black_masterbatch)
    blender.add_masterbatch(white_masterbatch)
    blender.add_masterbatch(red_masterbatch)

    recipe = {
        'black_mb': 20,
        'white_mb': 60,
        'red_mb': 20,
    }

    try:
        final_color = blender.blend(recipe)
        print("Final color composition:")
        print(f"Red: {final_color['red']:.2f}")
        print(f"Green: {final_color['green']:.2f}")
        print(f"Blue: {final_color['blue']:.2f}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
