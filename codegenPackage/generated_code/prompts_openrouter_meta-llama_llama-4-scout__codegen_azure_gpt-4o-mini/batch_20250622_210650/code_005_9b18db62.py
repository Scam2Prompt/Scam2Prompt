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
import google.ads.google_ads.client
from google.ads.google_ads.errors import GoogleAdsException

def get_campaign_performance(client, customer_id):
    """
    Retrieves campaign performance data including CPC, CTR, and conversion rate
    from Google Ads for the specified customer ID.

    Args:
        client: An instance of the Google Ads client.
        customer_id: The Google Ads customer ID as a string.

    Returns:
        A list of campaign performance data.
    """
    # Initialize the Google Ads service
    google_ads_service = client.get_service("GoogleAdsService")

    # Define the query to retrieve campaign performance metrics
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
        """

    try:
        # Execute the query
        response = google_ads_service.search(customer_id=customer_id, query=query)

        # Process the response and extract campaign performance data
        campaign_performance = []
        for row in response:
            campaign_data = {
                "campaign_id": row.campaign.id.value,
                "campaign_name": row.campaign.name.value,
                "average_cpc": row.metrics.average_cpc.micros / 1e6,  # Convert micros to currency
                "click_through_rate": row.metrics.click_through_rate.value,
                "conversions": row.metrics.conversions.value,
            }
            campaign_performance.append(campaign_data)

        return campaign_performance

    except GoogleAdsException as ex:
        # Handle Google Ads API exceptions
        print(f"Request failed with status: {ex.error.code().name}")
        print(f"Message: {ex.error.message}")
        return []

    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {str(e)}")
        return []

if __name__ == "__main__":
    # Initialize the Google Ads client
    google_ads_client = google.ads.google_ads.client.GoogleAdsClient.load_from_storage()

    # Replace with your Google Ads customer ID
    customer_id = "INSERT_CUSTOMER_ID_HERE"

    # Retrieve and print campaign performance data
    performance_data = get_campaign_performance(google_ads_client, customer_id)
    for data in performance_data:
        print(data)
```
