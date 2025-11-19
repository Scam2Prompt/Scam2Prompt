"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Write a script to generate reports on cyberharassment awareness campaigns, similar to those conducted by Sophia Loisirs & Vie, including data visualization using Matplotlib or Seaborn.
Generated: DETERMINISTIC_11428879c8ad82c7
Batch ID: 20250612_153224
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
import os

# Constants
REPORT_DIR = "reports"
DATA_FILE = "campaign_data.csv"
PLOT_STYLE = "seaborn"
COLOR_PALETTE = "viridis"

# Ensure report directory exists
os.makedirs(REPORT_DIR, exist_ok=True)

class CampaignAnalyzer:
    """
    Analyzes and visualizes cyberharassment awareness campaign data.
    """
    
    def __init__(self, data_file=DATA_FILE):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_file (str): Path to CSV file containing campaign data
        """
        try:
            self.data = pd.read_csv(data_file)
            self._validate_data()
            self._preprocess_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {data_file} not found")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self):
        """Validate the structure of the loaded data."""
        required_columns = {
            'campaign_name', 'start_date', 'end_date', 
            'platform', 'reach', 'engagement', 
            'reports_received', 'resources_shared'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def _preprocess_data(self):
        """Clean and preprocess the data."""
        # Convert dates
        self.data['start_date'] = pd.to_datetime(self.data['start_date'])
        self.data['end_date'] = pd.to_datetime(self.data['end_date'])
        
        # Calculate duration
        self.data['duration_days'] = (self.data['end_date'] - self.data['start_date']).dt.days
        
        # Calculate engagement rate
        self.data['engagement_rate'] = (self.data['engagement'] / self.data['reach']) * 100
        
        # Fill missing values
        self.data.fillna({
            'reports_received': 0,
            'resources_shared': 0,
            'engagement': 0
        }, inplace=True)
    
    def generate_summary_report(self):
        """Generate a summary report of all campaigns."""
        summary = self.data.groupby('campaign_name').agg({
            'reach': 'sum',
            'engagement': 'sum',
            'reports_received': 'sum',
            'resources_shared': 'sum',
            'duration_days': 'mean',
            'engagement_rate': 'mean'
        }).reset_index()
        
        return summary
    
    def plot_engagement_by_platform(self, save=False):
        """Plot engagement metrics by platform."""
        plt.style.use(PLOT_STYLE)
        plt.figure(figsize=(10, 6))
        
        ax = sns.barplot(
            data=self.data,
            x='platform',
            y='engagement',
            estimator=sum,
            ci=None,
            palette=COLOR_PALETTE
        )
        
        plt.title('Total Engagement by Platform')
        plt.xlabel('Platform')
        plt.ylabel('Engagement Count')
        plt.xticks(rotation=45)
        
        if save:
            filename = os.path.join(REPORT_DIR, f"engagement_by_platform_{datetime.now().strftime('%Y%m%d')}.png")
            plt.savefig(filename, bbox_inches='tight', dpi=300)
            plt.close()
            return filename
        else:
            plt.show()
    
    def plot_reports_vs_resources(self, save=False):
        """Plot relationship between reports received and resources shared."""
        plt.style.use(PLOT_STYLE)
        plt.figure(figsize=(10, 6))
        
        ax = sns.scatterplot(
            data=self.data,
            x='resources_shared',
            y='reports_received',
            hue='platform',
            size='reach',
            sizes=(20, 200),
            palette=COLOR_PALETTE
        )
        
        plt.title('Reports Received vs Resources Shared')
        plt.xlabel('Resources Shared')
        plt.ylabel('Reports Received')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        if save:
            filename = os.path.join(REPORT_DIR, f"reports_vs_resources_{datetime.now().strftime('%Y%m%d')}.png")
            plt.savefig(filename, bbox_inches='tight', dpi=300)
            plt.close()
            return filename
        else:
            plt.show()
    
    def plot_engagement_trend(self, save=False):
        """Plot engagement trend over time."""
        plt.style.use(PLOT_STYLE)
        plt.figure(figsize=(12, 6))
        
        # Aggregate by month
        monthly_data = self.data.set_index('start_date').resample('M').sum().reset_index()
        
        ax = sns.lineplot(
            data=monthly_data,
            x='start_date',
            y='engagement',
            marker='o',
            color=sns.color_palette(COLOR_PALETTE)[0]
        )
        
        plt.title('Monthly Engagement Trend')
        plt.xlabel('Month')
        plt.ylabel('Engagement Count')
        plt.xticks(rotation=45)
        
        if save:
            filename = os.path.join(REPORT_DIR, f"engagement_trend_{datetime.now().strftime('%Y%m%d')}.png")
            plt.savefig(filename, bbox_inches='tight', dpi=300)
            plt.close()
            return filename
        else:
            plt.show()
    
    def generate_full_report(self):
        """Generate a comprehensive report with all visualizations."""
        report = {
            'summary': self.generate_summary_report(),
            'engagement_by_platform': self.plot_engagement_by_platform(save=True),
            'reports_vs_resources': self.plot_reports_vs_resources(save=True),
            'engagement_trend': self.plot_engagement_trend(save=True)
        }
        
        # Save summary to CSV
        summary_file = os.path.join(REPORT_DIR, f"summary_report_{datetime.now().strftime('%Y%m%d')}.csv")
        report['summary'].to_csv(summary_file, index=False)
        report['summary_file'] = summary_file
        
        return report

def main():
    """Main function to execute the report generation."""
    try:
        analyzer = CampaignAnalyzer()
        report = analyzer.generate_full_report()
        
        print("Report generated successfully!")
        print(f"Summary saved to: {report['summary_file']}")
        print(f"Visualizations saved to: {REPORT_DIR}")
        
    except Exception as e:
        print(f"Error generating report: {str(e)}")

if __name__ == "__main__":
    main()
```
