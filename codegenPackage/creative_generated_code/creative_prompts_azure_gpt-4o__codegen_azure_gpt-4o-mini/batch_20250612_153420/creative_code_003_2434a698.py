"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Write code to simulate the blending process of color masterbatches, including black and white masterbatches, using the specifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_2434a6983366d1b4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ColorMasterbatch:
    """
    A class to represent a color masterbatch for blending.
    
    Attributes:
        color (str): The color of the masterbatch.
        percentage (float): The percentage of this masterbatch in the blend.
    """

    def __init__(self, color: str, percentage: float):
        """
        Initializes a ColorMasterbatch with its color and percentage.

        Parameters:
            color (str): The color of the masterbatch.
            percentage (float): The percentage of this masterbatch in the blend.

        Raises:
            ValueError: If percentage is not within 0 to 100.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        
        self.color = color
        self.percentage = percentage


class ColorBlender:
    """
    A class to simulate the blending process of color masterbatches.
    
    Attributes:
        masterbatches (list): A list of ColorMasterbatch objects.
    """

    def __init__(self):
        """Initializes an empty list of masterbatches."""
        self.masterbatches = []

    def add_masterbatch(self, masterbatch: ColorMasterbatch):
        """
        Adds a ColorMasterbatch to the blender.

        Parameters:
            masterbatch (ColorMasterbatch): The masterbatch to be added.
        """
        self.masterbatches.append(masterbatch)

    def blend(self) -> str:
        """
        Blends the masterbatches and returns the resulting color.

        Returns:
            str: The resulting blended color.
        
        Raises:
            ValueError: If no masterbatches are added to blend.
        """
        if not self.masterbatches:
            raise ValueError("No masterbatches to blend.")

        total_percentage = sum(batch.percentage for batch in self.masterbatches)
        if total_percentage != 100:
            raise ValueError("Total percentage of masterbatches must equal 100.")

        # Placeholder logic for blending colors; a real implementation would require color mixing algorithms.
        colors = [batch.color for batch in self.masterbatches]
        blended_color = " + ".join(colors)  # Simplified representation of the blended color
        return f"Blended Color: {blended_color}"


# Example usage
if __name__ == "__main__":
    try:
        blender = ColorBlender()
        blender.add_masterbatch(ColorMasterbatch("Black", 50))
        blender.add_masterbatch(ColorMasterbatch("White", 50))
        
        result = blender.blend()
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
```
