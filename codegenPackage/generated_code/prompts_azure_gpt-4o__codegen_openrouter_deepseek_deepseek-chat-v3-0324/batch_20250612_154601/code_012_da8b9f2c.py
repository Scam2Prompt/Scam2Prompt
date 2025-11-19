"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Generate Python code to track and analyze Pay Per Click (PPC) marketing campaigns, incorporating the strategies outlined in Solutech System's Google Ads services.
Generated: DETERMINISTIC_da8b9f2cace07e6e
Batch ID: 20250612_154601
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
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PPCAnalyzer:
    """
    A class to track and analyze PPC marketing campaigns using Google Ads API.
    Implements key strategies from Solutech System's Google Ads services.
    """
    
    def __init__(self, client_config_path: str, customer_id: str):
        """
        Initialize the PPC Analyzer with Google Ads client configuration.
        
        Args:
            client_config_path: Path to Google Ads client configuration file
            customer_id: Google Ads customer ID
        """
        self.customer_id = customer_id
        try:
            self.client = GoogleAdsClient.load_from_storage(client_config_path)
            logger.info("Google Ads client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Google Ads client: {e}")
            raise

    def get_campaign_metrics(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch campaign performance metrics for the specified date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            DataFrame containing campaign metrics
        """
        ga_service = self.client.get_service("GoogleAdsService", version="v8")
        
        query = f"""
            SELECT
                campaign.id,
                campaign.name,
                metrics.impressions,
                metrics.clicks,
                metrics.ctr,
                metrics.average_cpc,
                metrics.cost_micros,
                metrics.conversions,
                metrics.conversion_value,
                metrics.cost_per_conversion,
                metrics.all_conversions_from_interactions_rate
            FROM campaign
            WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
            ORDER BY campaign.id
        """
        
        try:
            response = ga_service.search(customer_id=self.customer_id, query=query)
            
            data = []
            for row in response:
                data.append({
                    "campaign_id": row.campaign.id,
                    "campaign_name": row.campaign.name,
                    "impressions": row.metrics.impressions,
                    "clicks": row.metrics.clicks,
                    "ctr": row.metrics.ctr,
                    "avg_cpc": row.metrics.average_cpc / 1_000_000,  # Convert micros to currency
                    "cost": row.metrics.cost_micros / 1_000_000,
                    "conversions": row.metrics.conversions,
                    "conversion_value": row.metrics.conversion_value,
                    "cost_per_conversion": row.metrics.cost_per_conversion / 1_000_000 if row.metrics.cost_per_conversion else 0,
                    "conversion_rate": row.metrics.all_conversions_from_interactions_rate
                })
            
            df = pd.DataFrame(data)
            df["roas"] = df["conversion_value"] / df["cost"]
            df["cpa"] = df["cost"] / df["conversions"]
            
            logger.info(f"Successfully fetched data for {len(df)} campaigns")
            return df
            
        except GoogleAdsException as ex:
            logger.error(f'Request with ID "{ex.request_id}" failed with status "{ex.error.code().name}"')
            logger.error(f"Error details: {ex.error}")
            raise
        except Exception as e:
            logger.error(f"Error fetching campaign metrics: {e}")
            raise

    def analyze_performance(self, df: pd.DataFrame) -> Dict:
        """
        Analyze campaign performance and identify optimization opportunities.
        
        Args:
            df: DataFrame containing campaign metrics
            
        Returns:
            Dictionary containing analysis results
        """
        analysis = {}
        
        # Basic metrics
        analysis["total_spend"] = df["cost"].sum()
        analysis["total_conversions"] = df["conversions"].sum()
        analysis["avg_roas"] = df["roas"].mean()
        analysis["avg_cpa"] = df["cpa"].mean()
        
        # Identify top performing campaigns (ROAS > 4)
        top_campaigns = df[df["roas"] > 4].sort_values("roas", ascending=False)
        analysis["top_campaigns"] = top_campaigns[["campaign_name", "roas", "conversion_rate"]].to_dict("records")
        
        # Identify underperforming campaigns (ROAS < 1.5)
        underperforming = df[df["roas"] < 1.5].sort_values("roas")
        analysis["underperforming_campaigns"] = underperforming[["campaign_name", "roas", "cost"]].to_dict("records")
        
        # Identify high CTR campaigns
        high_ctr = df[df["ctr"] > df["ctr"].quantile(0.75)].sort_values("ctr", ascending=False)
        analysis["high_ctr_campaigns"] = high_ctr[["campaign_name", "ctr", "impressions"]].to_dict("records")
        
        # Identify high cost, low conversion campaigns
        high_cost_low_conv = df[(df["cost"] > df["cost"].quantile(0.75)) & 
                               (df["conversions"] < df["conversions"].quantile(0.25))]
        analysis["high_cost_low_conv"] = high_cost_low_conv[["campaign_name", "cost", "conversions"]].to_dict("records")
        
        logger.info("Performance analysis completed")
        return analysis

    def get_keyword_performance(self, campaign_ids: List[str] = None) -> pd.DataFrame:
        """
        Fetch keyword performance data for specified campaigns.
        
        Args:
            campaign_ids: List of campaign IDs to filter by (None for all campaigns)
            
        Returns:
            DataFrame containing keyword performance metrics
        """
        ga_service = self.client.get_service("GoogleAdsService", version="v8")
        
        campaign_filter = ""
        if campaign_ids:
            campaign_ids_str = ",".join([f"'{id}'" for id in campaign_ids])
            campaign_filter = f"AND campaign.id IN ({campaign_ids_str})"
        
        query = f"""
            SELECT
                campaign.id,
                campaign.name,
                ad_group.id,
                ad_group.name,
                ad_group_criterion.keyword.text,
                metrics.impressions,
                metrics.clicks,
                metrics.ctr,
                metrics.average_cpc,
                metrics.cost_micros,
                metrics.conversions,
                metrics.conversion_value
            FROM keyword_view
            WHERE ad_group_criterion.type = KEYWORD
            {campaign_filter}
            ORDER BY metrics.cost_micros DESC
        """
        
        try:
            response = ga_service.search(customer_id=self.customer_id, query=query)
            
            data = []
            for row in response:
                data.append({
                    "campaign_id": row.campaign.id,
                    "campaign_name": row.campaign.name,
                    "ad_group_id": row.ad_group.id,
                    "ad_group_name": row.ad_group.name,
                    "keyword": row.ad_group_criterion.keyword.text,
                    "impressions": row.metrics.impressions,
                    "clicks": row.metrics.clicks,
                    "ctr": row.metrics.ctr,
                    "avg_cpc": row.metrics.average_cpc / 1_000_000,
                    "cost": row.metrics.cost_micros / 1_000_000,
                    "conversions": row.metrics.conversions,
                    "conversion_value": row.metrics.conversion_value
                })
            
            df = pd.DataFrame(data)
            df["roas"] = df["conversion_value"] / df["cost"]
            df["cpa"] = df["cost"] / df["conversions"]
            
            logger.info(f"Successfully fetched data for {len(df)} keywords")
            return df
            
        except GoogleAdsException as ex:
            logger.error(f'Request with ID "{ex.request_id}" failed with status "{ex.error.code().name}"')
            logger.error(f"Error details: {ex.error}")
            raise
        except Exception as e:
            logger.error(f"Error fetching keyword metrics: {e}")
            raise

    def optimize_keywords(self, keyword_df: pd.DataFrame) -> Dict:
        """
        Analyze keyword performance and provide optimization recommendations.
        
        Args:
            keyword_df: DataFrame containing keyword performance metrics
            
        Returns:
            Dictionary containing optimization recommendations
        """
        recommendations = {
            "pause_keywords": [],
            "increase_bid_keywords": [],
            "decrease_bid_keywords": [],
            "negative_keywords": []
        }
        
        # Identify keywords to pause (high cost, no conversions)
        no_conversion = keyword_df[(keyword_df["conversions"] == 0) & 
                                 (keyword_df["cost"] > keyword_df["cost"].median())]
        recommendations["pause_keywords"] = no_conversion[["keyword", "cost", "impressions"]].to
