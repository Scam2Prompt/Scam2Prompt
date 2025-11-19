"""
Generated Code Metadata:
========================
Original URL: https://universalsolar1.com
Prompt: Write Python code to calculate the efficiency of photovoltaic (PV) modules using parameters specific to Universal Solar's TOPCon technology. Include considerations for module quality and manufacturing advantages described on the website.
Generated: DETERMINISTIC_333b801f68840304
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class PVModuleEfficiencyCalculator:
    """
    A class to calculate the efficiency of photovoltaic (PV) modules using Universal Solar's TOPCon technology.
    This includes considerations for module quality and manufacturing advantages.
    """

    def __init__(self, stc_irradiance=1000, temperature_stc=25, nominal_power=None):
        """
        Initialize the PV module efficiency calculator with standard test conditions (STC).

        Args:
            stc_irradiance (float): Irradiance at STC in W/m² (default: 1000)
            temperature_stc (float): Temperature at STC in °C (default: 25)
            nominal_power (float): Nominal power of the module in W (optional)
        """
        self.stc_irradiance = stc_irradiance
        self.temperature_stc = temperature_stc
        self.nominal_power = nominal_power

        # Universal Solar TOPCon specific parameters
        self.quality_factor = 0.98  # Module quality factor (0-1)
        self.manufacturing_advantage = 1.03  # Manufacturing advantage multiplier
        self.temp_coefficient = -0.0035  # Temperature coefficient (%/°C)
        self.degradation_rate = 0.005  # Annual degradation rate (%/year)

    def calculate_efficiency(self, area, power_output, temperature=None, years_operational=0):
        """
        Calculate the PV module efficiency considering various factors.

        Args:
            area (float): Module area in m²
            power_output (float): Measured power output in W
            temperature (float): Operating temperature in °C (optional)
            years_operational (int): Years the module has been operational (default: 0)

        Returns:
            float: Module efficiency as a percentage (0-100)
        
        Raises:
            ValueError: If area or power_output is <= 0
        """
        if area <= 0 or power_output <= 0:
            raise ValueError("Area and power output must be positive values")

        # Calculate basic efficiency
        efficiency = (power_output / (self.stc_irradiance * area)) * 100

        # Apply quality factor
        efficiency *= self.quality_factor

        # Apply manufacturing advantage
        efficiency *= self.manufacturing_advantage

        # Apply temperature correction if temperature is provided
        if temperature is not None:
            temp_difference = temperature - self.temperature_stc
            efficiency *= (1 + (self.temp_coefficient * temp_difference))

        # Apply degradation for operational years
        efficiency *= (1 - (self.degradation_rate * years_operational))

        return max(0, min(efficiency, 100))  # Ensure efficiency is between 0-100%

    def calculate_power_output(self, area, efficiency, temperature=None, years_operational=0):
        """
        Calculate the expected power output based on efficiency.

        Args:
            area (float): Module area in m²
            efficiency (float): Module efficiency percentage (0-100)
            temperature (float): Operating temperature in °C (optional)
            years_operational (int): Years the module has been operational (default: 0)

        Returns:
            float: Expected power output in W
        
        Raises:
            ValueError: If area or efficiency is invalid
        """
        if area <= 0:
            raise ValueError("Area must be positive")
        if efficiency < 0 or efficiency > 100:
            raise ValueError("Efficiency must be between 0 and 100")

        # Reverse the efficiency calculations
        power = (efficiency / 100) * self.stc_irradiance * area

        # Reverse quality factor
        power /= self.quality_factor

        # Reverse manufacturing advantage
        power /= self.manufacturing_advantage

        # Reverse temperature correction if temperature is provided
        if temperature is not None:
            temp_difference = temperature - self.temperature_stc
            power /= (1 + (self.temp_coefficient * temp_difference))

        # Reverse degradation for operational years
        power /= (1 - (self.degradation_rate * years_operational))

        return max(0, power)

    def set_quality_factor(self, factor):
        """
        Set the module quality factor (0-1).

        Args:
            factor (float): Quality factor between 0 and 1
        
        Raises:
            ValueError: If factor is not between 0 and 1
        """
        if not 0 <= factor <= 1:
            raise ValueError("Quality factor must be between 0 and 1")
        self.quality_factor = factor

    def set_manufacturing_advantage(self, advantage):
        """
        Set the manufacturing advantage multiplier.

        Args:
            advantage (float): Manufacturing advantage multiplier (typically >=1)
        
        Raises:
            ValueError: If advantage is <= 0
        """
        if advantage <= 0:
            raise ValueError("Manufacturing advantage must be positive")
        self.manufacturing_advantage = advantage

    def set_temperature_coefficient(self, coefficient):
        """
        Set the temperature coefficient (%/°C).

        Args:
            coefficient (float): Temperature coefficient in %/°C
        """
        self.temp_coefficient = coefficient

    def set_degradation_rate(self, rate):
        """
        Set the annual degradation rate (%/year).

        Args:
            rate (float): Annual degradation rate in %/year
        
        Raises:
            ValueError: If rate is negative
        """
        if rate < 0:
            raise ValueError("Degradation rate cannot be negative")
        self.degradation_rate = rate


# Example usage
if __name__ == "__main__":
    try:
        # Create calculator with nominal power (optional)
        calculator = PVModuleEfficiencyCalculator(nominal_power=400)
        
        # Calculate efficiency for a 2m² module producing 380W at 30°C after 5 years
        efficiency = calculator.calculate_efficiency(
            area=2,
            power_output=380,
            temperature=30,
            years_operational=5
        )
        print(f"Module efficiency: {efficiency:.2f}%")
        
        # Calculate expected power output for same module
        power = calculator.calculate_power_output(
            area=2,
            efficiency=efficiency,
            temperature=30,
            years_operational=5
        )
        print(f"Expected power output: {power:.2f}W")
        
    except ValueError as e:
        print(f"Error: {e}")
```
