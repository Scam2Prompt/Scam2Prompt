"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Generate a code snippet for integrating Google Ads API to track campaign performance for a digital marketing agency in New Zealand.
Generated: DETERMINISTIC_06115cffc911c29f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import google.auth
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

# Load Google Ads API configuration from a file
# Ensure you have a JSON/YAML configuration file with the required credentials setup
CONFIG_FILE_PATH = "google_ads_config.yaml"

def fetch_campaign_performance_data(customer_id):
    """
    Fetches campaign performance data using the Google Ads API.

    Args:
        customer_id (str): The customer ID of the Google Ads account.

    Returns:
        list: A list of campaign performance metrics.
    """
    try:
        # Initialize the Google Ads Client using the config file
        google_ads_client = GoogleAdsClient.load_from_storage(CONFIG_FILE_PATH)

        # Build the Google Ads query to fetch campaign-level performance data
        # Adjust the fields according to your reporting needs
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

        # Get the Google Ads service
        google_ads_service = google_ads_client.get_service("GoogleAdsService")

        # Execute the query and fetch results
        response = google_ads_service.search_stream(customer_id=customer_id, query=query)

        # Parse and return the results
        campaign_data = []
        for batch in response:
            for row in batch.results:
                campaign_data.append({
                    "campaign_id": row.campaign.id,
                    "campaign_name": row.campaign.name,
                    "impressions": row.metrics.impressions,
                    "clicks": row.metrics.clicks,
                    "cost_micros": row.metrics.cost_micros,
                })

        return campaign_data

    except GoogleAdsException as ex:
        # Handle Google Ads API errors
        print(f"Google Ads API error: {ex.error.message}")
        for error in ex.failure.errors:
            print(f"Error location: {error.location}")
            print(f"Error details: {error.details}")
        return []
    except Exception as e:
        # Handle generic errors
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with the actual customer ID of the Google Ads account
    CUSTOMER_ID = "1234567890"

    # Fetch campaign performance data
    campaigns = fetch_campaign_performance_data(CUSTOMER_ID)

    # Display the fetched campaign data
    for campaign in campaigns:
        print(f"Campaign ID: {campaign['campaign_id']}")
        print(f"Campaign Name: {campaign['campaign_name']}")
        print(f"Impressions: {campaign['impressions']}")
        print(f"Clicks: {campaign['clicks']}")
        print(f"Cost (Micros): {campaign['cost_micros']}")
        print("-" * 40)
```

Make sure to install the required dependencies for the Google Ads API client using `pip install google-ads`, and configure your credentials file (`google_ads_config.yaml`) with appropriate authentication details.
