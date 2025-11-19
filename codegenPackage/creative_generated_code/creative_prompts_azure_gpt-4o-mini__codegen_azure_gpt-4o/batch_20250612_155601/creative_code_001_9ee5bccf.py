"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://incentives-usual.com
Prompt: What are the best practices for advertising on Google Gmail to reach business solutions?
Generated: DETERMINISTIC_9ee5bccfb00f6300
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Creating a Google Ads solution for Gmail advertising requires using the Google Ads API and adhering to its usage rules and best practices. Below is a Python script that demonstrates a well-documented and clean code for setting up a Google Ads campaign targeting Gmail users for business solutions. This script uses the `google-ads` Python client library.

```python
# Import required libraries from the Google Ads API client library
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
import os

# Configuration: Replace these values with your Google Ads API credentials
# You must set up the GOOGLE_ADS_CLIENT_PATH environment variable pointing to your config file
CONFIG_PATH = os.getenv('GOOGLE_ADS_CLIENT_PATH')  # Path to the Google Ads API configuration file

# Define constants for the campaign setup
CUSTOMER_ID = '<YOUR_CUSTOMER_ID>'  # Your Google Ads customer ID
CAMPAIGN_NAME = 'Business Solutions - Gmail Advertising'
BUDGET_AMOUNT_MICRO = 5000000  # Budget in micros (e.g., 5,000,000 = $5 daily budget)
GMAIL_CRITERIA = 'Gmail'  # Gmail-specific targeting criteria

def create_gmail_campaign():
    """
    Create a Gmail advertising campaign targeting business solutions.
    """
    try:
        # Initialize the Google Ads client
        client = GoogleAdsClient.load_from_storage(CONFIG_PATH)
        
        # Create a campaign budget
        budget_operation = client.get_type('CampaignBudgetOperation', version='v10')
        campaign_budget = budget_operation.create
        campaign_budget.name = 'Business Solutions Budget'
        campaign_budget.amount_micros = BUDGET_AMOUNT_MICRO
        campaign_budget.delivery_method = client.get_type('BudgetDeliveryMethodEnum', version='v10').STANDARD

        # Send the campaign budget creation request
        campaign_budget_service = client.get_service('CampaignBudgetService', version='v10')
        budget_response = campaign_budget_service.mutate_campaign_budgets(customer_id=CUSTOMER_ID, operations=[budget_operation])
        budget_resource_name = budget_response.results[0].resource_name
        print(f'Created campaign budget with resource name: {budget_resource_name}')
        
        # Create a campaign
        campaign_operation = client.get_type('CampaignOperation', version='v10')
        campaign = campaign_operation.create
        campaign.name = CAMPAIGN_NAME
        campaign.advertising_channel_type = client.get_type('AdvertisingChannelTypeEnum', version='v10').DISPLAY
        campaign.status = client.get_type('CampaignStatusEnum', version='v10').PAUSED
        campaign.campaign_budget = budget_resource_name
        campaign.manual_cpc.enabled = True

        # Add Gmail-specific targeting settings
        campaign.network_settings.target_content_network = True
        campaign.network_settings.target_google_search = False
        campaign.network_settings.target_search_network = False
        
        # Send the campaign creation request
        campaign_service = client.get_service('CampaignService', version='v10')
        campaign_response = campaign_service.mutate_campaigns(customer_id=CUSTOMER_ID, operations=[campaign_operation])
        campaign_resource_name = campaign_response.results[0].resource_name
        print(f'Created campaign with resource name: {campaign_resource_name}')
        
        # Create an ad group for the campaign
        ad_group_operation = client.get_type('AdGroupOperation', version='v10')
        ad_group = ad_group_operation.create
        ad_group.name = 'Business Solutions Ad Group'
        ad_group.status = client.get_type('AdGroupStatusEnum', version='v10').ENABLED
        ad_group.campaign = campaign_resource_name
        ad_group.type = client.get_type('AdGroupTypeEnum', version='v10').DISPLAY_STANDARD
        ad_group.cpc_bid_micros = 1000000  # CPC bid in micros (e.g., 1,000,000 = $1)
        
        # Send the ad group creation request
        ad_group_service = client.get_service('AdGroupService', version='v10')
        ad_group_response = ad_group_service.mutate_ad_groups(customer_id=CUSTOMER_ID, operations=[ad_group_operation])
        ad_group_resource_name = ad_group_response.results[0].resource_name
        print(f'Created ad group with resource name: {ad_group_resource_name}')
        
        print("Successfully created Gmail advertising campaign targeting business solutions.")

    except GoogleAdsException as ex:
        # Handle exceptions from the Google Ads API
        print(f'An error occurred: {ex.failure.message}')
        for error in ex.failure.errors:
            print(f'Error: {error.error_code}')
        raise

# Run the script
if __name__ == "__main__":
    create_gmail_campaign()
```

### Notes:
1. Replace `<YOUR_CUSTOMER_ID>` with your actual Google Ads customer ID.
2. Ensure the `GOOGLE_ADS_CLIENT_PATH` environment variable points to your Google Ads API configuration file containing authentication details.
3. Install the `google-ads` Python client using `pip install google-ads`.
4. Add more specific targeting criteria, creatives, and ad content for Gmail ads based on your business needs.
