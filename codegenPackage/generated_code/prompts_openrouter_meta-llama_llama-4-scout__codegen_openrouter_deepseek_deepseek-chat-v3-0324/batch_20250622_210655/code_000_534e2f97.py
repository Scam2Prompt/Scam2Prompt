"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: "Generate a Python script to calculate the potential savings of installing a solar photovoltaic system for self-consumption in a residential setting, considering a 25-year guarantee and over 30 years of lifespan."
Generated: DETERMINISTIC_534e2f97867a4408
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import sys
from typing import Optional, Tuple, Dict

class SolarSavingsCalculator:
    """
    A class to calculate potential savings from installing a solar PV system for residential use.
    Takes into account system lifespan, guarantee period, and various financial factors.
    """
    
    def __init__(
        self,
        system_size_kw: float,
        solar_irradiance: float,
        performance_ratio: float,
        electricity_rate: float,
        inflation_rate: float,
        discount_rate: float,
        system_cost: float,
        maintenance_cost_per_year: float,
        guarantee_period: int = 25,
        lifespan: int = 30
    ):
        """
        Initialize the calculator with system parameters and financial assumptions.
        
        Args:
            system_size_kw: Size of the solar PV system in kW
            solar_irradiance: Average solar irradiance in kWh/m²/day
            performance_ratio: System performance ratio (0 to 1)
            electricity_rate: Current electricity rate in $/kWh
            inflation_rate: Expected annual inflation rate (decimal)
            discount_rate: Discount rate for NPV calculation (decimal)
            system_cost: Total installed cost of the system in $
            maintenance_cost_per_year: Annual maintenance cost in $
            guarantee_period: Warranty period in years (default 25)
            lifespan: Expected system lifespan in years (default 30)
        """
        self.system_size_kw = system_size_kw
        self.solar_irradiance = solar_irradiance
        self.performance_ratio = performance_ratio
        self.electricity_rate = electricity_rate
        self.inflation_rate = inflation_rate
        self.discount_rate = discount_rate
        self.system_cost = system_cost
        self.maintenance_cost_per_year = maintenance_cost_per_year
        self.guarantee_period = guarantee_period
        self.lifespan = lifespan
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate that all inputs are within reasonable ranges."""
        if self.system_size_kw <= 0:
            raise ValueError("System size must be positive")
        if not (0 < self.solar_irradiance <= 10):
            raise ValueError("Solar irradiance should be between 0 and 10 kWh/m²/day")
        if not (0 < self.performance_ratio <= 1):
            raise ValueError("Performance ratio should be between 0 and 1")
        if self.electricity_rate <= 0:
            raise ValueError("Electricity rate must be positive")
        if not (-0.1 < self.inflation_rate < 0.2):
            raise ValueError("Inflation rate should be between -10% and 20%")
        if not (0 <= self.discount_rate < 0.2):
            raise ValueError("Discount rate should be between 0% and 20%")
        if self.system_cost <= 0:
            raise ValueError("System cost must be positive")
        if self.maintenance_cost_per_year < 0:
            raise ValueError("Maintenance cost cannot be negative")
        if self.guarantee_period <= 0 or self.lifespan <= 0:
            raise ValueError("Guarantee period and lifespan must be positive")
        if self.guarantee_period > self.lifespan:
            raise ValueError("Guarantee period cannot exceed system lifespan")
    
    def calculate_annual_production(self) -> float:
        """
        Calculate annual electricity production in kWh.
        
        Formula: System size (kW) * Solar irradiance * Performance ratio * 365 days
        """
        return self.system_size_kw * self.solar_irradiance * self.performance_ratio * 365
    
    def calculate_annual_savings(self, year: int) -> float:
        """
        Calculate electricity savings for a given year, accounting for inflation.
        
        Args:
            year: The year number (0-based) for which to calculate savings
        """
        inflated_rate = self.electricity_rate * (1 + self.inflation_rate) ** year
        annual_production = self.calculate_annual_production()
        return annual_production * inflated_rate
    
    def calculate_maintenance_cost(self, year: int) -> float:
        """
        Calculate maintenance cost for a given year, accounting for inflation.
        
        Args:
            year: The year number (0-based) for which to calculate maintenance
        """
        return self.maintenance_cost_per_year * (1 + self.inflation_rate) ** year
    
    def calculate_net_cash_flow(self, year: int) -> float:
        """
        Calculate net cash flow for a given year.
        
        Args:
            year: The year number (0-based) for which to calculate cash flow
        """
        if year == 0:
            return -self.system_cost  # Initial investment
        
        savings = self.calculate_annual_savings(year)
        maintenance = self.calculate_maintenance_cost(year)
        
        # After guarantee period, apply degradation factor
        if year > self.guarantee_period:
            degradation_factor = 0.995 ** (year - self.guarantee_period)
            savings *= degradation_factor
        
        return savings - maintenance
    
    def calculate_npv(self) -> float:
        """
        Calculate the Net Present Value (NPV) of the solar PV investment.
        """
        npv = 0.0
        for year in range(self.lifespan + 1):  # Include year 0 (initial investment)
            cash_flow = self.calculate_net_cash_flow(year)
            discount_factor = (1 + self.discount_rate) ** year
            npv += cash_flow / discount_factor
        return npv
    
    def calculate_payback_period(self) -> Optional[float]:
        """
        Calculate the payback period in years.
        Returns None if the system never pays back within its lifespan.
        """
        cumulative_cash_flow = 0.0
        for year in range(1, self.lifespan + 1):
            cash_flow = self.calculate_net_cash_flow(year)
            cumulative_cash_flow += cash_flow
            
            if cumulative_cash_flow >= self.system_cost:
                # Linear interpolation for more precise payback period
                if year == 1:
                    return year
                prev_cash_flow = cumulative_cash_flow - cash_flow
                fraction = (self.system_cost - prev_cash_flow) / (cumulative_cash_flow - prev_cash_flow)
                return year - 1 + fraction
        
        return None
    
    def generate_cash_flow_table(self) -> Dict[int, Dict[str, float]]:
        """
        Generate a detailed cash flow table for each year.
        
        Returns:
            A dictionary with years as keys and dictionaries of values as values
        """
        cash_flows = {}
        for year in range(self.lifespan + 1):
            cash_flows[year] = {
                'savings': self.calculate_annual_savings(year) if year > 0 else 0,
                'maintenance': self.calculate_maintenance_cost(year) if year > 0 else 0,
                'net_cash_flow': self.calculate_net_cash_flow(year),
                'cumulative_cash_flow': sum(self.calculate_net_cash_flow(y) for y in range(year + 1))
            }
        return cash_flows
    
    def get_summary(self) -> Dict[str, float]:
        """
        Return a summary of key financial metrics.
        """
        return {
            'system_size_kw': self.system_size_kw,
            'annual_production_kwh': self.calculate_annual_production(),
            'total_system_cost': self.system_cost,
            'net_present_value': self.calculate_npv(),
            'payback_period': self.calculate_payback_period(),
            'lifespan_years': self.lifespan,
            'guarantee_period_years': self.guarantee_period
        }


def main():
    """
    Example usage of the SolarSavingsCalculator with default values.
    """
    try:
        # Example parameters (can be replaced with user input)
        calculator = SolarSavingsCalculator(
            system_size_kw=5.0,
            solar_irradiance=4.5,
            performance_ratio=0.75,
            electricity_rate=0.15,
            inflation_rate=0.02,
            discount_rate=0.05,
            system_cost=10000,
            maintenance_cost_per_year=100,
            guarantee_period=25,
            lifespan=30
        )
        
        # Print summary
        summary = calculator.get_summary()
        print("\nSolar PV System Financial Summary:")
        print("---------------------------------")
        print(f"System Size: {summary['system_size_kw']} kW")
        print(f"Annual Production: {summary['annual_production_kwh']:,.0f} kWh")
        print(f"Total System Cost: ${summary['total_system_cost']:,.2f}")
        print(f"Net Present Value: ${summary['net_present_value']:,.2f}")
        
        payback = summary['payback_period']
        if payback is not None:
            print(f"Payback Period: {
