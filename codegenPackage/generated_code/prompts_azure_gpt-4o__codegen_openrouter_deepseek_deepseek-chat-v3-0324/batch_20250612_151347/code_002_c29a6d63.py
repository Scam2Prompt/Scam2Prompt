"""
Generated Code Metadata:
========================
Original URL: https://evamobi.com
Prompt: Generate code to analyze the effectiveness of a full-funnel app promotion campaign, including metrics like CR (conversion rate) and D1RR (day-one retention rate), as mentioned in Evamobi's case studies.
Generated: DETERMINISTIC_c29a6d637cab6c35
Batch ID: 20250612_151347
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
from typing import Dict, Tuple, List, Optional

class CampaignAnalyzer:
    """
    Analyzes the effectiveness of a full-funnel app promotion campaign.
    Calculates key metrics like Conversion Rate (CR) and Day-One Retention Rate (D1RR).
    """
    
    def __init__(self, campaign_data: pd.DataFrame):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            campaign_data: DataFrame containing campaign metrics with columns:
                - 'impressions': Number of ad impressions
                - 'clicks': Number of clicks on ads
                - 'installs': Number of app installs
                - 'd1_active_users': Number of users active on day 1
                - 'campaign_name': Name of the campaign (optional)
                - 'date': Date of the data point (optional)
        """
        self.data = campaign_data.copy()
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate input data structure and values."""
        required_columns = {'impressions', 'clicks', 'installs', 'd1_active_users'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Input data must contain columns: {required_columns}")
            
        if (self.data[['impressions', 'clicks', 'installs', 'd1_active_users']] < 0).any().any():
            raise ValueError("Metrics cannot contain negative values")
            
    def calculate_cr(self) -> pd.Series:
        """
        Calculate Conversion Rate (CR) from impressions to installs.
        
        Returns:
            Series with CR values (as percentages)
        """
        return (self.data['installs'] / self.data['impressions']) * 100
    
    def calculate_ctr(self) -> pd.Series:
        """
        Calculate Click-Through Rate (CTR) from impressions to clicks.
        
        Returns:
            Series with CTR values (as percentages)
        """
        return (self.data['clicks'] / self.data['impressions']) * 100
    
    def calculate_d1rr(self) -> pd.Series:
        """
        Calculate Day-One Retention Rate (D1RR).
        
        Returns:
            Series with D1RR values (as percentages)
        """
        return (self.data['d1_active_users'] / self.data['installs']) * 100
    
    def calculate_all_metrics(self) -> pd.DataFrame:
        """
        Calculate all key metrics (CR, CTR, D1RR) and return as DataFrame.
        
        Returns:
            DataFrame with original data plus calculated metrics
        """
        results = self.data.copy()
        results['cr'] = self.calculate_cr()
        results['ctr'] = self.calculate_ctr()
        results['d1rr'] = self.calculate_d1rr()
        return results
    
    def plot_metrics(self, metric: str, group_by: Optional[str] = None) -> plt.Figure:
        """
        Plot a specified metric over time or grouped by another column.
        
        Args:
            metric: One of 'cr', 'ctr', or 'd1rr'
            group_by: Column to group by (e.g., 'campaign_name' or 'date')
            
        Returns:
            Matplotlib Figure object
        """
        valid_metrics = {'cr', 'ctr', 'd1rr'}
        if metric not in valid_metrics:
            raise ValueError(f"Invalid metric. Must be one of: {valid_metrics}")
            
        df = self.calculate_all_metrics()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if group_by:
            if group_by not in df.columns:
                raise ValueError(f"Column '{group_by}' not found in data")
            df.groupby(group_by)[metric].mean().plot(kind='bar', ax=ax)
            ax.set_title(f"Average {metric.upper()} by {group_by}")
        else:
            if 'date' in df.columns:
                df.set_index('date')[metric].plot(ax=ax)
                ax.set_title(f"{metric.upper()} Over Time")
            else:
                df[metric].plot(kind='bar', ax=ax)
                ax.set_title(f"{metric.upper()} Distribution")
                
        ax.set_ylabel(f"{metric.upper()} (%)")
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        return fig
    
    def get_summary_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate summary statistics for all metrics.
        
        Returns:
            Dictionary with metric names as keys and dicts of statistics as values
        """
        df = self.calculate_all_metrics()
        metrics = ['cr', 'ctr', 'd1rr']
        
        stats = {}
        for metric in metrics:
            stats[metric] = {
                'mean': df[metric].mean(),
                'median': df[metric].median(),
                'std': df[metric].std(),
                'min': df[metric].min(),
                'max': df[metric].max()
            }
            
        return stats

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from a database or CSV)
    data = pd.DataFrame({
        'date': pd.date_range('2023-01-01', periods=7),
        'campaign_name': ['Campaign A']*3 + ['Campaign B']*4,
        'impressions': [10000, 12000, 15000, 8000, 9000, 11000, 13000],
        'clicks': [500, 600, 750, 400, 450, 550, 650],
        'installs': [250, 300, 375, 200, 225, 275, 325],
        'd1_active_users': [200, 240, 300, 160, 180, 220, 260]
    })
    
    analyzer = CampaignAnalyzer(data)
    
    # Calculate and print all metrics
    results = analyzer.calculate_all_metrics()
    print("Metrics Data:")
    print(results)
    
    # Get summary statistics
    stats = analyzer.get_summary_stats()
    print("\nSummary Statistics:")
    for metric, values in stats.items():
        print(f"{metric.upper()}: {values}")
    
    # Plot metrics
    analyzer.plot_metrics('cr', group_by='campaign_name')
    analyzer.plot_metrics('d1rr')
    plt.show()
```
