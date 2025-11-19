"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: "Write a Python script to analyze the performance of a commercial solar system with a 40kW capacity and provide recommendations for optimization."
Generated: DETERMINISTIC_4649c13cb3c467e9
Batch ID: 20250622_210216
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
from datetime import datetime
from scipy import stats
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class SolarSystemAnalyzer:
    """
    A class to analyze and optimize the performance of a commercial solar system.
    
    Attributes:
        capacity_kw (float): The rated capacity of the solar system in kW
        data (pd.DataFrame): DataFrame containing solar system performance data
    """
    
    def __init__(self, capacity_kw=40):
        """
        Initialize the SolarSystemAnalyzer with system capacity.
        
        Args:
            capacity_kw (float): Rated capacity of the solar system (default: 40kW)
        """
        self.capacity_kw = capacity_kw
        self.data = None
        
    def load_data(self, file_path):
        """
        Load solar system performance data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file containing performance data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file doesn't contain required columns
        """
        try:
            self.data = pd.read_csv(file_path, parse_dates=['timestamp'])
            
            required_columns = {'timestamp', 'power_output', 'irradiance', 'temperature'}
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            print(f"Successfully loaded data with {len(self.data)} records")
            
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def calculate_performance_metrics(self):
        """
        Calculate key performance metrics for the solar system.
        
        Returns:
            dict: Dictionary containing calculated performance metrics
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        metrics = {}
        
        # Basic metrics
        metrics['total_energy_kwh'] = self.data['power_output'].sum() / 4  # Assuming 15-min intervals
        metrics['capacity_factor'] = (metrics['total_energy_kwh'] / 
                                    (self.capacity_kw * 24 * len(self.data['timestamp'].dt.date.unique())))
        
        # Performance ratio
        metrics['performance_ratio'] = (self.data['power_output'].mean() / 
                                      (self.capacity_kw * self.data['irradiance'].mean() / 1000))
        
        # Degradation rate (if we have sufficient historical data)
        if len(self.data['timestamp'].dt.year.unique()) > 1:
            yearly_output = self.data.groupby(self.data['timestamp'].dt.year)['power_output'].mean()
            slope, _, _, _, _ = stats.linregress(yearly_output.index, yearly_output.values)
            metrics['degradation_rate'] = slope / self.capacity_kw * 100  # % per year
        
        return metrics
    
    def identify_underperformance(self, threshold=0.8):
        """
        Identify periods of underperformance based on expected output.
        
        Args:
            threshold (float): Threshold ratio for underperformance (default: 0.8)
            
        Returns:
            pd.DataFrame: DataFrame containing underperformance periods
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        expected_output = self.capacity_kw * (self.data['irradiance'] / 1000)
        performance_ratio = self.data['power_output'] / expected_output
        underperformance = self.data[performance_ratio < threshold].copy()
        underperformance['performance_ratio'] = performance_ratio[performance_ratio < threshold]
        
        return underperformance
    
    def plot_daily_production(self):
        """
        Plot daily energy production over time.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        daily_production = self.data.resample('D', on='timestamp')['power_output'].sum() / 4
        plt.figure(figsize=(12, 6))
        daily_production.plot()
        plt.title('Daily Energy Production')
        plt.ylabel('Energy (kWh)')
        plt.xlabel('Date')
        plt.grid(True)
        plt.show()
    
    def plot_efficiency_vs_temperature(self):
        """
        Plot system efficiency vs ambient temperature.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        efficiency = self.data['power_output'] / (self.capacity_kw * self.data['irradiance'] / 1000)
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['temperature'], efficiency, alpha=0.5)
        plt.title('System Efficiency vs Temperature')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Efficiency')
        plt.grid(True)
        plt.show()
    
    def generate_recommendations(self, metrics, underperformance):
        """
        Generate optimization recommendations based on analysis.
        
        Args:
            metrics (dict): Performance metrics from calculate_performance_metrics()
            underperformance (pd.DataFrame): Underperformance periods from identify_underperformance()
            
        Returns:
            list: List of optimization recommendations
        """
        recommendations = []
        
        # Check capacity factor
        if metrics.get('capacity_factor', 0) < 0.2:
            recommendations.append(
                "Low capacity factor suggests system may be oversized for current energy needs. "
                "Consider adding energy storage or finding additional loads."
            )
        
        # Check performance ratio
        if metrics.get('performance_ratio', 0) < 0.75:
            recommendations.append(
                "Low performance ratio indicates potential system issues. "
                "Check for shading, soiling, or equipment malfunctions."
            )
        
        # Check temperature impact
        temp_coef = np.polyfit(self.data['temperature'], 
                             self.data['power_output'] / (self.capacity_kw * self.data['irradiance'] / 1000), 
                             1)[0]
        if temp_coef < -0.003:  # Typical temperature coefficient is ~ -0.003 to -0.005 per °C
            recommendations.append(
                "Strong negative temperature coefficient observed. "
                "Consider improving panel cooling or using panels with better temperature coefficients."
            )
        
        # Analyze underperformance periods
        if len(underperformance) > 0:
            time_of_day = underperformance['timestamp'].dt.hour
            morning_hours = sum((time_of_day >= 8) & (time_of_day <= 11))
            afternoon_hours = sum((time_of_day >= 12) & (time_of_day <= 16))
            
            if morning_hours > afternoon_hours:
                recommendations.append(
                    "Morning underperformance detected. Check for east-side shading or panel orientation issues."
                )
            else:
                recommendations.append(
                    "Afternoon underperformance detected. Check for west-side shading or potential inverter throttling."
                )
        
        # Check degradation rate if available
        if 'degradation_rate' in metrics and metrics['degradation_rate'] < -1.0:
            recommendations.append(
                f"High degradation rate ({metrics['degradation_rate']:.2f}%/year) detected. "
                "Schedule maintenance to inspect panels and connections."
            )
        
        if not recommendations:
            recommendations.append("System performance is good. No major optimization recommendations at this time.")
        
        return recommendations

# Example usage
if __name__ == "__main__":
    try:
        analyzer = SolarSystemAnalyzer(capacity_kw=40)
        analyzer.load_data('solar_performance_data.csv')
        
        metrics = analyzer.calculate_performance_metrics()
        print("\nPerformance Metrics:")
        for k, v in metrics.items():
            print(f"{k.replace('_', ' ').title()}: {v:.2f}")
        
        underperformance = analyzer.identify_underperformance()
        print(f"\nFound {len(underperformance)} underperformance records")
        
        analyzer.plot_daily_production()
        analyzer.plot_efficiency_vs_temperature()
        
        recommendations = analyzer.generate_recommendations(metrics, underperformance)
        print("\nOptimization Recommendations:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
