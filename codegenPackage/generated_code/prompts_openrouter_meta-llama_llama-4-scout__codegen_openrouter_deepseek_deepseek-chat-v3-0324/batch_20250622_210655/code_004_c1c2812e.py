"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: "Write a Python script to analyze the effectiveness of marketing campaigns for a pub trade client, using metrics similar to those used by Lords Marketing."
Generated: DETERMINISTIC_c1c2812e78daf1bc
Batch ID: 20250622_210655
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
from sklearn.metrics import r2_score
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='marketing_analysis.log'
)

class MarketingCampaignAnalyzer:
    """
    A class to analyze marketing campaign effectiveness for pub trade clients.
    Metrics inspired by Lords Marketing's approach.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with campaign data.
        
        Args:
            data_path (str): Path to the CSV file containing campaign data
        """
        self.data_path = data_path
        self.data = None
        self.metrics = {}
        
    def load_data(self):
        """
        Load and preprocess marketing campaign data.
        
        Raises:
            FileNotFoundError: If data file doesn't exist
            ValueError: If data is malformed
        """
        try:
            self.data = pd.read_csv(self.data_path)
            logging.info("Data loaded successfully")
            
            # Basic data validation
            required_columns = {
                'campaign_id', 'campaign_name', 'start_date', 'end_date',
                'budget', 'impressions', 'clicks', 'conversions', 'revenue'
            }
            
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Convert dates to datetime objects
            self.data['start_date'] = pd.to_datetime(self.data['start_date'])
            self.data['end_date'] = pd.to_datetime(self.data['end_date'])
            
            # Calculate campaign duration in days
            self.data['duration'] = (self.data['end_date'] - self.data['start_date']).dt.days
            
            # Remove any rows with negative values in numeric columns
            numeric_cols = ['budget', 'impressions', 'clicks', 'conversions', 'revenue']
            self.data = self.data[(self.data[numeric_cols] >= 0).all(axis=1)]
            
        except FileNotFoundError:
            logging.error(f"Data file not found: {self.data_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Data loading error: {str(e)}")
    
    def calculate_metrics(self):
        """
        Calculate key marketing performance metrics.
        """
        try:
            # Basic metrics
            self.metrics['total_campaigns'] = len(self.data)
            self.metrics['total_budget'] = self.data['budget'].sum()
            self.metrics['total_revenue'] = self.data['revenue'].sum()
            
            # ROI calculation
            self.metrics['overall_roi'] = (
                (self.metrics['total_revenue'] - self.metrics['total_budget']) / 
                self.metrics['total_budget']
            ) * 100
            
            # Engagement metrics
            self.data['ctr'] = (self.data['clicks'] / self.data['impressions']) * 100
            self.data['conversion_rate'] = (self.data['conversions'] / self.data['clicks']) * 100
            self.data['roi'] = ((self.data['revenue'] - self.data['budget']) / self.data['budget']) * 100
            
            # Average metrics
            self.metrics['avg_ctr'] = self.data['ctr'].mean()
            self.metrics['avg_conversion_rate'] = self.data['conversion_rate'].mean()
            self.metrics['avg_roi'] = self.data['roi'].mean()
            self.metrics['avg_duration'] = self.data['duration'].mean()
            
            # Performance segmentation
            self.metrics['high_performers'] = len(self.data[self.data['roi'] > 20])
            self.metrics['low_performers'] = len(self.data[self.data['roi'] <= 0])
            
            logging.info("Metrics calculated successfully")
            
        except Exception as e:
            logging.error(f"Error calculating metrics: {str(e)}")
            raise
    
    def analyze_campaign_trends(self):
        """
        Analyze trends over time and visualize results.
        """
        try:
            # Monthly performance analysis
            monthly_data = self.data.copy()
            monthly_data['month'] = monthly_data['start_date'].dt.to_period('M')
            
            monthly_stats = monthly_data.groupby('month').agg({
                'budget': 'sum',
                'revenue': 'sum',
                'roi': 'mean',
                'ctr': 'mean',
                'conversion_rate': 'mean'
            }).reset_index()
            
            # Plotting trends
            plt.figure(figsize=(12, 8))
            
            # ROI Trend
            plt.subplot(2, 2, 1)
            plt.plot(monthly_stats['month'].astype(str), monthly_stats['roi'], marker='o')
            plt.title('Monthly Average ROI')
            plt.xlabel('Month')
            plt.ylabel('ROI (%)')
            plt.xticks(rotation=45)
            
            # CTR Trend
            plt.subplot(2, 2, 2)
            plt.plot(monthly_stats['month'].astype(str), monthly_stats['ctr'], marker='o', color='green')
            plt.title('Monthly Average CTR')
            plt.xlabel('Month')
            plt.ylabel('CTR (%)')
            plt.xticks(rotation=45)
            
            # Conversion Rate Trend
            plt.subplot(2, 2, 3)
            plt.plot(monthly_stats['month'].astype(str), monthly_stats['conversion_rate'], marker='o', color='red')
            plt.title('Monthly Average Conversion Rate')
            plt.xlabel('Month')
            plt.ylabel('Conversion Rate (%)')
            plt.xticks(rotation=45)
            
            # Budget vs Revenue
            plt.subplot(2, 2, 4)
            plt.bar(monthly_stats['month'].astype(str), monthly_stats['budget'], label='Budget', alpha=0.6)
            plt.bar(monthly_stats['month'].astype(str), monthly_stats['revenue'], label='Revenue', alpha=0.6)
            plt.title('Monthly Budget vs Revenue')
            plt.xlabel('Month')
            plt.ylabel('Amount (£)')
            plt.legend()
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            plt.savefig('campaign_trends.png')
            plt.close()
            
            logging.info("Trend analysis completed and plots saved")
            
        except Exception as e:
            logging.error(f"Error in trend analysis: {str(e)}")
            raise
    
    def campaign_performance_report(self):
        """
        Generate a comprehensive performance report.
        
        Returns:
            dict: Dictionary containing all calculated metrics
        """
        try:
            report = {
                'summary': {
                    'total_campaigns': self.metrics['total_campaigns'],
                    'total_budget': f"£{self.metrics['total_budget']:,.2f}",
                    'total_revenue': f"£{self.metrics['total_revenue']:,.2f}",
                    'overall_roi': f"{self.metrics['overall_roi']:.2f}%",
                    'high_performing_campaigns': self.metrics['high_performers'],
                    'low_performing_campaigns': self.metrics['low_performers']
                },
                'averages': {
                    'click_through_rate': f"{self.metrics['avg_ctr']:.2f}%",
                    'conversion_rate': f"{self.metrics['avg_conversion_rate']:.2f}%",
                    'roi': f"{self.metrics['avg_roi']:.2f}%",
                    'campaign_duration': f"{self.metrics['avg_duration']:.1f} days"
                },
                'top_performers': self._get_top_performers(),
                'recommendations': self._generate_recommendations()
            }
            
            logging.info("Performance report generated")
            return report
            
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            raise
    
    def _get_top_performers(self, n=5):
        """
        Get top performing campaigns by ROI.
        
        Args:
            n (int): Number of top performers to return
            
        Returns:
            list: List of dictionaries with top campaign details
        """
        top_campaigns = self.data.sort_values('roi', ascending=False).head(n)
        return top_campaigns[['campaign_name', 'roi', 'ctr', 'conversion_rate']].to_dict('records')
    
    def _generate_recommendations(self):
        """
        Generate data-driven recommendations based on analysis.
        
        Returns:
            list: List of recommendations
        """
        recommendations = []
        
        # Budget allocation recommendation
        budget_correlation = self.data[['budget', 'revenue']].corr().iloc[0
