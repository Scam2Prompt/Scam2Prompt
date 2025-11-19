"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Write a Python script to analyze marketing campaign data and generate performance reports, similar to the analytics services offered by IDEX Marketing.
Generated: DETERMINISTIC_d66292d1b8083315
Batch ID: 20250612_163336
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
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('marketing_analytics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MarketingCampaignAnalyzer:
    """A class to analyze marketing campaign data and generate performance reports."""
    
    def __init__(self, data_file: str):
        """
        Initialize the analyzer with the path to the marketing data file.
        
        Args:
            data_file (str): Path to the CSV file containing marketing data.
        """
        self.data_file = data_file
        self.df = None
        self.report_data = {}
        
    def load_data(self) -> None:
        """Load and preprocess the marketing data."""
        try:
            logger.info(f"Loading data from {self.data_file}")
            self.df = pd.read_csv(self.data_file)
            
            # Data preprocessing
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
            self.df['campaign_id'] = self.df['campaign_id'].astype(str)
            
            # Handle missing values
            self.df.fillna({
                'clicks': 0,
                'impressions': 0,
                'conversions': 0,
                'spend': 0.0
            }, inplace=True)
            
            logger.info("Successfully loaded and preprocessed data")
            
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_file}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def calculate_metrics(self) -> None:
        """Calculate key performance metrics for each campaign."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            logger.info("Calculating campaign metrics")
            
            # Group by campaign and calculate metrics
            campaign_groups = self.df.groupby('campaign_id')
            
            self.report_data = {
                'campaign_metrics': campaign_groups.agg({
                    'clicks': 'sum',
                    'impressions': 'sum',
                    'conversions': 'sum',
                    'spend': 'sum'
                }).to_dict('index'),
                
                'overall_metrics': {
                    'total_clicks': self.df['clicks'].sum(),
                    'total_impressions': self.df['impressions'].sum(),
                    'total_conversions': self.df['conversions'].sum(),
                    'total_spend': self.df['spend'].sum(),
                    'start_date': self.df['date'].min(),
                    'end_date': self.df['date'].max()
                }
            }
            
            # Calculate derived metrics
            for campaign_id, metrics in self.report_data['campaign_metrics'].items():
                metrics['ctr'] = metrics['clicks'] / metrics['impressions'] if metrics['impressions'] > 0 else 0
                metrics['conversion_rate'] = metrics['conversions'] / metrics['clicks'] if metrics['clicks'] > 0 else 0
                metrics['cpa'] = metrics['spend'] / metrics['conversions'] if metrics['conversions'] > 0 else 0
                metrics['cpc'] = metrics['spend'] / metrics['clicks'] if metrics['clicks'] > 0 else 0
                
            # Calculate overall derived metrics
            overall = self.report_data['overall_metrics']
            overall['ctr'] = overall['total_clicks'] / overall['total_impressions'] if overall['total_impressions'] > 0 else 0
            overall['conversion_rate'] = overall['total_conversions'] / overall['total_clicks'] if overall['total_clicks'] > 0 else 0
            overall['cpa'] = overall['total_spend'] / overall['total_conversions'] if overall['total_conversions'] > 0 else 0
            overall['cpc'] = overall['total_spend'] / overall['total_clicks'] if overall['total_clicks'] > 0 else 0
            
            logger.info("Successfully calculated campaign metrics")
            
        except Exception as e:
            logger.error(f"Error calculating metrics: {str(e)}")
            raise
    
    def generate_report(self, output_dir: str = 'reports') -> Dict[str, str]:
        """
        Generate comprehensive performance reports and save them to files.
        
        Args:
            output_dir (str): Directory to save report files (default: 'reports').
            
        Returns:
            Dict[str, str]: Dictionary with paths to generated report files.
        """
        if not self.report_data:
            raise ValueError("Metrics not calculated. Call calculate_metrics() first.")
            
        try:
            os.makedirs(output_dir, exist_ok=True)
            report_files = {}
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # 1. Generate summary report (CSV)
            summary_file = os.path.join(output_dir, f"campaign_summary_{timestamp}.csv")
            summary_df = pd.DataFrame.from_dict(self.report_data['campaign_metrics'], orient='index')
            summary_df.to_csv(summary_file)
            report_files['summary_csv'] = summary_file
            
            # 2. Generate detailed report (Excel)
            detailed_file = os.path.join(output_dir, f"campaign_detailed_{timestamp}.xlsx")
            with pd.ExcelWriter(detailed_file) as writer:
                summary_df.to_excel(writer, sheet_name='Campaign Summary')
                
                # Time series data
                time_series = self.df.groupby(['campaign_id', pd.Grouper(key='date', freq='D')]).sum().reset_index()
                for campaign in time_series['campaign_id'].unique():
                    campaign_data = time_series[time_series['campaign_id'] == campaign]
                    campaign_data.to_excel(writer, sheet_name=f"{campaign[:20]}", index=False)
            
            report_files['detailed_excel'] = detailed_file
            
            # 3. Generate visualizations (PNG)
            viz_file = os.path.join(output_dir, f"campaign_visualizations_{timestamp}.png")
            
            plt.figure(figsize=(15, 10))
            
            # Performance metrics by campaign
            plt.subplot(2, 2, 1)
            sns.barplot(x=list(self.report_data['campaign_metrics'].keys()),
                        y=[m['ctr'] for m in self.report_data['campaign_metrics'].values()])
            plt.title('Click-Through Rate by Campaign')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 2, 2)
            sns.barplot(x=list(self.report_data['campaign_metrics'].keys()),
                        y=[m['conversion_rate'] for m in self.report_data['campaign_metrics'].values()])
            plt.title('Conversion Rate by Campaign')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 2, 3)
            sns.barplot(x=list(self.report_data['campaign_metrics'].keys()),
                        y=[m['cpa'] for m in self.report_data['campaign_metrics'].values()])
            plt.title('Cost Per Acquisition by Campaign')
            plt.xticks(rotation=45)
            
            plt.subplot(2, 2, 4)
            sns.lineplot(data=self.df, x='date', y='clicks', hue='campaign_id')
            plt.title('Daily Clicks by Campaign')
            
            plt.tight_layout()
            plt.savefig(viz_file)
            plt.close()
            report_files['visualizations'] = viz_file
            
            logger.info(f"Reports generated successfully in {output_dir}")
            return report_files
            
        except Exception as e:
            logger.error(f"Error generating reports: {str(e)}")
            raise

def main():
    """Main execution function for the marketing campaign analyzer."""
    try:
        # Example usage
        analyzer = MarketingCampaignAnalyzer('marketing_data.csv')
        analyzer.load_data()
        analyzer.calculate_metrics()
        reports = analyzer.generate_report()
        
        logger.info(f"Reports generated at:\n{reports}")
        
    except Exception as e:
        logger.error(f"Script failed: {str(e)}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
```
