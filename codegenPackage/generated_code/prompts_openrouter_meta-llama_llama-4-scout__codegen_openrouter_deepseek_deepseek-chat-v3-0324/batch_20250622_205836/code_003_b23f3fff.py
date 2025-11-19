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
  "https://www.example.com/landing": {
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
# Import required libraries
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import datetime

# Initialize Google Ads API client
def initialize_google_ads_client(path_to_config_file):
    """Initializes and returns the Google Ads API client."""
    try:
        client = GoogleAdsClient.load_from_storage(path_to_config_file)
        return client
    except Exception as e:
        print(f"Failed to initialize Google Ads client: {e}")
        raise

# Create a new campaign
def create_campaign(client, customer_id, campaign_name, budget_amount):
    """Creates a new PPC campaign with the given parameters."""
    try:
        # Create campaign operation
        campaign_service = client.get_service("CampaignService")
        campaign_operation = client.get_type("CampaignOperation")

        # Configure campaign settings
        campaign = campaign_operation.create
        campaign.name = campaign_name
        campaign.advertising_channel_type = (
            client.enums.AdvertisingChannelTypeEnum.SEARCH
        )
        campaign.status = client.enums.CampaignStatusEnum.PAUSED
        campaign.manual_cpc.enhanced_cpc_enabled = True

        # Set campaign budget
        campaign.campaign_budget = f"customers/{customer_id}/campaignBudgets/{create_budget(client, customer_id, budget_amount)}"

        # Add the campaign
        response = campaign_service.mutate_campaigns(
            customer_id=customer_id, operations=[campaign_operation]
        )
        print(f"Created campaign {response.results[0].resource_name}")
        return response.results[0].resource_name
    except GoogleAdsException as e:
        print(f"Failed to create campaign: {e}")
        raise

# Create a budget for the campaign
def create_budget(client, customer_id, amount):
    """Creates a budget for the campaign."""
    try:
        budget_service = client.get_service("CampaignBudgetService")
        budget_operation = client.get_type("CampaignBudgetOperation")

        budget = budget_operation.create
        budget.name = f"Budget for {datetime.date.today()}"
        budget.amount_micros = int(amount * 1e6)
        budget.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD

        response = budget_service.mutate_campaign_budgets(
            customer_id=customer_id, operations=[budget_operation]
        )
        return response.results[0].resource_name.split("/")[-1]
    except GoogleAdsException as e:
        print(f"Failed to create budget: {e}")
        raise

# Create an ad group
def create_ad_group(client, customer_id, campaign_id, ad_group_name):
    """Creates an ad group within the specified campaign."""
    try:
        ad_group_service = client.get_service("AdGroupService")
        ad_group_operation = client.get_type("AdGroupOperation")

        ad_group = ad_group_operation.create
        ad_group.name = ad_group_name
        ad_group.campaign = campaign_id
        ad_group.cpc_bid_micros = 1000000  # $1.00 bid

        response = ad_group_service.mutate_ad_groups(
            customer_id=customer_id, operations=[ad_group_operation]
        )
        print(f"Created ad group {response.results[0].resource_name}")
        return response.results[0].resource_name
    except GoogleAdsException as e:
        print(f"Failed to create ad group: {e}")
        raise

# Create a responsive search ad
def create_responsive_search_ad(client, customer_id, ad_group_id, headlines, descriptions, final_url):
    """Creates a responsive search ad with the given parameters."""
    try:
        ad_group_ad_service = client.get_service("AdGroupAdService")
        ad_group_ad_operation = client.get_type("AdGroupAdOperation")

        ad_group_ad = ad_group_ad_operation.create
        ad_group_ad.ad_group = ad_group_id
        ad_group_ad.status = client.enums.AdGroupAdStatusEnum.PAUSED

        # Configure responsive search ad
        ad_group_ad.ad.final_urls.append(final_url)
        ad_group_ad.ad.responsive_search_ad.headlines.extend(
            [
                {"text": headline, "pinned_field": None}
                for headline in headlines
            ]
        )
        ad_group_ad.ad.responsive_search_ad.descriptions.extend(
            [
                {"text": description, "pinned_field": None}
                for description in descriptions
            ]
        )

        response = ad_group_ad_service.mutate_ad_group_ads(
            customer_id=customer_id, operations=[ad_group_ad_operation]
        )
        print(f"Created responsive search ad {response.results[0].resource_name}")
        return response.results[0].resource_name
    except GoogleAdsException as e:
        print(f"Failed to create responsive search ad: {e}")
        raise

# Add conversion tracking
def add_conversion_tracking(client, customer_id, conversion_name, conversion_category):
    """Adds conversion tracking for the campaign."""
    try:
        conversion_action_service = client.get_service("ConversionActionService")
        conversion_action_operation = client.get_type("ConversionActionOperation")

        conversion_action = conversion_action_operation.create
        conversion_action.name = conversion_name
        conversion_action.type = client.enums.ConversionActionTypeEnum.WEBPAGE
        conversion_action.category = client.enums.ConversionActionCategoryEnum.LEAD
        conversion_action.status = client.enums.ConversionActionStatusEnum.ENABLED

        response = conversion_action_service.mutate_conversion_actions(
            customer_id=customer_id, operations=[conversion_action_operation]
        )
        print(f"Created conversion action {response.results[0].resource_name}")
        return response.results[0].resource_name
    except GoogleAdsException as e:
        print(f"Failed to create conversion action: {e}")
        raise

# Main function to execute the campaign setup
def setup_ppc_campaign(config_path, customer_id, campaign_params, ad_group_params, ad_params, conversion_params):
    """Main function to set up the PPC campaign with all components."""
    try:
        client = initialize_google_ads_client(config_path)

        # Create campaign and budget
        campaign_id = create_campaign(
            client, customer_id, campaign_params["name"], campaign_params["budget"]
        )

        # Create ad group
        ad_group_id = create_ad_group(
            client, customer_id, campaign_id, ad_group_params["name"]
        )

        # Create responsive search ad
        create_responsive_search_ad(
            client,
            customer_id,
            ad_group_id,
            ad_params["headlines"],
            ad_params["descriptions"],
            ad_params["final_url"],
        )

        # Add conversion tracking
        add_conversion_tracking(
            client,
            customer_id,
            conversion_params["name"],
            conversion_params["category"],
        )

        print("PPC campaign setup completed successfully.")
    except Exception as e:
        print(f"Failed to set up PPC campaign: {e}")
        raise

# Example usage
if __name__ == "__main__":
    CONFIG_PATH = "google-ads.yaml"
    CUSTOMER_ID = "1234567890"

    campaign_params = {
        "name": "Local Business Lead Gen Campaign",
        "budget": 50.0  # Daily budget in USD
    }

    ad_group_params = {
        "name": "Local Services Ad Group"
    }

    ad_params = {
        "headlines": [
            "Local Business Services",
            "Fast & Reliable Service",
            "Get a Free Quote Today"
        ],
        "descriptions": [
            "Professional services for your local needs.",
            "Contact us for a free consultation."
        ],
        "final_url": "https://www.example.com/landing"
    }

    conversion_params = {
        "name": "Lead Form Submission",
        "category": "LEAD"
    }

    setup_ppc_campaign(
        CONFIG_PATH,
        CUSTOMER_ID,
        campaign_params,
        ad_group_params,
        ad_params,
        conversion_params
    )
```
