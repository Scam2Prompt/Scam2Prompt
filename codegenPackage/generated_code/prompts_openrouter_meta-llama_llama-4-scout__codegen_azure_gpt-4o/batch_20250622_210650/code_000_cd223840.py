"""
Generated Code Metadata:
========================
Original URL: https://efficiencydigitalmarketing.com.br
Prompt: "Write a Python script to manage Google Ads campaigns using the Google Ads API, focusing on optimizing performance and return on investment (ROI)."
Generated: DETERMINISTIC_cd22384072c71ba8
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

# Load the Google Ads API configuration from the google-ads.yaml file
# Ensure you have set up the configuration file with your credentials
CONFIG_FILE_PATH = "google-ads.yaml"

def main():
    try:
        # Initialize the Google Ads client
        client = GoogleAdsClient.load_from_storage(CONFIG_FILE_PATH)

        # Define the customer ID (replace with your Google Ads account ID)
        customer_id = "INSERT_CUSTOMER_ID"

        # Fetch campaign performance data
        campaigns = get_campaign_performance(client, customer_id)

        # Optimize campaigns based on performance metrics
        optimize_campaigns(client, customer_id, campaigns)

    except GoogleAdsException as ex:
        handle_google_ads_exception(ex)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def get_campaign_performance(client, customer_id):
    """
    Fetches campaign performance data for the given customer ID.

    Args:
        client: The Google Ads client instance.
        customer_id: The Google Ads account ID.

    Returns:
        A list of campaigns with their performance metrics.
    """
    query = """
        SELECT
            campaign.id,
            campaign.name,
            metrics.clicks,
            metrics.impressions,
            metrics.cost_micros,
            metrics.conversions
        FROM
            campaign
        WHERE
            campaign.status = 'ENABLED'
        ORDER BY
            metrics.conversions DESC
    """

    try:
        ga_service = client.get_service("GoogleAdsService")
        response = ga_service.search(customer_id=customer_id, query=query)

        campaigns = []
        for row in response:
            campaigns.append({
                "id": row.campaign.id,
                "name": row.campaign.name,
                "clicks": row.metrics.clicks,
                "impressions": row.metrics.impressions,
                "cost_micros": row.metrics.cost_micros,
                "conversions": row.metrics.conversions,
            })

        return campaigns

    except GoogleAdsException as ex:
        handle_google_ads_exception(ex)

def optimize_campaigns(client, customer_id, campaigns):
    """
    Optimizes campaigns based on performance metrics.

    Args:
        client: The Google Ads client instance.
        customer_id: The Google Ads account ID.
        campaigns: A list of campaigns with their performance metrics.
    """
    campaign_service = client.get_service("CampaignService")

    for campaign in campaigns:
        # Example optimization: Pause campaigns with low ROI
        if campaign["conversions"] < 10 and campaign["cost_micros"] > 1000000:
            campaign_operation = client.get_type("CampaignOperation")
            campaign_operation.update.resource_name = campaign_service.campaign_path(customer_id, campaign["id"])
            campaign_operation.update.status = client.enums.CampaignStatusEnum.PAUSED
            campaign_operation.update_mask.paths.append("status")

            try:
                campaign_service.mutate_campaigns(customer_id=customer_id, operations=[campaign_operation])
                print(f"Paused campaign '{campaign['name']}' due to low ROI.")
            except GoogleAdsException as ex:
                handle_google_ads_exception(ex)

def handle_google_ads_exception(exception):
    """
    Handles Google Ads API exceptions.

    Args:
        exception: The GoogleAdsException instance.
    """
    print(f"Request failed with status '{exception.error.code.name}' and includes the following errors:")
    for error in exception.failure.errors:
        print(f"Error: {error.message}")
        if error.location:
            for field_path_element in error.location.field_path_elements:
                print(f"On field: {field_path_element.field_name}")
    sys.exit(1)

if __name__ == "__main__":
    main()
```

**Note:** Before running this script, ensure you have installed the `google-ads` Python library (`pip install google-ads`) and configured the `google-ads.yaml` file with your credentials. Replace `INSERT_CUSTOMER_ID` with your actual Google Ads account ID.
