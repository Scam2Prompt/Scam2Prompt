"""
Generated Code Metadata:
========================
Original URL: https://powerafricasolar.com
Prompt: Write Python code to calculate the energy savings from installing Power Africa Solar's PV panels, factoring in energy storage solutions and residential power demands.
Generated: DETERMINISTIC_404352a16e35f0d1
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
from typing import Tuple, Dict, Optional

class SolarEnergySavingsCalculator:
    """
    A class to calculate energy savings from installing solar PV panels with energy storage.
    Factors in residential power demands, solar generation, and storage efficiency.
    """
    
    def __init__(
        self,
        panel_efficiency: float = 0.18,
        panel_area: float = 1.6,
        solar_irradiance: float = 5.0,
        system_loss: float = 0.14,
        battery_capacity_kwh: float = 10.0,
        battery_efficiency: float = 0.9,
        daily_energy_demand_kwh: float = 30.0
    ):
        """
        Initialize the calculator with system parameters.
        
        Args:
            panel_efficiency: Solar panel efficiency (0-1)
            panel_area: Area of single panel in m²
            solar_irradiance: Average daily solar irradiance in kWh/m²/day
            system_loss: System losses (0-1)
            battery_capacity_kwh: Battery storage capacity in kWh
            battery_efficiency: Round-trip battery efficiency (0-1)
            daily_energy_demand_kwh: Average daily household energy demand in kWh
        """
        self.panel_efficiency = panel_efficiency
        self.panel_area = panel_area
        self.solar_irradiance = solar_irradiance
        self.system_loss = system_loss
        self.battery_capacity_kwh = battery_capacity_kwh
        self.battery_efficiency = battery_efficiency
        self.daily_energy_demand_kwh = daily_energy_demand_kwh
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate that all inputs are within reasonable ranges."""
        if not 0 < self.panel_efficiency <= 1:
            raise ValueError("Panel efficiency must be between 0 and 1")
        if self.panel_area <= 0:
            raise ValueError("Panel area must be positive")
        if self.solar_irradiance <= 0:
            raise ValueError("Solar irradiance must be positive")
        if not 0 <= self.system_loss < 1:
            raise ValueError("System loss must be between 0 and 1")
        if self.battery_capacity_kwh <= 0:
            raise ValueError("Battery capacity must be positive")
        if not 0 < self.battery_efficiency <= 1:
            raise ValueError("Battery efficiency must be between 0 and 1")
        if self.daily_energy_demand_kwh <= 0:
            raise ValueError("Daily energy demand must be positive")
    
    def calculate_panel_output(self, num_panels: int) -> float:
        """
        Calculate daily energy output from solar panels.
        
        Args:
            num_panels: Number of solar panels installed
            
        Returns:
            Daily energy output in kWh
        """
        if num_panels <= 0:
            raise ValueError("Number of panels must be positive")
            
        total_area = num_panels * self.panel_area
        gross_output = total_area * self.solar_irradiance * self.panel_efficiency
        net_output = gross_output * (1 - self.system_loss)
        return net_output
    
    def calculate_daily_savings(
        self,
        num_panels: int,
        electricity_rate: float,
        use_battery: bool = True
    ) -> Tuple[float, float, Dict[str, float]]:
        """
        Calculate daily energy savings and performance metrics.
        
        Args:
            num_panels: Number of solar panels installed
            electricity_rate: Cost of grid electricity per kWh
            use_battery: Whether to use battery storage
            
        Returns:
            Tuple of (daily_savings, energy_deficit, metrics_dict)
        """
        if electricity_rate <= 0:
            raise ValueError("Electricity rate must be positive")
            
        solar_generation = self.calculate_panel_output(num_panels)
        energy_deficit = max(0, self.daily_energy_demand_kwh - solar_generation)
        
        if use_battery:
            stored_energy = min(solar_generation - self.daily_energy_demand_kwh, 
                              self.battery_capacity_kwh) * self.battery_efficiency
            if stored_energy > 0:
                energy_deficit = max(0, energy_deficit - stored_energy)
        
        grid_energy_used = energy_deficit
        solar_energy_used = self.daily_energy_demand_kwh - grid_energy_used
        
        daily_savings = solar_energy_used * electricity_rate
        
        metrics = {
            'solar_generation_kwh': solar_generation,
            'solar_energy_used_kwh': solar_energy_used,
            'grid_energy_used_kwh': grid_energy_used,
            'energy_deficit_kwh': energy_deficit,
            'battery_used': use_battery
        }
        
        return daily_savings, energy_deficit, metrics
    
    def calculate_annual_savings(
        self,
        num_panels: int,
        electricity_rate: float,
        use_battery: bool = True,
        days_in_year: int = 365
    ) -> Tuple[float, Dict[str, float]]:
        """
        Calculate annual energy savings and performance metrics.
        
        Args:
            num_panels: Number of solar panels installed
            electricity_rate: Cost of grid electricity per kWh
            use_battery: Whether to use battery storage
            days_in_year: Number of days to calculate for (default 365)
            
        Returns:
            Tuple of (annual_savings, annual_metrics)
        """
        total_savings = 0.0
        total_metrics = {
            'total_solar_generation_kwh': 0.0,
            'total_solar_used_kwh': 0.0,
            'total_grid_used_kwh': 0.0,
            'total_energy_deficit_kwh': 0.0,
            'days_with_deficit': 0
        }
        
        for _ in range(days_in_year):
            daily_savings, energy_deficit, metrics = self.calculate_daily_savings(
                num_panels, electricity_rate, use_battery
            )
            
            total_savings += daily_savings
            total_metrics['total_solar_generation_kwh'] += metrics['solar_generation_kwh']
            total_metrics['total_solar_used_kwh'] += metrics['solar_energy_used_kwh']
            total_metrics['total_grid_used_kwh'] += metrics['grid_energy_used_kwh']
            total_metrics['total_energy_deficit_kwh'] += metrics['energy_deficit_kwh']
            
            if metrics['energy_deficit_kwh'] > 0:
                total_metrics['days_with_deficit'] += 1
        
        return total_savings, total_metrics
    
    def calculate_payback_period(
        self,
        num_panels: int,
        electricity_rate: float,
        system_cost: float,
        use_battery: bool = True,
        days_in_year: int = 365
    ) -> float:
        """
        Calculate payback period in years for the solar PV system.
        
        Args:
            num_panels: Number of solar panels installed
            electricity_rate: Cost of grid electricity per kWh
            system_cost: Total installed cost of the system
            use_battery: Whether to use battery storage
            days_in_year: Number of days to calculate for (default 365)
            
        Returns:
            Payback period in years
        """
        if system_cost <= 0:
            raise ValueError("System cost must be positive")
            
        annual_savings, _ = self.calculate_annual_savings(
            num_panels, electricity_rate, use_battery, days_in_year
        )
        
        if annual_savings <= 0:
            return float('inf')  # Never pays back
        
        return system_cost / annual_savings


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator with default parameters
        calculator = SolarEnergySavingsCalculator()
        
        # Calculate for a 10-panel system with battery
        num_panels = 10
        electricity_rate = 0.15  # $0.15 per kWh
        system_cost = 15000  # $15,000 system cost
        
        # Daily calculation
        daily_savings, daily_deficit, daily_metrics = calculator.calculate_daily_savings(
            num_panels, electricity_rate, use_battery=True
        )
        print(f"Daily Savings: ${daily_savings:.2f}")
        print(f"Daily Deficit: {daily_deficit:.2f} kWh")
        
        # Annual calculation
        annual_savings, annual_metrics = calculator.calculate_annual_savings(
            num_panels, electricity_rate, use_battery=True
        )
        print(f"\nAnnual Savings: ${annual_savings:.2f}")
        print(f"Annual Solar Generation:
