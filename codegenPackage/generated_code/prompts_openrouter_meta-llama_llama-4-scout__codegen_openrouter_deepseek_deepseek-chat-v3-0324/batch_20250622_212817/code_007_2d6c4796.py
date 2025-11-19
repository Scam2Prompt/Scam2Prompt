"""
Generated Code Metadata:
========================
Original URL: https://veristenlabs.com
Prompt: Write a code example for generating easy-to-read charts for visualizing changes in health indicators, such as blood pressure and heart rate.
Generated: DETERMINISTIC_2d6c4796447facbe
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np

class HealthIndicatorVisualizer:
    """
    A class to visualize health indicators like blood pressure and heart rate.
    """
    
    def __init__(self):
        plt.style.use('ggplot')
    
    def _validate_data(self, data):
        """
        Validate input data structure.
        """
        required_columns = ['date', 'systolic', 'diastolic', 'heart_rate']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Data must contain columns: {required_columns}")
        
        if not isinstance(data['date'].iloc[0], (datetime, np.datetime64)):
            raise TypeError("Date column must contain datetime objects")
    
    def plot_blood_pressure(self, data, title="Blood Pressure Over Time"):
        """
        Plot systolic and diastolic blood pressure over time.
        
        Args:
            data (pd.DataFrame): DataFrame containing health data
            title (str): Title for the plot
        """
        try:
            self._validate_data(data)
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # Plot systolic and diastolic
            ax.plot(data['date'], data['systolic'], label='Systolic', color='#1f77b4', marker='o')
            ax.plot(data['date'], data['diastolic'], label='Diastolic', color='#ff7f0e', marker='o')
            
            # Add healthy range indicators
            ax.axhline(y=120, color='#1f77b4', linestyle='--', alpha=0.3, label='Normal Systolic')
            ax.axhline(y=80, color='#ff7f0e', linestyle='--', alpha=0.3, label='Normal Diastolic')
            
            # Formatting
            ax.set_title(title, pad=20)
            ax.set_xlabel('Date')
            ax.set_ylabel('mmHg')
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            return fig
        
        except Exception as e:
            print(f"Error plotting blood pressure: {str(e)}")
            return None
    
    def plot_heart_rate(self, data, title="Heart Rate Over Time"):
        """
        Plot heart rate over time.
        
        Args:
            data (pd.DataFrame): DataFrame containing health data
            title (str): Title for the plot
        """
        try:
            self._validate_data(data)
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # Plot heart rate
            ax.plot(data['date'], data['heart_rate'], label='Heart Rate', color='#2ca02c', marker='o')
            
            # Add healthy range indicators
            ax.axhline(y=60, color='#2ca02c', linestyle='--', alpha=0.3, label='Lower Normal')
            ax.axhline(y=100, color='#2ca02c', linestyle='--', alpha=0.3, label='Upper Normal')
            
            # Formatting
            ax.set_title(title, pad=20)
            ax.set_xlabel('Date')
            ax.set_ylabel('BPM')
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            return fig
        
        except Exception as e:
            print(f"Error plotting heart rate: {str(e)}")
            return None
    
    def plot_combined(self, data, title="Health Indicators"):
        """
        Plot both blood pressure and heart rate in subplots.
        
        Args:
            data (pd.DataFrame): DataFrame containing health data
            title (str): Title for the plot
        """
        try:
            self._validate_data(data)
            
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
            
            # Blood pressure plot
            ax1.plot(data['date'], data['systolic'], label='Systolic', color='#1f77b4', marker='o')
            ax1.plot(data['date'], data['diastolic'], label='Diastolic', color='#ff7f0e', marker='o')
            ax1.axhline(y=120, color='#1f77b4', linestyle='--', alpha=0.3, label='Normal Systolic')
            ax1.axhline(y=80, color='#ff7f0e', linestyle='--', alpha=0.3, label='Normal Diastolic')
            ax1.set_ylabel('mmHg')
            ax1.legend()
            
            # Heart rate plot
            ax2.plot(data['date'], data['heart_rate'], label='Heart Rate', color='#2ca02c', marker='o')
            ax2.axhline(y=60, color='#2ca02c', linestyle='--', alpha=0.3, label='Lower Normal')
            ax2.axhline(y=100, color='#2ca02c', linestyle='--', alpha=0.3, label='Upper Normal')
            ax2.set_ylabel('BPM')
            ax2.legend()
            
            # Formatting
            fig.suptitle(title, y=0.98)
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            return fig
        
        except Exception as e:
            print(f"Error plotting combined chart: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    # Sample data
    dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
    systolic = np.random.randint(110, 140, size=10)
    diastolic = np.random.randint(70, 90, size=10)
    heart_rate = np.random.randint(60, 100, size=10)
    
    data = pd.DataFrame({
        'date': dates,
        'systolic': systolic,
        'diastolic': diastolic,
        'heart_rate': heart_rate
    })
    
    # Create visualizer
    visualizer = HealthIndicatorVisualizer()
    
    # Generate plots
    bp_plot = visualizer.plot_blood_pressure(data)
    hr_plot = visualizer.plot_heart_rate(data)
    combined_plot = visualizer.plot_combined(data)
    
    # Show plots
    if bp_plot: plt.show(bp_plot)
    if hr_plot: plt.show(hr_plot)
    if combined_plot: plt.show(combined_plot)
```
