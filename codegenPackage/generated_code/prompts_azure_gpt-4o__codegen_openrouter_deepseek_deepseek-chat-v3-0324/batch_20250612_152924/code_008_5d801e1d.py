"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Write a program to visualize the impact of community-driven funding on education initiatives like Uni4Kashmir, using data analytics libraries.
Generated: DETERMINISTIC_5d801e1d25fb43cb
Batch ID: 20250612_152924
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

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class EducationFundingVisualizer:
    """
    A class to visualize the impact of community-driven funding on education initiatives.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the visualizer with optional data path.
        
        Args:
            data_path (str, optional): Path to CSV file containing funding data. 
                                      If None, generates synthetic data.
        """
        self.data_path = data_path
        self.data = None
        self._load_data()
        
    def _load_data(self):
        """
        Load data from CSV or generate synthetic data if no path provided.
        """
        if self.data_path:
            try:
                self.data = pd.read_csv(self.data_path)
                self._validate_data()
            except FileNotFoundError:
                raise FileNotFoundError(f"Data file not found at {self.data_path}")
            except Exception as e:
                raise Exception(f"Error loading data: {str(e)}")
        else:
            self._generate_synthetic_data()
            
    def _validate_data(self):
        """
        Validate the loaded data has required columns.
        """
        required_columns = ['date', 'amount', 'initiative', 'students_impacted']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")
                
    def _generate_synthetic_data(self):
        """
        Generate synthetic data for demonstration purposes.
        """
        np.random.seed(42)
        date_range = pd.date_range(start='2020-01-01', end='2023-12-31', freq='M')
        initiatives = ['Uni4Kashmir', 'EducationForAll', 'Tech4Students', 'LiteracyDrive']
        
        data = {
            'date': np.random.choice(date_range, 200),
            'amount': np.random.randint(1000, 50000, 200),
            'initiative': np.random.choice(initiatives, 200),
            'students_impacted': np.random.randint(5, 500, 200)
        }
        
        self.data = pd.DataFrame(data)
        self.data['date'] = pd.to_datetime(self.data['date'])
        
    def _prepare_data(self):
        """
        Prepare data for visualization by aggregating and calculating metrics.
        """
        # Calculate cumulative funding and impact over time
        self.data['cumulative_funding'] = self.data.groupby('initiative')['amount'].cumsum()
        self.data['cumulative_students'] = self.data.groupby('initiative')['students_impacted'].cumsum()
        
        # Calculate funding efficiency (students per dollar)
        self.data['funding_efficiency'] = self.data['students_impacted'] / self.data['amount']
        
    def plot_funding_trends(self):
        """
        Plot funding trends over time for all initiatives.
        """
        self._prepare_data()
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            data=self.data,
            x='date',
            y='cumulative_funding',
            hue='initiative',
            estimator='sum',
            errorbar=None
        )
        plt.title('Community Funding Growth Over Time')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Funding ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    def plot_impact_vs_funding(self):
        """
        Plot students impacted versus funding amount.
        """
        self._prepare_data()
        
        plt.figure(figsize=(12, 6))
        sns.scatterplot(
            data=self.data,
            x='amount',
            y='students_impacted',
            hue='initiative',
            size='funding_efficiency',
            sizes=(20, 200),
            alpha=0.7
        )
        plt.title('Students Impacted vs Funding Amount')
        plt.xlabel('Funding Amount ($)')
        plt.ylabel('Students Impacted')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    def plot_funding_efficiency(self):
        """
        Plot funding efficiency (students per dollar) by initiative.
        """
        self._prepare_data()
        
        plt.figure(figsize=(12, 6))
        sns.boxplot(
            data=self.data,
            x='initiative',
            y='funding_efficiency'
        )
        plt.title('Funding Efficiency by Initiative')
        plt.xlabel('Initiative')
        plt.ylabel('Students Impacted per Dollar')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    def plot_summary_stats(self):
        """
        Plot summary statistics of funding and impact.
        """
        self._prepare_data()
        
        # Create summary dataframe
        summary = self.data.groupby('initiative').agg({
            'amount': ['sum', 'mean', 'count'],
            'students_impacted': 'sum',
            'funding_efficiency': 'mean'
        }).reset_index()
        
        summary.columns = ['initiative', 'total_funding', 'avg_funding', 
                          'donation_count', 'total_students', 'avg_efficiency']
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Total Funding
        sns.barplot(data=summary, x='initiative', y='total_funding', ax=axes[0, 0])
        axes[0, 0].set_title('Total Funding by Initiative')
        axes[0, 0].set_ylabel('Total Funding ($)')
        
        # Total Students Impacted
        sns.barplot(data=summary, x='initiative', y='total_students', ax=axes[0, 1])
        axes[0, 1].set_title('Total Students Impacted')
        axes[0, 1].set_ylabel('Students Impacted')
        
        # Average Funding Efficiency
        sns.barplot(data=summary, x='initiative', y='avg_efficiency', ax=axes[1, 0])
        axes[1, 0].set_title('Average Funding Efficiency')
        axes[1, 0].set_ylabel('Students per Dollar')
        
        # Donation Count
        sns.barplot(data=summary, x='initiative', y='donation_count', ax=axes[1, 1])
        axes[1, 1].set_title('Number of Donations')
        axes[1, 1].set_ylabel('Donation Count')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with synthetic data (or provide path to real data)
        visualizer = EducationFundingVisualizer()
        
        # Generate and display visualizations
        visualizer.plot_funding_trends()
        visualizer.plot_impact_vs_funding()
        visualizer.plot_funding_efficiency()
        visualizer.plot_summary_stats()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
