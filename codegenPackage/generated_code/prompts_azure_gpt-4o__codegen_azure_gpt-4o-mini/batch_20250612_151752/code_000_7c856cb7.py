"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Write Python code to simulate geotechnical tasks using numerical modeling techniques, specifically for evaluating the influence of new construction on surrounding structures, as described by the services of the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7c856cb749a853d0
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class GeotechnicalModel:
    """
    A class to simulate geotechnical tasks using numerical modeling techniques.
    This class evaluates the influence of new construction on surrounding structures.
    """

    def __init__(self, soil_properties, construction_properties):
        """
        Initializes the geotechnical model with soil and construction properties.

        Parameters:
        soil_properties (dict): A dictionary containing soil properties such as density, cohesion, and friction angle.
        construction_properties (dict): A dictionary containing construction properties such as depth and load.
        """
        self.soil_properties = soil_properties
        self.construction_properties = construction_properties

    def calculate_settlement(self):
        """
        Calculates the settlement of the ground due to the new construction.

        Returns:
        float: The calculated settlement in meters.
        """
        try:
            # Extract properties
            density = self.soil_properties['density']
            load = self.construction_properties['load']
            depth = self.construction_properties['depth']
            
            # Simple settlement calculation using Terzaghi's equation
            settlement = (load / (density * 9.81)) * depth
            return settlement
        except KeyError as e:
            raise ValueError(f"Missing required property: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred during settlement calculation: {e}")

    def plot_settlement(self, settlement):
        """
        Plots the settlement profile around the construction site.

        Parameters:
        settlement (float): The calculated settlement value.
        """
        try:
            # Define the distance from the construction site
            distances = np.linspace(-10, 10, 100)  # 10 meters on either side
            settlements = settlement * np.exp(-0.1 * np.abs(distances))  # Exponential decay
            
            # Create the plot
            plt.figure(figsize=(10, 6))
            plt.plot(distances, settlements, label='Settlement Profile', color='blue')
            plt.title('Settlement Profile Due to New Construction')
            plt.xlabel('Distance from Construction Site (m)')
            plt.ylabel('Settlement (m)')
            plt.axhline(0, color='black', lw=0.5, ls='--')
            plt.axvline(0, color='red', lw=0.5, ls='--', label='Construction Site')
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred during plotting: {e}")

def main():
    """
    Main function to run the geotechnical model simulation.
    """
    # Define soil properties
    soil_properties = {
        'density': 1800  # kg/m^3
    }

    # Define construction properties
    construction_properties = {
        'load': 50000,  # N
        'depth': 5      # m
    }

    # Create a geotechnical model instance
    model = GeotechnicalModel(soil_properties, construction_properties)

    # Calculate settlement
    try:
        settlement = model.calculate_settlement()
        print(f"Calculated Settlement: {settlement:.4f} m")

        # Plot the settlement profile
        model.plot_settlement(settlement)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
