"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Generate code to model the energy output of a hybrid renewable energy system (solar and wind) for a residential "isla energética," referencing the efficiency principles discussed on the Digar Green website.
Generated: DETERMINISTIC_f56d1d41a7297e76
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Tuple, Dict, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class SolarPanelConfig:
    """Configuration for solar panel system."""
    area: float  # m²
    efficiency: float  # percentage (0-1)
    tilt_angle: float  # degrees
    orientation: float  # degrees (0=N, 90=E, 180=S, 270=W)
    temperature_coefficient: float = -0.004  # %/°C
    reference_temp: float = 25.0  # °C

@dataclass
class WindTurbineConfig:
    """Configuration for wind turbine system."""
    rotor_diameter: float  # meters
    efficiency: float  # percentage (0-1)
    cut_in_speed: float  # m/s
    rated_speed: float  # m/s
    cut_out_speed: float  # m/s
    hub_height: float  # meters

class HybridEnergySystem:
    """Model for hybrid renewable energy system (solar + wind)."""
    
    def __init__(
        self,
        solar_config: SolarPanelConfig,
        wind_config: WindTurbineConfig,
        location: Tuple[float, float]  # (latitude, longitude)
    ):
        self.solar_config = solar_config
        self.wind_config = wind_config
        self.latitude, self.longitude = location
        
    def calculate_solar_output(
        self,
        irradiance: float,  # W/m²
        ambient_temp: float,  # °C
        hours: float = 1.0
    ) -> float:
        """
        Calculate solar energy output considering panel efficiency and temperature.
        
        Args:
            irradiance: Solar irradiance in W/m²
            ambient_temp: Ambient temperature in °C
            hours: Time period in hours
            
        Returns:
            Energy output in Wh
        """
        try:
            # Temperature correction
            temp_diff = ambient_temp - self.solar_config.reference_temp
            efficiency_correction = 1 + (self.solar_config.temperature_coefficient * temp_diff)
            corrected_efficiency = max(0, min(1, self.solar_config.efficiency * efficiency_correction))
            
            # Energy calculation
            energy = irradiance * self.solar_config.area * corrected_efficiency * hours
            return max(0, energy)
        except Exception as e:
            logger.error(f"Error calculating solar output: {e}")
            return 0.0
    
    def calculate_wind_output(
        self,
        wind_speed: float,  # m/s at measurement height
        air_density: float = 1.225,  # kg/m³
        hours: float = 1.0
    ) -> float:
        """
        Calculate wind energy output based on wind speed and turbine characteristics.
        
        Args:
            wind_speed: Wind speed at measurement height in m/s
            air_density: Air density in kg/m³
            hours: Time period in hours
            
        Returns:
            Energy output in Wh
        """
        try:
            # Adjust wind speed to hub height using power law (exponent 1/7)
            adjusted_speed = wind_speed * (self.wind_config.hub_height / 10) ** (1/7)
            
            # Check operational limits
            if (adjusted_speed < self.wind_config.cut_in_speed or 
                adjusted_speed > self.wind_config.cut_out_speed):
                return 0.0
                
            # Calculate power
            rotor_area = np.pi * (self.wind_config.rotor_diameter / 2) ** 2
            if adjusted_speed <= self.wind_config.rated_speed:
                power = 0.5 * air_density * rotor_area * adjusted_speed ** 3 * self.wind_config.efficiency
            else:
                # At rated speed, power is capped
                rated_power = 0.5 * air_density * rotor_area * self.wind_config.rated_speed ** 3 * self.wind_config.efficiency
                power = min(rated_power, 0.5 * air_density * rotor_area * adjusted_speed ** 3 * self.wind_config.efficiency)
            
            return max(0, power * hours)
        except Exception as e:
            logger.error(f"Error calculating wind output: {e}")
            return 0.0
    
    def calculate_hybrid_output(
        self,
        irradiance: float,
        wind_speed: float,
        ambient_temp: float,
        hours: float = 1.0
    ) -> Dict[str, float]:
        """
        Calculate combined energy output from both solar and wind systems.
        
        Args:
            irradiance: Solar irradiance in W/m²
            wind_speed: Wind speed at 10m height in m/s
            ambient_temp: Ambient temperature in °C
            hours: Time period in hours
            
        Returns:
            Dictionary with solar, wind, and total energy output in Wh
        """
        solar = self.calculate_solar_output(irradiance, ambient_temp, hours)
        wind = self.calculate_wind_output(wind_speed, hours=hours)
        
        return {
            "solar_energy_wh": solar,
            "wind_energy_wh": wind,
            "total_energy_wh": solar + wind
        }

def simulate_daily_production(
    system: HybridEnergySystem,
    weather_data: pd.DataFrame
) -> pd.DataFrame:
    """
    Simulate daily energy production from weather data.
    
    Args:
        system: Configured hybrid energy system
        weather_data: DataFrame with columns:
            - 'irradiance' (W/m²)
            - 'wind_speed' (m/s at 10m)
            - 'temperature' (°C)
            - 'hour' (0-23)
            
    Returns:
        DataFrame with original data plus energy output columns
    """
    results = weather_data.copy()
    
    # Calculate energy for each hour
    energy_outputs = []
    for _, row in weather_data.iterrows():
        output = system.calculate_hybrid_output(
            irradiance=row['irradiance'],
            wind_speed=row['wind_speed'],
            ambient_temp=row['temperature'],
            hours=1.0
        )
        energy_outputs.append(output)
    
    # Add energy columns to results
    energy_df = pd.DataFrame(energy_outputs)
    results = pd.concat([results, energy_df], axis=1)
    
    return results

# Example usage
if __name__ == "__main__":
    # System configuration
    solar_config = SolarPanelConfig(
        area=10.0,
        efficiency=0.18,
        tilt_angle=30.0,
        orientation=180.0
    )
    
    wind_config = WindTurbineConfig(
        rotor_diameter=3.2,
        efficiency=0.35,
        cut_in_speed=3.0,
        rated_speed=12.0,
        cut_out_speed=25.0,
        hub_height=15.0
    )
    
    # Location (example: Canary Islands)
    location = (28.1, -15.4)
    
    # Create system
    system = HybridEnergySystem(solar_config, wind_config, location)
    
    # Sample weather data (simplified for example)
    weather_data = pd.DataFrame({
        'hour': range(24),
        'irradiance': [0, 0, 0, 0, 0, 50, 300, 600, 800, 900, 950, 1000,
                      950, 850, 700, 500, 300, 100, 0, 0, 0, 0, 0, 0],
        'wind_speed': [4.2, 4.0, 3.8, 3.5, 3.7, 4.1, 5.0, 6.2, 7.0, 7.5,
                      7.8, 8.0, 8.2, 8.5, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 5.0, 4.5, 4.3, 4.1],
        'temperature': [18, 17, 17, 16, 16, 17, 19, 22, 24, 26, 27, 28,
                       28, 27, 26, 25, 23, 21, 20, 19, 19, 18, 18, 18]
    })
    
    # Simulate daily production
    results = simulate_daily_production(system, weather_data)
    
    # Print results summary
    print("\nDaily Energy Production Summary:")
    print(f"Total Solar: {results['solar_energy_wh'].sum():.2f} Wh")
    print(f"Total Wind:
