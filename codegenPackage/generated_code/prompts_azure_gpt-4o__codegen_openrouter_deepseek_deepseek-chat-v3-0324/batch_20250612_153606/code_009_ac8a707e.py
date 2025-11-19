"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Write a program to calculate the optimal configuration for a solar mini-grid system, using metrics like energy demand and storage capacity, as discussed by IMB Cambodia Group.
Generated: DETERMINISTIC_ac8a707e9412999f
Batch ID: 20250612_153606
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
from typing import Dict, Tuple, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SolarMiniGridOptimizer:
    """
    A class to calculate the optimal configuration for a solar mini-grid system.
    Takes into account energy demand, solar potential, and storage requirements.
    """
    
    def __init__(self, 
                 daily_energy_demand: float,  # kWh/day
                 peak_power_demand: float,    # kW
                 solar_irradiance: float,     # kWh/m²/day
                 autonomy_days: int = 3,      # Days of battery backup
                 system_voltage: float = 48,  # V
                 battery_dod: float = 0.8,    # Depth of Discharge (0-1)
                 inverter_efficiency: float = 0.95,
                 charge_controller_efficiency: float = 0.98,
                 derating_factor: float = 0.85):
        """
        Initialize the solar mini-grid optimizer with system parameters.
        
        Args:
            daily_energy_demand: Average daily energy consumption in kWh
            peak_power_demand: Maximum instantaneous power demand in kW
            solar_irradiance: Average daily solar irradiance in kWh/m²/day
            autonomy_days: Number of days battery should provide backup
            system_voltage: System operating voltage in volts
            battery_dod: Battery depth of discharge (0-1)
            inverter_efficiency: Efficiency of inverter (0-1)
            charge_controller_efficiency: Efficiency of charge controller (0-1)
            derating_factor: System derating factor accounting for losses (0-1)
        """
        self.daily_energy_demand = daily_energy_demand
        self.peak_power_demand = peak_power_demand
        self.solar_irradiance = solar_irradiance
        self.autonomy_days = autonomy_days
        self.system_voltage = system_voltage
        self.battery_dod = battery_dod
        self.inverter_efficiency = inverter_efficiency
        self.charge_controller_efficiency = charge_controller_efficiency
        self.derating_factor = derating_factor
        
        # Validate inputs
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate that all input parameters are within reasonable ranges."""
        if self.daily_energy_demand <= 0:
            raise ValueError("Daily energy demand must be positive")
        if self.peak_power_demand <= 0:
            raise ValueError("Peak power demand must be positive")
        if self.solar_irradiance <= 0:
            raise ValueError("Solar irradiance must be positive")
        if not (0 < self.battery_dod <= 1):
            raise ValueError("Battery depth of discharge must be between 0 and 1")
        if not (0 < self.inverter_efficiency <= 1):
            raise ValueError("Inverter efficiency must be between 0 and 1")
        if not (0 < self.charge_controller_efficiency <= 1):
            raise ValueError("Charge controller efficiency must be between 0 and 1")
        if not (0 < self.derating_factor <= 1):
            raise ValueError("Derating factor must be between 0 and 1")
    
    def calculate_pv_requirements(self, panel_wattage: float = 300) -> Tuple[float, int]:
        """
        Calculate the required PV array size and number of panels.
        
        Args:
            panel_wattage: Wattage of individual PV panels in watts
            
        Returns:
            Tuple of (total_pv_kw, number_of_panels)
        """
        try:
            # Calculate total energy needed from PV considering system losses
            total_energy_needed = self.daily_energy_demand / (
                self.charge_controller_efficiency * 
                self.inverter_efficiency * 
                self.derating_factor
            )
            
            # Calculate PV array size in kW
            pv_array_kw = total_energy_needed / self.solar_irradiance
            
            # Calculate number of panels
            number_of_panels = int(np.ceil(pv_array_kw * 1000 / panel_wattage))
            actual_pv_kw = number_of_panels * panel_wattage / 1000
            
            logger.info(f"PV Requirements: {actual_pv_kw:.2f} kW ({number_of_panels} x {panel_wattage}W panels)")
            
            return actual_pv_kw, number_of_panels
        except Exception as e:
            logger.error(f"Error calculating PV requirements: {str(e)}")
            raise
    
    def calculate_battery_requirements(self, battery_ah: float = 200) -> Tuple[float, int]:
        """
        Calculate the required battery bank size and number of batteries.
        
        Args:
            battery_ah: Capacity of individual batteries in Ah
            
        Returns:
            Tuple of (total_battery_kwh, number_of_batteries)
        """
        try:
            # Calculate total energy to be stored considering autonomy days
            total_storage_kwh = self.daily_energy_demand * self.autonomy_days
            
            # Adjust for depth of discharge and inverter efficiency
            usable_storage_kwh = total_storage_kwh / (self.battery_dod * self.inverter_efficiency)
            
            # Convert to Ah at system voltage
            total_ah = (usable_storage_kwh * 1000) / self.system_voltage
            
            # Calculate number of batteries
            number_of_batteries = int(np.ceil(total_ah / battery_ah))
            actual_battery_kwh = number_of_batteries * battery_ah * self.system_voltage / 1000
            
            logger.info(f"Battery Requirements: {actual_battery_kwh:.2f} kWh ({number_of_batteries} x {battery_ah}Ah batteries)")
            
            return actual_battery_kwh, number_of_batteries
        except Exception as e:
            logger.error(f"Error calculating battery requirements: {str(e)}")
            raise
    
    def calculate_inverter_requirements(self) -> float:
        """
        Calculate the required inverter size based on peak power demand.
        
        Returns:
            Required inverter size in kW
        """
        try:
            # Add 25% margin to peak demand
            inverter_kw = self.peak_power_demand * 1.25
            
            logger.info(f"Inverter Requirements: {inverter_kw:.2f} kW")
            
            return inverter_kw
        except Exception as e:
            logger.error(f"Error calculating inverter requirements: {str(e)}")
            raise
    
    def optimize_system(self, 
                       panel_wattage: float = 300, 
                       battery_ah: float = 200) -> Dict[str, float]:
        """
        Calculate the complete optimal system configuration.
        
        Args:
            panel_wattage: Wattage of individual PV panels in watts
            battery_ah: Capacity of individual batteries in Ah
            
        Returns:
            Dictionary containing all system components with their specifications
        """
        try:
            pv_kw, num_panels = self.calculate_pv_requirements(panel_wattage)
            battery_kwh, num_batteries = self.calculate_battery_requirements(battery_ah)
            inverter_kw = self.calculate_inverter_requirements()
            
            return {
                "pv_capacity_kw": pv_kw,
                "number_of_panels": num_panels,
                "panel_wattage": panel_wattage,
                "battery_capacity_kwh": battery_kwh,
                "number_of_batteries": num_batteries,
                "battery_ah": battery_ah,
                "inverter_capacity_kw": inverter_kw,
                "system_voltage": self.system_voltage,
                "autonomy_days": self.autonomy_days,
                "daily_energy_demand": self.daily_energy_demand,
                "peak_power_demand": self.peak_power_demand
            }
        except Exception as e:
            logger.error(f"Error optimizing system: {str(e)}")
            raise

def load_demand_data(file_path: str) -> Tuple[float, float]:
    """
    Load energy demand data from a CSV file.
    
    Args:
        file_path: Path to CSV file with columns ['timestamp', 'demand_kw']
        
    Returns:
        Tuple of (average_daily_energy_kwh, peak_demand_kw)
    """
    try:
        df = pd.read_csv(file_path, parse_dates=['timestamp'])
        daily_energy = df['demand_kw'].sum() * (24 / len(df))  # kWh/day
        peak_demand = df['demand_kw'].max()  # kW
        return daily_energy, peak_demand
    except Exception as e:
        logger.error(f"Error loading demand data: {str(e)}")
        raise

def main():
    """Example usage of the Solar
