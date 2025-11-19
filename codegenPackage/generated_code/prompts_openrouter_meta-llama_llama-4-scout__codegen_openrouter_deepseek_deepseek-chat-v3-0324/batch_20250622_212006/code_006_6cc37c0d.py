"""
Generated Code Metadata:
========================
Original URL: https://fraud.grekrefunds.info
Prompt: Create a script to analyze and visualize scam trends, including types of scams (e.g., online scams, crypto scams, trading scams) and their corresponding recovery rates.
Generated: DETERMINISTIC_6cc37c0df15ccab2
Batch ID: 20250622_212006
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
from datetime import datetime
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

class ScamAnalyzer:
    """
    A class to analyze and visualize scam trends and recovery rates.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the ScamAnalyzer.
        
        Args:
            data_path (str, optional): Path to the scam data CSV file. Defaults to None.
        """
        self.data = None
        if data_path:
            self.load_data(data_path)
    
    def load_data(self, data_path):
        """
        Load scam data from a CSV file.
        
        Args:
            data_path (str): Path to the CSV file containing scam data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid CSV or missing required columns.
        """
        try:
            self.data = pd.read_csv(data_path)
            required_columns = ['scam_type', 'amount_lost', 'amount_recovered', 'date_reported']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError(f"CSV file must contain these columns: {required_columns}")
            
            # Convert date to datetime and calculate recovery rate
            self.data['date_reported'] = pd.to_datetime(self.data['date_reported'])
            self.data['recovery_rate'] = (self.data['amount_recovered'] / self.data['amount_lost']) * 100
            
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {data_path} does not exist.")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def get_scam_type_stats(self):
        """
        Calculate statistics by scam type.
        
        Returns:
            pandas.DataFrame: DataFrame with statistics for each scam type.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        stats = self.data.groupby('scam_type').agg(
            total_cases=('scam_type', 'count'),
            total_amount_lost=('amount_lost', 'sum'),
            total_amount_recovered=('amount_recovered', 'sum'),
            avg_recovery_rate=('recovery_rate', 'mean')
        ).reset_index()
        
        stats['avg_recovery_rate'] = stats['avg_recovery_rate'].round(2)
        return stats
    
    def plot_scam_trends(self, time_period='M'):
        """
        Plot scam trends over time.
        
        Args:
            time_period (str): Time period for grouping ('M' for month, 'Q' for quarter, 'Y' for year).
                              Defaults to 'M'.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        # Group by time period
        grouped = self.data.set_index('date_reported').groupby([pd.Grouper(freq=time_period), 'scam_type']).agg(
            cases=('scam_type', 'count'),
            amount_lost=('amount_lost', 'sum')
        ).reset_index()
        
        # Plot
        plt.figure(figsize=(14, 8))
        sns.lineplot(
            data=grouped,
            x='date_reported',
            y='cases',
            hue='scam_type',
            marker='o'
        )
        
        plt.title(f'Scam Cases Over Time (Grouped by {time_period})')
        plt.xlabel('Date')
        plt.ylabel('Number of Cases')
        plt.legend(title='Scam Type')
        plt.tight_layout()
        plt.show()
    
    def plot_recovery_rates(self):
        """
        Plot recovery rates by scam type.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        stats = self.get_scam_type_stats()
        
        plt.figure(figsize=(14, 8))
        sns.barplot(
            data=stats,
            x='scam_type',
            y='avg_recovery_rate',
            palette='viridis'
        )
        
        plt.title('Average Recovery Rate by Scam Type')
        plt.xlabel('Scam Type')
        plt.ylabel('Average Recovery Rate (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def plot_amounts_comparison(self):
        """
        Plot comparison of amounts lost vs recovered by scam type.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        stats = self.get_scam_type_stats()
        
        # Melt the data for easier plotting
        melted = stats.melt(
            id_vars=['scam_type'],
            value_vars=['total_amount_lost', 'total_amount_recovered'],
            var_name='amount_type',
            value_name='amount'
        )
        
        plt.figure(figsize=(14, 8))
        sns.barplot(
            data=melted,
            x='scam_type',
            y='amount',
            hue='amount_type',
            palette=['#ff6b6b', '#51cf66']
        )
        
        plt.title('Total Amount Lost vs Recovered by Scam Type')
        plt.xlabel('Scam Type')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.legend(title='Amount Type')
        plt.tight_layout()
        plt.show()
    
    def generate_report(self, output_file='scam_analysis_report.html'):
        """
        Generate an HTML report with all visualizations.
        
        Args:
            output_file (str): Path to save the HTML report. Defaults to 'scam_analysis_report.html'.
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
            
        from matplotlib.backends.backend_pdf import PdfPages
        
        with PdfPages(output_file.replace('.html', '.pdf')) as pdf:
            # Scam trends plot
            self.plot_scam_trends()
            pdf.savefig()
            plt.close()
            
            # Recovery rates plot
            self.plot_recovery_rates()
            pdf.savefig()
            plt.close()
            
            # Amounts comparison plot
            self.plot_amounts_comparison()
            pdf.savefig()
            plt.close()
            
        # Also save stats to CSV
        stats = self.get_scam_type_stats()
        stats.to_csv(output_file.replace('.html', '_stats.csv'), index=False)

# Example usage
if __name__ == "__main__":
    try:
        analyzer = ScamAnalyzer('scam_data.csv')  # Replace with your data file path
        analyzer.plot_scam_trends()
        analyzer.plot_recovery_rates()
        analyzer.plot_amounts_comparison()
        analyzer.generate_report()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
