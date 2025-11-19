"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gendis.energia.misiones.gob.ar
Prompt: Can you provide a code example for calculating the efficiency of a solar photovoltaic system based on the information from the Misiones Energy Secretariat?
Generated: DETERMINISTIC_7f42f83f4776c2a4
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarPVSystem:
    """
    A class to represent a solar photovoltaic (PV) system and calculate its efficiency.
    
    Attributes:
        panel_area (float): The area of the solar panels in square meters.
        solar_irradiance (float): The solar power received per unit area (W/m^2).
        energy_output (float): The energy output of the system in watt-hours (Wh).
    """

    def __init__(self, panel_area, solar_irradiance, energy_output):
        """
        Initializes the SolarPVSystem with the given parameters.
        
        Parameters:
            panel_area (float): The area of the solar panels in square meters.
            solar_irradiance (float): The solar power received per unit area in W/m^2.
            energy_output (float): The energy output of the system in Wh.
        """
        self.panel_area = panel_area
        self.solar_irradiance = solar_irradiance
        self.energy_output = energy_output

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the solar PV system as a percentage.
        
        Returns:
            float: The efficiency of the system.
        
        Raises:
            ValueError: If panel_area or solar_irradiance is zero or negative.
        """
        if self.panel_area <= 0:
            raise ValueError("Panel area must be greater than zero.")
        if self.solar_irradiance <= 0:
            raise ValueError("Solar irradiance must be greater than zero.")

        # Calculate the total potential energy (in Wh) from solar irradiance
        total_potential_energy = self.solar_irradiance * self.panel_area * 1  # 1 hour considered
        # Calculate efficiency as a percentage
        efficiency = (self.energy_output / total_potential_energy) * 100
        
        return efficiency

def main():
    """
    Main function to demonstrate the efficiency calculation of a solar PV system.
    """
    try:
        # Example parameters (These values should be defined based on actual data)
        panel_area = 25.0          # in square meters
        solar_irradiance = 1000.0  # in W/m^2
        energy_output = 2000.0      # in Wh
        
        # Create SolarPVSystem instance
        solar_system = SolarPVSystem(panel_area, solar_irradiance, energy_output)
        
        # Calculate and display efficiency
        efficiency = solar_system.calculate_efficiency()
        print(f"Solar PV System Efficiency: {efficiency:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
