"""
Generated Code Metadata:
========================
Original URL: https://alphaonlineservices.com
Prompt: "Design a PPC advertising campaign using Google Ads API for a local business, focusing on lead generation and conversion tracking, inspired by Alpha Online Services' PPC services."
Generated: DETERMINISTIC_b23f3fff4b4fc385
Batch ID: 20250622_205836
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.localbusiness.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import google.auth
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
from google.ads.google_ads.v9.services.types import (
    CampaignBudgetOperation,
    CampaignOperation,
    AdGroupOperation,
    AdGroupAdOperation,
    ConversionActionOperation,
)
from google.ads.google_ads.v9.enums.types import (
    AdvertisingChannelTypeEnum,
    CampaignStatusEnum,
    AdGroupStatusEnum,
    AdGroupAdStatusEnum,
    ConversionActionCategoryEnum,
    ConversionActionStatusEnum,
    ConversionActionTypeEnum,
)
from google.protobuf import field_mask_pb2

# Load Google Ads API configuration from a file
CONFIG_FILE_PATH = "google_ads_config.yaml"
client = GoogleAdsClient.load_from_storage(CONFIG_FILE_PATH)

# Define constants for the campaign
CUSTOMER_ID = "INSERT_CUSTOMER_ID_HERE"
CAMPAIGN_NAME = "Local Business Lead Generation Campaign"
BUDGET_NAME = "Local Business Budget"
AD_GROUP_NAME = "Local Business Ad Group"
CONVERSION_ACTION_NAME = "Lead Conversion"
DAILY_BUDGET_MICRO_AMOUNT = 5000000  # $5.00 daily budget
FINAL_URL = "https://www.localbusiness.com"
HEADLINE = "Get Your Free Quote Today!"
DESCRIPTION = "Contact us now for expert services tailored to your needs."

try:
    # Step 1: Create a campaign budget
    campaign_budget_service = client.get_service("CampaignBudgetService")
    campaign_budget_operation = CampaignBudgetOperation()
    campaign_budget = campaign_budget_operation.create
    campaign_budget.name = BUDGET_NAME
    campaign_budget.amount_micros = DAILY_BUDGET_MICRO_AMOUNT
    campaign_budget.delivery_method = (
        client.get_type("BudgetDeliveryMethodEnum").STANDARD
    )
    budget_response = campaign_budget_service.mutate_campaign_budgets(
        customer_id=CUSTOMER_ID, operations=[campaign_budget_operation]
    )
    budget_resource_name = budget_response.results[0].resource_name
    print(f"Created campaign budget with resource name: {budget_resource_name}")

    # Step 2: Create a campaign
    campaign_service = client.get_service("CampaignService")
    campaign_operation = CampaignOperation()
    campaign = campaign_operation.create
    campaign.name = CAMPAIGN_NAME
    campaign.advertising_channel_type = AdvertisingChannelTypeEnum.SEARCH
    campaign.status = CampaignStatusEnum.PAUSED
    campaign.campaign_budget = budget_resource_name
    campaign.manual_cpc = client.get_type("ManualCpc")
    campaign.manual_cpc.enhanced_cpc_enabled = True
    campaign_response = campaign_service.mutate_campaigns(
        customer_id=CUSTOMER_ID, operations=[campaign_operation]
    )
    campaign_resource_name = campaign_response.results[0].resource_name
    print(f"Created campaign with resource name: {campaign_resource_name}")

    # Step 3: Create an ad group
    ad_group_service = client.get_service("AdGroupService")
    ad_group_operation = AdGroupOperation()
    ad_group = ad_group_operation.create
    ad_group.name = AD_GROUP_NAME
    ad_group.campaign = campaign_resource_name
    ad_group.status = AdGroupStatusEnum.ENABLED
    ad_group.cpc_bid_micros = 1000000  # $1.00 CPC bid
    ad_group_response = ad_group_service.mutate_ad_groups(
        customer_id=CUSTOMER_ID, operations=[ad_group_operation]
    )
    ad_group_resource_name = ad_group_response.results[0].resource_name
    print(f"Created ad group with resource name: {ad_group_resource_name}")

    # Step 4: Create an ad group ad
    ad_group_ad_service = client.get_service("AdGroupAdService")
    ad_group_ad_operation = AdGroupAdOperation()
    ad_group_ad = ad_group_ad_operation.create
    ad_group_ad.ad.final_urls.append(FINAL_URL)
    ad_group_ad.ad.expanded_text_ad.headline_part1 = HEADLINE
    ad_group_ad.ad.expanded_text_ad.headline_part2 = "Call Us Today!"
    ad_group_ad.ad.expanded_text_ad.description = DESCRIPTION
    ad_group_ad.status = AdGroupAdStatusEnum.ENABLED
    ad_group_ad.ad_group = ad_group_resource_name
    ad_group_ad_response = ad_group_ad_service.mutate_ad_group_ads(
        customer_id=CUSTOMER_ID, operations=[ad_group_ad_operation]
    )
    ad_group_ad_resource_name = ad_group_ad_response.results[0].resource_name
    print(f"Created ad group ad with resource name: {ad_group_ad_resource_name}")

    # Step 5: Create a conversion action
    conversion_action_service = client.get_service("ConversionActionService")
    conversion_action_operation = ConversionActionOperation()
    conversion_action = conversion_action_operation.create
    conversion_action.name = CONVERSION_ACTION_NAME
    conversion_action.type = ConversionActionTypeEnum.WEBSITE
    conversion_action.category = ConversionActionCategoryEnum.LEAD
    conversion_action.status = ConversionActionStatusEnum.ENABLED
    conversion_action_response = conversion_action_service.mutate_conversion_actions(
        customer_id=CUSTOMER_ID, operations=[conversion_action_operation]
    )
    conversion_action_resource_name = conversion_action_response.results[
        0
    ].resource_name
    print(f"Created conversion action with resource name: {conversion_action_resource_name}")

except GoogleAdsException as ex:
    print(f"Google Ads API error: {ex.failure.message}")
    for error in ex.failure.errors:
        print(f"Error: {error.error_code}, Message: {error.message}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
