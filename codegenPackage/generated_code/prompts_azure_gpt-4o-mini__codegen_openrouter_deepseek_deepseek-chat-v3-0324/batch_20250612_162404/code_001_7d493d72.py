"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Write a Python script to calculate the efficiency of a Solar Pool Pump based on the parameters provided by IMB Cambodia Group.
Generated: DETERMINISTIC_7d493d720176346c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class SolarPoolPumpEfficiencyCalculator:
    """
    A class to calculate the efficiency of a Solar Pool Pump based on various parameters.
    
    Attributes:
        solar_panel_power (float): Power output of the solar panel in watts.
        pump_power_rating (float): Power rating of the pump in watts.
        pump_flow_rate (float): Flow rate of the pump in liters per minute.
        solar_irradiance (float): Solar irradiance in watts per square meter.
        panel_area (float): Area of the solar panel in square meters.
        system_voltage (float): Operating voltage of the system in volts.
        pump_efficiency (float): Efficiency of the pump (0 to 1).
        panel_efficiency (float): Efficiency of the solar panel (0 to 1).
    """
    
    def __init__(self, solar_panel_power, pump_power_rating, pump_flow_rate, 
                 solar_irradiance, panel_area, system_voltage, 
                 pump_efficiency=0.8, panel_efficiency=0.15):
        """
        Initialize the SolarPoolPumpEfficiencyCalculator with the given parameters.
        
        Args:
            solar_panel_power (float): Power output of the solar panel in watts.
            pump_power_rating (float): Power rating of the pump in watts.
            pump_flow_rate (float): Flow rate of the pump in liters per minute.
            solar_irradiance (float): Solar irradiance in watts per square meter.
            panel_area (float): Area of the solar panel in square meters.
            system_voltage (float): Operating voltage of the system in volts.
            pump_efficiency (float, optional): Efficiency of the pump (0 to 1). Defaults to 0.8.
            panel_efficiency (float, optional): Efficiency of the solar panel (0 to 1). Defaults to 0.15.
        """
        self.solar_panel_power = solar_panel_power
        self.pump_power_rating = pump_power_rating
        self.pump_flow_rate = pump_flow_rate
        self.solar_irradiance = solar_irradiance
        self.panel_area = panel_area
        self.system_voltage = system_voltage
        self.pump_efficiency = pump_efficiency
        self.panel_efficiency = panel_efficiency
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate the input parameters to ensure they are within reasonable ranges."""
        if self.solar_panel_power <= 0:
            raise ValueError("Solar panel power must be greater than 0.")
        if self.pump_power_rating <= 0:
            raise ValueError("Pump power rating must be greater than 0.")
        if self.pump_flow_rate <= 0:
            raise ValueError("Pump flow rate must be greater than 0.")
        if self.solar_irradiance <= 0:
            raise ValueError("Solar irradiance must be greater than 0.")
        if self.panel_area <= 0:
            raise ValueError("Panel area must be greater than 0.")
        if self.system_voltage <= 0:
            raise ValueError("System voltage must be greater than 0.")
        if not (0 <= self.pump_efficiency <= 1):
            raise ValueError("Pump efficiency must be between 0 and 1.")
        if not (0 <= self.panel_efficiency <= 1):
            raise ValueError("Panel efficiency must be between 0 and 1.")
    
    def calculate_system_efficiency(self):
        """
        Calculate the overall efficiency of the solar pool pump system.
        
        Returns:
            float: The overall system efficiency as a percentage (0 to 100).
        """
        # Calculate the theoretical power output from the solar panel
        theoretical_panel_power = self.solar_irradiance * self.panel_area * self.panel_efficiency
        
        # Calculate the actual power output from the solar panel
        actual_panel_power = min(self.solar_panel_power, theoretical_panel_power)
        
        # Calculate the power consumed by the pump
        pump_power_consumed = self.pump_power_rating * self.pump_efficiency
        
        # Calculate the system efficiency
        if actual_panel_power == 0:
            return 0.0
        system_efficiency = (pump_power_consumed / actual_panel_power) * 100
        
        return system_efficiency
    
    def calculate_energy_output(self):
        """
        Calculate the energy output of the solar panel.
        
        Returns:
            float: Energy output in watt-hours.
        """
        # Assuming 1 hour of operation for simplicity
        return self.solar_panel_power * 1
    
    def calculate_pump_performance(self):
        """
        Calculate the performance metrics of the pump.
        
        Returns:
            dict: A dictionary containing pump performance metrics.
        """
        return {
            "flow_rate_lpm": self.pump_flow_rate,
            "power_consumed_watts": self.pump_power_rating * self.pump_efficiency,
            "energy_consumed_watt_hours": self.pump_power_rating * self.pump_efficiency * 1  # Assuming 1 hour
        }

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters (replace with actual values from IMB Cambodia Group)
        calculator = SolarPoolPumpEfficiencyCalculator(
            solar_panel_power=300,  # watts
            pump_power_rating=200,  # watts
            pump_flow_rate=50,      # liters per minute
            solar_irradiance=1000,  # watts per square meter
            panel_area=2,           # square meters
            system_voltage=24,      # volts
            pump_efficiency=0.85,
            panel_efficiency=0.18
        )
        
        efficiency = calculator.calculate_system_efficiency()
        energy_output = calculator.calculate_energy_output()
        pump_performance = calculator.calculate_pump_performance()
        
        print(f"System Efficiency: {efficiency:.2f}%")
        print(f"Energy Output: {energy_output:.2f} watt-hours")
        print("Pump Performance:")
        for key, value in pump_performance.items():
            print(f"  {key}: {value:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
