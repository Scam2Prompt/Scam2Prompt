"""
Generated Code Metadata:
========================
Original URL: https://efficiencydigitalmarketing.com.br
Prompt: "Create a sample API request to retrieve campaign performance data from Google Ads using the Google Ads API, including metrics such as CPC, CTR, and conversion rate."
Generated: DETERMINISTIC_9b18db621c51234a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import google.auth
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

# Load Google Ads API configuration from the google-ads.yaml file
# Ensure you have set up the configuration file with your credentials
google_ads_client = GoogleAdsClient.load_from_storage("google-ads.yaml")

def get_campaign_performance(customer_id):
    """
    Retrieves campaign performance data from Google Ads API.
    
    Args:
        customer_id (str): The Google Ads customer ID.
    
    Returns:
        list: A list of dictionaries containing campaign performance metrics.
    """
    # Define the GAQL query to fetch campaign performance metrics
    query = """
        SELECT
            campaign.id,
            campaign.name,
            metrics.average_cpc,
            metrics.click_through_rate,
            metrics.conversions
        FROM
            campaign
        WHERE
            segments.date DURING LAST_30_DAYS
        ORDER BY
            metrics.click_through_rate DESC
    """

    try:
        # Get the Google Ads service
        google_ads_service = google_ads_client.get_service("GoogleAdsService")

        # Execute the query
        response = google_ads_service.search_stream(customer_id=customer_id, query=query)

        # Parse the response and extract campaign performance data
        campaign_data = []
        for batch in response:
            for row in batch.results:
                campaign_data.append({
                    "campaign_id": row.campaign.id,
                    "campaign_name": row.campaign.name,
                    "average_cpc": row.metrics.average_cpc,
                    "ctr": row.metrics.click_through_rate,
                    "conversions": row.metrics.conversions,
                })

        return campaign_data

    except GoogleAdsException as ex:
        # Handle Google Ads API errors
        print(f"Request failed with error: {ex.error.message}")
        for error in ex.failure.errors:
            print(f"Error: {error.error_code}, Message: {error.message}")
        return []

    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with your Google Ads customer ID
    CUSTOMER_ID = "1234567890"

    # Fetch campaign performance data
    performance_data = get_campaign_performance(CUSTOMER_ID)

    # Print the retrieved data
    for campaign in performance_data:
        print(f"Campaign ID: {campaign['campaign_id']}, Name: {campaign['campaign_name']}, "
              f"Average CPC: {campaign['average_cpc']}, CTR: {campaign['ctr']}, Conversions: {campaign['conversions']}")
```

### Notes:
- Ensure you have installed the `google-ads` Python library (`pip install google-ads`).
- Replace `"google-ads.yaml"` with the path to your configuration file containing Google Ads API credentials.
- Replace `CUSTOMER_ID` with your actual Google Ads customer ID.
