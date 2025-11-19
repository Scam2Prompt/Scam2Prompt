"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efficiencydigitalmarketing.com.br
Prompt: Write a Python script to automate the management of Google Ads campaigns, focusing on performance optimization as described by Efficiency Digital Marketing.
Generated: DETERMINISTIC_98947a98b6a58076
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Google Ads Campaign Management Script

This script automates the management of Google Ads campaigns, focusing on 
performance optimization. It uses the Google Ads API to retrieve campaign 
performance data, identify underperforming campaigns, and adjust budgets 
or pause campaigns based on pre-defined conditions.

Pre-requisites:
1. Install the Google Ads API Python client library:
   pip install google-ads
2. Set up a Google Ads Developer Token and OAuth credentials.

"""

import sys
from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException


def main(client, customer_id):
    """
    Main function to manage Google Ads campaigns.

    Parameters:
        client (GoogleAdsClient): The Google Ads client instance.
        customer_id (str): Google Ads account customer ID.
    """
    try:
        # Fetch campaigns and their performance metrics
        campaigns = get_campaign_performance(client, customer_id)
        
        for campaign in campaigns:
            # Identify underperforming campaigns
            if is_underperforming(campaign):
                # Optimize the campaign (adjust budget or pause it)
                optimize_campaign(client, customer_id, campaign)
    except GoogleAdsException as ex:
        print(f"Google Ads API request failed: {ex}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_campaign_performance(client, customer_id):
    """
    Retrieve performance metrics for all campaigns in the specified account.

    Parameters:
        client (GoogleAdsClient): The Google Ads client instance.
        customer_id (str): Google Ads account customer ID.

    Returns:
        list: A list of campaign performance data.
    """
    query = """
        SELECT campaign.id, campaign.name, metrics.clicks, metrics.impressions, metrics.cost_micros
        FROM campaign
        WHERE campaign.status = 'ENABLED'
    """
    response = client.service.google_ads.search_stream(customer_id=customer_id, query=query)

    campaigns = []
    for batch in response:
        for row in batch.results:
            campaigns.append({
                "id": row.campaign.id,
                "name": row.campaign.name,
                "clicks": row.metrics.clicks,
                "impressions": row.metrics.impressions,
                "cost_micros": row.metrics.cost_micros
            })
    return campaigns


def is_underperforming(campaign):
    """
    Determine if a campaign is underperforming based on performance thresholds.

    Parameters:
        campaign (dict): Campaign performance data.

    Returns:
        bool: True if the campaign is underperforming, False otherwise.
    """
    # Define performance thresholds
    MIN_CLICKS = 50
    MIN_IMPRESSIONS = 1000
    MAX_COST_MICROS = 50000000  # 50 USD

    return (
        campaign["clicks"] < MIN_CLICKS or
        campaign["impressions"] < MIN_IMPRESSIONS or
        campaign["cost_micros"] > MAX_COST_MICROS
    )


def optimize_campaign(client, customer_id, campaign):
    """
    Optimize a campaign by adjusting its budget or pausing it.

    Parameters:
        client (GoogleAdsClient): The Google Ads client instance.
        customer_id (str): Google Ads account customer ID.
        campaign (dict): Campaign performance data.
    """
    try:
        # Example logic: Pause the campaign if underperforming
        campaign_service = client.service.campaign
        campaign_operation = client.get_type("CampaignOperation")
        campaign_operation.update.resource_name = campaign_service.campaign_path(customer_id, campaign["id"])
        campaign_operation.update.status = client.enums.CampaignStatusEnum.PAUSED
        campaign_operation.update_mask = client.field_mask(["status"])

        response = campaign_service.mutate_campaigns(customer_id=customer_id, operations=[campaign_operation])
        print(f"Paused campaign {campaign['name']} (ID: {campaign['id']}).")
    except GoogleAdsException as ex:
        print(f"Failed to optimize campaign {campaign['name']} (ID: {campaign['id']}): {ex}")
    except Exception as e:
        print(f"An unexpected error occurred while optimizing campaign {campaign['name']} (ID: {campaign['id']}): {e}")


if __name__ == "__main__":
    # Load Google Ads client configuration from google-ads.yaml
    try:
        google_ads_client = GoogleAdsClient.load_from_storage("google-ads.yaml")
        # Replace with your Google Ads customer ID
        CUSTOMER_ID = "INSERT_CUSTOMER_ID_HERE"
        main(google_ads_client, CUSTOMER_ID)
    except FileNotFoundError:
        print("Error: Could not find google-ads.yaml configuration file.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
