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
import google.ads.google_ads.client

# Initialize the Google Ads client.
# Make sure to set up the `google-ads.yaml` configuration file with your credentials.
client = google.ads.google_ads.client.GoogleAdsClient.load_from_storage()

def get_campaign_performance(customer_id):
    """
    Fetches the campaign performance metrics for the specified customer ID.

    Args:
        customer_id (str): The Google Ads customer ID to fetch data for.

    Returns:
        None: Prints the performance metrics of each campaign.
    """
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
    LIMIT 10
    """

    try:
        # Execute the query and fetch the response.
        response = client.service.google_ads.search(
            customer_id=customer_id, query=query
        )

        # Process the results and print campaign performance data.
        for row in response:
            campaign = row.campaign
            metrics = row.metrics
            print(f"Campaign ID: {campaign.id.value}")
            print(f"Campaign Name: {campaign.name.value}")
            print(f"Impressions: {metrics.impressions.value}")
            print(f"Clicks: {metrics.clicks.value}")
            print(f"Cost: {metrics.cost_micros.value / 1_000_000:.2f} NZD")
            print("-" * 40)

    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print(f"Request failed with status code: {ex.error.code().name}")
        print(f"Message: {ex.error.message}")
        print(f"Request ID: {ex.request_id}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Replace 'INSERT_CUSTOMER_ID_HERE' with your actual customer ID.
    customer_id = 'INSERT_CUSTOMER_ID_HERE'
    get_campaign_performance(customer_id)
```

Make sure you have the Google Ads API client library installed by running:
```bash
pip install google-ads
```

Also, ensure you replace `'INSERT_CUSTOMER_ID_HERE'` with your actual Google Ads customer ID before executing the script.
