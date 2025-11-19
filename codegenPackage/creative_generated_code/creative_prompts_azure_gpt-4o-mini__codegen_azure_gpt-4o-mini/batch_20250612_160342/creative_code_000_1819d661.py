"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.raymasterbatch.com
Prompt: Generate a code snippet that demonstrates how to create a custom color masterbatch using the principles of nano dispersion as described by Ray Colors.
Generated: DETERMINISTIC_1819d6615932bbed
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class ColorMasterbatch:
    """
    A class to create a custom color masterbatch using nano dispersion principles.
    
    Attributes:
        base_material: The base material for the masterbatch.
        colorant: The colorant used for the masterbatch.
        concentration: The concentration of the colorant in the masterbatch.
        dispersion_method: The method used for nano dispersion.
    """

    def __init__(self, base_material: str, colorant: str, concentration: float, dispersion_method: str):
        """
        Initializes the ColorMasterbatch instance with required parameters.
        
        Args:
            base_material (str): The base material for the masterbatch.
            colorant (str): The colorant used for the masterbatch.
            concentration (float): The concentration of the colorant in the masterbatch (0 to 100).
            dispersion_method (str): The method used for nano dispersion.
        
        Raises:
            ValueError: If concentration is not between 0 and 100.
        """
        if not (0 <= concentration <= 100):
            raise ValueError("Concentration must be between 0 and 100.")
        
        self.base_material = base_material
        self.colorant = colorant
        self.concentration = concentration
        self.dispersion_method = dispersion_method

    def create_masterbatch(self):
        """
        Simulates the creation of a color masterbatch.
        
        Returns:
            dict: A dictionary containing the properties of the masterbatch.
        """
        # Simulate nano dispersion process
        print(f"Dispersion method: {self.dispersion_method}")
        print(f"Creating masterbatch with {self.concentration}% {self.colorant} in {self.base_material}.")

        # Placeholder for actual dispersion simulation
        dispersion_quality = self.simulate_dispersion()
        
        return {
            "base_material": self.base_material,
            "colorant": self.colorant,
            "concentration": self.concentration,
            "dispersion_quality": dispersion_quality
        }

    def simulate_dispersion(self):
        """
        Simulates the dispersion quality based on concentration.
        
        Returns:
            str: Quality of the dispersion.
        """
        # Simple logic to determine dispersion quality
        if self.concentration < 10:
            return "Poor"
        elif self.concentration < 50:
            return "Fair"
        elif self.concentration < 90:
            return "Good"
        else:
            return "Excellent"

    def visualize_masterbatch(self):
        """
        Visualizes the color masterbatch by plotting the color representation.
        """
        color_representation = np.random.rand(3,)  # Random RGB color for demonstration
        plt.figure(figsize=(5, 5))
        plt.imshow([[color_representation]])
        plt.axis('off')
        plt.title(f"{self.concentration}% {self.colorant} in {self.base_material}")
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Create a color masterbatch instance
        masterbatch = ColorMasterbatch("Polypropylene", "Red", 30, "High-shear mixing")
        
        # Create the masterbatch
        result = masterbatch.create_masterbatch()
        
        # Print the result
        print("Masterbatch created:", result)
        
        # Visualize the created masterbatch
        masterbatch.visualize_masterbatch()
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
