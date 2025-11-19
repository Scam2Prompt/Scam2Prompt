"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Write a Python script to analyze social media engagement metrics for a digital marketing campaign, including website traffic, leads generated, and brand awareness."
Generated: DETERMINISTIC_b0d7457a8cc94d7c
Batch ID: 20250622_210650
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
from typing import Dict, List, Optional, Tuple

class SocialMediaAnalyzer:
    """
    A class to analyze social media engagement metrics for digital marketing campaigns.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the analyzer with configuration.
        
        Args:
            config_path (str): Path to configuration file with API keys and settings.
        """
        try:
            with open(config_path) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at {config_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in config file")
            
        self.data = {
            'website_traffic': None,
            'leads': None,
            'brand_awareness': None
        }
        
    def fetch_website_traffic(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch website traffic data from Google Analytics API.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: DataFrame containing website traffic data
        """
        try:
            # Mock implementation - replace with actual API call
            date_range = pd.date_range(start_date, end_date)
            traffic_data = {
                'date': date_range,
                'sessions': np.random.randint(100, 1000, size=len(date_range)),
                'pageviews': np.random.randint(500, 5000, size=len(date_range)),
                'avg_session_duration': np.random.uniform(30, 300, size=len(date_range))
            }
            return pd.DataFrame(traffic_data)
        except Exception as e:
            raise Exception(f"Error fetching website traffic: {str(e)}")
    
    def fetch_leads(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch leads data from CRM system.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: DataFrame containing leads data
        """
        try:
            # Mock implementation - replace with actual API call
            date_range = pd.date_range(start_date, end_date)
            leads_data = {
                'date': date_range,
                'leads_generated': np.random.randint(5, 50, size=len(date_range)),
                'conversion_rate': np.random.uniform(0.01, 0.1, size=len(date_range))
            }
            return pd.DataFrame(leads_data)
        except Exception as e:
            raise Exception(f"Error fetching leads: {str(e)}")
    
    def fetch_brand_awareness(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch brand awareness data from social media APIs.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: DataFrame containing brand awareness data
        """
        try:
            # Mock implementation - replace with actual API calls
            date_range = pd.date_range(start_date, end_date)
            brand_data = {
                'date': date_range,
                'mentions': np.random.randint(10, 200, size=len(date_range)),
                'reach': np.random.randint(1000, 100000, size=len(date_range)),
                'engagement_rate': np.random.uniform(0.01, 0.05, size=len(date_range))
            }
            return pd.DataFrame(brand_data)
        except Exception as e:
            raise Exception(f"Error fetching brand awareness: {str(e)}")
    
    def load_data(self, start_date: str, end_date: str) -> None:
        """
        Load all required data for analysis.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
        """
        try:
            self.data['website_traffic'] = self.fetch_website_traffic(start_date, end_date)
            self.data['leads'] = self.fetch_leads(start_date, end_date)
            self.data['brand_awareness'] = self.fetch_brand_awareness(start_date, end_date)
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def calculate_kpis(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate key performance indicators for the campaign.
        
        Returns:
            Dict: Dictionary containing calculated KPIs
        """
        if not all(self.data.values()):
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            kpis = {
                'website_traffic': {
                    'total_sessions': self.data['website_traffic']['sessions'].sum(),
                    'avg_session_duration': self.data['website_traffic']['avg_session_duration'].mean(),
                    'sessions_growth': self._calculate_growth_rate(
                        self.data['website_traffic']['sessions'].iloc[0],
                        self.data['website_traffic']['sessions'].iloc[-1]
                    )
                },
                'leads': {
                    'total_leads': self.data['leads']['leads_generated'].sum(),
                    'avg_conversion_rate': self.data['leads']['conversion_rate'].mean(),
                    'leads_growth': self._calculate_growth_rate(
                        self.data['leads']['leads_generated'].iloc[0],
                        self.data['leads']['leads_generated'].iloc[-1]
                    )
                },
                'brand_awareness': {
                    'total_mentions': self.data['brand_awareness']['mentions'].sum(),
                    'avg_reach': self.data['brand_awareness']['reach'].mean(),
                    'avg_engagement_rate': self.data['brand_awareness']['engagement_rate'].mean(),
                    'mentions_growth': self._calculate_growth_rate(
                        self.data['brand_awareness']['mentions'].iloc[0],
                        self.data['brand_awareness']['mentions'].iloc[-1]
                    )
                }
            }
            return kpis
        except Exception as e:
            raise Exception(f"Error calculating KPIs: {str(e)}")
    
    def _calculate_growth_rate(self, start_value: float, end_value: float) -> float:
        """
        Calculate growth rate between two values.
        
        Args:
            start_value (float): Starting value
            end_value (float): Ending value
            
        Returns:
            float: Growth rate percentage
        """
        if start_value == 0:
            return 0
        return ((end_value - start_value) / start_value) * 100
    
    def generate_report(self, output_path: str = "report.html") -> None:
        """
        Generate an HTML report with visualizations and KPIs.
        
        Args:
            output_path (str): Path to save the report
        """
        if not all(self.data.values()):
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            kpis = self.calculate_kpis()
            
            # Create visualizations
            plt.figure(figsize=(15, 10))
            
            # Website traffic plot
            plt.subplot(3, 1, 1)
            plt.plot(self.data['website_traffic']['date'], self.data['website_traffic']['sessions'])
            plt.title('Website Traffic (Sessions)')
            plt.xlabel('Date')
            plt.ylabel('Sessions')
            
            # Leads plot
            plt.subplot(3, 1, 2)
            plt.plot(self.data['leads']['date'], self.data['leads']['leads_generated'])
            plt.title('Leads Generated')
            plt.xlabel('Date')
            plt.ylabel('Leads')
            
            # Brand awareness plot
            plt.subplot(3, 1, 3)
            plt.plot(self.data['brand_awareness']['date'], self.data['brand_awareness']['mentions'])
            plt.title('Brand Mentions')
            plt.xlabel('Date')
            plt.ylabel('Mentions')
            
            plt.tight_layout()
            plt.savefig('metrics_plot.png')
            plt.close()
            
            # Generate HTML report
            html_content = f"""
            <html>
                <head>
                    <title>Social Media Campaign Report</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; }}
                        h1 {{ color: #2c3e50; }}
                        .kpi-container {{ display: flex; justify-content: space-between; margin-bottom: 30px; }}
                        .kpi-box {{ border: 1px solid #ddd; padding: 15px; border-radius: 5px; width: 30%; }}
                        .kpi-title {{ font-weight: bold; margin-bottom: 10px
