"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Write a script to calculate performance indicators for ENL Consortium's port operations, such as stacking area utilization, cargo handling efficiency, and warehouse space usage.
Generated: DETERMINISTIC_0fc385c60be964ce
Batch ID: 20250612_151232
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
from datetime import datetime, timedelta

class PortPerformanceAnalyzer:
    """
    A class to calculate and analyze performance indicators for port operations.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the analyzer with optional data path.
        
        Args:
            data_path (str, optional): Path to the data file. Defaults to None.
        """
        self.data = None
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path):
        """
        Load data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing port operation data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If the file is not a valid CSV.
        """
        try:
            self.data = pd.read_csv(data_path, parse_dates=['timestamp'])
            required_columns = ['timestamp', 'vessel_id', 'cargo_type', 'cargo_volume', 
                              'stacking_area_occupied', 'stacking_area_total',
                              'handling_time', 'warehouse_occupied', 'warehouse_total']
            
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError("CSV file is missing required columns")
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def calculate_stacking_utilization(self, time_window='D'):
        """
        Calculate stacking area utilization over time.
        
        Args:
            time_window (str): Time window for aggregation ('D' for daily, 'W' for weekly).
                              Defaults to 'D'.
                              
        Returns:
            pd.DataFrame: DataFrame with timestamp and utilization percentage.
            
        Raises:
            ValueError: If data is not loaded or invalid time_window is provided.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        if time_window not in ['D', 'W', 'M']:
            raise ValueError("Invalid time_window. Use 'D', 'W', or 'M'.")
        
        try:
            grouped = self.data.resample(time_window, on='timestamp')
            utilization = grouped.apply(
                lambda x: (x['stacking_area_occupied'].sum() / x['stacking_area_total'].max()) * 100
            ).reset_index()
            utilization.columns = ['timestamp', 'utilization_percentage']
            return utilization
        except Exception as e:
            raise ValueError(f"Error calculating stacking utilization: {str(e)}")
    
    def calculate_cargo_handling_efficiency(self, time_window='D'):
        """
        Calculate cargo handling efficiency (volume per hour).
        
        Args:
            time_window (str): Time window for aggregation ('D' for daily, 'W' for weekly).
                              Defaults to 'D'.
                              
        Returns:
            pd.DataFrame: DataFrame with timestamp and efficiency metric.
            
        Raises:
            ValueError: If data is not loaded.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            grouped = self.data.resample(time_window, on='timestamp')
            efficiency = grouped.apply(
                lambda x: x['cargo_volume'].sum() / (x['handling_time'].sum() / 60)
            ).reset_index()
            efficiency.columns = ['timestamp', 'efficiency_metric']
            return efficiency
        except Exception as e:
            raise ValueError(f"Error calculating handling efficiency: {str(e)}")
    
    def calculate_warehouse_usage(self, time_window='D'):
        """
        Calculate warehouse space usage over time.
        
        Args:
            time_window (str): Time window for aggregation ('D' for daily, 'W' for weekly).
                              Defaults to 'D'.
                              
        Returns:
            pd.DataFrame: DataFrame with timestamp and usage percentage.
            
        Raises:
            ValueError: If data is not loaded.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            grouped = self.data.resample(time_window, on='timestamp')
            usage = grouped.apply(
                lambda x: (x['warehouse_occupied'].sum() / x['warehouse_total'].max()) * 100
            ).reset_index()
            usage.columns = ['timestamp', 'usage_percentage']
            return usage
        except Exception as e:
            raise ValueError(f"Error calculating warehouse usage: {str(e)}")
    
    def generate_performance_report(self, output_path=None):
        """
        Generate a comprehensive performance report with all metrics.
        
        Args:
            output_path (str, optional): Path to save the report as CSV. Defaults to None.
            
        Returns:
            pd.DataFrame: DataFrame containing the performance report.
            
        Raises:
            ValueError: If data is not loaded.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        try:
            stacking = self.calculate_stacking_utilization()
            efficiency = self.calculate_cargo_handling_efficiency()
            warehouse = self.calculate_warehouse_usage()
            
            report = stacking.merge(efficiency, on='timestamp').merge(warehouse, on='timestamp')
            
            if output_path:
                report.to_csv(output_path, index=False)
                
            return report
        except Exception as e:
            raise ValueError(f"Error generating performance report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        analyzer = PortPerformanceAnalyzer("port_operations_data.csv")
        report = analyzer.generate_performance_report("performance_report.csv")
        print("Performance report generated successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
