"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: Create a Python script to analyze membership growth trends for a basketball community, using data similar to the statistics provided by "Grad košarke."
Generated: DETERMINISTIC_29e5ed31c1940531
Batch ID: 20250612_152739
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
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('membership_analysis.log'),
        logging.StreamHandler()
    ]
)

class MembershipAnalyzer:
    """Analyze membership growth trends for a basketball community."""
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing membership data.
        """
        self.data_path = data_path
        self.data = None
        self._load_data()
        
    def _load_data(self) -> None:
        """Load and preprocess the membership data."""
        try:
            self.data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully.")
            
            # Convert date column to datetime if exists
            if 'date' in self.data.columns:
                self.data['date'] = pd.to_datetime(self.data['date'])
                self.data.sort_values('date', inplace=True)
                
            # Basic data validation
            required_columns = ['members', 'date']
            for col in required_columns:
                if col not in self.data.columns:
                    raise ValueError(f"Missing required column: {col}")
                    
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise
            
    def calculate_growth_rate(self, period: str = 'M') -> pd.DataFrame:
        """
        Calculate membership growth rate over time.
        
        Args:
            period (str): Time period for resampling ('M' for monthly, 'Y' for yearly).
                         Default is monthly.
                         
        Returns:
            pd.DataFrame: DataFrame with growth rate statistics.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call _load_data() first.")
            
        try:
            resampled = self.data.set_index('date').resample(period)
            
            # Calculate growth metrics
            growth = resampled['members'].agg(['sum', 'mean', 'std'])
            growth['growth_rate'] = growth['sum'].pct_change() * 100
            growth['cumulative_growth'] = growth['sum'].cumsum()
            
            return growth.dropna()
            
        except Exception as e:
            logging.error(f"Error calculating growth rate: {str(e)}")
            raise
            
    def plot_growth_trends(self, growth_data: pd.DataFrame, output_path: Optional[str] = None) -> None:
        """
        Plot membership growth trends.
        
        Args:
            growth_data (pd.DataFrame): Growth data from calculate_growth_rate()
            output_path (str, optional): Path to save the plot. If None, shows the plot.
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot cumulative growth
            plt.subplot(1, 2, 1)
            plt.plot(growth_data.index, growth_data['cumulative_growth'], 'b-')
            plt.title('Cumulative Membership Growth')
            plt.xlabel('Date')
            plt.ylabel('Total Members')
            plt.grid(True)
            
            # Plot growth rate
            plt.subplot(1, 2, 2)
            plt.bar(growth_data.index, growth_data['growth_rate'], color='g', alpha=0.7)
            plt.title('Monthly Growth Rate (%)')
            plt.xlabel('Date')
            plt.ylabel('Growth Rate %')
            plt.grid(True)
            
            plt.tight_layout()
            
            if output_path:
                plt.savefig(output_path)
                logging.info(f"Plot saved to {output_path}")
            else:
                plt.show()
                
        except Exception as e:
            logging.error(f"Error plotting growth trends: {str(e)}")
            raise
            
    def generate_report(self, output_path: str = 'growth_report.txt') -> None:
        """
        Generate a text report with key growth statistics.
        
        Args:
            output_path (str): Path to save the report.
        """
        try:
            growth_data = self.calculate_growth_rate()
            
            with open(output_path, 'w') as f:
                f.write("Basketball Community Membership Growth Report\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("Summary Statistics:\n")
                f.write(f"Total members: {int(growth_data['sum'].sum())}\n")
                f.write(f"Average monthly growth: {growth_data['growth_rate'].mean():.2f}%\n")
                f.write(f"Peak growth month: {growth_data['growth_rate'].idxmax().strftime('%Y-%m')} "
                       f"({growth_data['growth_rate'].max():.2f}%)\n\n")
                
                f.write("Monthly Growth Data:\n")
                f.write(growth_data.to_string())
                
            logging.info(f"Report generated at {output_path}")
            
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        analyzer = MembershipAnalyzer('basketball_membership.csv')
        
        # Analyze and visualize growth
        growth_data = analyzer.calculate_growth_rate()
        analyzer.plot_growth_trends(growth_data, 'growth_trends.png')
        
        # Generate report
        analyzer.generate_report()
        
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
```
