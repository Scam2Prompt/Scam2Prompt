"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.specialmetal.ir
Prompt: Develop a code example that simulates the stress-strain behavior of DUPLEX ALLOY 2205 in a high-temperature environment.
Generated: DETERMINISTIC_8be5db515b2f7106
Batch ID: 20250612_163156
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

class DuplexAlloy2205:
    def __init__(self, temperature):
        """
        Initialize the Duplex Alloy 2205 material properties at a given temperature.
        
        Parameters:
        temperature (float): Operating temperature in degrees Celsius.
        """
        self.temperature = temperature
        self.modulus_of_elasticity = self.calculate_modulus_of_elasticity()
        self.yield_strength = self.calculate_yield_strength()

    def calculate_modulus_of_elasticity(self):
        """
        Calculate the modulus of elasticity based on temperature.
        
        Returns:
        float: Modulus of elasticity in GPa.
        """
        # Base modulus of elasticity at room temperature
        base_modulus = 200  # GPa
        # Temperature coefficient
        temperature_coefficient = -0.004  # GPa/°C
        return base_modulus + temperature_coefficient * (self.temperature - 20)

    def calculate_yield_strength(self):
        """
        Calculate the yield strength based on temperature.
        
        Returns:
        float: Yield strength in MPa.
        """
        # Base yield strength at room temperature
        base_yield_strength = 450  # MPa
        # Temperature coefficient
        temperature_coefficient = -0.5  # MPa/°C
        return base_yield_strength + temperature_coefficient * (self.temperature - 20)

    def stress_strain_curve(self, strain):
        """
        Simulate the stress-strain behavior of Duplex Alloy 2205.
        
        Parameters:
        strain (np.ndarray): Array of strain values.
        
        Returns:
        np.ndarray: Corresponding stress values.
        """
        stress = np.zeros_like(strain)

        for i, e in enumerate(strain):
            if e < 0:  # Elastic region
                stress[i] = self.modulus_of_elasticity * e
            elif e < self.yield_strength / self.modulus_of_elasticity:  # Linear elastic region
                stress[i] = self.modulus_of_elasticity * e
            else:  # Plastic region
                stress[i] = self.yield_strength + (e - self.yield_strength / self.modulus_of_elasticity) * (self.modulus_of_elasticity / 10)

        return stress

def main():
    """
    Main function to run the stress-strain simulation for Duplex Alloy 2205.
    """
    # Define temperature and strain range
    temperature = 300  # Degrees Celsius
    strain = np.linspace(-0.01, 0.05, 100)  # Strain values from -1% to 5%

    try:
        # Instantiate the material
        alloy = DuplexAlloy2205(temperature)

        # Calculate stress values
        stress = alloy.stress_strain_curve(strain)

        # Plotting the stress-strain curve
        plt.figure(figsize=(10, 5))
        plt.plot(strain, stress, label=f'Temperature: {temperature} °C', color='blue')
        plt.title('Stress-Strain Behavior of Duplex Alloy 2205')
        plt.xlabel('Strain')
        plt.ylabel('Stress (MPa)')
        plt.axhline(y=alloy.yield_strength, color='r', linestyle='--', label='Yield Strength')
        plt.axvline(x=alloy.yield_strength / alloy.modulus_of_elasticity, color='g', linestyle='--', label='Elastic Limit')
        plt.legend()
        plt.grid()
        plt.show()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
