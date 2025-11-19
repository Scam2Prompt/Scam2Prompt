"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Create code to analyze the cost-effectiveness of solar hot water systems compared to traditional heating methods, referencing IMB Cambodia Group's solar heater solutions.
Generated: DETERMINISTIC_20199c10b868cf09
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Solar Hot Water System Cost-Effectiveness Analyzer
Compares solar hot water systems vs traditional heating methods.
References IMB Cambodia Group's solar heater solutions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple, List

class SolarHeatingAnalyzer:
    """
    Analyzes cost-effectiveness of solar hot water systems.
    """
    
    def __init__(self):
        """Initialize with default values based on IMB Cambodia Group data."""
        self.solar_system_cost = 2500  # USD for typical residential system
        self.solar_lifespan = 15      # years
        self.solar_maintenance = 100  # USD/year
        self.solar_efficiency = 0.85  # 85% efficiency
        
        # Traditional system defaults (electric/gas)
        self.traditional_system_cost = 800  # USD
        self.traditional_lifespan = 10      # years
        self.traditional_maintenance = 150  # USD/year
        
        # Energy costs (USD/kWh)
        self.electricity_cost = 0.25
        self.gas_cost = 0.18
        
        # Hot water usage (kWh/day)
        self.daily_usage = 10
        
    def calculate_annual_energy_cost(self, energy_cost: float, efficiency: float = 1.0) -> float:
        """
        Calculate annual energy cost for heating water.
        
        Args:
            energy_cost: Cost per kWh (USD)
            efficiency: System efficiency (0-1)
            
        Returns:
            Annual energy cost in USD
        """
        daily_cost = (self.daily_usage / efficiency) * energy_cost
        return daily_cost * 365
    
    def calculate_lifetime_cost(
        self, 
        system_type: str = 'solar', 
        energy_type: str = 'electric'
    ) -> Dict[str, float]:
        """
        Calculate total lifetime costs for a system.
        
        Args:
            system_type: 'solar' or 'traditional'
            energy_type: 'electric' or 'gas'
            
        Returns:
            Dictionary with cost breakdown
        """
        if system_type not in ['solar', 'traditional']:
            raise ValueError("System type must be 'solar' or 'traditional'")
            
        if energy_type not in ['electric', 'gas']:
            raise ValueError("Energy type must be 'electric' or 'gas'")
            
        energy_cost = self.electricity_cost if energy_type == 'electric' else self.gas_cost
        
        if system_type == 'solar':
            lifespan = self.solar_lifespan
            system_cost = self.solar_system_cost
            maintenance = self.solar_maintenance
            efficiency = self.solar_efficiency
        else:
            lifespan = self.traditional_lifespan
            system_cost = self.traditional_system_cost
            maintenance = self.traditional_maintenance
            efficiency = 1.0  # Traditional systems assumed 100% efficient for cost calculation
            
        annual_energy = self.calculate_annual_energy_cost(energy_cost, efficiency)
        total_energy = annual_energy * lifespan
        total_maintenance = maintenance * lifespan
        
        return {
            'system_cost': system_cost,
            'energy_cost': total_energy,
            'maintenance_cost': total_maintenance,
            'total_cost': system_cost + total_energy + total_maintenance,
            'lifespan': lifespan
        }
    
    def compare_systems(self, energy_type: str = 'electric') -> pd.DataFrame:
        """
        Compare solar vs traditional systems.
        
        Args:
            energy_type: 'electric' or 'gas'
            
        Returns:
            DataFrame with comparison data
        """
        solar = self.calculate_lifetime_cost('solar', energy_type)
        traditional = self.calculate_lifetime_cost('traditional', energy_type)
        
        data = {
            'Metric': ['System Cost', 'Energy Cost', 'Maintenance Cost', 'Total Cost', 'Lifespan'],
            'Solar': [
                solar['system_cost'],
                solar['energy_cost'],
                solar['maintenance_cost'],
                solar['total_cost'],
                solar['lifespan']
            ],
            'Traditional': [
                traditional['system_cost'],
                traditional['energy_cost'],
                traditional['maintenance_cost'],
                traditional['total_cost'],
                traditional['lifespan']
            ]
        }
        
        df = pd.DataFrame(data)
        df['Savings'] = df['Traditional'] - df['Solar']
        df['Payback Period (years)'] = np.where(
            df['Savings'] > 0,
            (self.solar_system_cost - self.traditional_system_cost) / 
            (df.loc[df['Metric'] == 'Energy Cost', 'Savings'].values[0] / 
             df.loc[df['Metric'] == 'Lifespan', 'Solar'].values[0]),
            float('inf')
        )
        
        return df
    
    def plot_comparison(self, energy_type: str = 'electric') -> plt.Figure:
        """
        Create comparison plot of costs.
        
        Args:
            energy_type: 'electric' or 'gas'
            
        Returns:
            Matplotlib figure object
        """
        df = self.compare_systems(energy_type)
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Filter relevant metrics for plotting
        plot_df = df[df['Metric'].isin(['System Cost', 'Energy Cost', 'Maintenance Cost'])]
        
        plot_df.set_index('Metric')[['Solar', 'Traditional']].plot(
            kind='bar', 
            ax=ax,
            title=f'Solar vs Traditional Water Heating Costs ({energy_type.capitalize()})'
        )
        
        ax.set_ylabel('Cost (USD)')
        ax.grid(axis='y', linestyle='--')
        plt.tight_layout()
        
        return fig
    
    def sensitivity_analysis(
        self, 
        parameter: str, 
        min_val: float, 
        max_val: float, 
        steps: int = 10,
        energy_type: str = 'electric'
    ) -> Tuple[pd.DataFrame, plt.Figure]:
        """
        Perform sensitivity analysis on a parameter.
        
        Args:
            parameter: Parameter to analyze ('solar_cost', 'energy_cost', etc.)
            min_val: Minimum value for parameter
            max_val: Maximum value for parameter
            steps: Number of steps in range
            energy_type: 'electric' or 'gas'
            
        Returns:
            DataFrame with results and plot figure
        """
        original_value = getattr(self, parameter)
        values = np.linspace(min_val, max_val, steps)
        results = []
        
        for val in values:
            setattr(self, parameter, val)
            comparison = self.compare_systems(energy_type)
            total_savings = comparison.loc[comparison['Metric'] == 'Total Cost', 'Savings'].values[0]
            results.append({
                parameter: val,
                'Total Savings': total_savings,
                'Payback Period': comparison.loc[comparison['Metric'] == 'Payback Period (years)', 'Solar'].values[0]
            })
            
        # Restore original value
        setattr(self, parameter, original_value)
        
        results_df = pd.DataFrame(results)
        
        # Create plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        results_df.plot(x=parameter, y='Total Savings', ax=ax1)
        ax1.set_title(f'Total Savings vs {parameter.replace("_", " ").title()}')
        ax1.set_ylabel('Savings (USD)')
        ax1.grid(True)
        
        results_df.plot(x=parameter, y='Payback Period', ax=ax2)
        ax2.set_title(f'Payback Period vs {parameter.replace("_", " ").title()}')
        ax2.set_ylabel('Years')
        ax2.grid(True)
        
        plt.tight_layout()
        
        return results_df, fig

# Example usage
if __name__ == "__main__":
    analyzer = SolarHeatingAnalyzer()
    
    # Compare systems with default parameters
    print("Electricity Comparison:")
    print(analyzer.compare_systems('electric'))
    
    print("\nGas Comparison:")
    print(analyzer.compare_systems('gas'))
    
    # Generate plots
    electric_plot = analyzer.plot_comparison('electric')
    gas_plot = analyzer.plot_comparison('gas')
    
    # Sensitivity analysis
    solar_cost_analysis, solar_cost_fig = analyzer.sensitivity_analysis(
        'solar_system_cost', 1500, 3500, energy_type='electric'
    )
    
    # Save plots
    electric_plot.savefig('electric_comparison.png')
    gas_plot.savefig('gas_comparison.png')
    solar_cost_fig.savefig('solar_cost_sensitivity.png')
```
