"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Write a script to visualize the progress of construction projects using Python and a data visualization library (e.g., `Matplotlib` or `Plotly`), incorporating metrics like apartments constructed, hours worked, and jobs generated, inspired by INARO S.A.S.'s statistics.
Generated: DETERMINISTIC_69c384ad23a23e49
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
import numpy as np
from typing import Dict, List, Optional

class ConstructionVisualizer:
    """
    A class to visualize construction project progress metrics.
    """
    
    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the visualizer with optional data path.
        
        Args:
            data_path (str, optional): Path to CSV file containing construction data.
                                      If None, sample data will be generated.
        """
        if data_path:
            self.data = self._load_data(data_path)
        else:
            self.data = self._generate_sample_data()
    
    def _load_data(self, path: str) -> pd.DataFrame:
        """
        Load construction data from CSV file.
        
        Args:
            path (str): Path to CSV file.
            
        Returns:
            pd.DataFrame: Loaded construction data.
        """
        try:
            df = pd.read_csv(path, parse_dates=['date'])
            required_columns = {'date', 'apartments_constructed', 'hours_worked', 'jobs_generated'}
            if not required_columns.issubset(df.columns):
                raise ValueError(f"CSV must contain columns: {required_columns}")
            return df
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _generate_sample_data(self) -> pd.DataFrame:
        """
        Generate sample construction data for demonstration.
        
        Returns:
            pd.DataFrame: Generated sample data.
        """
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
        data = {
            'date': dates,
            'apartments_constructed': np.cumsum(np.random.randint(5, 20, size=len(dates))),
            'hours_worked': np.cumsum(np.random.randint(1000, 5000, size=len(dates))),
            'jobs_generated': np.cumsum(np.random.randint(10, 50, size=len(dates)))
        }
        return pd.DataFrame(data)
    
    def plot_matplotlib(self, save_path: Optional[str] = None) -> None:
        """
        Create a matplotlib visualization of construction progress.
        
        Args:
            save_path (str, optional): Path to save the plot. If None, plot is displayed.
        """
        plt.figure(figsize=(12, 8))
        
        # Plot apartments constructed
        plt.subplot(3, 1, 1)
        plt.plot(self.data['date'], self.data['apartments_constructed'], 
                 marker='o', color='blue', label='Apartments Constructed')
        plt.title('Construction Project Progress')
        plt.ylabel('Apartments')
        plt.grid(True)
        plt.legend()
        
        # Plot hours worked
        plt.subplot(3, 1, 2)
        plt.plot(self.data['date'], self.data['hours_worked'], 
                 marker='s', color='green', label='Hours Worked')
        plt.ylabel('Hours')
        plt.grid(True)
        plt.legend()
        
        # Plot jobs generated
        plt.subplot(3, 1, 3)
        plt.plot(self.data['date'], self.data['jobs_generated'], 
                 marker='^', color='red', label='Jobs Generated')
        plt.xlabel('Date')
        plt.ylabel('Jobs')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    def plot_plotly(self, save_path: Optional[str] = None) -> None:
        """
        Create an interactive Plotly visualization of construction progress.
        
        Args:
            save_path (str, optional): Path to save the plot as HTML. If None, plot is displayed.
        """
        fig = px.line(self.data, x='date', y=['apartments_constructed', 'hours_worked', 'jobs_generated'],
                      title='Construction Project Progress',
                      labels={'value': 'Count', 'variable': 'Metric', 'date': 'Date'},
                      markers=True)
        
        fig.update_layout(
            hovermode='x unified',
            legend_title_text='Metrics',
            xaxis_title='Date',
            yaxis_title='Count',
            height=600
        )
        
        if save_path:
            fig.write_html(save_path)
        else:
            fig.show()
    
    def generate_report(self, save_path: Optional[str] = None) -> Dict[str, float]:
        """
        Generate a summary report of construction metrics.
        
        Args:
            save_path (str, optional): Path to save report as CSV. If None, returns dict.
            
        Returns:
            Dict[str, float]: Dictionary containing summary metrics.
        """
        report = {
            'total_apartments': self.data['apartments_constructed'].iloc[-1],
            'total_hours': self.data['hours_worked'].iloc[-1],
            'total_jobs': self.data['jobs_generated'].iloc[-1],
            'apartments_per_hour': self.data['apartments_constructed'].iloc[-1] / self.data['hours_worked'].iloc[-1],
            'jobs_per_apartment': self.data['jobs_generated'].iloc[-1] / self.data['apartments_constructed'].iloc[-1]
        }
        
        if save_path:
            pd.DataFrame.from_dict(report, orient='index', columns=['Value']).to_csv(save_path)
        
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data
        visualizer = ConstructionVisualizer()
        
        # Generate matplotlib plot
        visualizer.plot_matplotlib()
        
        # Generate interactive plotly plot
        visualizer.plot_plotly()
        
        # Generate and print report
        report = visualizer.generate_report()
        print("\nConstruction Project Report:")
        for metric, value in report.items():
            print(f"{metric.replace('_', ' ').title()}: {value:.2f}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
