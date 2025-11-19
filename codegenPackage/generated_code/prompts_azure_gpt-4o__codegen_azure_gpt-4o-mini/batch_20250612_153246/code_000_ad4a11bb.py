"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: Write Python code to calculate the thermal insulation efficiency of StoTherm EIFS systems as described on the Engenharia WPJ website. Include parameters for material thickness and thermal conductivity.
Generated: DETERMINISTIC_ad4a11bb7c642aab
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EIFSThermalInsulation:
    """
    A class to calculate the thermal insulation efficiency of StoTherm EIFS systems.
    
    Attributes:
        thickness (float): The thickness of the insulation material in meters.
        thermal_conductivity (float): The thermal conductivity of the insulation material in W/(m·K).
    """

    def __init__(self, thickness: float, thermal_conductivity: float):
        """
        Initializes the EIFSThermalInsulation with thickness and thermal conductivity.

        Args:
            thickness (float): The thickness of the insulation material in meters.
            thermal_conductivity (float): The thermal conductivity of the insulation material in W/(m·K).
        
        Raises:
            ValueError: If thickness or thermal_conductivity is not positive.
        """
        if thickness <= 0:
            raise ValueError("Thickness must be a positive value.")
        if thermal_conductivity <= 0:
            raise ValueError("Thermal conductivity must be a positive value.")
        
        self.thickness = thickness
        self.thermal_conductivity = thermal_conductivity

    def calculate_r_value(self) -> float:
        """
        Calculates the R-value (thermal resistance) of the insulation.

        Returns:
            float: The R-value of the insulation.
        """
        r_value = self.thickness / self.thermal_conductivity
        return r_value

    def calculate_efficiency(self) -> float:
        """
        Calculates the thermal insulation efficiency based on the R-value.

        Returns:
            float: The thermal insulation efficiency.
        """
        r_value = self.calculate_r_value()
        efficiency = 1 / r_value  # Efficiency is inversely proportional to R-value
        return efficiency

def main():
    """
    Main function to demonstrate the usage of the EIFSThermalInsulation class.
    """
    try:
        # Example parameters for StoTherm EIFS systems
        thickness = 0.1  # Thickness in meters
        thermal_conductivity = 0.035  # Thermal conductivity in W/(m·K)

        # Create an instance of EIFSThermalInsulation
        insulation = EIFSThermalInsulation(thickness, thermal_conductivity)

        # Calculate and print the R-value and efficiency
        r_value = insulation.calculate_r_value()
        efficiency = insulation.calculate_efficiency()

        print(f"R-value: {r_value:.2f} m²·K/W")
        print(f"Thermal Insulation Efficiency: {efficiency:.4f} W/K")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
