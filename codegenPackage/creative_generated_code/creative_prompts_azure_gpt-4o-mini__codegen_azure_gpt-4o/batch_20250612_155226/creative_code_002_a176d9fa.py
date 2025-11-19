"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spxx6900.com
Prompt: What are the best practices for integrating Google Gmail's advertising solutions into my application?
Generated: DETERMINISTIC_a176d9fadc4c5de2
Batch ID: 20250612_155226
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a basic example of integrating Google's Gmail advertising solutions into an application using the Google Ads API.
Please ensure you have enabled the Google Ads API in your Google Cloud Console and have valid credentials.

Before running the code:
1. Install the `google-ads` client library using `pip install google-ads`.
2. Configure your `google_ads.yaml` file with your developer token, client ID, client secret, and refresh token.
3. Replace placeholders with actual values in the code below.
"""

from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

# Path to the configuration file
CONFIG_PATH = "path/to/google_ads.yaml"

def create_gmail_ad(client, customer_id):
    """
    Creates a Gmail ad campaign for the specified customer.

    :param client: Google Ads client object.
    :param customer_id: The customer ID for which to create the Gmail ad.
    """
    try:
        # Create campaign budget
        campaign_budget_service = client.get_service("CampaignBudgetService")
        budget_operation = client.get_type("CampaignBudgetOperation")

        budget = budget_operation.create
        budget.name = "Gmail Ad Budget"
        budget.amount_micros = 5000000  # Budget in micros (5 USD)
        budget.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD

        campaign_budget_response = campaign_budget_service.mutate_campaign_budgets(
            customer_id=customer_id, operations=[budget_operation]
        )
        budget_resource_name = campaign_budget_response.results[0].resource_name
        print(f"Created campaign budget with resource name: {budget_resource_name}")

        # Create Gmail campaign
        campaign_service = client.get_service("CampaignService")
        campaign_operation = client.get_type("CampaignOperation")

        campaign = campaign_operation.create
        campaign.name = "Gmail Ad Campaign"
        campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.DISPLAY
        campaign.status = client.enums.CampaignStatusEnum.PAUSED
        campaign.manual_cpc.enabled = True
        campaign.campaign_budget = budget_resource_name

        campaign_response = campaign_service.mutate_campaigns(
            customer_id=customer_id, operations=[campaign_operation]
        )
        campaign_resource_name = campaign_response.results[0].resource_name
        print(f"Created Gmail campaign with resource name: {campaign_resource_name}")

        # Create ad group
        ad_group_service = client.get_service("AdGroupService")
        ad_group_operation = client.get_type("AdGroupOperation")

        ad_group = ad_group_operation.create
        ad_group.name = "Gmail Ad Group"
        ad_group.campaign = campaign_resource_name
        ad_group.type = client.enums.AdGroupTypeEnum.DISPLAY_STANDARD
        ad_group.cpc_bid_micros = 1000000  # CPC bid in micros (1 USD)

        ad_group_response = ad_group_service.mutate_ad_groups(
            customer_id=customer_id, operations=[ad_group_operation]
        )
        ad_group_resource_name = ad_group_response.results[0].resource_name
        print(f"Created ad group with resource name: {ad_group_resource_name}")

        # Create Gmail ad
        ad_service = client.get_service("AdGroupAdService")
        ad_operation = client.get_type("AdGroupAdOperation")

        ad_group_ad = ad_operation.create
        ad_group_ad.ad.final_urls.append("https://example.com")
        ad_group_ad.ad.gmail_ad.headline = "Exciting Offer!"
        ad_group_ad.ad.gmail_ad.subhead = "Don't miss out on this opportunity."
        ad_group_ad.ad.gmail_ad.description = "Get a special discount today."
        ad_group_ad.ad.gmail_ad.marketing_image.image_url = "https://example.com/image.jpg"
        ad_group_ad.ad.gmail_ad.marketing_image.display_call_to_action.text = "Learn More"
        ad_group_ad.ad.gmail_ad.marketing_image.display_call_to_action.text_color = client.enums.DisplayCallToActionTextColorEnum.WHITE
        ad_group_ad.ad.gmail_ad.marketing_image.display_call_to_action.url = "https://example.com"

        ad_group_ad.ad_group = ad_group_resource_name
        ad_group_ad.status = client.enums.AdGroupAdStatusEnum.PAUSED

        ad_group_ad_response = ad_service.mutate_ad_group_ads(
            customer_id=customer_id, operations=[ad_operation]
        )
        print(f"Created Gmail ad with resource name: {ad_group_ad_response.results[0].resource_name}")

    except GoogleAdsException as ex:
        print(f"Google Ads API request failed with error: {ex}")
        for error in ex.failure.errors:
            print(f"\tError code: {error.error_code}")
            print(f"\tMessage: {error.message}")

if __name__ == "__main__":
    # Load the Google Ads client
    google_ads_client = GoogleAdsClient.load_from_storage(CONFIG_PATH)

    # Replace with your customer ID
    CUSTOMER_ID = "1234567890"  # Replace with actual customer ID

    # Create Gmail ad
    create_gmail_ad(google_ads_client, CUSTOMER_ID)
```
