"""
Generated Code Metadata:
========================
Original URL: https://corridorweb.com
Prompt: "Develop a pay-per-click advertising model using Google Ads API and Python, as per Corridor Web Agency's pay-per-click advertising services."
Generated: DETERMINISTIC_bb667e3f516b9a68
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from datetime import datetime
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from google.auth.exceptions import GoogleAuthError

# Configuration class for Google Ads API
class GoogleAdsConfig:
    def __init__(self):
        self.developer_token = os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN")
        self.client_id = os.getenv("GOOGLE_ADS_CLIENT_ID")
        self.client_secret = os.getenv("GOOGLE_ADS_CLIENT_SECRET")
        self.refresh_token = os.getenv("GOOGLE_ADS_REFRESH_TOKEN")
        self.login_customer_id = os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID")
        
        self.validate_config()

    def validate_config(self):
        """Validate that all required environment variables are set."""
        required_vars = {
            "GOOGLE_ADS_DEVELOPER_TOKEN": self.developer_token,
            "GOOGLE_ADS_CLIENT_ID": self.client_id,
            "GOOGLE_ADS_CLIENT_SECRET": self.client_secret,
            "GOOGLE_ADS_REFRESH_TOKEN": self.refresh_token,
            "GOOGLE_ADS_LOGIN_CUSTOMER_ID": self.login_customer_id,
        }
        
        missing_vars = [var for var, value in required_vars.items() if not value]
        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )

# Main PPC Manager class
class PPCManager:
    def __init__(self, config):
        self.config = config
        self.client = self._initialize_client()

    def _initialize_client(self):
        """Initialize and return Google Ads client."""
        credentials = {
            "developer_token": self.config.developer_token,
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "refresh_token": self.config.refresh_token,
            "login_customer_id": self.config.login_customer_id,
            "use_proto_plus": True,
        }
        
        try:
            return GoogleAdsClient.load_from_dict(credentials)
        except GoogleAuthError as e:
            raise SystemExit(f"Failed to initialize Google Ads client: {e}")

    def create_campaign(self, customer_id, campaign_name, budget_amount, start_date=None, end_date=None):
        """
        Create a new Google Ads campaign.
        
        Args:
            customer_id: The customer ID for the Google Ads account
            campaign_name: Name of the campaign
            budget_amount: Daily budget in micros (1,000,000 micros = 1 currency unit)
            start_date: Campaign start date (YYYY-MM-DD)
            end_date: Campaign end date (YYYY-MM-DD)
            
        Returns:
            The created campaign resource name
        """
        if not start_date:
            start_date = datetime.now().strftime("%Y-%m-%d")
            
        campaign_service = self.client.get_service("CampaignService")
        campaign_budget_service = self.client.get_service("CampaignBudgetService")
        
        try:
            # Create campaign budget
            campaign_budget_operation = self.client.get_type("CampaignBudgetOperation")
            campaign_budget = campaign_budget_operation.create
            campaign_budget.name = f"{campaign_name} Budget"
            campaign_budget.amount_micros = budget_amount
            campaign_budget.delivery_method = self.client.enums.BudgetDeliveryMethodEnum.STANDARD
            
            budget_response = campaign_budget_service.mutate_campaign_budgets(
                customer_id=customer_id,
                operations=[campaign_budget_operation],
            )
            budget_resource_name = budget_response.results[0].resource_name
            
            # Create campaign
            campaign_operation = self.client.get_type("CampaignOperation")
            campaign = campaign_operation.create
            campaign.name = campaign_name
            campaign.advertising_channel_type = self.client.enums.AdvertisingChannelTypeEnum.SEARCH
            campaign.status = self.client.enums.CampaignStatusEnum.PAUSED
            campaign.manual_cpc.enhanced_cpc_enabled = True
            campaign.campaign_budget = budget_resource_name
            campaign.start_date = start_date
            
            if end_date:
                campaign.end_date = end_date
                
            campaign.network_settings.target_google_search = True
            campaign.network_settings.target_search_network = True
            campaign.network_settings.target_content_network = False
            
            response = campaign_service.mutate_campaigns(
                customer_id=customer_id,
                operations=[campaign_operation],
            )
            
            return response.results[0].resource_name
            
        except GoogleAdsException as e:
            print(f"Failed to create campaign: {e}")
            raise

    def create_ad_group(self, customer_id, campaign_id, ad_group_name, cpc_bid_micros):
        """
        Create a new ad group within a campaign.
        
        Args:
            customer_id: The customer ID for the Google Ads account
            campaign_id: The campaign ID to add the ad group to
            ad_group_name: Name of the ad group
            cpc_bid_micros: CPC bid amount in micros
            
        Returns:
            The created ad group resource name
        """
        ad_group_service = self.client.get_service("AdGroupService")
        
        try:
            ad_group_operation = self.client.get_type("AdGroupOperation")
            ad_group = ad_group_operation.create
            ad_group.name = ad_group_name
            ad_group.campaign = f"customers/{customer_id}/campaigns/{campaign_id}"
            ad_group.type_ = self.client.enums.AdGroupTypeEnum.SEARCH_STANDARD
            ad_group.cpc_bid_micros = cpc_bid_micros
            ad_group.status = self.client.enums.AdGroupStatusEnum.ENABLED
            
            response = ad_group_service.mutate_ad_groups(
                customer_id=customer_id,
                operations=[ad_group_operation],
            )
            
            return response.results[0].resource_name
            
        except GoogleAdsException as e:
            print(f"Failed to create ad group: {e}")
            raise

    def create_text_ad(self, customer_id, ad_group_id, headline1, headline2, description, display_url, final_url):
        """
        Create a new text ad within an ad group.
        
        Args:
            customer_id: The customer ID for the Google Ads account
            ad_group_id: The ad group ID to add the ad to
            headline1: First headline text
            headline2: Second headline text
            description: Description text
            display_url: Display URL
            final_url: Final URL
            
        Returns:
            The created ad resource name
        """
        ad_group_ad_service = self.client.get_service("AdGroupAdService")
        
        try:
            ad_group_ad_operation = self.client.get_type("AdGroupAdOperation")
            ad_group_ad = ad_group_ad_operation.create
            ad_group_ad.ad_group = f"customers/{customer_id}/adGroups/{ad_group_id}"
            ad_group_ad.status = self.client.enums.AdGroupAdStatusEnum.ENABLED
            
            # Create text ad
            text_ad = ad_group_ad.ad.expanded_text_ad
            text_ad.headline_part1 = headline1
            text_ad.headline_part2 = headline2
            text_ad.description = description
            text_ad.path1 = display_url.split("/")[0] if "/" in display_url else display_url
            text_ad.path2 = display_url.split("/")[1] if "/" in display_url else ""
            
            ad_group_ad.ad.final_urls.append(final_url)
            
            response = ad_group_ad_service.mutate_ad_group_ads(
                customer_id=customer_id,
                operations=[ad_group_ad_operation],
            )
            
            return response.results[0].resource_name
            
        except GoogleAdsException as e:
            print(f"Failed to create text ad: {e}")
            raise

    def get_campaign_metrics(self, customer_id, campaign_id, date_range="LAST_30_DAYS"):
        """
        Get performance metrics for a campaign.
        
        Args:
            customer_id: The customer ID for the Google Ads account
            campaign_id: The campaign ID to get metrics for
            date_range: Date range for metrics (e.g., "LAST_30_DAYS")
            
        Returns:
            Dictionary containing campaign metrics
        """
        googleads_service = self.client.get_service("GoogleAdsService")
        
        query = f"""
            SELECT
                campaign.id,
                metrics.impressions,
                metrics.clicks,
                metrics.ctr,
                metrics.average_cpc,
                metrics.cost_micros,
                metrics.conversions,
                metrics.conversion_value
            FROM campaign
            WHERE campaign.id = {campaign_id}
            AND segments.date DURING {date_range}
        """
        
        try:
            response = googleads_service.search(
                customer_id=customer_id,
                query=query,
            )
            
            metrics = {}
            for row in response:
                metrics = {
                    "impressions": row.metrics.impressions,
                    "clicks": row.metrics.clicks,
                    "
