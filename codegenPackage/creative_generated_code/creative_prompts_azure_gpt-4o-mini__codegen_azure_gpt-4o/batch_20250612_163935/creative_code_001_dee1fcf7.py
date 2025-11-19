"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stuff-artgobblers.com
Prompt: How can I use SEM to drive targeted traffic for my business? Provide an example based on the services offered by ACE Digital Marketing.
Generated: DETERMINISTIC_dee1fcf72b6ee9fe
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates using Search Engine Marketing (SEM) to drive targeted traffic 
for a business offering services similar to ACE Digital Marketing. It uses Google Ads API 
to create a sample ad campaign targeting specific keywords related to digital marketing services.
"""

from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

def create_google_ads_campaign():
    """Creates a sample Google Ads campaign to drive targeted traffic."""
    try:
        # Load Google Ads API client
        client = GoogleAdsClient.load_from_storage("google_ads_config.yaml")
        
        # Define the customer ID (replace with your Google Ads account customer ID)
        customer_id = "1234567890"
        
        # Create a new campaign
        campaign_service = client.get_service("CampaignService")
        campaign_operation = client.get_type("CampaignOperation")
        campaign = campaign_operation.create
        
        campaign.name = "ACE Digital Marketing SEM Campaign"
        campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
        campaign.status = client.enums.CampaignStatusEnum.PAUSED  # Start with paused
        campaign.manual_cpc = client.get_type("ManualCpc")._pb
        campaign.manual_cpc.enhanced_cpc_enabled = True
        campaign.start_date = "20240101"  # Format: YYYYMMDD
        campaign.end_date = "20241231"    # Format: YYYYMMDD

        # Add the campaign to the account
        response = campaign_service.mutate_campaigns(customer_id=customer_id, operations=[campaign_operation])
        campaign_id = response.results[0].resource_name
        print(f"Created campaign with resource name: {campaign_id}")
        
        # Add keywords to target (e.g., "digital marketing services", "SEO agency")
        add_keywords_to_ad_group(client, customer_id, campaign_id, ["digital marketing services", "SEO agency", "PPC management"])
    
    except GoogleAdsException as ex:
        print(f"Google Ads API error: {ex}")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_keywords_to_ad_group(client, customer_id, campaign_id, keywords):
    """Adds keywords to the ad group for the specified campaign."""
    try:
        ad_group_service = client.get_service("AdGroupService")
        ad_group_operation = client.get_type("AdGroupOperation")
        ad_group = ad_group_operation.create
        
        ad_group.name = "ACE Digital Marketing Ad Group"
        ad_group.campaign = campaign_id
        ad_group.status = client.enums.AdGroupStatusEnum.ENABLED

        # Add the ad group
        response = ad_group_service.mutate_ad_groups(customer_id=customer_id, operations=[ad_group_operation])
        ad_group_id = response.results[0].resource_name
        print(f"Created ad group with resource name: {ad_group_id}")

        # Add keywords to the ad group
        add_keywords(client, customer_id, ad_group_id, keywords)
    
    except GoogleAdsException as ex:
        print(f"Google Ads API error: {ex}")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_keywords(client, customer_id, ad_group_id, keywords):
    """Adds keywords to the specified ad group."""
    try:
        ad_group_criterion_service = client.get_service("AdGroupCriterionService")
        operations = []

        for keyword in keywords:
            ad_group_criterion_operation = client.get_type("AdGroupCriterionOperation")
            ad_group_criterion = ad_group_criterion_operation.create
            ad_group_criterion.keyword.text = keyword
            ad_group_criterion.keyword.match_type = client.enums.KeywordMatchTypeEnum.EXACT
            ad_group_criterion.ad_group = ad_group_id
            ad_group_criterion.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
            operations.append(ad_group_criterion_operation)
        
        # Add the keywords
        response = ad_group_criterion_service.mutate_ad_group_criteria(customer_id=customer_id, operations=operations)
        for result in response.results:
            print(f"Added keyword: {result.resource_name}")

    except GoogleAdsException as ex:
        print(f"Google Ads API error: {ex}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_google_ads_campaign()
```

Make sure to replace `google_ads_config.yaml` with your actual Google Ads API configuration file and `customer_id` with your Google Ads account customer ID. You may also need to set up access to the Google Ads API and enable the API for your Google account.
