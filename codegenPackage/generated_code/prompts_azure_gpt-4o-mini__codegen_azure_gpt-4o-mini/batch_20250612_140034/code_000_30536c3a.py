"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Write a Python script that performs numerical modeling of geotechnical tasks as described by the Geotechnical Center's services.
Generated: DETERMINISTIC_30536c3a3ae4ffce
Batch ID: 20250612_140034
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
    A class to model geotechnical tasks such as soil settlement and bearing capacity.
    """

    def __init__(self, soil_properties, load):
        """
        Initializes the geotechnical model with soil properties and load.

        Parameters:
        soil_properties (dict): A dictionary containing soil properties such as 
                                'cohesion', 'friction_angle', and 'unit_weight'.
        load (float): The applied load on the soil in kN/m^2.
        """
        self.soil_properties = soil_properties
        self.load = load

    def calculate_settlement(self, depth, modulus_of_elasticity):
        """
        Calculates the settlement of the soil under a given load.

        Parameters:
        depth (float): The depth at which to calculate settlement in meters.
        modulus_of_elasticity (float): The modulus of elasticity of the soil in kN/m^2.

        Returns:
        float: The calculated settlement in meters.
        """
        try:
            # Settlement formula: S = (q * B) / (E * (1 - v^2))
            # Assuming a rectangular footing for simplicity
            q = self.load  # Load per unit area
            B = 1.0  # Width of the footing in meters (assumed)
            v = 0.3  # Poisson's ratio (assumed)
            settlement = (q * B) / (modulus_of_elasticity * (1 - v**2))
            return settlement
        except ZeroDivisionError:
            print("Error: Modulus of elasticity cannot be zero.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def calculate_bearing_capacity(self):
        """
        Calculates the bearing capacity of the soil using Terzaghi's equation.

        Returns:
        float: The calculated bearing capacity in kN/m^2.
        """
        try:
            # Terzaghi's bearing capacity equation: q_ult = c*N_c + q*N_q + 0.5*γ*B*N_γ
            c = self.soil_properties['cohesion']  # Cohesion in kN/m^2
            q = self.load  # Effective stress in kN/m^2
            gamma = self.soil_properties['unit_weight']  # Unit weight in kN/m^3
            B = 1.0  # Width of the footing in meters (assumed)
            N_c = 5.14  # Bearing capacity factor for cohesion
            N_q = 1.0  # Bearing capacity factor for surcharge
            N_gamma = 0.5  # Bearing capacity factor for weight of soil

            bearing_capacity = c * N_c + q * N_q + 0.5 * gamma * B * N_gamma
            return bearing_capacity
        except KeyError as e:
            print(f"Error: Missing soil property {e}.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def plot_settlement(self, depths, modulus_of_elasticity):
        """
        Plots the settlement against depth for a range of depths.

        Parameters:
        depths (list): A list of depths in meters.
        modulus_of_elasticity (float): The modulus of elasticity of the soil in kN/m^2.
        """
        settlements = []
        for depth in depths:
            settlement = self.calculate_settlement(depth, modulus_of_elasticity)
            settlements.append(settlement)

        plt.figure(figsize=(10, 6))
        plt.plot(depths, settlements, marker='o')
        plt.title('Settlement vs Depth')
        plt.xlabel('Depth (m)')
        plt.ylabel('Settlement (m)')
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    soil_properties = {
        'cohesion': 25,  # kN/m^2
        'unit_weight': 18  # kN/m^3
    }
    load = 100  # kN/m^2

    model = GeotechnicalModel(soil_properties, load)

    # Calculate and print settlement at a depth of 5m with a modulus of elasticity of 20000 kN/m^2
    settlement = model.calculate_settlement(depth=5, modulus_of_elasticity=20000)
    print(f"Settlement at 5m depth: {settlement:.4f} m")

    # Calculate and print bearing capacity
    bearing_capacity = model.calculate_bearing_capacity()
    print(f"Bearing capacity: {bearing_capacity:.4f} kN/m^2")

    # Plot settlement for depths from 0 to 10m
    model.plot_settlement(depths=np.linspace(0, 10, 100), modulus_of_elasticity=20000)
```
