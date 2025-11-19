"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: "Write a code to simulate the energy production and cost savings of a grid-positive solar generation system, like the one implemented at Butte College by Chico Electric."
Generated: DETERMINISTIC_cdebbcab621fa6f4
Batch ID: 20250622_204607
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
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class SolarEnergySimulator:
    """
    Simulates energy production and cost savings of a grid-positive solar generation system.
    """
    
    def __init__(self, system_capacity_kw, panel_efficiency, degradation_rate, 
                 electricity_rate, feed_in_tariff, system_cost, 
                 latitude=39.8, longitude=-121.8, tilt_angle=30):
        """
        Initialize solar energy simulator with system parameters.
        
        Args:
            system_capacity_kw (float): Total system capacity in kW
            panel_efficiency (float): Panel efficiency (0-1)
            degradation_rate (float): Annual degradation rate (0-1)
            electricity_rate (float): Cost per kWh in dollars
            feed_in_tariff (float): Rate paid for excess energy fed back to grid
            system_cost (float): Total system installation cost
            latitude (float): Location latitude
            longitude (float): Location longitude
            tilt_angle (float): Panel tilt angle in degrees
        """
        self.system_capacity_kw = system_capacity_kw
        self.panel_efficiency = panel_efficiency
        self.degradation_rate = degradation_rate
        self.electricity_rate = electricity_rate
        self.feed_in_tariff = feed_in_tariff
        self.system_cost = system_cost
        self.latitude = latitude
        self.longitude = longitude
        self.tilt_angle = tilt_angle
        
        # Validate inputs
        if not (0 <= panel_efficiency <= 1):
            raise ValueError("Panel efficiency must be between 0 and 1")
        if not (0 <= degradation_rate <= 1):
            raise ValueError("Degradation rate must be between 0 and 1")
        if electricity_rate <= 0 or feed_in_tariff <= 0 or system_cost <= 0:
            raise ValueError("Rates and costs must be positive values")
    
    def calculate_solar_irradiance(self, date_time):
        """
        Simplified solar irradiance calculation based on date/time and location.
        
        Args:
            date_time (datetime): Date and time to calculate irradiance for
            
        Returns:
            float: Solar irradiance in kW/m²
        """
        try:
            day_of_year = date_time.timetuple().tm_yday
            hour = date_time.hour + date_time.minute/60
            
            # Solar position calculations
            declination = 23.45 * np.sin(np.radians(360/365 * (284 + day_of_year)))
            hour_angle = 15 * (hour - 12)
            elevation = np.arcsin(np.sin(np.radians(self.latitude)) * np.sin(np.radians(declination)) + 
                                np.cos(np.radians(self.latitude)) * np.cos(np.radians(declination)) * 
                                np.cos(np.radians(hour_angle)))
            
            # Atmospheric effects
            air_mass = 1 / np.cos(np.radians(90 - np.degrees(elevation)))
            atmospheric_transmittance = 0.7 ** air_mass
            
            # Tilt factor
            incidence_angle = np.arccos(np.sin(np.radians(declination)) * np.sin(np.radians(self.latitude)) * 
                                      np.cos(np.radians(self.tilt_angle)) - 
                                      np.sin(np.radians(declination)) * np.cos(np.radians(self.latitude)) * 
                                      np.sin(np.radians(self.tilt_angle)) * np.cos(np.radians(0)) + 
                                      np.cos(np.radians(declination)) * np.cos(np.radians(self.latitude)) * 
                                      np.cos(np.radians(self.tilt_angle)) * np.cos(np.radians(hour_angle)) + 
                                      np.cos(np.radians(declination)) * np.sin(np.radians(self.latitude)) * 
                                      np.sin(np.radians(self.tilt_angle)) * np.cos(np.radians(0)) * 
                                      np.cos(np.radians(hour_angle)))
            
            # Total irradiance
            irradiance = 1.367 * atmospheric_transmittance * np.cos(incidence_angle)
            return max(0, irradiance)
        except Exception as e:
            raise RuntimeError(f"Error calculating solar irradiance: {str(e)}")
    
    def simulate_day(self, date, consumption_profile):
        """
        Simulate energy production and consumption for a single day.
        
        Args:
            date (datetime.date): Date to simulate
            consumption_profile (dict): Hourly consumption profile (kWh)
            
        Returns:
            dict: Dictionary containing production, consumption, and net values
        """
        try:
            production = []
            net_energy = []
            feed_in = []
            grid_draw = []
            
            for hour in range(24):
                time = datetime(date.year, date.month, date.day, hour)
                irradiance = self.calculate_solar_irradiance(time)
                
                # Calculate production with efficiency
                hourly_production = irradiance * self.system_capacity_kw * self.panel_efficiency
                production.append(hourly_production)
                
                # Calculate net energy
                consumption = consumption_profile.get(hour, 0)
                net = hourly_production - consumption
                net_energy.append(net)
                
                # Track feed-in and grid draw
                if net > 0:
                    feed_in.append(net)
                    grid_draw.append(0)
                else:
                    feed_in.append(0)
                    grid_draw.append(abs(net))
            
            return {
                'production': production,
                'consumption': [consumption_profile.get(h, 0) for h in range(24)],
                'net_energy': net_energy,
                'feed_in': feed_in,
                'grid_draw': grid_draw
            }
        except Exception as e:
            raise RuntimeError(f"Error simulating day: {str(e)}")
    
    def simulate_year(self, start_date, annual_consumption_kwh, consumption_profile):
        """
        Simulate energy production and savings for a full year.
        
        Args:
            start_date (datetime.date): Start date of simulation
            annual_consumption_kwh (float): Total annual consumption in kWh
            consumption_profile (dict): Hourly consumption profile (relative values)
            
        Returns:
            pd.DataFrame: DataFrame with daily simulation results
        """
        try:
            # Normalize consumption profile to match annual total
            total_profile = sum(consumption_profile.values())
            normalized_profile = {h: (v/total_profile) * (annual_consumption_kwh/365/24) 
                                for h, v in consumption_profile.items()}
            
            # Initialize results storage
            dates = []
            daily_production = []
            daily_consumption = []
            daily_feed_in = []
            daily_grid_draw = []
            daily_savings = []
            
            current_date = start_date
            for _ in range(365):
                day_result = self.simulate_day(current_date, normalized_profile)
                
                dates.append(current_date)
                daily_production.append(sum(day_result['production']))
                daily_consumption.append(sum(day_result['consumption']))
                daily_feed_in.append(sum(day_result['feed_in']))
                daily_grid_draw.append(sum(day_result['grid_draw']))
                
                # Calculate daily savings
                savings = (sum(day_result['production']) - sum(day_result['grid_draw'])) * self.electricity_rate
                savings += sum(day_result['feed_in']) * self.feed_in_tariff
                daily_savings.append(savings)
                
                current_date += timedelta(days=1)
            
            # Create DataFrame with results
            results = pd.DataFrame({
                'date': dates,
                'production_kwh': daily_production,
                'consumption_kwh': daily_consumption,
                'feed_in_kwh': daily_feed_in,
                'grid_draw_kwh': daily_grid_draw,
                'daily_savings_usd': daily_savings
            })
            
            return results
        except Exception as e:
            raise RuntimeError(f"Error simulating year: {str(e)}")
    
    def calculate_financials(self, simulation_results, years=25):
        """
        Calculate financial metrics over system lifetime.
        
        Args:
            simulation_results (pd.DataFrame): Results from simulate_year
            years (int): System lifetime in years
            
        Returns:
            dict: Dictionary containing financial metrics
        """
        try:
            # Calculate annual values from first year simulation
            annual_production = simulation_results['production_kwh'].sum()
            annual_savings = simulation_results['daily_savings_usd'].sum()
            
            # Project over system lifetime with degradation
            total_production = 0
            total_savings = 0
            production_by_year = []
            savings_by_year = []
            
            for year in range(years):
                degradation_factor = (1 - self.degradation_rate) ** year
                year_production = annual_production * degradation_factor
                year_savings = annual_savings * degradation_factor
                
                total
