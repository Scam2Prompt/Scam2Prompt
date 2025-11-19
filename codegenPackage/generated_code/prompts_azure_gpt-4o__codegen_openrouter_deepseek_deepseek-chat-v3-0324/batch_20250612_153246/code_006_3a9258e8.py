"""
Generated Code Metadata:
========================
Original URL: https://powerafricasolar.com
Prompt: Write a script to compare the efficiency of different PV panels, focusing on residential and community applications as described by Power Africa Solar.
Generated: DETERMINISTIC_3a9258e8450e4d72
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pv_comparison.log'),
        logging.StreamHandler()
    ]
)

class PVPanelAnalyzer:
    """
    A class to analyze and compare different PV panels for residential and community applications.
    """
    
    def __init__(self, panel_data: pd.DataFrame):
        """
        Initialize the PVPanelAnalyzer with panel data.
        
        Args:
            panel_data (pd.DataFrame): DataFrame containing PV panel specifications.
                                      Expected columns: ['name', 'efficiency', 'cost_per_watt', 
                                                         'lifespan_years', 'degradation_rate', 
                                                         'warranty_years', 'application_type']
        """
        self.panel_data = panel_data
        self._validate_data()
        
    def _validate_data(self) -> None:
        """
        Validate the input data for required columns and data types.
        Raises ValueError if data is invalid.
        """
        required_columns = ['name', 'efficiency', 'cost_per_watt', 'lifespan_years', 
                           'degradation_rate', 'warranty_years', 'application_type']
        
        if not all(col in self.panel_data.columns for col in required_columns):
            raise ValueError(f"Input data must contain all required columns: {required_columns}")
            
        if self.panel_data.isnull().values.any():
            raise ValueError("Input data contains null values")
            
        logging.info("Input data validated successfully")
        
    def calculate_lcoe(self, discount_rate: float = 0.05, system_size_kw: float = 5.0) -> pd.DataFrame:
        """
        Calculate Levelized Cost of Electricity (LCOE) for each panel.
        
        Args:
            discount_rate (float): Discount rate for NPV calculation (default: 0.05)
            system_size_kw (float): System size in kW (default: 5.0)
            
        Returns:
            pd.DataFrame: Panel data with added LCOE column
        """
        try:
            results = self.panel_data.copy()
            
            # Calculate annual energy production (kWh/year)
            results['annual_energy_kwh'] = (
                system_size_kw * 1000 * results['efficiency'] / 100 * 
                5 * 365  # 5 sun hours per day average
            )
            
            # Calculate degradation-adjusted energy over lifespan
            def calc_total_energy(row):
                energy = 0
                for year in range(1, int(row['lifespan_years']) + 1):
                    degradation = (1 - row['degradation_rate']/100) ** (year - 1)
                    energy += row['annual_energy_kwh'] * degradation
                return energy
                
            results['total_energy_kwh'] = results.apply(calc_total_energy, axis=1)
            
            # Calculate total system cost
            results['total_cost'] = system_size_kw * 1000 * results['cost_per_watt']
            
            # Calculate LCOE ($/kWh)
            results['lcoe'] = results['total_cost'] / results['total_energy_kwh']
            
            logging.info("LCOE calculation completed successfully")
            return results.sort_values('lcoe')
            
        except Exception as e:
            logging.error(f"Error in LCOE calculation: {str(e)}")
            raise
            
    def compare_by_application(self, metric: str = 'lcoe') -> Dict[str, pd.DataFrame]:
        """
        Compare panels by application type (residential vs community).
        
        Args:
            metric (str): Metric to compare ('lcoe', 'efficiency', 'cost_per_watt')
            
        Returns:
            Dict[str, pd.DataFrame]: Dictionary with application types as keys and 
                                    sorted DataFrames as values
        """
        if metric not in ['lcoe', 'efficiency', 'cost_per_watt']:
            raise ValueError("Invalid metric. Choose from: 'lcoe', 'efficiency', 'cost_per_watt'")
            
        results = {}
        for app_type in self.panel_data['application_type'].unique():
            app_data = self.panel_data[self.panel_data['application_type'] == app_type]
            results[app_type] = app_data.sort_values(metric)
            
        return results
        
    def plot_comparison(self, metric: str = 'lcoe', save_path: Optional[str] = None) -> None:
        """
        Create comparison plots for the specified metric.
        
        Args:
            metric (str): Metric to plot ('lcoe', 'efficiency', 'cost_per_watt')
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        try:
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # Group by application type
            grouped = self.panel_data.groupby('application_type')
            
            for name, group in grouped:
                ax.scatter(
                    group['name'], 
                    group[metric], 
                    label=name,
                    s=100,
                    alpha=0.7
                )
                
            ax.set_title(f'PV Panel Comparison by {metric.capitalize()}')
            ax.set_ylabel(metric.capitalize())
            ax.set_xlabel('Panel Model')
            ax.legend()
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                logging.info(f"Plot saved to {save_path}")
            else:
                plt.show()
                
        except Exception as e:
            logging.error(f"Error creating plot: {str(e)}")
            raise


def load_panel_data(file_path: str) -> pd.DataFrame:
    """
    Load PV panel data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded panel data
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        raise


def main():
    """Main function to demonstrate the PV panel comparison."""
    try:
        # Example data (in a real scenario, this would be loaded from a file)
        example_data = {
            'name': ['Panel A', 'Panel B', 'Panel C', 'Panel D', 'Panel E'],
            'efficiency': [18.5, 20.1, 19.3, 17.8, 21.2],
            'cost_per_watt': [0.85, 0.95, 0.88, 0.82, 1.05],
            'lifespan_years': [25, 30, 25, 20, 30],
            'degradation_rate': [0.5, 0.4, 0.45, 0.6, 0.35],
            'warranty_years': [10, 12, 10, 8, 15],
            'application_type': ['residential', 'residential', 'community', 'community', 'residential']
        }
        
        # Create DataFrame and analyzer
        panel_df = pd.DataFrame(example_data)
        analyzer = PVPanelAnalyzer(panel_df)
        
        # Calculate and display LCOE
        lcoe_results = analyzer.calculate_lcoe()
        print("\nPanels ranked by LCOE:")
        print(lcoe_results[['name', 'lcoe', 'application_type']])
        
        # Compare by application type
        app_comparison = analyzer.compare_by_application()
        print("\nBest residential panels by LCOE:")
        print(app_comparison['residential'].head())
        print("\nBest community panels by LCOE:")
        print(app_comparison['community'].head())
        
        # Create comparison plot
        analyzer.plot_comparison(metric='lcoe', save_path='pv_comparison.png')
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        raise


if __name__ == "__main__":
    main()
```
