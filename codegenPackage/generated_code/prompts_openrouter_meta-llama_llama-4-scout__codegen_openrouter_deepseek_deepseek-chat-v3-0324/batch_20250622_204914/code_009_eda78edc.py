"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: "Write a script to optimize a sales funnel for a pet grooming business using data from Google Ads and Facebook Ads."
Generated: DETERMINISTIC_eda78edc5e452e00
Batch ID: 20250622_204914
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
from google.ads.google_ads.client import GoogleAdsClient
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FunnelOptimizer:
    def __init__(
        self,
        google_ads_config: Dict,
        facebook_ads_config: Dict,
        start_date: str,
        end_date: str
    ):
        """
        Initialize the FunnelOptimizer with configuration and date range.
        
        Args:
            google_ads_config: Dictionary containing Google Ads API credentials
            facebook_ads_config: Dictionary containing Facebook Ads API credentials
            start_date: Start date for data analysis (YYYY-MM-DD)
            end_date: End date for data analysis (YYYY-MM-DD)
        """
        self.google_ads_config = google_ads_config
        self.facebook_ads_config = facebook_ads_config
        self.start_date = start_date
        self.end_date = end_date
        
        # Initialize API clients
        self._init_google_ads_client()
        self._init_facebook_ads_client()
        
    def _init_google_ads_client(self) -> None:
        """Initialize Google Ads API client."""
        try:
            self.google_ads_client = GoogleAdsClient.load_from_dict(self.google_ads_config)
            logger.info("Google Ads client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Google Ads client: {str(e)}")
            raise
            
    def _init_facebook_ads_client(self) -> None:
        """Initialize Facebook Ads API client."""
        try:
            FacebookAdsApi.init(
                app_id=self.facebook_ads_config['app_id'],
                app_secret=self.facebook_ads_config['app_secret'],
                access_token=self.facebook_ads_config['access_token'],
                api_version='v12.0'
            )
            logger.info("Facebook Ads client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Facebook Ads client: {str(e)}")
            raise
    
    def fetch_google_ads_data(self, customer_id: str) -> pd.DataFrame:
        """
        Fetch Google Ads campaign performance data.
        
        Args:
            customer_id: Google Ads customer ID
            
        Returns:
            DataFrame containing Google Ads performance metrics
        """
        try:
            ga_service = self.google_ads_client.get_service('GoogleAdsService')
            
            query = f"""
                SELECT
                    campaign.id,
                    campaign.name,
                    metrics.impressions,
                    metrics.clicks,
                    metrics.cost_micros,
                    metrics.conversions,
                    metrics.conversions_value
                FROM campaign
                WHERE segments.date BETWEEN '{self.start_date}' AND '{self.end_date}'
                ORDER BY campaign.id
            """
            
            response = ga_service.search(customer_id=customer_id, query=query)
            
            data = []
            for row in response:
                data.append({
                    'platform': 'google_ads',
                    'campaign_id': row.campaign.id,
                    'campaign_name': row.campaign.name,
                    'impressions': row.metrics.impressions,
                    'clicks': row.metrics.clicks,
                    'cost': row.metrics.cost_micros / 1000000,
                    'conversions': row.metrics.conversions,
                    'conversion_value': row.metrics.conversions_value
                })
            
            df = pd.DataFrame(data)
            logger.info(f"Fetched {len(df)} Google Ads records")
            return df
            
        except Exception as e:
            logger.error(f"Error fetching Google Ads data: {str(e)}")
            raise
    
    def fetch_facebook_ads_data(self, account_id: str) -> pd.DataFrame:
        """
        Fetch Facebook Ads campaign performance data.
        
        Args:
            account_id: Facebook Ads account ID
            
        Returns:
            DataFrame containing Facebook Ads performance metrics
        """
        try:
            fields = [
                AdsInsights.Field.campaign_id,
                AdsInsights.Field.campaign_name,
                AdsInsights.Field.impressions,
                AdsInsights.Field.clicks,
                AdsInsights.Field.spend,
                AdsInsights.Field.conversions,
                AdsInsights.Field.conversion_values
            ]
            
            params = {
                'time_range': {
                    'since': self.start_date,
                    'until': self.end_date
                },
                'level': 'campaign',
                'time_increment': 1
            }
            
            insights = AdAccount(account_id).get_insights(
                fields=fields,
                params=params
            )
            
            data = []
            for insight in insights:
                data.append({
                    'platform': 'facebook_ads',
                    'campaign_id': insight['campaign_id'],
                    'campaign_name': insight['campaign_name'],
                    'impressions': insight['impressions'],
                    'clicks': insight['clicks'],
                    'cost': insight['spend'],
                    'conversions': insight['conversions'],
                    'conversion_value': insight['conversion_values']
                })
            
            df = pd.DataFrame(data)
            logger.info(f"Fetched {len(df)} Facebook Ads records")
            return df
            
        except Exception as e:
            logger.error(f"Error fetching Facebook Ads data: {str(e)}")
            raise
    
    def calculate_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate key performance metrics from raw data.
        
        Args:
            df: DataFrame containing raw performance data
            
        Returns:
            DataFrame with calculated metrics
        """
        try:
            # Calculate metrics
            df['ctr'] = df['clicks'] / df['impressions']
            df['cpc'] = df['cost'] / df['clicks']
            df['conversion_rate'] = df['conversions'] / df['clicks']
            df['roas'] = df['conversion_value'] / df['cost']
            df['cpa'] = df['cost'] / df['conversions']
            
            # Replace infinities and NaNs with 0
            df.replace([np.inf, -np.inf], np.nan, inplace=True)
            df.fillna(0, inplace=True)
            
            return df
            
        except Exception as e:
            logger.error(f"Error calculating metrics: {str(e)}")
            raise
    
    def optimize_funnel(self, df: pd.DataFrame) -> Dict:
        """
        Analyze performance data and provide optimization recommendations.
        
        Args:
            df: DataFrame containing performance metrics
            
        Returns:
            Dictionary containing optimization recommendations
        """
        try:
            recommendations = {
                'top_performing_campaigns': [],
                'underperforming_campaigns': [],
                'general_recommendations': []
            }
            
            # Identify top performing campaigns (ROAS > 4)
            top_campaigns = df[df['roas'] > 4].sort_values('roas', ascending=False)
            if not top_campaigns.empty:
                recommendations['top_performing_campaigns'] = top_campaigns[
                    ['platform', 'campaign_name', 'roas', 'conversion_rate']
                ].to_dict('records')
            
            # Identify underperforming campaigns (ROAS < 1.5)
            underperforming_campaigns = df[df['roas'] < 1.5].sort_values('roas')
            if not underperforming_campaigns.empty:
                recommendations['underperforming_campaigns'] = underperforming_campaigns[
                    ['platform', 'campaign_name', 'roas', 'cpa']
                ].to_dict('records')
            
            # General recommendations
            avg_ctr = df['ctr'].mean()
            avg_cr = df['conversion_rate'].mean()
            
            if avg_ctr < 0.02:
                recommendations['general_recommendations'].append(
                    "Low average CTR (%.2f%%). Consider improving ad creatives and targeting." % (avg_ctr * 100)
                )
            
            if avg_cr < 0.05:
                recommendations['general_recommendations'].append(
                    "Low average conversion rate (%.2f%%). Review landing pages and offer quality." % (avg_cr * 100)
                )
            
            # Platform-specific recommendations
            if 'google_ads' in df['platform'].unique():
                recommendations['general_recommendations'].append(
                    "Review Google Ads keyword match types and negative keywords."
                )
            
            if 'facebook_ads' in df['platform'].unique():
                recommendations['general_recommendations'].append(
                    "Test different Facebook ad formats (carousel, video, etc.) and audience segments."
                )
            
            return recommendations
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            raise
    
    def run_optimization(
        self,
        google_ads_customer_id: str,
        facebook_ads_account_id: str
    ) -> Dict:
        """
        Run the complete optimization pipeline.
