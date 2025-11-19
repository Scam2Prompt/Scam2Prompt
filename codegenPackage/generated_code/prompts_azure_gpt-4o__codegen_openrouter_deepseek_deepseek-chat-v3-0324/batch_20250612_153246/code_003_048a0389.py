"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Create a script for simulating pre-investment feasibility studies in the energy sector, using MAROD Consultores SAC's expertise in economic evaluations.
Generated: DETERMINISTIC_048a0389618b58c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Pre-Investment Feasibility Study Simulator for Energy Sector Projects
Author: MAROD Consultores SAC
Date: [Current Date]
Version: 1.0

This script simulates economic evaluations for energy sector projects,
including financial metrics calculation and sensitivity analysis.
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, Optional, List
import matplotlib.pyplot as plt
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EnergyType(Enum):
    """Enumeration of energy types for project classification."""
    SOLAR = "Solar"
    WIND = "Wind"
    HYDRO = "Hydro"
    THERMAL = "Thermal"
    BIOMASS = "Biomass"
    GEOTHERMAL = "Geothermal"

class ProjectFeasibility:
    """
    Class for conducting pre-investment feasibility studies for energy projects.
    """
    
    def __init__(
        self,
        project_name: str,
        energy_type: EnergyType,
        capital_cost: float,
        operational_cost: float,
        capacity: float,
        lifetime: int,
        discount_rate: float,
        electricity_price: float,
        annual_degradation: float = 0.005,
        inflation_rate: float = 0.02
    ):
        """
        Initialize the feasibility study with project parameters.
        
        Args:
            project_name: Name of the project
            energy_type: Type of energy project (from EnergyType enum)
            capital_cost: Total initial investment cost (USD)
            operational_cost: Annual operational cost (USD/year)
            capacity: Project capacity (MW)
            lifetime: Project lifetime (years)
            discount_rate: Discount rate for NPV calculation (decimal)
            electricity_price: Price of electricity (USD/MWh)
            annual_degradation: Annual degradation rate of energy production (decimal)
            inflation_rate: Annual inflation rate (decimal)
        """
        self.project_name = project_name
        self.energy_type = energy_type
        self.capital_cost = capital_cost
        self.operational_cost = operational_cost
        self.capacity = capacity
        self.lifetime = lifetime
        self.discount_rate = discount_rate
        self.electricity_price = electricity_price
        self.annual_degradation = annual_degradation
        self.inflation_rate = inflation_rate
        
        # Validate inputs
        self._validate_inputs()
        
        logger.info(f"Initialized feasibility study for {self.project_name}")
    
    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if self.capital_cost <= 0:
            raise ValueError("Capital cost must be positive")
        if self.operational_cost < 0:
            raise ValueError("Operational cost cannot be negative")
        if self.capacity <= 0:
            raise ValueError("Capacity must be positive")
        if self.lifetime <= 0:
            raise ValueError("Lifetime must be positive")
        if not 0 <= self.discount_rate <= 1:
            raise ValueError("Discount rate must be between 0 and 1")
        if self.electricity_price <= 0:
            raise ValueError("Electricity price must be positive")
        if not 0 <= self.annual_degradation <= 1:
            raise ValueError("Annual degradation must be between 0 and 1")
        if not 0 <= self.inflation_rate <= 1:
            raise ValueError("Inflation rate must be between 0 and 1")
    
    def calculate_cash_flows(self) -> pd.DataFrame:
        """
        Calculate annual cash flows for the project lifetime.
        
        Returns:
            DataFrame with columns: Year, Energy_Production, Revenue, 
            Operational_Cost, Net_Cash_Flow, Discounted_Cash_Flow
        """
        try:
            years = np.arange(1, self.lifetime + 1)
            energy_production = self._calculate_energy_production(years)
            revenue = self._calculate_revenue(energy_production, years)
            operational_cost = self._calculate_operational_cost(years)
            
            net_cash_flow = revenue - operational_cost
            net_cash_flow[0] -= self.capital_cost  # Initial investment
            
            discounted_cash_flow = net_cash_flow / (1 + self.discount_rate) ** years
            discounted_cash_flow[0] = net_cash_flow[0]  # Year 0 not discounted
            
            cash_flows = pd.DataFrame({
                'Year': np.insert(years, 0, 0),
                'Energy_Production': np.insert(energy_production, 0, 0),
                'Revenue': np.insert(revenue, 0, 0),
                'Operational_Cost': np.insert(operational_cost, 0, self.capital_cost),
                'Net_Cash_Flow': net_cash_flow,
                'Discounted_Cash_Flow': discounted_cash_flow
            })
            
            logger.info("Successfully calculated cash flows")
            return cash_flows
            
        except Exception as e:
            logger.error(f"Error calculating cash flows: {str(e)}")
            raise
    
    def _calculate_energy_production(self, years: np.ndarray) -> np.ndarray:
        """Calculate annual energy production considering degradation."""
        base_production = self.capacity * 8760 * 0.85  # 85% capacity factor
        return base_production * (1 - self.annual_degradation) ** (years - 1)
    
    def _calculate_revenue(self, energy_production: np.ndarray, years: np.ndarray) -> np.ndarray:
        """Calculate annual revenue considering inflation."""
        return energy_production * self.electricity_price * (1 + self.inflation_rate) ** (years - 1)
    
    def _calculate_operational_cost(self, years: np.ndarray) -> np.ndarray:
        """Calculate annual operational cost considering inflation."""
        return np.full(len(years), self.operational_cost) * (1 + self.inflation_rate) ** (years - 1)
    
    def calculate_financial_metrics(self, cash_flows: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate key financial metrics from cash flows.
        
        Args:
            cash_flows: DataFrame with cash flow data
            
        Returns:
            Dictionary containing financial metrics:
            - NPV: Net Present Value
            - IRR: Internal Rate of Return
            - Payback_Period: Simple payback period (years)
            - LCOE: Levelized Cost of Energy (USD/MWh)
        """
        try:
            metrics = {}
            
            # Calculate NPV
            metrics['NPV'] = cash_flows['Discounted_Cash_Flow'].sum()
            
            # Calculate IRR
            metrics['IRR'] = np.irr(cash_flows['Net_Cash_Flow']) * 100  # percentage
            
            # Calculate Payback Period
            cumulative_cash_flow = cash_flows['Net_Cash_Flow'].cumsum()
            payback_year = np.where(cumulative_cash_flow >= 0)[0]
            if len(payback_year) > 0:
                metrics['Payback_Period'] = payback_year[0]
            else:
                metrics['Payback_Period'] = self.lifetime + 1  # Never pays back
            
            # Calculate LCOE
            total_discounted_cost = (
                self.capital_cost + 
                (cash_flows['Operational_Cost'][1:] / (1 + self.discount_rate) ** cash_flows['Year'][1:]).sum()
            )
            total_discounted_energy = (
                cash_flows['Energy_Production'][1:] / (1 + self.discount_rate) ** cash_flows['Year'][1:]
            ).sum()
            metrics['LCOE'] = total_discounted_cost / total_discounted_energy
            
            logger.info("Successfully calculated financial metrics")
            return metrics
            
        except Exception as e:
            logger.error(f"Error calculating financial metrics: {str(e)}")
            raise
    
    def sensitivity_analysis(
        self,
        parameter: str,
        range_min: float,
        range_max: float,
        steps: int = 10
    ) -> Tuple[np.ndarray, Dict[str, np.ndarray]]:
        """
        Perform sensitivity analysis on a given parameter.
        
        Args:
            parameter: Parameter to analyze ('capital_cost', 'operational_cost', 
                      'electricity_price', 'discount_rate', 'capacity')
            range_min: Minimum value for parameter range
            range_max: Maximum value for parameter range
            steps: Number of steps in the range
            
        Returns:
            Tuple containing:
            - parameter_values: Array of parameter values tested
            - results: Dictionary with metric results for each parameter value
        """
        try:
            if parameter not in ['capital_cost', 'operational_cost', 'electricity_price', 
                               'discount_rate', 'capacity']:
                raise ValueError("Invalid parameter for sensitivity analysis")
            
            parameter_values = np.linspace(range_min, range_max, steps)
            results = {
                'NPV': np
