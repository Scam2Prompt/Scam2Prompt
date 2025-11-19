"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Write Python code to analyze user engagement metrics for newsletters and blogs, similar to the ALPS Foundation's monthly updates system.
Generated: DETERMINISTIC_e41fedd956fe8a7f
Batch ID: 20250612_151126
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
import logging
from typing import Dict, List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('engagement_metrics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EngagementAnalyzer:
    """
    Analyzes user engagement metrics for newsletters and blogs.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data path.
        
        Args:
            data_path: Path to the CSV file containing engagement data
        """
        self.data_path = data_path
        self.data = None
        self.metrics = None
        
    def load_data(self) -> None:
        """
        Load and preprocess engagement data from CSV.
        
        Raises:
            FileNotFoundError: If data file doesn't exist
            ValueError: If data is malformed
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logger.info(f"Successfully loaded data from {self.data_path}")
            
            # Basic data validation
            required_columns = ['user_id', 'content_type', 'date', 'time_spent', 'clicks', 'opens']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError(f"Missing required columns. Expected: {required_columns}")
                
            # Convert date to datetime
            self.data['date'] = pd.to_datetime(self.data['date'])
            
            # Calculate additional metrics
            self.data['engagement_score'] = (
                0.4 * self.data['time_spent'] / self.data['time_spent'].max() +
                0.3 * self.data['clicks'] / self.data['clicks'].max() +
                0.3 * self.data['opens'] / self.data['opens'].max()
            )
            
        except FileNotFoundError as e:
            logger.error(f"Data file not found: {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Data loading failed: {str(e)}")
    
    def calculate_metrics(self) -> Dict[str, Dict]:
        """
        Calculate key engagement metrics.
        
        Returns:
            Dictionary containing calculated metrics
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        metrics = {
            'overall': {},
            'by_content_type': {},
            'by_time_period': {}
        }
        
        try:
            # Overall metrics
            metrics['overall']['avg_time_spent'] = self.data['time_spent'].mean()
            metrics['overall']['avg_clicks'] = self.data['clicks'].mean()
            metrics['overall']['avg_opens'] = self.data['opens'].mean()
            metrics['overall']['total_users'] = self.data['user_id'].nunique()
            metrics['overall']['engagement_score'] = self.data['engagement_score'].mean()
            
            # By content type
            for content_type, group in self.data.groupby('content_type'):
                metrics['by_content_type'][content_type] = {
                    'avg_time_spent': group['time_spent'].mean(),
                    'avg_clicks': group['clicks'].mean(),
                    'avg_opens': group['opens'].mean(),
                    'user_count': group['user_id'].nunique(),
                    'engagement_score': group['engagement_score'].mean()
                }
            
            # By time period (monthly)
            self.data['month'] = self.data['date'].dt.to_period('M')
            for month, group in self.data.groupby('month'):
                metrics['by_time_period'][str(month)] = {
                    'avg_time_spent': group['time_spent'].mean(),
                    'avg_clicks': group['clicks'].mean(),
                    'avg_opens': group['opens'].mean(),
                    'user_count': group['user_id'].nunique(),
                    'engagement_score': group['engagement_score'].mean()
                }
                
            self.metrics = metrics
            logger.info("Successfully calculated engagement metrics")
            return metrics
            
        except Exception as e:
            logger.error(f"Error calculating metrics: {str(e)}")
            raise
            
    def generate_report(self, output_path: Optional[str] = None) -> None:
        """
        Generate a visual report of engagement metrics.
        
        Args:
            output_path: Path to save the report. If None, displays the report.
        """
        if self.metrics is None:
            raise ValueError("Metrics not calculated. Call calculate_metrics() first.")
            
        try:
            plt.figure(figsize=(15, 10))
            
            # Content type comparison
            plt.subplot(2, 2, 1)
            content_types = list(self.metrics['by_content_type'].keys())
            engagement_scores = [v['engagement_score'] for v in self.metrics['by_content_type'].values()]
            plt.bar(content_types, engagement_scores)
            plt.title('Engagement by Content Type')
            plt.ylabel('Engagement Score')
            
            # Monthly trends
            plt.subplot(2, 2, 2)
            months = list(self.metrics['by_time_period'].keys())
            monthly_engagement = [v['engagement_score'] for v in self.metrics['by_time_period'].values()]
            plt.plot(months, monthly_engagement, marker='o')
            plt.title('Monthly Engagement Trend')
            plt.ylabel('Engagement Score')
            plt.xticks(rotation=45)
            
            # Time spent distribution
            plt.subplot(2, 2, 3)
            plt.hist(self.data['time_spent'], bins=20)
            plt.title('Time Spent Distribution')
            plt.xlabel('Time Spent (seconds)')
            plt.ylabel('Frequency')
            
            # Opens vs Clicks scatter
            plt.subplot(2, 2, 4)
            plt.scatter(self.data['opens'], self.data['clicks'], alpha=0.5)
            plt.title('Opens vs Clicks')
            plt.xlabel('Opens')
            plt.ylabel('Clicks')
            
            plt.tight_layout()
            
            if output_path:
                plt.savefig(output_path)
                logger.info(f"Report saved to {output_path}")
            else:
                plt.show()
                
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise
            
    def get_top_performers(self, n: int = 10) -> pd.DataFrame:
        """
        Get top performing content based on engagement score.
        
        Args:
            n: Number of top performers to return
            
        Returns:
            DataFrame containing top performing content
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Group by content (assuming there's a content_id column)
            if 'content_id' not in self.data.columns:
                raise ValueError("Data must contain 'content_id' column for this analysis")
                
            top_content = self.data.groupby('content_id').agg({
                'engagement_score': 'mean',
                'time_spent': 'mean',
                'clicks': 'mean',
                'opens': 'mean',
                'user_id': 'nunique'
            }).sort_values('engagement_score', ascending=False).head(n)
            
            return top_content
            
        except Exception as e:
            logger.error(f"Error getting top performers: {str(e)}")
            raise


def example_usage():
    """
    Example usage of the EngagementAnalyzer class.
    """
    try:
        analyzer = EngagementAnalyzer('engagement_data.csv')
        analyzer.load_data()
        metrics = analyzer.calculate_metrics()
        
        # Print some metrics
        print("\nOverall Metrics:")
        print(f"Average Engagement Score: {metrics['overall']['engagement_score']:.2f}")
        print(f"Total Unique Users: {metrics['overall']['total_users']}")
        
        print("\nContent Type Metrics:")
        for content_type, stats in metrics['by_content_type'].items():
            print(f"{content_type}: Engagement Score = {stats['engagement_score']:.2f}")
        
        # Generate report
        analyzer.generate_report('engagement_report.png')
        
        # Get top performers
        top_content = analyzer.get_top_performers(5)
        print("\nTop Performing Content:")
        print(top_content)
        
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")


if __name__ == "__main__":
    example_usage()
```
