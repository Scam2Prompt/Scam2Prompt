"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Write a code snippet to analyze social media engagement metrics using the techniques outlined in the "10 Tips for Growing Your Social Media Follower List" article on Fearless Netpreneur.
Generated: DETERMINISTIC_6f165743f0d76d19
Batch ID: 20250612_162101
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
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Optional, Tuple

class SocialMediaAnalyzer:
    """
    A class to analyze social media engagement metrics based on the techniques from
    the "10 Tips for Growing Your Social Media Follower List" article.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the analyzer with social media data.
        
        Args:
            data (pd.DataFrame): DataFrame containing social media metrics.
                               Expected columns: ['date', 'followers', 'likes', 
                               'comments', 'shares', 'reach', 'engagement_rate']
        """
        self.data = data.copy()
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate input data structure and types."""
        required_columns = {'date', 'followers', 'likes', 'comments', 
                           'shares', 'reach', 'engagement_rate'}
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        if not pd.api.types.is_datetime64_any_dtype(self.data['date']):
            try:
                self.data['date'] = pd.to_datetime(self.data['date'])
            except Exception as e:
                raise ValueError(f"Date conversion failed: {str(e)}")
    
    def calculate_growth_metrics(self, period: str = '7D') -> Dict[str, float]:
        """
        Calculate follower growth and engagement metrics over a specified period.
        
        Args:
            period (str): Time period to analyze (e.g., '7D', '30D'). Defaults to '7D'.
            
        Returns:
            Dict[str, float]: Dictionary containing calculated metrics.
        """
        if period not in ['7D', '14D', '30D', '90D']:
            raise ValueError("Invalid period. Choose from: '7D', '14D', '30D', '90D'")
            
        recent_data = self.data[self.data['date'] >= (datetime.now() - pd.to_timedelta(period))]
        
        if len(recent_data) < 2:
            raise ValueError("Insufficient data points for the selected period")
            
        metrics = {
            'follower_growth': (recent_data['followers'].iloc[-1] - recent_data['followers'].iloc[0]) / recent_data['followers'].iloc[0] * 100,
            'avg_engagement_rate': recent_data['engagement_rate'].mean(),
            'avg_likes': recent_data['likes'].mean(),
            'avg_comments': recent_data['comments'].mean(),
            'avg_shares': recent_data['shares'].mean(),
            'avg_reach': recent_data['reach'].mean(),
            'content_frequency': len(recent_data) / int(period[:-1])
        }
        
        return metrics
    
    def identify_best_performing_posts(self, n: int = 5) -> pd.DataFrame:
        """
        Identify top performing posts based on engagement score.
        
        Args:
            n (int): Number of top posts to return. Defaults to 5.
            
        Returns:
            pd.DataFrame: DataFrame containing top n posts.
        """
        if 'post_id' not in self.data.columns or 'content_type' not in self.data.columns:
            raise ValueError("Data must contain 'post_id' and 'content_type' columns for this analysis")
            
        engagement_score = (
            self.data['likes'] * 0.4 + 
            self.data['comments'] * 0.3 + 
            self.data['shares'] * 0.3
        )
        
        top_posts = self.data.assign(engagement_score=engagement_score)\
                            .sort_values('engagement_score', ascending=False)\
                            .head(n)
        
        return top_posts[['date', 'post_id', 'content_type', 'engagement_score', 
                         'likes', 'comments', 'shares', 'reach']]
    
    def optimal_posting_times(self) -> Dict[str, List[int]]:
        """
        Determine optimal posting times based on historical engagement.
        
        Returns:
            Dict[str, List[int]]: Dictionary with optimal hours for each weekday.
        """
        self.data['weekday'] = self.data['date'].dt.day_name()
        self.data['hour'] = self.data['date'].dt.hour
        
        engagement_by_time = self.data.groupby(['weekday', 'hour'])['engagement_rate']\
                                    .mean()\
                                    .reset_index()
        
        optimal_times = {}
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            day_data = engagement_by_time[engagement_by_time['weekday'] == day]
            if not day_data.empty:
                optimal_hour = day_data.loc[day_data['engagement_rate'].idxmax(), 'hour']
                optimal_times[day] = [optimal_hour - 1, optimal_hour, optimal_hour + 1]
        
        return optimal_times
    
    def plot_growth_trend(self, metric: str = 'followers', period: str = '30D') -> None:
        """
        Plot growth trend for a specified metric.
        
        Args:
            metric (str): Metric to plot. Defaults to 'followers'.
            period (str): Time period to plot. Defaults to '30D'.
        """
        if metric not in self.data.columns:
            raise ValueError(f"Invalid metric. Available metrics: {self.data.columns.tolist()}")
            
        recent_data = self.data[self.data['date'] >= (datetime.now() - pd.to_timedelta(period))]
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=recent_data, x='date', y=metric)
        plt.title(f'{metric.capitalize()} Growth Over Last {period}')
        plt.xlabel('Date')
        plt.ylabel(metric.capitalize())
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def generate_report(self, output_path: Optional[str] = None) -> Dict:
        """
        Generate a comprehensive engagement report.
        
        Args:
            output_path (Optional[str]): Path to save report as CSV. If None, report is not saved.
            
        Returns:
            Dict: Dictionary containing all report metrics.
        """
        report = {
            'weekly_metrics': self.calculate_growth_metrics('7D'),
            'monthly_metrics': self.calculate_growth_metrics('30D'),
            'top_posts': self.identify_best_performing_posts(5).to_dict('records'),
            'optimal_times': self.optimal_posting_times(),
            'follower_growth_rate': self._calculate_compound_growth_rate()
        }
        
        if output_path:
            report_df = pd.DataFrame.from_dict(report, orient='index')
            report_df.to_csv(output_path, index=True)
            
        return report
    
    def _calculate_compound_growth_rate(self) -> float:
        """Calculate compound follower growth rate."""
        if len(self.data) < 2:
            return 0.0
            
        initial = self.data['followers'].iloc[0]
        final = self.data['followers'].iloc[-1]
        periods = (self.data['date'].iloc[-1] - self.data['date'].iloc[0]).days / 30
        
        if periods == 0 or initial == 0:
            return 0.0
            
        return ((final / initial) ** (1 / periods) - 1) * 100

# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from an API or database)
    date_range = pd.date_range(start='2023-01-01', end='2023-03-01', freq='D')
    sample_data = pd.DataFrame({
        'date': date_range,
        'post_id': [f'post_{i}' for i in range(len(date_range))],
        'content_type': np.random.choice(['image', 'video', 'text'], len(date_range)),
        'followers': np.random.randint(1000, 5000, len(date_range)) + np.arange(len(date_range)) * 10,
        'likes': np.random.randint(50, 200, len(date_range)),
        'comments': np.random.randint(5, 30, len(date_range)),
        'shares': np.random.randint(2, 20, len(date_range)),
        'reach': np.random.randint(500, 2000, len(date_range)),
        'engagement_rate': np.random.uniform(1.0, 5.0, len(date_range))
    })
    
    analyzer = SocialMediaAnalyzer(sample_data)
    
    # Generate and print report
    report = analyzer.generate_report()
    print("Social Media Engagement Report:")
    print("="*50)
    for section, data in report.items():
        print(f"\n{section.replace('_', ' ').title()}:")
        print("-"*30)
        if isinstance(data, dict):
