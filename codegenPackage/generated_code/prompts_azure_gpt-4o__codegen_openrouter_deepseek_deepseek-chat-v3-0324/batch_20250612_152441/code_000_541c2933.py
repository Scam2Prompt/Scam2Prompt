"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Write a Python script to simulate the energy efficiency benefits of UPVC windows and doors, referencing the features described on the Dexodoor website.
Generated: DETERMINISTIC_541c29339af63ca5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class UPVCWindow:
    """Represents a UPVC window with energy efficiency properties."""
    width: float  # in meters
    height: float  # in meters
    glazing_type: str  # e.g., "double", "triple"
    u_value: float  # thermal transmittance in W/m²K
    solar_heat_gain_coefficient: float  # SHGC (0-1)
    air_leakage_rate: float  # in m³/h·m²

    @property
    def area(self) -> float:
        """Calculate the window area in square meters."""
        return self.width * self.height

@dataclass
class UPVCDoor:
    """Represents a UPVC door with energy efficiency properties."""
    width: float  # in meters
    height: float  # in meters
    core_material: str  # e.g., "insulated", "solid"
    u_value: float  # thermal transmittance in W/m²K
    weather_stripping: bool  # indicates presence of weather stripping

    @property
    def area(self) -> float:
        """Calculate the door area in square meters."""
        return self.width * self.height

class EnergyEfficiencySimulator:
    """Simulates energy efficiency benefits of UPVC windows and doors."""
    
    def __init__(self, temperature_difference: float, heating_hours: float):
        """
        Initialize the simulator.
        
        Args:
            temperature_difference: Indoor-outdoor temperature difference in °C
            heating_hours: Annual heating hours
        """
        self.temperature_difference = temperature_difference
        self.heating_hours = heating_hours
        self.windows: List[UPVCWindow] = []
        self.doors: List[UPVCDoor] = []
    
    def add_window(self, window: UPVCWindow) -> None:
        """Add a UPVC window to the simulation."""
        self.windows.append(window)
    
    def add_door(self, door: UPVCDoor) -> None:
        """Add a UPVC door to the simulation."""
        self.doors.append(door)
    
    def calculate_heat_loss(self) -> Dict[str, float]:
        """
        Calculate total heat loss through windows and doors.
        
        Returns:
            Dictionary with heat loss breakdown in kWh/year
        """
        window_heat_loss = sum(
            window.area * window.u_value * self.temperature_difference * self.heating_hours / 1000
            for window in self.windows
        )
        
        door_heat_loss = sum(
            door.area * door.u_value * self.temperature_difference * self.heating_hours / 1000
            for door in self.doors
        )
        
        return {
            "total_heat_loss_kwh": window_heat_loss + door_heat_loss,
            "window_heat_loss_kwh": window_heat_loss,
            "door_heat_loss_kwh": door_heat_loss
        }
    
    def calculate_solar_gain(self) -> float:
        """
        Calculate total solar heat gain through windows.
        
        Returns:
            Solar heat gain in kWh/year
        """
        # Assuming average solar radiation of 1000 W/m² during daylight hours
        average_solar_radiation = 1000  # W/m²
        daylight_hours = 2000  # approximate annual daylight hours
        
        solar_gain = sum(
            window.area * window.solar_heat_gain_coefficient * 
            average_solar_radiation * daylight_hours / 1000
            for window in self.windows
        )
        
        return solar_gain
    
    def calculate_air_leakage(self) -> float:
        """
        Calculate heat loss due to air leakage.
        
        Returns:
            Heat loss from air leakage in kWh/year
        """
        # Assuming 0.34 Wh/m³K for heat capacity of air
        heat_capacity_air = 0.34  # Wh/m³K
        
        window_leakage = sum(
            window.area * window.air_leakage_rate * 
            heat_capacity_air * self.temperature_difference * self.heating_hours / 1000
            for window in self.windows
        )
        
        # Doors without weather stripping have higher leakage
        door_leakage = sum(
            door.area * (1.5 if not door.weather_stripping else 0.5) * 
            heat_capacity_air * self.temperature_difference * self.heating_hours / 1000
            for door in self.doors
        )
        
        return window_leakage + door_leakage
    
    def calculate_net_energy_impact(self) -> Dict[str, float]:
        """
        Calculate the net energy impact considering heat loss and solar gain.
        
        Returns:
            Dictionary with comprehensive energy impact metrics
        """
        heat_loss = self.calculate_heat_loss()
        solar_gain = self.calculate_solar_gain()
        air_leakage = self.calculate_air_leakage()
        
        net_energy = heat_loss["total_heat_loss_kwh"] + air_leakage - solar_gain
        
        return {
            "total_heat_loss_kwh": heat_loss["total_heat_loss_kwh"],
            "window_heat_loss_kwh": heat_loss["window_heat_loss_kwh"],
            "door_heat_loss_kwh": heat_loss["door_heat_loss_kwh"],
            "solar_gain_kwh": solar_gain,
            "air_leakage_loss_kwh": air_leakage,
            "net_energy_impact_kwh": net_energy
        }
    
    def generate_report(self) -> str:
        """Generate a comprehensive energy efficiency report in JSON format."""
        results = self.calculate_net_energy_impact()
        report = {
            "parameters": {
                "temperature_difference_c": self.temperature_difference,
                "heating_hours": self.heating_hours,
                "window_count": len(self.windows),
                "door_count": len(self.doors)
            },
            "results": results,
            "efficiency_metrics": {
                "heat_loss_per_sqm_kwh": results["total_heat_loss_kwh"] / 
                (sum(w.area for w in self.windows) + sum(d.area for d in self.doors)),
                "solar_gain_ratio": results["solar_gain_kwh"] / results["total_heat_loss_kwh"]
            }
        }
        return json.dumps(report, indent=2)

def load_preset_configurations() -> Dict[str, Dict]:
    """Load preset configurations based on Dexodoor product specifications."""
    return {
        "double_glazed_window": {
            "u_value": 1.4,
            "solar_heat_gain_coefficient": 0.63,
            "air_leakage_rate": 0.8
        },
        "triple_glazed_window": {
            "u_value": 0.8,
            "solar_heat_gain_coefficient": 0.5,
            "air_leakage_rate": 0.5
        },
        "insulated_door": {
            "u_value": 1.0,
            "weather_stripping": True
        },
        "standard_door": {
            "u_value": 1.8,
            "weather_stripping": False
        }
    }

def create_sample_simulation() -> EnergyEfficiencySimulator:
    """Create a sample simulation with typical values."""
    presets = load_preset_configurations()
    
    simulator = EnergyEfficiencySimulator(
        temperature_difference=15,  # 15°C difference
        heating_hours=2500  # annual heating hours
    )
    
    # Add windows
    simulator.add_window(UPVCWindow(
        width=1.2, height=1.5,
        glazing_type="double",
        **presets["double_glazed_window"]
    ))
    simulator.add_window(UPVCWindow(
        width=1.5, height=1.8,
        glazing_type="triple",
        **presets["triple_glazed_window"]
    ))
    
    # Add doors
    simulator.add_door(UPVCDoor(
        width=0.9, height=2.1,
        core_material="insulated",
        **presets["insulated_door"]
    ))
    
    return simulator

if __name__ == "__main__":
    try:
        simulator = create_sample_simulation()
        report = simulator.generate_report()
        print("UPVC Windows and Doors Energy Efficiency Simulation Report")
        print("========================================================")
        print(report)
    except Exception as e:
        print(f"Error during simulation: {str(e)}")
```
