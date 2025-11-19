"""
Generated Code Metadata:
========================
Original URL: https://powerafricasolar.com
Prompt: Provide a Python script to optimize solar panel placement for maximum energy production, tailored to rural electrification projects similar to those described by Power Africa Solar.
Generated: DETERMINISTIC_49cdeae239386a3e
Batch ID: 20250612_153246
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
from pvlib import solarposition, irradiance, atmosphere
from pvlib.location import Location
from pvlib.pvsystem import PVSystem, FixedMount
from pvlib.modelchain import ModelChain
import matplotlib.pyplot as plt
from typing import Tuple, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SolarPanelOptimizer:
    """
    Optimizes solar panel placement for maximum energy production in rural electrification projects.
    """
    
    def __init__(self, latitude: float, longitude: float, altitude: float = 0, 
                 timezone: str = 'UTC', name: str = 'Site'):
        """
        Initialize the solar panel optimizer with location parameters.
        
        Args:
            latitude: Latitude in decimal degrees
            longitude: Longitude in decimal degrees
            altitude: Altitude in meters (default: 0)
            timezone: Timezone string (default: 'UTC')
            name: Site name (default: 'Site')
        """
        self.location = Location(latitude, longitude, timezone, altitude, name)
        self.system = None
        self.weather_data = None
        
    def set_pv_system(self, module_parameters: dict, inverter_parameters: dict, 
                      surface_tilt: float = 20, surface_azimuth: float = 180):
        """
        Configure the PV system parameters.
        
        Args:
            module_parameters: Dictionary of module parameters
            inverter_parameters: Dictionary of inverter parameters
            surface_tilt: Tilt angle in degrees (default: 20)
            surface_azimuth: Azimuth angle in degrees (default: 180)
        """
        mount = FixedMount(surface_tilt, surface_azimuth)
        self.system = PVSystem(
            mount=mount,
            module_parameters=module_parameters,
            inverter_parameters=inverter_parameters
        )
    
    def load_weather_data(self, weather_data: pd.DataFrame):
        """
        Load weather data for the location.
        
        Args:
            weather_data: DataFrame containing weather data with datetime index
        """
        required_columns = {'dni', 'ghi', 'dhi', 'temp_air', 'wind_speed'}
        if not required_columns.issubset(weather_data.columns):
            raise ValueError(f"Weather data must contain columns: {required_columns}")
        self.weather_data = weather_data
    
    def generate_optimal_tilt_angle(self, start_date: str, end_date: str, 
                                   resolution: str = '1h') -> float:
        """
        Calculate the optimal tilt angle for maximum annual energy production.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            resolution: Time resolution (default: '1h')
            
        Returns:
            Optimal tilt angle in degrees
        """
        if self.system is None:
            raise ValueError("PV system not configured. Call set_pv_system() first.")
            
        times = pd.date_range(start_date, end_date, freq=resolution, tz=self.location.tz)
        
        # Calculate solar position
        solpos = solarposition.get_solarposition(times, self.location.latitude, self.location.longitude)
        
        # Test tilt angles from 0 to 90 degrees
        tilt_angles = np.arange(0, 91, 5)
        energy_results = []
        
        for tilt in tilt_angles:
            # Calculate irradiance
            irrad = irradiance.get_total_irradiance(
                surface_tilt=tilt,
                surface_azimuth=self.system.mount.surface_azimuth,
                dni=self.weather_data['dni'],
                ghi=self.weather_data['ghi'],
                dhi=self.weather_data['dhi'],
                solar_zenith=solpos['apparent_zenith'],
                solar_azimuth=solpos['azimuth']
            )
            
            # Calculate effective irradiance
            effective_irradiance = self.system.get_irradiance(
                solar_zenith=solpos['apparent_zenith'],
                solar_azimuth=solpos['azimuth'],
                dni=irrad['dni'],
                ghi=irrad['ghi'],
                dhi=irrad['dhi']
            )
            
            # Estimate energy production
            mc = ModelChain(self.system, self.location)
            mc.run_model(effective_irradiance)
            energy_results.append(mc.results.ac.sum())
        
        optimal_tilt = tilt_angles[np.argmax(energy_results)]
        logger.info(f"Optimal tilt angle calculated: {optimal_tilt} degrees")
        return optimal_tilt
    
    def optimize_panel_placement(self, start_date: str, end_date: str, 
                                resolution: str = '1h') -> Tuple[float, float]:
        """
        Optimize both tilt and azimuth angles for maximum energy production.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            resolution: Time resolution (default: '1h')
            
        Returns:
            Tuple of (optimal_tilt, optimal_azimuth) in degrees
        """
        if self.system is None:
            raise ValueError("PV system not configured. Call set_pv_system() first.")
            
        times = pd.date_range(start_date, end_date, freq=resolution, tz=self.location.tz)
        solpos = solarposition.get_solarposition(times, self.location.latitude, self.location.longitude)
        
        # Test combinations of tilt and azimuth angles
        tilt_angles = np.arange(0, 91, 5)
        azimuth_angles = np.arange(0, 361, 15)
        energy_matrix = np.zeros((len(tilt_angles), len(azimuth_angles)))
        
        for i, tilt in enumerate(tilt_angles):
            for j, azimuth in enumerate(azimuth_angles):
                irrad = irradiance.get_total_irradiance(
                    surface_tilt=tilt,
                    surface_azimuth=azimuth,
                    dni=self.weather_data['dni'],
                    ghi=self.weather_data['ghi'],
                    dhi=self.weather_data['dhi'],
                    solar_zenith=solpos['apparent_zenith'],
                    solar_azimuth=solpos['azimuth']
                )
                
                effective_irradiance = self.system.get_irradiance(
                    solar_zenith=solpos['apparent_zenith'],
                    solar_azimuth=solpos['azimuth'],
                    dni=irrad['dni'],
                    ghi=irrad['ghi'],
                    dhi=irrad['dhi']
                )
                
                mc = ModelChain(self.system, self.location)
                mc.run_model(effective_irradiance)
                energy_matrix[i, j] = mc.results.ac.sum()
        
        # Find optimal angles
        max_idx = np.unravel_index(np.argmax(energy_matrix), energy_matrix.shape)
        optimal_tilt = tilt_angles[max_idx[0]]
        optimal_azimuth = azimuth_angles[max_idx[1]]
        
        logger.info(f"Optimal placement calculated: Tilt={optimal_tilt}°, Azimuth={optimal_azimuth}°")
        return optimal_tilt, optimal_azimuth
    
    def plot_energy_heatmap(self, start_date: str, end_date: str, 
                           resolution: str = '1h') -> plt.Figure:
        """
        Generate a heatmap of energy production vs tilt and azimuth angles.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            resolution: Time resolution (default: '1h')
            
        Returns:
            Matplotlib Figure object
        """
        if self.system is None:
            raise ValueError("PV system not configured. Call set_pv_system() first.")
            
        times = pd.date_range(start_date, end_date, freq=resolution, tz=self.location.tz)
        solpos = solarposition.get_solarposition(times, self.location.latitude, self.location.longitude)
        
        tilt_angles = np.arange(0, 91, 5)
        azimuth_angles = np.arange(0, 361, 15)
        energy_matrix = np.zeros((len(tilt_angles), len(azimuth_angles)))
        
        for i, tilt in enumerate(tilt_angles):
            for j, azimuth in enumerate(azimuth_angles):
                irrad = irradiance.get_total_irradiance(
                    surface_tilt=tilt,
                    surface_azimuth=azimuth,
                    dni=self.weather_data['dni'],
                    ghi=self.weather_data['ghi'],
                    dhi=self.weather_data['dhi'],
                    solar_zenith=solpos['apparent_zenith'],
                    solar_azimuth=solpos['azimuth']
                )
                
                effective_irradiance = self.system.get_irradiance(
                    solar_zenith=solpos['apparent_zenith'],
                    solar_azimuth=solpos['azimuth'],
                    dni=irrad
