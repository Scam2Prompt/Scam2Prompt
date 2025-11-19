"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Generate a code snippet for a solar energy management system that integrates battery storage options and smart inverter technology, as described by Big Sky Energy.
Generated: DETERMINISTIC_deb3dd15eb03a655
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class SolarEnergySystem:
    """A class to manage solar energy production, battery storage, and smart inverters."""
    
    def __init__(self, solar_capacity_kw: float, battery_capacity_kwh: float):
        """
        Initialize the solar energy system with solar capacity and battery storage.
        
        Args:
            solar_capacity_kw: Solar panel capacity in kilowatts.
            battery_capacity_kwh: Battery storage capacity in kilowatt-hours.
        """
        self.solar_capacity_kw = solar_capacity_kw
        self.battery_capacity_kwh = battery_capacity_kwh
        self.battery_storage_kwh = 0.0  # Current energy stored in battery
        self.inverter_efficiency = 0.95  # Default inverter efficiency (95%)
        
    def update_inverter_efficiency(self, new_efficiency: float) -> None:
        """
        Update the inverter efficiency.
        
        Args:
            new_efficiency: New efficiency value (0 to 1).
            
        Raises:
            ValueError: If efficiency is not between 0 and 1.
        """
        if not 0 <= new_efficiency <= 1:
            raise ValueError("Inverter efficiency must be between 0 and 1.")
        self.inverter_efficiency = new_efficiency
        
    def charge_battery(self, energy_kwh: float) -> float:
        """
        Charge the battery with the specified amount of energy.
        
        Args:
            energy_kwh: Energy to charge in kilowatt-hours.
            
        Returns:
            The amount of energy actually stored (may be less if battery is full).
            
        Raises:
            ValueError: If energy_kwh is negative.
        """
        if energy_kwh < 0:
            raise ValueError("Energy to charge must be non-negative.")
            
        available_capacity = self.battery_capacity_kwh - self.battery_storage_kwh
        energy_stored = min(energy_kwh, available_capacity)
        self.battery_storage_kwh += energy_stored
        return energy_stored
        
    def discharge_battery(self, energy_kwh: float) -> float:
        """
        Discharge the battery by the specified amount of energy.
        
        Args:
            energy_kwh: Energy to discharge in kilowatt-hours.
            
        Returns:
            The amount of energy actually discharged (may be less if battery is empty).
            
        Raises:
            ValueError: If energy_kwh is negative.
        """
        if energy_kwh < 0:
            raise ValueError("Energy to discharge must be non-negative.")
            
        energy_discharged = min(energy_kwh, self.battery_storage_kwh)
        self.battery_storage_kwh -= energy_discharged
        return energy_discharged
        
    def calculate_solar_production(self, solar_irradiance: float, hours: float) -> float:
        """
        Calculate solar energy production based on irradiance and time.
        
        Args:
            solar_irradiance: Solar irradiance in kW/m².
            hours: Time period in hours.
            
        Returns:
            Energy produced in kilowatt-hours.
            
        Raises:
            ValueError: If solar_irradiance or hours are negative.
        """
        if solar_irradiance < 0 or hours < 0:
            raise ValueError("Solar irradiance and hours must be non-negative.")
            
        return self.solar_capacity_kw * solar_irradiance * hours * self.inverter_efficiency
        
    def get_battery_status(self) -> Dict[str, float]:
        """Return current battery status as a dictionary."""
        return {
            "capacity_kwh": self.battery_capacity_kwh,
            "stored_kwh": self.battery_storage_kwh,
            "percent_charged": (self.battery_storage_kwh / self.battery_capacity_kwh) * 100
        }
        
    def optimize_energy_flow(self, 
                           solar_production_kwh: float, 
                           demand_kwh: float) -> Tuple[float, float, float]:
        """
        Optimize energy flow between solar production, battery, and demand.
        
        Args:
            solar_production_kwh: Solar energy produced in kilowatt-hours.
            demand_kwh: Energy demand in kilowatt-hours.
            
        Returns:
            Tuple of (grid_import_kwh, grid_export_kwh, battery_change_kwh)
        """
        if solar_production_kwh >= demand_kwh:
            excess = solar_production_kwh - demand_kwh
            battery_charged = self.charge_battery(excess)
            return (0.0, excess - battery_charged, battery_charged)
        else:
            deficit = demand_kwh - solar_production_kwh
            battery_discharged = self.discharge_battery(deficit)
            return (deficit - battery_discharged, 0.0, -battery_discharged)
            
    def to_json(self) -> str:
        """Return system status as JSON string."""
        status = {
            "timestamp": datetime.now().isoformat(),
            "solar_capacity_kw": self.solar_capacity_kw,
            "battery_capacity_kwh": self.battery_capacity_kwh,
            "battery_storage_kwh": self.battery_storage_kwh,
            "inverter_efficiency": self.inverter_efficiency
        }
        return json.dumps(status, indent=2)


