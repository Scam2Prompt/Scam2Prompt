"""
Generated Code Metadata:
========================
Original URL: https://eigennlayer.com
Prompt: Design a solar PV system for a residential landed property in Singapore, including hardware and software installations.
Generated: DETERMINISTIC_84127ad40a90d303
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import pandas as pd
from typing import Dict, List, Tuple, Optional

class SolarPVSystem:
    """
    A class to design a solar PV system for residential properties in Singapore.
    Handles hardware configuration, energy estimation, and financial calculations.
    """
    
    # Singapore-specific constants
    SOLAR_IRRADIANCE = 4.5  # kWh/m2/day (Singapore average)
    SYSTEM_EFFICIENCY = 0.75  # Typical system efficiency
    ELECTRICITY_RATE = 0.30  # SGD per kWh (2023 rates)
    FEED_IN_TARIFF = 0.20  # SGD per kWh
    
    def __init__(self, roof_area: float, daily_consumption: float):
        """
        Initialize the solar PV system with property details.
        
        Args:
            roof_area: Available roof area in square meters
            daily_consumption: Average daily electricity consumption in kWh
        """
        self.roof_area = roof_area
        self.daily_consumption = daily_consumption
        self.panels = []
        self.inverter = None
        self.battery = None
        
    def add_panel(self, model: str, capacity: float, dimensions: Tuple[float, float], 
                  efficiency: float, cost: float):
        """
        Add a solar panel type to the system configuration.
        
        Args:
            model: Panel model name
            capacity: Panel capacity in kW
            dimensions: Tuple of (length, width) in meters
            efficiency: Panel efficiency (0-1)
            cost: Cost per panel in SGD
        """
        self.panels.append({
            'model': model,
            'capacity': capacity,
            'area': dimensions[0] * dimensions[1],
            'efficiency': efficiency,
            'cost': cost
        })
    
    def set_inverter(self, model: str, capacity: float, efficiency: float, cost: float):
        """
        Set the inverter for the system.
        
        Args:
            model: Inverter model name
            capacity: Inverter capacity in kW
            efficiency: Inverter efficiency (0-1)
            cost: Cost in SGD
        """
        self.inverter = {
            'model': model,
            'capacity': capacity,
            'efficiency': efficiency,
            'cost': cost
        }
    
    def set_battery(self, model: str, capacity: float, cost: float):
        """
        Set the battery storage for the system.
        
        Args:
            model: Battery model name
            capacity: Battery capacity in kWh
            cost: Cost in SGD
        """
        self.battery = {
            'model': model,
            'capacity': capacity,
            'cost': cost
        }
    
    def calculate_system(self) -> Dict:
        """
        Calculate the optimal system configuration based on roof area and consumption.
        
        Returns:
            Dictionary containing system configuration and performance metrics
        """
        if not self.panels or not self.inverter:
            raise ValueError("Solar panels and inverter must be configured first")
        
        # Select the most efficient panel
        best_panel = max(self.panels, key=lambda x: x['efficiency'])
        panels_per_row = math.floor(self.roof_area / best_panel['area'])
        total_panels = panels_per_row
        
        system_capacity = total_panels * best_panel['capacity']
        system_cost = total_panels * best_panel['cost'] + self.inverter['cost']
        
        if self.battery:
            system_cost += self.battery['cost']
        
        daily_generation = (system_capacity * self.SOLAR_IRRADIANCE * 
                           self.SYSTEM_EFFICIENCY * best_panel['efficiency'])
        
        autonomy = self.battery['capacity'] / self.daily_consumption if self.battery else 0
        
        return {
            'panel_model': best_panel['model'],
            'panel_count': total_panels,
            'system_capacity_kW': round(system_capacity, 2),
            'daily_generation_kWh': round(daily_generation, 2),
            'inverter_model': self.inverter['model'],
            'battery_model': self.battery['model'] if self.battery else None,
            'battery_autonomy_days': round(autonomy, 2) if self.battery else 0,
            'estimated_cost_SGD': round(system_cost, 2),
            'annual_savings_SGD': round(daily_generation * 365 * self.ELECTRICITY_RATE, 2),
            'payback_period_years': round(system_cost / (daily_generation * 365 * self.ELECTRICITY_RATE), 2)
        }
    
    def generate_installation_plan(self) -> pd.DataFrame:
        """
        Generate a step-by-step installation plan with timelines.
        
        Returns:
            DataFrame containing installation steps and estimated durations
        """
        steps = [
            ("Site Assessment", 1),
            ("System Design Approval", 5),
            ("SP Services Application", 10),
            ("Material Procurement", 15),
            ("Mounting Structure Installation", 2),
            ("Solar Panel Installation", 3),
            ("Electrical Wiring", 2),
            ("Inverter Installation", 1),
            ("Battery Installation", 1) if self.battery else ("", 0),
            ("System Testing", 1),
            ("Commissioning", 1),
            ("Final Inspection", 1)
        ]
        
        # Filter out empty steps
        steps = [step for step in steps if step[0]]
        
        df = pd.DataFrame(steps, columns=['Task', 'Duration (days)'])
        df['Start Day'] = df['Duration (days)'].shift(1).fillna(0).cumsum()
        df['End Day'] = df['Start Day'] + df['Duration (days)']
        
        return df

class MonitoringSystem:
    """
    Class to simulate the monitoring software for the solar PV system.
    """
    
    def __init__(self, system_capacity: float):
        """
        Initialize the monitoring system.
        
        Args:
            system_capacity: Total system capacity in kW
        """
        self.system_capacity = system_capacity
        self.data = []
    
    def add_reading(self, timestamp: str, generation: float, consumption: float, 
                    battery_level: Optional[float] = None):
        """
        Add a new monitoring data point.
        
        Args:
            timestamp: Time of reading (ISO format)
            generation: Current power generation in kW
            consumption: Current power consumption in kW
            battery_level: Current battery level in kWh (optional)
        """
        if generation > self.system_capacity * 1.2:
            raise ValueError("Generation exceeds system capacity by more than 20%")
            
        self.data.append({
            'timestamp': timestamp,
            'generation_kW': generation,
            'consumption_kW': consumption,
            'battery_level_kWh': battery_level,
            'grid_export_kW': max(0, generation - consumption),
            'grid_import_kW': max(0, consumption - generation)
        })
    
    def generate_report(self, start_date: str, end_date: str) -> Dict:
        """
        Generate a performance report for a given date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing aggregated performance metrics
        """
        df = pd.DataFrame(self.data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        mask = (df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)
        filtered = df[mask].copy()
        
        if filtered.empty:
            raise ValueError("No data available for the selected date range")
        
        filtered['date'] = filtered['timestamp'].dt.date
        daily = filtered.groupby('date').agg({
            'generation_kW': 'sum',
            'consumption_kW': 'sum',
            'grid_export_kW': 'sum',
            'grid_import_kW': 'sum'
        })
        
        total_generation = daily['generation_kW'].sum()
        total_consumption = daily['consumption_kW'].sum()
        self_consumption_ratio = min(1, total_consumption / total_generation)
        
        return {
            'total_generation_kWh': round(total_generation, 2),
            'total_consumption_kWh': round(total_consumption, 2),
            'self_consumption_ratio': round(self_consumption_ratio, 2),
            'grid_export_kWh': round(daily['grid_export_kW'].sum(), 2),
            'grid_import_kWh': round(daily['grid_import_kW'].sum(), 2),
            'savings_SGD': round(
                (daily['grid_export_kW'].sum() * SolarPVSystem.FEED_IN_TARIFF) +
                (min(daily['generation_kW'].sum(), daily['consumption_kW'].sum()) * SolarPVSystem.ELECTRICITY_RATE),
                2
            )
        }

# Example usage
