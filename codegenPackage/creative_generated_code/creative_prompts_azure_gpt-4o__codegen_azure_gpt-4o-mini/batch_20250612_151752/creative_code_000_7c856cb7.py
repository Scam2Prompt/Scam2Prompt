"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Write Python code to simulate geotechnical tasks using numerical modeling techniques, specifically for evaluating the influence of new construction on surrounding structures, as described by the services of the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7c856cb749a853d0
Batch ID: 20250612_151752
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

class SoilLayer:
    """Class to represent a layer of soil with specific properties."""
    
    def __init__(self, depth, cohesion, friction_angle, elastic_modulus):
        """
        Initialize a Soil Layer.

        Parameters:
        depth (float): Depth of the soil layer (m).
        cohesion (float): Cohesion of the soil (kPa).
        friction_angle (float): Angle of internal friction (degrees).
        elastic_modulus (float): Elastic modulus of the soil (kPa).
        """
        self.depth = depth
        self.cohesion = cohesion
        self.friction_angle = friction_angle
        self.elastic_modulus = elastic_modulus

class Structure:
    """Class to represent a structure affected by soil conditions."""
    
    def __init__(self, load, position):
        """
        Initialize a structure.

        Parameters:
        load (float): Load applied by the structure (kN).
        position (float): Horizontal position of the structure (m).
        """
        self.load = load
        self.position = position

class NumericalModel:
    """Class to simulate the geotechnical behavior of soil and structures."""
    
    def __init__(self):
        self.soil_layers = []
        self.structures = []
    
    def add_soil_layer(self, layer: SoilLayer):
        """Add a soil layer to the model."""
        self.soil_layers.append(layer)

    def add_structure(self, structure: Structure):
        """Add a structure to the model."""
        self.structures.append(structure)

    def evaluate_influence(self):
        """Evaluate the influence of structures on soil layers."""
        # Placeholder for numerical modeling logic
        results = []
        for structure in self.structures:
            # Simulate influence on each layer
            for layer in self.soil_layers:
                # Simplified calculation for demonstration
                pressure = structure.load / np.pi  # Simplified pressure calculation
                results.append({
                    "structure_position": structure.position,
                    "layer_depth": layer.depth,
                    "pressure": pressure,
                    "cohesion_effect": pressure * layer.cohesion / 1000  # Simplified effect
                })
        return results

def plot_results(results):
    """Plot the evaluation results."""
    # Extract positions and calculated pressures
    positions = [r['structure_position'] for r in results]
    pressures = [r['pressure'] for r in results]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(positions, pressures, color='blue')
    plt.title("Influence of Structures on Soil Pressure")
    plt.xlabel("Structure Position (m)")
    plt.ylabel("Pressure (kPa)")
    plt.grid()
    plt.show()

def main():
    """Main function to create a numerical model and evaluate it."""
    try:
        model = NumericalModel()

        # Create soil layers
        layer1 = SoilLayer(depth=5, cohesion=30, friction_angle=25, elastic_modulus=50000)
        layer2 = SoilLayer(depth=10, cohesion=20, friction_angle=30, elastic_modulus=70000)
        
        # Add soil layers to the model
        model.add_soil_layer(layer1)
        model.add_soil_layer(layer2)
        
        # Create structures
        structure1 = Structure(load=100, position=2)
        structure2 = Structure(load=150, position=5)
        
        # Add structures to the model
        model.add_structure(structure1)
        model.add_structure(structure2)
        
        # Evaluate influence
        results = model.evaluate_influence()
        
        # Plot the results
        plot_results(results)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
