"""
Generated Code Metadata:
========================
Original URL: https://evamobi.com
Prompt: "Create a full-funnel app promotion analysis template using metrics improvement and creative production techniques."
Generated: DETERMINISTIC_cf60ed81cbdc2970
Batch ID: 20250622_204803
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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class CampaignMetrics:
    """Dataclass to store campaign performance metrics"""
    impressions: int
    clicks: int
    installs: int
    registrations: int
    purchases: int
    revenue: float
    creative_id: str
    campaign_id: str
    date: str

class PromotionAnalyzer:
    """Main class for app promotion analysis"""
    
    def __init__(self, data: List[CampaignMetrics]):
        """
        Initialize analyzer with campaign data
        
        Args:
            data: List of CampaignMetrics objects
        """
        self.data = data
        self.df = self._prepare_dataframe()
        
    def _prepare_dataframe(self) -> pd.DataFrame:
        """Convert list of CampaignMetrics to pandas DataFrame"""
        try:
            df = pd.DataFrame([vars(item) for item in self.data])
            df['date'] = pd.to_datetime(df['date'])
            df['ctr'] = df['clicks'] / df['impressions']
            df['conversion_rate'] = df['installs'] / df['clicks']
            df['registration_rate'] = df['registrations'] / df['installs']
            df['purchase_rate'] = df['purchases'] / df['registrations']
            df['roas'] = df['revenue'] / (df['clicks'] * 0.1)  # Assuming $0.1 CPC
            return df
        except Exception as e:
            logger.error(f"Error preparing dataframe: {e}")
            raise
            
    def get_funnel_metrics(self) -> Dict[str, float]:
        """Calculate average funnel metrics across all campaigns"""
        try:
            return {
                'avg_ctr': self.df['ctr'].mean(),
                'avg_conversion_rate': self.df['conversion_rate'].mean(),
                'avg_registration_rate': self.df['registration_rate'].mean(),
                'avg_purchase_rate': self.df['purchase_rate'].mean(),
                'avg_roas': self.df['roas'].mean()
            }
        except Exception as e:
            logger.error(f"Error calculating funnel metrics: {e}")
            raise
            
    def plot_funnel(self) -> None:
        """Visualize the conversion funnel"""
        try:
            funnel_data = self.get_funnel_metrics()
            stages = ['CTR', 'Install', 'Register', 'Purchase']
            rates = [
                funnel_data['avg_ctr'],
                funnel_data['avg_conversion_rate'],
                funnel_data['avg_registration_rate'],
                funnel_data['avg_purchase_rate']
            ]
            
            plt.figure(figsize=(10, 6))
            sns.barplot(x=stages, y=rates, palette='viridis')
            plt.title('App Promotion Conversion Funnel')
            plt.ylabel('Conversion Rate')
            plt.ylim(0, 1)
            plt.show()
        except Exception as e:
            logger.error(f"Error plotting funnel: {e}")
            raise
            
    def compare_creatives(self) -> pd.DataFrame:
        """Compare performance across different creatives"""
        try:
            return self.df.groupby('creative_id').agg({
                'ctr': 'mean',
                'conversion_rate': 'mean',
                'registration_rate': 'mean',
                'purchase_rate': 'mean',
                'roas': 'mean'
            }).sort_values('roas', ascending=False)
        except Exception as e:
            logger.error(f"Error comparing creatives: {e}")
            raise
            
    def time_series_analysis(self, metric: str = 'roas') -> None:
        """
        Plot metric over time
        
        Args:
            metric: Metric to plot (default: 'roas')
        """
        try:
            if metric not in self.df.columns:
                raise ValueError(f"Metric {metric} not found in data")
                
            plt.figure(figsize=(12, 6))
            sns.lineplot(
                data=self.df,
                x='date',
                y=metric,
                hue='campaign_id',
                marker='o'
            )
            plt.title(f'{metric.upper()} Over Time')
            plt.xticks(rotation=45)
            plt.show()
        except Exception as e:
            logger.error(f"Error in time series analysis: {e}")
            raise
            
    def get_improvement_recommendations(self) -> Dict[str, str]:
        """Generate recommendations for improving campaign performance"""
        try:
            recommendations = {}
            funnel = self.get_funnel_metrics()
            
            if funnel['avg_ctr'] < 0.02:
                recommendations['ctr'] = "Test new ad creatives and headlines to improve CTR"
            if funnel['avg_conversion_rate'] < 0.3:
                recommendations['conversion'] = "Optimize landing page and simplify install flow"
            if funnel['avg_registration_rate'] < 0.5:
                recommendations['registration'] = "Implement social login and reduce form fields"
            if funnel['avg_purchase_rate'] < 0.1:
                recommendations['purchase'] = "Add incentives and improve onboarding flow"
            if funnel['avg_roas'] < 2.0:
                recommendations['roas'] = "Refine targeting and test higher-value audience segments"
                
            return recommendations
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = [
        CampaignMetrics(
            impressions=10000,
            clicks=200,
            installs=60,
            registrations=30,
            purchases=6,
            revenue=120.0,
            creative_id="creative_1",
            campaign_id="campaign_1",
            date="2023-01-01"
        ),
        CampaignMetrics(
            impressions=15000,
            clicks=450,
            installs=135,
            registrations=68,
            purchases=20,
            revenue=400.0,
            creative_id="creative_2",
            campaign_id="campaign_1",
            date="2023-01-02"
        ),
        CampaignMetrics(
            impressions=8000,
            clicks=160,
            installs=48,
            registrations=24,
            purchases=4,
            revenue=80.0,
            creative_id="creative_1",
            campaign_id="campaign_2",
            date="2023-01-01"
        ),
    ]
    
    analyzer = PromotionAnalyzer(sample_data)
    
    # Print funnel metrics
    print("Funnel Metrics:")
    print(analyzer.get_funnel_metrics())
    
    # Plot funnel
    analyzer.plot_funnel()
    
    # Compare creatives
    print("\nCreative Performance:")
    print(analyzer.compare_creatives())
    
    # Time series analysis
    analyzer.time_series_analysis('roas')
    
    # Get recommendations
    print("\nImprovement Recommendations:")
    for k, v in analyzer.get_improvement_recommendations().items():
        print(f"{k}: {v}")
```
