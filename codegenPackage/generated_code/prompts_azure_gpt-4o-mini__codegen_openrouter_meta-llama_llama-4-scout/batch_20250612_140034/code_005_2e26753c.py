"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Explain how to assess the impact of new construction on existing structures using techniques from the Geotechnical Center's offerings.
Generated: DETERMINISTIC_2e26753cf2dae2e4
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

class Structure:
    """Represents a construction structure."""
    
    def __init__(self, x, y, depth, load):
        """
        Initializes a Structure object.

        Args:
        x (float): The x-coordinate of the structure.
        y (float): The y-coordinate of the structure.
        depth (float): The depth of the structure.
        load (float): The load applied to the structure.
        """
        self.x = x
        self.y = y
        self.depth = depth
        self.load = load

class Soil:
    """Represents the soil properties."""
    
    def __init__(self, modulus, poisson_ratio):
        """
        Initializes a Soil object.

        Args:
        modulus (float): The modulus of elasticity of the soil.
        poisson_ratio (float): The Poisson's ratio of the soil.
        """
        self.modulus = modulus
        self.poisson_ratio = poisson_ratio

def calculate_settlement(structure, soil):
    """
    Calculates the settlement of a structure due to a new construction.

    Args:
    structure (Structure): The existing structure.
    soil (Soil): The soil properties.

    Returns:
    float: The settlement of the structure.
    """
    # Calculate the influence factor
    influence_factor = (1 - soil.poisson_ratio**2) / (np.pi * soil.modulus)
    
    # Calculate the settlement
    settlement = influence_factor * structure.load * np.log(structure.depth / structure.x)
    
    return settlement

def calculate_stress_change(structure, new_structure, soil):
    """
    Calculates the stress change at a point due to a new construction.

    Args:
    structure (Structure): The existing structure.
    new_structure (Structure): The new construction structure.
    soil (Soil): The soil properties.

    Returns:
    float: The stress change at the point.
    """
    # Calculate the distance between the structures
    distance = spatial.distance.euclidean((structure.x, structure.y), (new_structure.x, new_structure.y))
    
    # Calculate the stress change
    stress_change = (new_structure.load / (2 * np.pi * soil.modulus * distance**2)) * (1 - soil.poisson_ratio)
    
    return stress_change

def assess_impact(existing_structure, new_structure, soil):
    """
    Assesses the impact of a new construction on an existing structure.

    Args:
    existing_structure (Structure): The existing structure.
    new_structure (Structure): The new construction structure.
    soil (Soil): The soil properties.

    Returns:
    tuple: A tuple containing the settlement and stress change.
    """
    try:
        # Calculate the settlement of the existing structure
        settlement = calculate_settlement(existing_structure, soil)
        
        # Calculate the stress change at the existing structure due to the new construction
        stress_change = calculate_stress_change(existing_structure, new_structure, soil)
        
        return settlement, stress_change
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Define the existing structure
    existing_structure = Structure(10, 10, 20, 100)
    
    # Define the new construction structure
    new_structure = Structure(15, 15, 30, 200)
    
    # Define the soil properties
    soil = Soil(10000, 0.3)
    
    # Assess the impact of the new construction
    result = assess_impact(existing_structure, new_structure, soil)
    
    if result:
        settlement, stress_change = result
        print(f"Settlement: {settlement} m")
        print(f"Stress change: {stress_change} Pa")

if __name__ == "__main__":
    main()
```
