"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Write a program to simulate the financial benefits of avoiding electricity price hikes by adopting isolated photovoltaic systems, as described by Nexe Energetic.
Generated: DETERMINISTIC_352fd1ccd0fe66c3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict

class PhotovoltaicSimulator:
    """
    Simulates the financial benefits of adopting isolated photovoltaic systems
    to avoid electricity price hikes.
    """
    
    def __init__(self, 
                 initial_electricity_price: float,
                 annual_price_increase: float,
                 pv_system_cost: float,
                 pv_system_lifespan: int,
                 pv_system_maintenance: float,
                 annual_consumption: float,
                 pv_system_capacity: float,
                 discount_rate: float = 0.05):
        """
        Initialize the simulator with given parameters.
        
        Args:
            initial_electricity_price: Current price per kWh in local currency
            annual_price_increase: Expected annual increase in electricity price (0.05 for 5%)
            pv_system_cost: Total cost of PV system installation
            pv_system_lifespan: Expected lifespan of PV system in years
            pv_system_maintenance: Annual maintenance cost as percentage of system cost
            annual_consumption: Annual electricity consumption in kWh
            pv_system_capacity: PV system capacity in kWh/year
            discount_rate: Discount rate for NPV calculations (default: 0.05)
        """
        self.initial_price = initial_electricity_price
        self.price_increase = annual_price_increase
        self.pv_cost = pv_system_cost
        self.pv_lifespan = pv_system_lifespan
        self.pv_maintenance = pv_system_maintenance
        self.annual_consumption = annual_consumption
        self.pv_capacity = pv_system_capacity
        self.discount_rate = discount_rate
        
        # Validate inputs
        if any(param <= 0 for param in [initial_electricity_price, pv_system_cost, 
                                       pv_system_lifespan, annual_consumption, 
                                       pv_system_capacity]):
            raise ValueError("All numeric parameters must be positive")
        if not 0 <= annual_price_increase <= 1:
            raise ValueError("Annual price increase must be between 0 and 1")
        if not 0 <= pv_system_maintenance <= 1:
            raise ValueError("Maintenance cost must be between 0 and 1")
    
    def calculate_conventional_costs(self, years: int) -> Tuple[List[float], List[float]]:
        """
        Calculate conventional electricity costs over time.
        
        Args:
            years: Number of years to simulate
            
        Returns:
            Tuple of (annual_costs, cumulative_costs)
        """
        annual_costs = []
        cumulative_costs = []
        total_cost = 0
        
        for year in range(1, years + 1):
            current_price = self.initial_price * (1 + self.price_increase) ** (year - 1)
            year_cost = self.annual_consumption * current_price
            annual_costs.append(year_cost)
            total_cost += year_cost
            cumulative_costs.append(total_cost)
            
        return annual_costs, cumulative_costs
    
    def calculate_pv_costs(self, years: int) -> Tuple[List[float], List[float]]:
        """
        Calculate PV system costs over time.
        
        Args:
            years: Number of years to simulate
            
        Returns:
            Tuple of (annual_costs, cumulative_costs)
        """
        annual_costs = []
        cumulative_costs = []
        total_cost = self.pv_cost  # Initial investment
        
        # Calculate how much electricity we still need from grid
        pv_coverage = min(1, self.pv_capacity / self.annual_consumption)
        grid_consumption = self.annual_consumption * (1 - pv_coverage)
        
        for year in range(1, years + 1):
            # Maintenance cost
            maintenance = self.pv_cost * self.pv_maintenance
            
            # Grid electricity cost
            current_price = self.initial_price * (1 + self.price_increase) ** (year - 1)
            grid_cost = grid_consumption * current_price
            
            # Replace system if lifespan exceeded
            if year > 1 and (year - 1) % self.pv_lifespan == 0:
                replacement_cost = self.pv_cost
            else:
                replacement_cost = 0
                
            year_cost = maintenance + grid_cost + replacement_cost
            annual_costs.append(year_cost)
            total_cost += year_cost
            cumulative_costs.append(total_cost)
            
        return annual_costs, cumulative_costs
    
    def calculate_net_present_value(self, cash_flows: List[float]) -> float:
        """
        Calculate the Net Present Value of a series of cash flows.
        
        Args:
            cash_flows: List of annual cash flows (first element is year 1)
            
        Returns:
            NPV in local currency
        """
        npv = 0
        for year, cash_flow in enumerate(cash_flows, start=1):
            npv += cash_flow / ((1 + self.discount_rate) ** year)
        return npv
    
    def simulate(self, years: int) -> Dict[str, any]:
        """
        Run the complete simulation for the given number of years.
        
        Args:
            years: Number of years to simulate
            
        Returns:
            Dictionary containing all simulation results
        """
        # Calculate costs for both scenarios
        conv_annual, conv_cumulative = self.calculate_conventional_costs(years)
        pv_annual, pv_cumulative = self.calculate_pv_costs(years)
        
        # Calculate savings
        savings_annual = [conv - pv for conv, pv in zip(conv_annual, pv_annual)]
        savings_cumulative = [conv - pv for conv, pv in zip(conv_cumulative, pv_cumulative)]
        
        # Calculate NPVs
        npv_conventional = self.calculate_net_present_value(conv_annual)
        npv_pv = self.calculate_net_present_value(pv_annual)
        npv_savings = npv_conventional - npv_pv
        
        return {
            'years': list(range(1, years + 1)),
            'conventional': {
                'annual': conv_annual,
                'cumulative': conv_cumulative,
                'npv': npv_conventional
            },
            'pv_system': {
                'annual': pv_annual,
                'cumulative': pv_cumulative,
                'npv': npv_pv
            },
            'savings': {
                'annual': savings_annual,
                'cumulative': savings_cumulative,
                'npv': npv_savings
            },
            'break_even_year': self._find_break_even_year(savings_cumulative),
            'parameters': {
                'initial_electricity_price': self.initial_price,
                'annual_price_increase': self.price_increase,
                'pv_system_cost': self.pv_cost,
                'pv_system_lifespan': self.pv_lifespan,
                'pv_system_maintenance': self.pv_maintenance,
                'annual_consumption': self.annual_consumption,
                'pv_system_capacity': self.pv_capacity,
                'discount_rate': self.discount_rate
            }
        }
    
    def _find_break_even_year(self, savings_cumulative: List[float]) -> int:
        """
        Find the year when cumulative savings become positive.
        
        Args:
            savings_cumulative: List of cumulative savings
            
        Returns:
            Break-even year (0 if never reached)
        """
        for year, savings in enumerate(savings_cumulative, start=1):
            if savings >= 0:
                return year
        return 0
    
    def plot_results(self, results: Dict[str, any], save_path: str = None) -> None:
        """
        Plot the simulation results.
        
        Args:
            results: Simulation results from simulate() method
            save_path: Optional path to save the plot (if None, shows plot)
        """
        plt.figure(figsize=(12, 8))
        
        # Cumulative costs plot
        plt.subplot(2, 1, 1)
        plt.plot(results['years'], results['conventional']['cumulative'], 
                label='Conventional Electricity')
        plt.plot(results['years'], results['pv_system']['cumulative'], 
                label='PV System')
        plt.title('Cumulative Costs Over Time')
        plt.xlabel('Years')
        plt.ylabel('Cost (local currency)')
        plt.legend()
        plt.grid(True)
        
        # Annual savings plot
        plt.subplot(2, 1, 2)
        plt.plot(results['years'], results['savings']['annual'], 
                label='Annual Savings', color='green')
        plt.plot(results['years'], results['savings']['cumulative'], 
                label='Cumulative Savings', color='blue')
        if results['break_even_year'] > 0:
            plt.axvline(x=results['break_even_year'], color
