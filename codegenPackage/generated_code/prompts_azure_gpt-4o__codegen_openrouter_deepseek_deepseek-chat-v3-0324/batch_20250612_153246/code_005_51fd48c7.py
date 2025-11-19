"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: Create a program to calculate the efficiency of solar panels based on specifications like traction battery capacity and mileage, referencing eControl SA's solar panel solutions.
Generated: DETERMINISTIC_51fd48c79c31fced
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Panel Efficiency Calculator
This program calculates the efficiency of solar panels based on specifications
like traction battery capacity and mileage, referencing eControl SA's solutions.
"""

import math

class SolarPanelEfficiencyCalculator:
    """
    A class to calculate solar panel efficiency based on various parameters.
    """
    
    def __init__(self):
        """
        Initialize default values for solar panel parameters.
        """
        self.panel_area = 1.6  # m² (standard panel size)
        self.solar_irradiance = 1000  # W/m² (standard test condition)
        self.system_loss_factor = 0.14  # 14% system losses
    
    def calculate_efficiency(self, power_output, panel_area=None):
        """
        Calculate solar panel efficiency based on power output and panel area.
        
        Args:
            power_output (float): Power output of the panel in watts
            panel_area (float, optional): Area of the panel in m². Defaults to class default.
        
        Returns:
            float: Efficiency percentage (0-100)
        
        Raises:
            ValueError: If power_output is negative or panel_area is zero/negative
        """
        if power_output < 0:
            raise ValueError("Power output cannot be negative")
        
        area = panel_area if panel_area is not None else self.panel_area
        if area <= 0:
            raise ValueError("Panel area must be positive")
        
        input_power = area * self.solar_irradiance
        if input_power == 0:
            return 0.0
            
        efficiency = (power_output / input_power) * 100
        return round(efficiency * (1 - self.system_loss_factor), 2)
    
    def calculate_battery_charging_time(self, battery_capacity_kwh, solar_power_kw):
        """
        Calculate time required to charge a battery using solar power.
        
        Args:
            battery_capacity_kwh (float): Battery capacity in kWh
            solar_power_kw (float): Solar power output in kW
            
        Returns:
            float: Charging time in hours
            
        Raises:
            ValueError: If any input is negative or zero
        """
        if battery_capacity_kwh <= 0 or solar_power_kw <= 0:
            raise ValueError("Battery capacity and solar power must be positive")
        
        return battery_capacity_kwh / solar_power_kw
    
    def calculate_mileage_coverage(self, mileage_km, battery_capacity_kwh, efficiency):
        """
        Calculate how much mileage can be covered by solar-charged battery.
        
        Args:
            mileage_km (float): Vehicle mileage in km/kWh
            battery_capacity_kwh (float): Battery capacity in kWh
            efficiency (float): Charging efficiency (0-1)
            
        Returns:
            float: Estimated mileage in km
            
        Raises:
            ValueError: If any input is invalid
        """
        if mileage_km <= 0 or battery_capacity_kwh <= 0:
            raise ValueError("Mileage and battery capacity must be positive")
        if not 0 <= efficiency <= 1:
            raise ValueError("Efficiency must be between 0 and 1")
        
        return mileage_km * battery_capacity_kwh * efficiency


def main():
    """
    Main function to demonstrate the SolarPanelEfficiencyCalculator.
    """
    try:
        calculator = SolarPanelEfficiencyCalculator()
        
        # Example 1: Calculate panel efficiency
        power_output = 300  # watts
        efficiency = calculator.calculate_efficiency(power_output)
        print(f"Panel Efficiency: {efficiency}%")
        
        # Example 2: Calculate battery charging time
        battery_capacity = 75  # kWh
        solar_power = 5  # kW
        charging_time = calculator.calculate_battery_charging_time(battery_capacity, solar_power)
        print(f"Charging Time: {charging_time:.2f} hours")
        
        # Example 3: Calculate mileage coverage
        mileage = 6.5  # km/kWh
        efficiency_factor = 0.85  # 85% charging efficiency
        coverage = calculator.calculate_mileage_coverage(mileage, battery_capacity, efficiency_factor)
        print(f"Mileage Coverage: {coverage:.2f} km")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
