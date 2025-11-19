"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: Develop a program to model grid-positive solar generation for educational institutions, referencing Chico Electric's installation at Butte College.
Generated: DETERMINISTIC_f0f68e5ed45a2f29
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Grid-Positive Solar Generation Model for Educational Institutions
Reference: Chico Electric's installation at Butte College

This program models solar energy generation and consumption for educational institutions,
comparing on-site generation with grid consumption to determine grid-positive status.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List

class SolarGenerationModel:
    """
    A class to model solar generation and consumption for educational institutions.
    
    Attributes:
        solar_capacity_kw (float): Installed solar capacity in kW
        institution_name (str): Name of the educational institution
        location (str): Geographic location of the institution
        solar_production_data (pd.DataFrame): Timeseries of solar production
        consumption_data (pd.DataFrame): Timeseries of energy consumption
    """
    
    def __init__(self, solar_capacity_kw: float, institution_name: str, location: str):
        """
        Initialize the solar generation model.
        
        Args:
            solar_capacity_kw: Installed solar capacity in kilowatts
            institution_name: Name of the educational institution
            location: Geographic location for solar calculations
        """
        self.solar_capacity_kw = solar_capacity_kw
        self.institution_name = institution_name
        self.location = location
        self.solar_production_data = pd.DataFrame()
        self.consumption_data = pd.DataFrame()
        
    def generate_solar_production(self, start_date: str, end_date: str) -> None:
        """
        Generate simulated solar production data based on capacity and location.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
        """
        try:
            date_range = pd.date_range(start=start_date, end=end_date, freq='H')
            num_periods = len(date_range)
            
            # Base production curve (simplified for demonstration)
            hours = np.arange(24)
            daily_profile = np.sin((hours - 6) * np.pi / 12)  # Peaks at noon
            daily_profile[daily_profile < 0] = 0  # No negative production
            
            # Seasonal adjustment (more production in summer)
            seasons = (date_range.month % 12 // 3 + 1).values
            season_factors = np.array([0.8, 1.0, 1.2, 0.9])  # Winter, Spring, Summer, Fall
            
            # Generate production data
            production = np.tile(daily_profile, len(date_range) // 24 + 1)[:num_periods]
            season_multiplier = season_factors[seasons - 1]
            production = production * season_multiplier * self.solar_capacity_kw
            
            self.solar_production_data = pd.DataFrame({
                'timestamp': date_range,
                'production_kwh': production
            })
            
        except Exception as e:
            raise ValueError(f"Error generating solar production data: {str(e)}")
    
    def load_consumption_data(self, filepath: str) -> None:
        """
        Load consumption data from a CSV file.
        
        Args:
            filepath: Path to CSV file with consumption data
                      Expected columns: timestamp, consumption_kwh
        """
        try:
            self.consumption_data = pd.read_csv(filepath, parse_dates=['timestamp'])
            if 'consumption_kwh' not in self.consumption_data.columns:
                raise ValueError("CSV must contain 'consumption_kwh' column")
        except Exception as e:
            raise ValueError(f"Error loading consumption data: {str(e)}")
    
    def analyze_grid_impact(self) -> Dict[str, float]:
        """
        Analyze the grid impact by comparing production and consumption.
        
        Returns:
            Dictionary with analysis results including:
            - total_production_kwh
            - total_consumption_kwh
            - net_export_kwh
            - grid_positive (boolean)
        """
        if self.solar_production_data.empty or self.consumption_data.empty:
            raise ValueError("Both production and consumption data must be loaded")
            
        try:
            # Merge data on timestamp
            merged = pd.merge(
                self.solar_production_data,
                self.consumption_data,
                on='timestamp',
                how='inner'
            )
            
            # Calculate net energy
            merged['net_energy'] = merged['production_kwh'] - merged['consumption_kwh']
            
            # Calculate totals
            total_production = merged['production_kwh'].sum()
            total_consumption = merged['consumption_kwh'].sum()
            net_export = merged['net_energy'].sum()
            
            return {
                'total_production_kwh': total_production,
                'total_consumption_kwh': total_consumption,
                'net_export_kwh': net_export,
                'grid_positive': net_export > 0,
                'percentage_offset': (total_production / total_consumption) * 100
            }
            
        except Exception as e:
            raise ValueError(f"Error analyzing grid impact: {str(e)}")
    
    def plot_results(self, analysis_results: Dict[str, float]) -> None:
        """
        Generate visualization of the solar production and consumption.
        
        Args:
            analysis_results: Results from analyze_grid_impact()
        """
        try:
            # Sample plot - in a real implementation would be more detailed
            plt.figure(figsize=(12, 6))
            
            # Plot production and consumption
            plt.plot(
                self.solar_production_data['timestamp'],
                self.solar_production_data['production_kwh'],
                label='Solar Production'
            )
            plt.plot(
                self.consumption_data['timestamp'],
                self.consumption_data['consumption_kwh'],
                label='Energy Consumption'
            )
            
            plt.title(f'Solar Generation vs Consumption\n{self.institution_name}')
            plt.xlabel('Date')
            plt.ylabel('Energy (kWh)')
            plt.legend()
            plt.grid(True)
            
            # Add summary text
            summary_text = (
                f"Total Production: {analysis_results['total_production_kwh']:.1f} kWh\n"
                f"Total Consumption: {analysis_results['total_consumption_kwh']:.1f} kWh\n"
                f"Net Export: {analysis_results['net_export_kwh']:.1f} kWh\n"
                f"Grid Positive: {'Yes' if analysis_results['grid_positive'] else 'No'}\n"
                f"Percentage Offset: {analysis_results['percentage_offset']:.1f}%"
            )
            plt.annotate(
                summary_text,
                xy=(0.02, 0.7),
                xycoords='axes fraction',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
            )
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise ValueError(f"Error generating plot: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Create model for Butte College example
        butte_college = SolarGenerationModel(
            solar_capacity_kw=5000,  # Example capacity (5 MW)
            institution_name="Butte College",
            location="Oroville, CA"
        )
        
        # Generate solar production for a year
        butte_college.generate_solar_production('2023-01-01', '2023-12-31')
        
        # Load consumption data (in a real implementation, this would be from actual data)
        # For demo purposes, we'll create sample data
        dates = pd.date_range('2023-01-01', '2023-12-31', freq='H')
        consumption = np.random.normal(loc=4000, scale=1000, size=len(dates))  # Simulated consumption
        consumption_df = pd.DataFrame({'timestamp': dates, 'consumption_kwh': consumption})
        consumption_df.to_csv('butte_college_consumption.csv', index=False)
        
        butte_college.load_consumption_data('butte_college_consumption.csv')
        
        # Analyze grid impact
        results = butte_college.analyze_grid_impact()
        print("Analysis Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
        
        # Plot results
        butte_college.plot_results(results)
        
    except Exception as e:
        print(f"Error in example usage: {str(e)}")
```
