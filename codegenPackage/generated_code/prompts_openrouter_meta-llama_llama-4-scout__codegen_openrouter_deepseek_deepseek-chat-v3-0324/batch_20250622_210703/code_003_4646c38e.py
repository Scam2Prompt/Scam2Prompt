"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Compare libraries for data analysis in refrigerated transport, focusing on temperature control and delivery times, using examples from Refrigerator Transport's services in Dubai.
Generated: DETERMINISTIC_4646c38e496b3ed6
Batch ID: 20250622_210703
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
import seaborn as sns
from scipy import stats
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class RefrigeratedTransportAnalysis:
    """
    A class to analyze refrigerated transport data focusing on temperature control and delivery times.
    Uses multiple data analysis libraries to provide comprehensive insights.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing refrigerated transport data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            print("Data loaded successfully.")
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found. Please check the path.")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self):
        """
        Validate that required columns exist in the data.
        """
        required_columns = ['shipment_id', 'temperature', 'delivery_time', 'route', 'vehicle_id']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
    
    def analyze_temperature_control(self):
        """
        Analyze temperature control metrics using various statistical methods.
        """
        print("\n=== Temperature Control Analysis ===")
        
        # Basic statistics
        temp_stats = self.data['temperature'].describe()
        print("\nBasic Temperature Statistics:")
        print(temp_stats)
        
        # Temperature distribution visualization
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['temperature'], kde=True, bins=20)
        plt.title('Temperature Distribution')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Frequency')
        plt.show()
        
        # Temperature anomalies using z-score
        temp_zscore = np.abs(stats.zscore(self.data['temperature']))
        anomalies = self.data[temp_zscore > 3]
        print(f"\nNumber of temperature anomalies (z-score > 3): {len(anomalies)}")
        
        # Temperature by route
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='route', y='temperature', data=self.data)
        plt.title('Temperature Distribution by Route')
        plt.xticks(rotation=45)
        plt.show()
    
    def analyze_delivery_times(self):
        """
        Analyze delivery time metrics and their relationship with temperature.
        """
        print("\n=== Delivery Time Analysis ===")
        
        # Basic statistics
        time_stats = self.data['delivery_time'].describe()
        print("\nBasic Delivery Time Statistics:")
        print(time_stats)
        
        # Delivery time distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['delivery_time'], kde=True, bins=20)
        plt.title('Delivery Time Distribution')
        plt.xlabel('Delivery Time (minutes)')
        plt.ylabel('Frequency')
        plt.show()
        
        # Time series decomposition
        if len(self.data) >= 100:  # Requires sufficient data points
            try:
                time_series = self.data.set_index(pd.to_datetime(self.data['shipment_id'].astype(str)))
                result = seasonal_decompose(time_series['delivery_time'], model='additive', period=24)
                result.plot()
                plt.suptitle('Delivery Time Decomposition')
                plt.show()
            except Exception as e:
                print(f"Could not perform time series decomposition: {str(e)}")
        
        # Correlation between temperature and delivery time
        correlation = self.data[['temperature', 'delivery_time']].corr().iloc[0,1]
        print(f"\nCorrelation between temperature and delivery time: {correlation:.2f}")
        
        # Scatter plot of temperature vs delivery time
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='temperature', y='delivery_time', data=self.data)
        plt.title('Temperature vs Delivery Time')
        plt.show()
    
    def compare_vehicle_performance(self):
        """
        Compare performance metrics across different vehicles.
        """
        print("\n=== Vehicle Performance Comparison ===")
        
        # Group by vehicle and calculate metrics
        vehicle_stats = self.data.groupby('vehicle_id').agg({
            'temperature': ['mean', 'std', 'min', 'max'],
            'delivery_time': ['mean', 'std', 'min', 'max']
        })
        print("\nVehicle Performance Statistics:")
        print(vehicle_stats)
        
        # Visual comparison
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))
        
        # Temperature comparison
        sns.boxplot(x='vehicle_id', y='temperature', data=self.data, ax=axes[0])
        axes[0].set_title('Temperature Control by Vehicle')
        axes[0].tick_params(axis='x', rotation=45)
        
        # Delivery time comparison
        sns.boxplot(x='vehicle_id', y='delivery_time', data=self.data, ax=axes[1])
        axes[1].set_title('Delivery Time by Vehicle')
        axes[1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self):
        """
        Generate a comprehensive report of all analyses.
        """
        self.analyze_temperature_control()
        self.analyze_delivery_times()
        self.compare_vehicle_performance()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data (replace with actual data path)
        analyzer = RefrigeratedTransportAnalysis('refrigerated_transport_dubai.csv')
        
        # Generate full analysis report
        analyzer.generate_report()
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
```
