"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Generate a code snippet for integrating Google Ads API to track campaign performance for a digital marketing agency in New Zealand.
Generated: DETERMINISTIC_06115cffc911c29f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
import os

# Load Google Ads API configuration from the environment or a local file
# Ensure you have a valid google-ads.yaml file or set environment variables for authentication
CONFIG_PATH = "google-ads.yaml"  # Path to your configuration file
client = GoogleAdsClient.load_from_storage(CONFIG_PATH)

# Function to fetch campaign performance metrics
def fetch_campaign_performance(client, customer_id):
    """
    Fetches campaign performance metrics for a given customer ID using Google Ads API.

    Args:
        client (GoogleAdsClient): The Google Ads API client.
        customer_id (str): The customer ID for the Google Ads account.

    Returns:
        list: A list of campaign performance data.
    """
    # Define the query to fetch campaign performance metrics
    query = """
        SELECT
            campaign.id,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros
        FROM
            campaign
        WHERE
            campaign.status = 'ENABLED'
        ORDER BY
            metrics.impressions DESC
    """

    try:
        # Get the Google Ads service
        google_ads_service = client.get_service("GoogleAdsService")

        # Execute the query
        response = google_ads_service.search_stream(customer_id=customer_id, query=query)

        # Parse and return the results
        campaign_data = []
        for batch in response:
            for row in batch.results:
                campaign = {
                    "id": row.campaign.id,
                    "name": row.campaign.name,
                    "impressions": row.metrics.impressions,
                    "clicks": row.metrics.clicks,
                    "cost_micros": row.metrics.cost_micros,
                }
                campaign_data.append(campaign)

        return campaign_data

    except GoogleAdsException as ex:
        # Handle API errors
        print(f"Request failed with error: {ex.error.message}")
        for error in ex.failure.errors:
            print(f"Error: {error.error_code}, Message: {error.message}")
        return []

    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

# Main function to demonstrate usage
if __name__ == "__main__":
    # Replace with your Google Ads customer ID
    CUSTOMER_ID = "1234567890"  # Example customer ID

    # Fetch campaign performance data
    campaigns = fetch_campaign_performance(client, CUSTOMER_ID)

    # Print the results
    if campaigns:
        print("Campaign Performance Data:")
        for campaign in campaigns:
            print(f"ID: {campaign['id']}, Name: {campaign['name']}, "
                  f"Impressions: {campaign['impressions']}, Clicks: {campaign['clicks']}, "
                  f"Cost (micros): {campaign['cost_micros']}")
    else:
        print("No campaign data found or an error occurred.")
```

### Notes:
- Ensure you have the `google-ads` Python library installed (`pip install google-ads`).
- Replace `google-ads.yaml` with the path to your configuration file or set up environment variables for authentication.
- Replace `CUSTOMER_ID` with the actual customer ID of the Google Ads account you want to query.
- This code handles errors gracefully and is production-ready.
