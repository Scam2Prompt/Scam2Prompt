"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Provide a step-by-step guide to set up and optimize paid advertising campaigns on Google Ads for businesses targeting the Jordanian market, similar to IDEX Marketing's PPC services.
Generated: DETERMINISTIC_8bd8076e353d3118
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Google Ads Campaign Setup and Optimization Script for Jordanian Market
# Inspired by IDEX Marketing's PPC Services

import pandas as pd
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
from datetime import datetime, timedelta

class GoogleAdsCampaignManager:
    def __init__(self, credentials_path, developer_token, customer_id):
        """
        Initialize Google Ads client with credentials.
        
        Args:
            credentials_path (str): Path to Google Ads API credentials JSON file
            developer_token (str): Google Ads developer token
            customer_id (str): Google Ads customer ID
        """
        self.credentials = {
            'developer_token': developer_token,
            'use_proto_plus': True
        }
        self.customer_id = customer_id
        self.client = GoogleAdsClient.load_from_storage(credentials_path, **self.credentials)
        
    def create_campaign(self, campaign_name, budget, start_date, end_date=None):
        """
        Create a new Google Ads campaign optimized for Jordanian market.
        
        Args:
            campaign_name (str): Name of the campaign
            budget (int): Daily budget in local currency (JOD)
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str, optional): End date in YYYY-MM-DD format
            
        Returns:
            str: ID of the created campaign
        """
        try:
            campaign_budget_service = self.client.get_service('CampaignBudgetService')
            campaign_service = self.client.get_service('CampaignService')
            
            # Create budget
            budget_operation = self.client.get_type('CampaignBudgetOperation')
            budget = budget_operation.create
            budget.name = f"{campaign_name} Budget"
            budget.amount_micros = budget * 1000000  # Convert to micros
            budget.delivery_method = self.client.enums.BudgetDeliveryMethodEnum.STANDARD
            
            # Add budget
            budget_response = campaign_budget_service.mutate_campaign_budgets(
                customer_id=self.customer_id,
                operations=[budget_operation]
            )
            
            # Create campaign
            campaign_operation = self.client.get_type('CampaignOperation')
            campaign = campaign_operation.create
            campaign.name = campaign_name
            campaign.advertising_channel_type = self.client.enums.AdvertisingChannelTypeEnum.SEARCH
            campaign.status = self.client.enums.CampaignStatusEnum.PAUSED  # Start paused for review
            
            # Set targeting for Jordan
            campaign.network_settings.target_google_search = True
            campaign.network_settings.target_search_network = True
            campaign.network_settings.target_content_network = False
            campaign.network_settings.target_partner_search_network = False
            
            # Set budget
            campaign.campaign_budget = budget_response.results[0].resource_name
            
            # Set dates
            campaign.start_date = datetime.strptime(start_date, '%Y-%m-%d').strftime('%Y%m%d')
            if end_date:
                campaign.end_date = datetime.strptime(end_date, '%Y-%m-%d').strftime('%Y%m%d')
            
            # Set location targeting to Jordan
            campaign.geo_target_type_setting.positive_geo_target_type = (
                self.client.enums.PositiveGeoTargetTypeEnum.PRESENCE_OR_INTEREST
            )
            
            # Add campaign
            campaign_response = campaign_service.mutate_campaigns(
                customer_id=self.customer_id,
                operations=[campaign_operation]
            )
            
            return campaign_response.results[0].resource_name
            
        except GoogleAdsException as ex:
            print(f'Request with ID "{ex.request_id}" failed with status "{ex.error.code().name}"')
            print(f'\tError message: {ex.error.message}')
            raise

    def add_ad_group(self, campaign_id, ad_group_name, cpc_bid):
        """
        Add an ad group to a campaign.
        
        Args:
            campaign_id (str): ID of the parent campaign
            ad_group_name (str): Name of the ad group
            cpc_bid (int): CPC bid in local currency (JOD)
            
        Returns:
            str: ID of the created ad group
        """
        try:
            ad_group_service = self.client.get_service('AdGroupService')
            
            # Create ad group
            ad_group_operation = self.client.get_type('AdGroupOperation')
            ad_group = ad_group_operation.create
            ad_group.name = ad_group_name
            ad_group.status = self.client.enums.AdGroupStatusEnum.ENABLED
            ad_group.campaign = campaign_id
            ad_group.type_ = self.client.enums.AdGroupTypeEnum.SEARCH_STANDARD
            ad_group.cpc_bid_micros = cpc_bid * 1000000  # Convert to micros
            
            # Add ad group
            ad_group_response = ad_group_service.mutate_ad_groups(
                customer_id=self.customer_id,
                operations=[ad_group_operation]
            )
            
            return ad_group_response.results[0].resource_name
            
        except GoogleAdsException as ex:
            print(f'Request with ID "{ex.request_id}" failed with status "{ex.error.code().name}"')
            print(f'\tError message: {ex.error.message}')
            raise

    def add_keywords(self, ad_group_id, keywords):
        """
        Add keywords to an ad group.
        
        Args:
            ad_group_id (str): ID of the ad group
            keywords (list): List of keyword dictionaries with 'text' and 'match_type'
                           (match_type can be 'EXACT', 'PHRASE', or 'BROAD')
        """
        try:
            ad_group_criterion_service = self.client.get_service('AdGroupCriterionService')
            operations = []
            
            for keyword in keywords:
                operation = self.client.get_type('AdGroupCriterionOperation')
                criterion = operation.create
                criterion.ad_group = ad_group_id
                criterion.status = self.client.enums.AdGroupCriterionStatusEnum.ENABLED
                criterion.keyword.text = keyword['text']
                criterion.keyword.match_type = getattr(
                    self.client.enums.KeywordMatchTypeEnum,
                    keyword['match_type']
                )
                operations.append(operation)
            
            # Add keywords
            keyword_response = ad_group_criterion_service.mutate_ad_group_criteria(
                customer_id=self.customer_id,
                operations=operations
            )
            
            return keyword_response.results
            
        except GoogleAdsException as ex:
            print(f'Request with ID "{ex.request_id}" failed with status "{ex.error.code().name}"')
            print(f'\tError message: {ex.error.message}')
            raise

    def create_responsive_search_ad(self, ad_group_id, headlines, descriptions, final_url):
        """
        Create a responsive search ad.
        
        Args:
            ad_group_id (str): ID of the ad group
            headlines (list): List of headlines (up to 15)
            descriptions (list): List of descriptions (up to 4)
            final_url (str): Final URL for the ad
        """
        try:
            ad_group_ad_service = self.client.get_service('AdGroupAdService')
            
            # Create ad
            ad_group_ad_operation = self.client.get_type('AdGroupAdOperation')
            ad_group_ad = ad_group_ad_operation.create
            ad_group_ad.ad_group = ad_group_id
            ad_group_ad.status = self.client.enums.AdGroupAdStatusEnum.ENABLED
            
            # Set responsive search ad info
            ad_group_ad.ad.final_urls.append(final_url)
            responsive_search_ad = ad_group_ad.ad.responsive_search_ad
            
            # Add headlines
            for headline_text in headlines[:15]:  # Max 15 headlines
                headline = responsive_search_ad.headlines.add()
                headline.text = headline_text
                headline.pinned_field = self.client.enums.ServedAssetFieldTypeEnum.HEADLINE_1
                
            # Add descriptions
            for description_text in descriptions[:4]:  # Max 4 descriptions
                description = responsive_search_ad.descriptions.add()
                description.text = description_text
                
            # Add ad
            ad_response = ad_group_ad_service.mutate_ad_group_ads(
                customer_id=self.customer_id,
                operations=[ad_group_ad_operation]
            )
            
            return ad_response.results[0].resource_name
            
        except GoogleAdsException as ex:
            print(f'Request with ID "{ex.request_id}" failed with status "{ex.error.code().name}"')
            print(f'\tError message: {ex.error.message}')
            raise

    def optimize_campaign(self, campaign_id, optimization_params):
        """
        Optimize an existing campaign based on performance data.
        
        Args:
            campaign_id (str): ID of the campaign to optimize
            optimization_params (dict): Optimization parameters including:
                - bid_adjustments (dict): Bid adjustments for devices, locations, etc.
                - negative_keywords (list): Negative keywords to add
                - budget_adjustment (float): Percentage to adjust budget (+/-)
        """
        try:
            # Get campaign service
            campaign_service = self.client.get_service('CampaignService')
            
            # Get current campaign
