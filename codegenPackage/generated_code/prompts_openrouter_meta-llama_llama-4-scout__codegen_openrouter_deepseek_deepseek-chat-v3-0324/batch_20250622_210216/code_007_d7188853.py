"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: "Design a large-scale solar system for an industrial facility in Queensland, Australia, considering factors like energy demand and system durability."
Generated: DETERMINISTIC_d7188853187479aa
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import pvlib
from pvlib.location import Location
from pvlib.pvsystem import PVSystem
from pvlib.modelchain import ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SolarSystemDesign:
    """
    Class for designing a large-scale solar PV system for industrial facilities.
    """
    
    def __init__(self, facility_name, location, energy_demand_kwh, roof_area_m2, 
                 panel_efficiency=0.20, tilt=20, azimuth=180, system_losses=0.14):
        """
        Initialize solar system design parameters.
        
        Args:
            facility_name (str): Name of the industrial facility
            location (dict): Dictionary with 'latitude', 'longitude', 'altitude', 'tz'
            energy_demand_kwh (float): Annual energy demand in kWh
            roof_area_m2 (float): Available roof area in square meters
            panel_efficiency (float): Solar panel efficiency (0-1)
            tilt (float): Panel tilt angle in degrees
            azimuth (float): Panel azimuth angle in degrees (180=south)
            system_losses (float): System losses (0-1)
        """
        self.facility_name = facility_name
        self.location = Location(
            latitude=location['latitude'],
            longitude=location['longitude'],
            altitude=location['altitude'],
            tz=location['tz']
        )
        self.energy_demand_kwh = energy_demand_kwh
        self.roof_area_m2 = roof_area_m2
        self.panel_efficiency = panel_efficiency
        self.tilt = tilt
        self.azimuth = azimuth
        self.system_losses = system_losses
        
        # Default panel parameters (can be overridden)
        self.panel_parameters = {
            'pdc0': 400,  # W
            'gamma_pdc': -0.004,  # temperature coefficient
            'temp_ref': 25  # °C
        }
        
        # Default inverter parameters (can be overridden)
        self.inverter_parameters = {
            'pdc0': 100000,  # W
            'eta_inv_nom': 0.96  # nominal inverter efficiency
        }
        
        self.weather_data = None
        self.system = None
        self.modelchain = None
        
    def set_panel_parameters(self, pdc0, gamma_pdc, temp_ref):
        """
        Set custom panel parameters.
        
        Args:
            pdc0 (float): Power at reference conditions (W)
            gamma_pdc (float): Temperature coefficient (%/°C)
            temp_ref (float): Reference temperature (°C)
        """
        self.panel_parameters = {
            'pdc0': pdc0,
            'gamma_pdc': gamma_pdc,
            'temp_ref': temp_ref
        }
        
    def set_inverter_parameters(self, pdc0, eta_inv_nom):
        """
        Set custom inverter parameters.
        
        Args:
            pdc0 (float): DC power input (W)
            eta_inv_nom (float): Nominal inverter efficiency (0-1)
        """
        self.inverter_parameters = {
            'pdc0': pdc0,
            'eta_inv_nom': eta_inv_nom
        }
        
    def load_weather_data(self, start_date, end_date, source='nasa'):
        """
        Load weather data for the location.
        
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str): End date in 'YYYY-MM-DD' format
            source (str): Data source ('nasa' or 'era5')
            
        Returns:
            pd.DataFrame: Weather data
        """
        try:
            if source == 'nasa':
                weather = self.location.get_clearsky(
                    pd.date_range(start=start_date, end=end_date, freq='H', tz=self.location.tz)
                )
            elif source == 'era5':
                # In a real implementation, this would fetch from ERA5 API
                weather = self.location.get_clearsky(
                    pd.date_range(start=start_date, end=end_date, freq='H', tz=self.location.tz)
                )
                logger.warning("Using clearsky data as placeholder for ERA5 data")
            else:
                raise ValueError("Invalid weather data source")
                
            self.weather_data = weather
            return weather
        except Exception as e:
            logger.error(f"Error loading weather data: {e}")
            raise
            
    def initialize_pv_system(self):
        """
        Initialize the PV system with configured parameters.
        """
        try:
            temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
            
            self.system = PVSystem(
                surface_tilt=self.tilt,
                surface_azimuth=self.azimuth,
                module_parameters=self.panel_parameters,
                inverter_parameters=self.inverter_parameters,
                temperature_model_parameters=temperature_model_parameters
            )
            
            self.modelchain = ModelChain(
                self.system, 
                self.location,
                aoi_model='physical',
                spectral_model='no_loss'
            )
            
            logger.info("PV system initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing PV system: {e}")
            raise
            
    def calculate_system_capacity(self):
        """
        Calculate the optimal system capacity based on roof area and efficiency.
        
        Returns:
            tuple: (system_capacity_kw, number_of_panels)
        """
        try:
            panel_area_m2 = 1.6  # Typical panel area in m²
            panels_possible = int(self.roof_area_m2 / panel_area_m2)
            system_capacity_kw = (panels_possible * self.panel_parameters['pdc0'] * 
                                self.panel_efficiency) / 1000
            return system_capacity_kw, panels_possible
        except Exception as e:
            logger.error(f"Error calculating system capacity: {e}")
            raise
            
    def simulate_system(self):
        """
        Simulate the PV system performance.
        
        Returns:
            pd.DataFrame: Simulation results
        """
        try:
            if not self.weather_data:
                raise ValueError("Weather data not loaded")
            if not self.modelchain:
                raise ValueError("PV system not initialized")
                
            self.modelchain.run_model(self.weather_data)
            results = self.modelchain.results
            
            # Calculate performance metrics
            results.ac = results.ac.fillna(0)
            annual_energy_kwh = results.ac.sum() / 1000
            capacity_factor = annual_energy_kwh / (self.calculate_system_capacity()[0] * 8760)
            
            logger.info(f"Simulation complete. Annual energy: {annual_energy_kwh:.2f} kWh")
            logger.info(f"Capacity factor: {capacity_factor:.2%}")
            
            return results
        except Exception as e:
            logger.error(f"Error simulating system: {e}")
            raise
            
    def calculate_financials(self, system_cost_per_kw=1000, electricity_price=0.15):
        """
        Calculate financial metrics for the solar system.
        
        Args:
            system_cost_per_kw (float): Cost per kW installed (AUD)
            electricity_price (float): Electricity price in AUD/kWh
            
        Returns:
            dict: Financial metrics
        """
        try:
            system_capacity_kw, _ = self.calculate_system_capacity()
            total_cost = system_capacity_kw * system_cost_per_kw
            
            simulation_results = self.simulate_system()
            annual_energy_kwh = simulation_results.ac.sum() / 1000
            annual_savings = annual_energy_kwh * electricity_price
            
            payback_years = total_cost / annual_savings
            roi = (annual_savings * 25) / total_cost  # Assuming 25-year lifespan
            
            return {
                'total_cost_aud': total_cost,
                'annual_energy_kwh': annual_energy_kwh,
                'annual_savings_aud': annual_savings,
                'payback_years': payback_years,
                'roi': roi,
                'capacity_factor': annual_energy_kwh / (system_capacity_kw * 8760)
            }
        except Exception as e:
            logger.error(f"Error calculating financials: {e}")
            raise
            
    def generate_report(self):
        """
        Generate a comprehensive report of the solar system design.
        
        Returns:
            dict: Report containing all key metrics
        """
        try:
            system_capacity_kw, panels_possible = self.calculate_system_capacity()
            financials = self.calculate_financials()
            simulation_results = self.simulate_system()
            
            report = {
                'facility_name': self.facility_name,
                'location': {
                    'latitude': self.location.latitude
