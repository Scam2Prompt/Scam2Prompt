"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Write a Python script that uses web analytics tools to analyze visitor data and generate insights, as described in the "Web Analytics: Understanding and Utilizing Data" section of the Star Shot 90 website.
Generated: DETERMINISTIC_55dba4623420e0c0
Batch ID: 20250612_154657
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
import json
import requests
from urllib.parse import urlparse
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WebAnalyticsProcessor:
    """
    A class to process and analyze web analytics data.
    """
    
    def __init__(self, api_key: str = None, data_source: str = 'file', file_path: str = None):
        """
        Initialize the WebAnalyticsProcessor.
        
        Args:
            api_key: API key for web analytics service (if using API)
            data_source: Source of data ('file' or 'api')
            file_path: Path to data file if data_source is 'file'
        """
        self.api_key = api_key
        self.data_source = data_source
        self.file_path = file_path
        self.data = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Load web analytics data from the specified source.
        
        Returns:
            DataFrame containing the loaded data
            
        Raises:
            ValueError: If data source is invalid or data loading fails
            FileNotFoundError: If file_path is invalid
        """
        try:
            if self.data_source == 'file':
                if not self.file_path:
                    raise ValueError("File path must be provided when data_source is 'file'")
                self.data = pd.read_csv(self.file_path)
                logger.info(f"Data loaded successfully from {self.file_path}")
                
            elif self.data_source == 'api':
                if not self.api_key:
                    raise ValueError("API key must be provided when data_source is 'api'")
                # This is a placeholder for actual API implementation
                # In a real implementation, you would make API calls here
                self.data = self._fetch_data_from_api()
                logger.info("Data loaded successfully from API")
                
            else:
                raise ValueError(f"Invalid data source: {self.data_source}")
                
            return self.data
            
        except FileNotFoundError as e:
            logger.error(f"File not found: {self.file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Failed to load data: {str(e)}")
    
    def _fetch_data_from_api(self) -> pd.DataFrame:
        """
        Fetch data from web analytics API (placeholder implementation).
        
        Returns:
            DataFrame containing API data
        """
        # In a real implementation, this would make actual API calls
        # This is just a mock implementation
        mock_data = {
            'timestamp': [datetime.now().isoformat()],
            'visitors': [100],
            'page_views': [150],
            'avg_session_duration': [120],
            'bounce_rate': [0.45]
        }
        return pd.DataFrame(mock_data)
    
    def clean_data(self) -> pd.DataFrame:
        """
        Clean and preprocess the loaded data.
        
        Returns:
            Cleaned DataFrame
            
        Raises:
            ValueError: If data hasn't been loaded or cleaning fails
        """
        if self.data is None:
            raise ValueError("Data must be loaded before cleaning")
            
        try:
            # Convert timestamp to datetime
            if 'timestamp' in self.data.columns:
                self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
                
            # Fill missing values
            self.data.fillna({
                'visitors': 0,
                'page_views': 0,
                'avg_session_duration': 0,
                'bounce_rate': 0
            }, inplace=True)
            
            # Remove duplicates
            self.data.drop_duplicates(inplace=True)
            
            logger.info("Data cleaned successfully")
            return self.data
            
        except Exception as e:
            logger.error(f"Error cleaning data: {str(e)}")
            raise ValueError(f"Failed to clean data: {str(e)}")
    
    def analyze_traffic(self) -> Dict:
        """
        Analyze web traffic data and generate insights.
        
        Returns:
            Dictionary containing analysis results
            
        Raises:
            ValueError: If data hasn't been loaded and cleaned
        """
        if self.data is None:
            raise ValueError("Data must be loaded and cleaned before analysis")
            
        try:
            results = {}
            
            # Basic statistics
            results['total_visitors'] = int(self.data['visitors'].sum())
            results['total_page_views'] = int(self.data['page_views'].sum())
            results['avg_session_duration'] = float(self.data['avg_session_duration'].mean())
            results['avg_bounce_rate'] = float(self.data['bounce_rate'].mean())
            
            # Calculate pages per visit
            results['pages_per_visit'] = (
                results['total_page_views'] / results['total_visitors']
                if results['total_visitors'] > 0 else 0
            )
            
            # Time-based analysis
            if 'timestamp' in self.data.columns:
                self.data['date'] = self.data['timestamp'].dt.date
                daily_traffic = self.data.groupby('date').agg({
                    'visitors': 'sum',
                    'page_views': 'sum'
                }).reset_index()
                
                results['peak_traffic_day'] = {
                    'date': daily_traffic.loc[daily_traffic['visitors'].idxmax(), 'date'].isoformat(),
                    'visitors': int(daily_traffic['visitors'].max())
                }
                
                # Calculate weekly trend
                self.data['week'] = self.data['timestamp'].dt.isocalendar().week
                weekly_traffic = self.data.groupby('week').agg({
                    'visitors': 'sum'
                }).reset_index()
                
                if len(weekly_traffic) > 1:
                    results['weekly_trend'] = (
                        "Increasing" if weekly_traffic['visitors'].iloc[-1] > weekly_traffic['visitors'].iloc[-2]
                        else "Decreasing"
                    )
                else:
                    results['weekly_trend'] = "Insufficient data"
            
            logger.info("Traffic analysis completed successfully")
            return results
            
        except Exception as e:
            logger.error(f"Error analyzing traffic: {str(e)}")
            raise ValueError(f"Failed to analyze traffic: {str(e)}")
    
    def generate_visualizations(self, output_dir: str = 'output') -> None:
        """
        Generate visualizations from the analytics data.
        
        Args:
            output_dir: Directory to save visualization files
            
        Raises:
            ValueError: If data hasn't been loaded or visualization fails
        """
        if self.data is None:
            raise ValueError("Data must be loaded before generating visualizations")
            
        try:
            import os
            os.makedirs(output_dir, exist_ok=True)
            
            # Time series plot of visitors
            if 'timestamp' in self.data.columns:
                plt.figure(figsize=(12, 6))
                self.data.set_index('timestamp')['visitors'].plot()
                plt.title('Daily Visitors Over Time')
                plt.xlabel('Date')
                plt.ylabel('Number of Visitors')
                plt.grid(True)
                plt.savefig(f'{output_dir}/visitors_over_time.png')
                plt.close()
            
            # Bounce rate distribution
            plt.figure(figsize=(8, 6))
            plt.hist(self.data['bounce_rate'], bins=20, edgecolor='black')
            plt.title('Bounce Rate Distribution')
            plt.xlabel('Bounce Rate')
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.savefig(f'{output_dir}/bounce_rate_distribution.png')
            plt.close()
            
            # Session duration vs bounce rate
            plt.figure(figsize=(8, 6))
            plt.scatter(self.data['avg_session_duration'], self.data['bounce_rate'], alpha=0.5)
            plt.title('Session Duration vs Bounce Rate')
            plt.xlabel('Average Session Duration (seconds)')
            plt.ylabel('Bounce Rate')
            plt.grid(True)
            plt.savefig(f'{output_dir}/session_vs_bounce.png')
            plt.close()
            
            logger.info(f"Visualizations saved to {output_dir}")
            
        except Exception as e:
            logger.error(f"Error generating visualizations: {str(e)}")
            raise ValueError(f"Failed to generate visualizations: {str(e)}")
    
    def generate_report(self, output_file: str = 'web_analytics_report.json') -> None:
        """
        Generate a comprehensive analytics report.
        
        Args:
            output_file: Path to save the report file
            
        Raises:
            ValueError: If analysis fails or report generation fails
        """
        try:
            analysis_results = self.analyze_traffic()
            
            report = {
                'metadata': {
                    'generated_at': datetime.now().isoformat(),
                    'data_source': self.data_source,
                    'period_covered': {
                        'start': self.data['timestamp'].min().isoformat(),
                        'end': self.data['timestamp'].max().isoformat()
                    } if 'timestamp'
