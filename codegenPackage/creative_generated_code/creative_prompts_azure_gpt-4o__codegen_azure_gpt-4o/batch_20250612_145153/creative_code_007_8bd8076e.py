"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Provide a step-by-step guide to set up and optimize paid advertising campaigns on Google Ads for businesses targeting the Jordanian market, similar to IDEX Marketing's PPC services.
Generated: DETERMINISTIC_8bd8076e353d3118
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

As your request is related to setting up and optimizing paid advertising campaigns on Google Ads, this task involves programmatically interacting with the Google Ads API. Below is Python code that utilizes the Google Ads API to create and optimize a campaign targeting the Jordanian market:

```python
# Required Libraries
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
import os

# Load Google Ads API configuration file (google-ads.yaml) that contains credentials
google_ads_client = GoogleAdsClient.load_from_storage("google-ads.yaml")

def create_google_ads_campaign(client, customer_id):
    """
    Creates a Google Ads campaign targeting the Jordanian market.
    
    Args:
        client: An instance of GoogleAdsClient.
        customer_id: The Google Ads customer ID.
    """
    try:
        # Define campaign budget
        campaign_budget_service = client.get_service("CampaignBudgetService")
        campaign_budget_operation = client.get_type("CampaignBudgetOperation")
        campaign_budget = campaign_budget_operation.create
        campaign_budget.name = "Jordanian Market Budget"
        campaign_budget.amount_micros = 50000000  # $50.00 daily budget
        campaign_budget.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD
        budget_response = campaign_budget_service.mutate_campaign_budgets(
            customer_id=customer_id, operations=[campaign_budget_operation]
        )
        budget_resource_name = budget_response.results[0].resource_name
        print(f"Created campaign budget with resource name: {budget_resource_name}")

        # Define campaign
        campaign_service = client.get_service("CampaignService")
        campaign_operation = client.get_type("CampaignOperation")
        campaign = campaign_operation.create
        campaign.name = "Jordanian Market Campaign"
        campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
        campaign.status = client.enums.CampaignStatusEnum.PAUSED
        campaign.manual_cpc.enhanced_cpc_enabled = True
        campaign.campaign_budget = budget_resource_name
        campaign.network_settings.target_google_search = True
        campaign.network_settings.target_search_network = True
        campaign.network_settings.target_content_network = False
        campaign.targeting_setting.target_restrictions = False
        campaign.geo_target_type_setting.geo_target_type = client.enums.GeoTargetTypeSettingEnum.LOCATION_OF_PRESENCE

        # Set Jordanian location targeting
        jordanian_location_id = 2392  # GeoTargetConstant ID for Jordan
        campaign.targeting_setting.target_locations.add().geo_target_constant = f"geoTargetConstants/{jordanian_location_id}"

        campaign_response = campaign_service.mutate_campaigns(
            customer_id=customer_id, operations=[campaign_operation]
        )
        campaign_resource_name = campaign_response.results[0].resource_name
        print(f"Created campaign with resource name: {campaign_resource_name}")

        return campaign_resource_name
    except GoogleAdsException as ex:
        print("Error while creating campaign:")
        print(f"Request id: {ex.request_id}")
        print(f"Failure: {ex.failure}")
        print(f"Location: {ex.location}")
        raise

def optimize_google_ads_campaign(client, customer_id, campaign_resource_name):
    """
    Optimizes a Google Ads campaign by adding Ad Groups and Keywords.
    
    Args:
        client: An instance of GoogleAdsClient.
        customer_id: The Google Ads customer ID.
        campaign_resource_name: The resource name of the campaign to optimize.
    """
    try:
        # Create Ad Group
        ad_group_service = client.get_service("AdGroupService")
        ad_group_operation = client.get_type("AdGroupOperation")
        ad_group = ad_group_operation.create
        ad_group.name = "Jordanian Market Ad Group"
        ad_group.campaign = campaign_resource_name
        ad_group.status = client.enums.AdGroupStatusEnum.ENABLED
        ad_group.cpc_bid_micros = 1000000  # $1.00 CPC bid
        ad_group_response = ad_group_service.mutate_ad_groups(
            customer_id=customer_id, operations=[ad_group_operation]
        )
        ad_group_resource_name = ad_group_response.results[0].resource_name
        print(f"Created ad group with resource name: {ad_group_resource_name}")

        # Add Keywords
        ad_group_criterion_service = client.get_service("AdGroupCriterionService")
        keywords = ["digital marketing services", "online advertising Jordan", 
                    "PPC Jordan", "Google Ads experts Jordan"]
        
        operations = []
        for keyword in keywords:
            ad_group_criterion_operation = client.get_type("AdGroupCriterionOperation")
            criterion = ad_group_criterion_operation.create
            criterion.keyword.text = keyword
            criterion.keyword.match_type = client.enums.KeywordMatchTypeEnum.EXACT
            criterion.ad_group = ad_group_resource_name
            criterion.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
            operations.append(ad_group_criterion_operation)

        ad_group_criterion_response = ad_group_criterion_service.mutate_ad_group_criteria(
            customer_id=customer_id, operations=operations
        )
        print("Added keywords to ad group successfully.")
    except GoogleAdsException as ex:
        print("Error while optimizing campaign:")
        print(f"Request id: {ex.request_id}")
        print(f"Failure: {ex.failure}")
        print(f"Location: {ex.location}")
        raise

# Main execution
if __name__ == "__main__":
    # Replace with your Google Ads customer ID
    CUSTOMER_ID = "INSERT_CUSTOMER_ID"
    
    # Step 1: Create Campaign
    campaign_resource_name = create_google_ads_campaign(google_ads_client, CUSTOMER_ID)
    
    # Step 2: Optimize Campaign
    optimize_google_ads_campaign(google_ads_client, CUSTOMER_ID, campaign_resource_name)
```

### Notes:
- Before running this code, ensure you have access to the Google Ads API, set up credentials (`google-ads.yaml`), and installed the `google-ads` Python library (`pip install google-ads`).
- Replace `INSERT_CUSTOMER_ID` with your actual Google Ads customer ID.
- Follow good security practices, such as keeping API credentials safe and not hardcoding sensitive information.
