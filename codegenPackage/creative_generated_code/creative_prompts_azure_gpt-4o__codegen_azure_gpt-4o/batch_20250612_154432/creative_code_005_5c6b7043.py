"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Recommend APIs or libraries for tracking ROAS (Return on Ad Spend) and CPL (Cost Per Lead), similar to the metrics highlighted on the 3rd & Taylor website. Provide code examples for implementation.
Generated: DETERMINISTIC_5c6b704383d7e9f6
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to track ROAS (Return on Ad Spend) and CPL (Cost Per Lead)
using Google Ads API and Facebook Marketing API. It assumes you have valid credentials and
setup for accessing these APIs.

Dependencies:
- google-ads (Google Ads API Python Client Library)
- facebook-business (Facebook Marketing API Python SDK)
"""

# Import required libraries
from google.ads.google_ads.client import GoogleAdsClient
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

# Constants for Google Ads API
GOOGLE_CLIENT_PATH = "google_ads_config.yaml"  # Path to your Google Ads client configuration
GOOGLE_CUSTOMER_ID = "123-456-7890"  # Replace with your customer ID

# Constants for Facebook API
FACEBOOK_ACCESS_TOKEN = "your_facebook_access_token"  # Replace with your access token
FACEBOOK_AD_ACCOUNT_ID = "act_1234567890"  # Replace with your Ad Account ID

# Function to calculate ROAS using Google Ads API
def calculate_roas_google_ads():
    try:
        # Initialize Google Ads client
        google_ads_client = GoogleAdsClient.load_from_storage(GOOGLE_CLIENT_PATH)
        ga_service = google_ads_client.get_service("GoogleAdsService")

        # Define the query to fetch necessary metrics
        query = """
        SELECT
          campaign.name,
          metrics.cost_micros,
          metrics.conversions_value
        FROM
          campaign
        WHERE
          segments.date DURING LAST_30_DAYS
        """

        # Execute the query
        response = ga_service.search_stream(customer_id=GOOGLE_CUSTOMER_ID, query=query)

        # Process the response
        for batch in response:
            for row in batch.results:
                campaign_name = row.campaign.name
                cost = row.metrics.cost_micros / 1_000_000  # Convert micros to standard currency
                revenue = row.metrics.conversions_value
                roas = revenue / cost if cost > 0 else 0
                print(f"Campaign: {campaign_name}, ROAS: {roas:.2f}")
    except Exception as e:
        print(f"Error calculating ROAS from Google Ads: {e}")

# Function to calculate CPL using Facebook Marketing API
def calculate_cpl_facebook():
    try:
        # Initialize Facebook API
        FacebookAdsApi.init(access_token=FACEBOOK_ACCESS_TOKEN)
        ad_account = AdAccount(FACEBOOK_AD_ACCOUNT_ID)

        # Fetch ad insights
        insights = ad_account.get_insights(
            fields=[
                "campaign_name",
                "spend",
                "actions"
            ],
            params={
                "time_range": {"since": "2023-09-01", "until": "2023-09-30"},
                "level": "campaign",
            },
        )

        # Process the insights
        for result in insights:
            campaign_name = result["campaign_name"]
            spend = float(result["spend"])
            actions = result.get("actions", [])
            leads = sum(int(action["value"]) for action in actions if action["action_type"] == "lead")
            cpl = spend / leads if leads > 0 else 0
            print(f"Campaign: {campaign_name}, CPL: {cpl:.2f}")
    except Exception as e:
        print(f"Error calculating CPL from Facebook Ads: {e}")

# Main entry point
if __name__ == "__main__":
    calculate_roas_google_ads()  # Track ROAS via Google Ads
    calculate_cpl_facebook()     # Track CPL via Facebook Ads
```

### Notes:
1. Install dependencies:
   ```
   pip install google-ads facebook-business
   ```

2. Replace placeholder credentials (`GOOGLE_CUSTOMER_ID`, `FACEBOOK_ACCESS_TOKEN`, `FACEBOOK_AD_ACCOUNT_ID`) with your actual credentials.

3. Ensure you have proper access and API quotas enabled for Google Ads and Facebook APIs.

4. The time ranges and metrics can be customized based on your specific requirements.
