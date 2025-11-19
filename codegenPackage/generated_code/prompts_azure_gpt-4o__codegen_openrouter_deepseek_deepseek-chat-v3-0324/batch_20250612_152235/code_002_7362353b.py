"""
Generated Code Metadata:
========================
Original URL: https://alphaonlineservices.com
Prompt: Generate code for a PPC advertising campaign that focuses on lead generation rather than clicks, inspired by the PPC strategies mentioned on Alpha Online Services.
Generated: DETERMINISTIC_7362353bab44e9da
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LeadGenerationPPC:
    def __init__(self, client_config_path, customer_id):
        """
        Initialize the PPC campaign manager for lead generation.
        
        Args:
            client_config_path (str): Path to Google Ads API client configuration
            customer_id (str): Google Ads customer ID
        """
        self.client = GoogleAdsClient.load_from_storage(client_config_path)
        self.customer_id = customer_id
        self.service = self.client.get_service('GoogleAdsService', version='v8')

    def create_campaign(self, campaign_name, budget_amount, start_date=None, end_date=None):
        """
        Create a new lead generation campaign.
        
        Args:
            campaign_name (str): Name of the campaign
            budget_amount (int): Daily budget in micros (1,000,000 micros = 1 currency unit)
            start_date (str): Optional start date in YYYY-MM-DD format
            end_date (str): Optional end date in YYYY-MM-DD format
        Returns:
            str: Resource name of the created campaign
        """
        try:
            campaign_budget_service = self.client.get_service('CampaignBudgetService')
            campaign_service = self.client.get_service('CampaignService')

            # Create budget
            budget_operation = self.client.get_type('CampaignBudgetOperation')
            budget = budget_operation.create
            budget.name = f"{campaign_name} Budget"
            budget.amount_micros = budget_amount
            budget.delivery_method = self.client.get_type(
                'BudgetDeliveryMethodEnum').STANDARD

            # Add budget
            budget_response = campaign_budget_service.mutate_campaign_budgets(
                customer_id=self.customer_id,
                operations=[budget_operation]
            )

            # Create campaign
            campaign_operation = self.client.get_type('CampaignOperation')
            campaign = campaign_operation.create
            campaign.name = campaign_name
            campaign.advertising_channel_type = self.client.get_type(
                'AdvertisingChannelTypeEnum').SEARCH
            campaign.status = self.client.get_type('CampaignStatusEnum').PAUSED
            campaign.manual_cpc.enhanced_cpc_enabled = True
            campaign.campaign_budget = budget_response.results[0].resource_name

            # Set dates if provided
            if start_date:
                campaign.start_date = start_date
            if end_date:
                campaign.end_date = end_date

            # Optimize for lead generation
            campaign.selective_optimization.conversion_actions.extend([
                self._get_lead_conversion_action()
            ])

            # Add campaign
            campaign_response = campaign_service.mutate_campaigns(
                customer_id=self.customer_id,
                operations=[campaign_operation]
            )

            logger.info(f"Created campaign {campaign_name} with resource name: "
                      f"{campaign_response.results[0].resource_name}")
            return campaign_response.results[0].resource_name

        except GoogleAdsException as ex:
            logger.error(f"Failed to create campaign: {ex}")
            raise

    def create_ad_group(self, campaign_resource_name, ad_group_name, cpc_bid_micros):
        """
        Create an ad group optimized for lead generation.
        
        Args:
            campaign_resource_name (str): Resource name of the parent campaign
            ad_group_name (str): Name of the ad group
            cpc_bid_micros (int): CPC bid in micros
        Returns:
            str: Resource name of the created ad group
        """
        try:
            ad_group_service = self.client.get_service('AdGroupService')

            # Create ad group
            ad_group_operation = self.client.get_type('AdGroupOperation')
            ad_group = ad_group_operation.create
            ad_group.name = ad_group_name
            ad_group.status = self.client.get_type('AdGroupStatusEnum').ENABLED
            ad_group.campaign = campaign_resource_name
            ad_group.cpc_bid_micros = cpc_bid_micros

            # Target lead generation
            ad_group.target_roas_override = 0  # Focus on conversions, not ROAS
            ad_group.target_cpa_micros = 0  # Let Google optimize for conversions

            # Add ad group
            ad_group_response = ad_group_service.mutate_ad_groups(
                customer_id=self.customer_id,
                operations=[ad_group_operation]
            )

            logger.info(f"Created ad group {ad_group_name} with resource name: "
                      f"{ad_group_response.results[0].resource_name}")
            return ad_group_response.results[0].resource_name

        except GoogleAdsException as ex:
            logger.error(f"Failed to create ad group: {ex}")
            raise

    def create_responsive_search_ad(self, ad_group_resource_name, headlines, descriptions, final_url):
        """
        Create a responsive search ad optimized for lead generation.
        
        Args:
            ad_group_resource_name (str): Resource name of the parent ad group
            headlines (list): List of headline texts (15-30 chars recommended)
            descriptions (list): List of description texts (up to 90 chars)
            final_url (str): Final URL for the ad
        Returns:
            str: Resource name of the created ad
        """
        try:
            ad_group_ad_service = self.client.get_service('AdGroupAdService')

            # Create ad
            ad_group_ad_operation = self.client.get_type('AdGroupAdOperation')
            ad_group_ad = ad_group_ad_operation.create
            ad_group_ad.ad_group = ad_group_resource_name
            ad_group_ad.status = self.client.get_type('AdGroupAdStatusEnum').ENABLED

            # Set responsive search ad
            responsive_search_ad = ad_group_ad.ad.responsive_search_ad
            for headline in headlines:
                ad_headline = responsive_search_ad.headlines.add()
                ad_headline.text = headline
                ad_headline.pin_status = self.client.get_type('PinStatusEnum').UNPINNED

            for description in descriptions:
                ad_description = responsive_search_ad.descriptions.add()
                ad_description.text = description

            # Set URL and tracking
            ad_group_ad.ad.final_urls.append(final_url)
            ad_group_ad.ad.tracking_url_template = (
                "{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}"
                "&utm_adgroup={adgroupid}&utm_term={keyword}"
            )

            # Add ad
            ad_response = ad_group_ad_service.mutate_ad_group_ads(
                customer_id=self.customer_id,
                operations=[ad_group_ad_operation]
            )

            logger.info(f"Created responsive search ad with resource name: "
                      f"{ad_response.results[0].resource_name}")
            return ad_response.results[0].resource_name

        except GoogleAdsException as ex:
            logger.error(f"Failed to create responsive search ad: {ex}")
            raise

    def add_conversion_tracking(self, conversion_name, category, value_settings=None):
        """
        Add conversion tracking for lead generation.
        
        Args:
            conversion_name (str): Name for the conversion action
            category (str): Conversion category (e.g., 'LEAD')
            value_settings (dict): Optional settings for conversion value
        Returns:
            str: Resource name of the conversion action
        """
        try:
            conversion_action_service = self.client.get_service('ConversionActionService')

            # Create conversion action
            conversion_action_operation = self.client.get_type('ConversionActionOperation')
            conversion_action = conversion_action_operation.create
            conversion_action.name = conversion_name
            conversion_action.type = self.client.get_type('ConversionActionTypeEnum').UPLOAD_CLICKS
            conversion_action.category = self.client.get_type(
                'ConversionActionCategoryEnum').value[category]

            # Set value if provided
            if value_settings:
                conversion_action.value_settings.default_value = value_settings.get('default_value', 0)
                conversion_action.value_settings.always_use_default_value = value_settings.get(
                    'always_use_default_value', True)

            # Add conversion action
            conversion_response = conversion_action_service.mutate_conversion_actions(
                customer_id=self.customer_id,
                operations=[conversion_action_operation]
            )

            logger.info(f"Created conversion action {conversion_name} with resource name: "
                      f"{conversion_response.results[0].resource_name}")
            return conversion_response.results[0].resource_name

        except GoogleAdsException as ex:
            logger.error(f"Failed to create conversion action: {ex}")
            raise

    def _get_lead_conversion_action(self):
        """Helper method to get the lead conversion action resource name."""
        # In a real implementation, this would query or create the appropriate conversion action
        return "customers/{}/conversionActions/123456789".format(self.customer_id)

    def get_campaign_performance(self, campaign_resource_name, days=7):
        """
        Get performance metrics for a campaign focused on lead generation.