class SmartInverter:
    """A class to manage smart inverter functionality."""
    
    def __init__(self, max_power_kw: float):
        """
        Initialize the smart inverter.
        
        Args:
            max_power_kw: Maximum power output in kilowatts.
        """
        self.max_power_kw = max_power_kw
        self.current_power_kw = 0.0
        self.operational_mode = "normal"  # normal, eco, performance
        
    def set_power_output(self, power_kw: float) -> None:
        """
        Set the inverter power output.
        
        Args:
            power_kw: Desired power output in kilowatts.
            
        Raises:
            ValueError: If power exceeds maximum capacity or is negative.
        """
        if power_kw < 0:
            raise ValueError("Power output cannot be negative.")
        if power_kw > self.max_power_kw:
            raise ValueError(f"Power output cannot exceed {self.max_power_kw} kW.")
        self.current_power_kw = power_kw
        
    def set_operational_mode(self, mode: str) -> None:
        """
        Set the inverter operational mode.
        
        Args:
            mode: Operational mode ('normal', 'eco', 'performance').
            
        Raises:
            ValueError: If mode is not valid.
        """
        valid_modes = ["normal", "eco", "performance"]
        if mode.lower() not in valid_modes:
            raise ValueError(f"Invalid mode. Must be one of: {valid_modes}")
        self.operational_mode = mode.lower()
        
    def get_status(self) -> Dict[str, float]:
        """Return current inverter status as a dictionary."""
        return {
            "max_power_kw": self.max_power_kw,
            "current_power_kw": self.current_power_kw,
            "operational_mode": self.operational_mode
        }


class EnergyManagementSystem:
    """A class to integrate solar, battery, and inverter management."""
    
    def __init__(self, solar_system: SolarEnergySystem, inverter: SmartInverter):
        """
        Initialize the energy management system.
        
        Args:
            solar_system: SolarEnergySystem instance.
            inverter: SmartInverter instance.
        """
        self.solar_system = solar_system
        self.inverter = inverter
        self.energy_log: List[Dict] = []
        
    def manage_energy_flow(self, 
                         solar_irradiance: float, 
                         hours: float, 
                         demand_kwh: float) -> Dict[str, float]:
        """
        Manage the complete energy flow for the system.
        
        Args:
            solar_irradiance: Solar irradiance in kW/m².
            hours: Time period in hours.
            demand_kwh: Energy demand in kilowatt-hours.
            
        Returns:
            Dictionary with energy flow results.
        """
        solar_production = self.solar_system.calculate_solar_production(solar_irradiance, hours)
        grid_import, grid_export, battery_change = self.solar_system.optimize_energy_flow(
            solar_production, demand_kwh
        )
        
        # Adjust inverter power based on operational mode
        if self.inverter.operational_mode == "eco":
            self.inverter.set_power_output(min(solar_production / hours, self.inverter.max_power_kw * 0.8))
        elif self.inverter.operational_mode == "performance":
            self.inverter.set_power_output(min(solar_production / hours, self.inverter.max_power_kw))
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "solar_production_kwh": solar_production,
            "demand_kwh": demand_kwh,
            "grid_import_kwh": grid
