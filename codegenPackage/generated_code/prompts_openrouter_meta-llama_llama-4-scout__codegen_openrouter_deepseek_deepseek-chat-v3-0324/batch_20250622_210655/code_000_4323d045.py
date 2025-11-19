"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: "Design a sustainable energy system for an industrial setting using renewable energy sources like solar and wind power, considering the Real Decreto 900/2015 regulations in Spain."
Generated: DETERMINISTIC_4323d0453bcc49cd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sustainable Energy System for Industrial Setting in Spain
Compliant with Real Decreto 900/2015 regulations
"""

import math
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class EnergySource:
    """Base class for renewable energy sources."""
    
    def __init__(self, name: str, capacity_kw: float):
        self.name = name
        self.capacity_kw = capacity_kw
        self.energy_produced_kwh: float = 0.0
        
    def calculate_daily_production(self, date: datetime) -> float:
        """Calculate daily energy production in kWh."""
        raise NotImplementedError
        
    def update_energy_produced(self, energy_kwh: float) -> None:
        """Update total energy produced."""
        self.energy_produced_kwh += energy_kwh

class SolarPanelSystem(EnergySource):
    """Solar energy system implementation."""
    
    def __init__(self, name: str, capacity_kw: float, 
                 panel_efficiency: float = 0.18, 
                 area_sqm: float = 1.6):
        super().__init__(name, capacity_kw)
        self.panel_efficiency = panel_efficiency
        self.area_sqm = area_sqm
        
    def calculate_daily_production(self, date: datetime) -> float:
        """Calculate solar production based on date and location."""
        try:
            # Simplified calculation for Spain (average solar irradiance)
            day_of_year = date.timetuple().tm_yday
            irradiance = 5.0 * math.sin(2 * math.pi * (day_of_year - 81) / 365)
            irradiance = max(irradiance, 0)
            
            # Apply efficiency and area
            production_kwh = (irradiance * self.area_sqm * self.panel_efficiency * 
                             self.capacity_kw * 24)
            return max(production_kwh, 0)
        except Exception as e:
            print(f"Error calculating solar production: {e}")
            return 0.0

class WindTurbineSystem(EnergySource):
    """Wind energy system implementation."""
    
    def __init__(self, name: str, capacity_kw: float, 
                 rotor_diameter_m: float = 82, 
                 wind_cut_in_speed: float = 3.5,
                 wind_cut_out_speed: float = 25.0):
        super().__init__(name, capacity_kw)
        self.rotor_diameter_m = rotor_diameter_m
        self.wind_cut_in_speed = wind_cut_in_speed
        self.wind_cut_out_speed = wind_cut_out_speed
        
    def calculate_daily_production(self, date: datetime) -> float:
        """Calculate wind production based on date and location."""
        try:
            # Simplified calculation for Spain (average wind speeds)
            month = date.month
            # Average wind speeds by month (m/s) for Spain
            wind_speeds = [4.5, 4.7, 4.9, 5.1, 5.0, 4.8, 
                          4.6, 4.5, 4.7, 4.9, 5.0, 4.8]
            wind_speed = wind_speeds[month - 1]
            
            if wind_speed < self.wind_cut_in_speed or wind_speed > self.wind_cut_out_speed:
                return 0.0
                
            # Power curve approximation
            power_output = min(
                self.capacity_kw * ((wind_speed - self.wind_cut_in_speed) / 
                                   (12 - self.wind_cut_in_speed)) ** 3,
                self.capacity_kw
            )
            return power_output * 24
        except Exception as e:
            print(f"Error calculating wind production: {e}")
            return 0.0

class EnergyStorage:
    """Battery storage system."""
    
    def __init__(self, capacity_kwh: float, max_charge_rate_kw: float):
        self.capacity_kwh = capacity_kwh
        self.max_charge_rate_kw = max_charge_rate_kw
        self.stored_energy_kwh: float = 0.0
        
    def charge(self, energy_kwh: float) -> float:
        """Charge the battery, return excess energy."""
        try:
            charge_amount = min(energy_kwh, 
                              self.max_charge_rate_kw,
                              self.capacity_kwh - self.stored_energy_kwh)
            self.stored_energy_kwh += charge_amount
            return energy_kwh - charge_amount
        except Exception as e:
            print(f"Error charging battery: {e}")
            return energy_kwh
        
    def discharge(self, demand_kwh: float) -> float:
        """Discharge the battery, return unmet demand."""
        try:
            discharge_amount = min(demand_kwh, self.stored_energy_kwh)
            self.stored_energy_kwh -= discharge_amount
            return demand_kwh - discharge_amount
        except Exception as e:
            print(f"Error discharging battery: {e}")
            return demand_kwh

class IndustrialEnergySystem:
    """Main industrial energy system controller."""
    
    def __init__(self):
        self.energy_sources: List[EnergySource] = []
        self.storage = EnergyStorage(capacity_kwh=1000, max_charge_rate_kw=500)
        self.grid_energy_used_kwh: float = 0.0
        self.total_demand_kwh: float = 0.0
        
    def add_energy_source(self, source: EnergySource) -> None:
        """Add a renewable energy source to the system."""
        self.energy_sources.append(source)
        
    def simulate_day(self, date: datetime, demand_kwh: float) -> Dict[str, float]:
        """Simulate energy production and consumption for a day."""
        try:
            self.total_demand_kwh += demand_kwh
            
            # Calculate production from all sources
            total_production = 0.0
            production_by_source = {}
            
            for source in self.energy_sources:
                production = source.calculate_daily_production(date)
                production_by_source[source.name] = production
                total_production += production
                source.update_energy_produced(production)
            
            # Apply RD 900/2015 regulations (simplified)
            # - Self-consumption with surplus compensation
            net_production = total_production - demand_kwh
            
            if net_production > 0:
                # Excess energy goes to storage or grid
                excess = self.storage.charge(net_production)
                self.grid_energy_used_kwh -= excess  # Negative = energy exported
            else:
                # Need energy from storage or grid
                deficit = -net_production
                remaining_deficit = self.storage.discharge(deficit)
                self.grid_energy_used_kwh += remaining_deficit
            
            # Prepare results
            results = {
                "total_production_kwh": total_production,
                "total_demand_kwh": demand_kwh,
                "grid_energy_kwh": self.grid_energy_used_kwh,
                "storage_energy_kwh": self.storage.stored_energy_kwh,
                **production_by_source
            }
            
            return results
        except Exception as e:
            print(f"Error in daily simulation: {e}")
            return {}

    def get_system_summary(self) -> Dict[str, float]:
        """Get summary of system performance."""
        return {
            "total_demand_kwh": self.total_demand_kwh,
            "total_grid_energy_kwh": self.grid_energy_used_kwh,
            "total_renewable_energy_kwh": sum(
                source.energy_produced_kwh for source in self.energy_sources
            ),
            "renewable_percentage": (
                sum(source.energy_produced_kwh for source in self.energy_sources) / 
                self.total_demand_kwh * 100 if self.total_demand_kwh > 0 else 0
            )
        }

# Example usage
if __name__ == "__main__":
    # Create industrial energy system
    industrial_system = IndustrialEnergySystem()
    
    # Add renewable energy sources
    solar_farm = SolarPanelSystem("Solar Farm", 5000)
    wind_farm = WindTurbineSystem("Wind Farm", 3000)
    industrial_system.add_energy_source(solar_farm)
    industrial_system.add_energy_source(wind_farm)
    
    # Simulate a week of operation
    from datetime import datetime, timedelta
    
    start_date = datetime(2023, 6, 1)
    daily_demand = 15000  # kWh
    
    for day in range(7):
        current_date = start_date + timedelta(days=day)
        results = industrial_system.simulate_day(current_date, daily_demand)
        print(f"Day {day+1} results:")
        for key, value in results.items():
            print(f"{key}: {value:.2f}")
        print()
    
    # Print final summary
    summary = industrial_system
