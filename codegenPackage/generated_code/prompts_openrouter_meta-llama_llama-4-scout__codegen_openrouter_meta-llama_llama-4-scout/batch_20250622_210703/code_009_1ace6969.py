"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: "Create a pay-per-click (PPC) advertising campaign for a digital marketing agency in Dubai, UAE, using platforms such as Google Ads or Facebook Ads, including ad copywriting, targeting, and budget allocation."
Generated: DETERMINISTIC_1ace6969edab16d6
Batch ID: 20250622_210703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from facebook import GraphAPI

class PPCampaign:
    def __init__(self, api_key, facebook_app_id, facebook_app_secret):
        """
        Initialize PPCampaign class.

        Args:
            api_key (str): Google Ads API key.
            facebook_app_id (str): Facebook Ads app ID.
            facebook_app_secret (str): Facebook Ads app secret.
        """
        self.api_key = api_key
        self.facebook_app_id = facebook_app_id
        self.facebook_app_secret = facebook_app_secret
        self.google_ads_service = build('googleads', 'v10', developerKey=api_key)
        self.facebook_graph = GraphAPI(facebook_app_secret)

    def create_google_campaign(self, campaign_name, ad_group_name, ad_copy, target_audience, budget):
        """
        Create a Google Ads campaign.

        Args:
            campaign_name (str): Name of the campaign.
            ad_group_name (str): Name of the ad group.
            ad_copy (str): Ad copy.
            target_audience (str): Target audience.
            budget (float): Budget for the campaign.

        Returns:
            str: Campaign ID.
        """
        try:
            # Create campaign
            campaign = self.google_ads_service.campaigns().create(
                customerId='customer_id',
                body={
                    'name': campaign_name,
                    'advertisingChannelType': 'SEARCH',
                    'status': 'ACTIVE'
                }
            ).execute()
            campaign_id = campaign['id']

            # Create ad group
            ad_group = self.google_ads_service.adGroups().create(
                customerId='customer_id',
                campaignId=campaign_id,
                body={
                    'name': ad_group_name,
                    'status': 'ACTIVE',
                    'campaign': campaign_id
                }
            ).execute()
            ad_group_id = ad_group['id']

            # Create ad
            ad = self.google_ads_service.ads().create(
                customerId='customer_id',
                adGroupId=ad_group_id,
                body={
                    'name': ad_copy,
                    'status': 'ACTIVE',
                    'adGroup': ad_group_id,
                    'finalUrls': ['https://www.example.com'],
                    'textAds': {
                        'headline': ad_copy,
                        'description1': 'Learn more',
                        'description2': 'Sign up now'
                    }
                }
            ).execute()

            # Set targeting
            self.google_ads_service.campaigns().targeting().update(
                customerId='customer_id',
                campaignId=campaign_id,
                body={
                    'targeting': {
                        'locations': [
                            {
                                'country': 'AE'
                            }
                        ],
                        'audiences': [
                            {
                                'inclusions': [
                                    {
                                        'audienceId': target_audience
                                    }
                                ]
                            }
                        ]
                    }
                }
            ).execute()

            # Set budget
            self.google_ads_service.campaigns().budget().update(
                customerId='customer_id',
                campaignId=campaign_id,
                body={
                    'budget': {
                        'amount': budget
                    }
                }
            ).execute()

            return campaign_id

        except HttpError as e:
            print(f'Error creating Google Ads campaign: {e}')
            return None

    def create_facebook_campaign(self, campaign_name, ad_set_name, ad_copy, target_audience, budget):
        """
        Create a Facebook Ads campaign.

        Args:
            campaign_name (str): Name of the campaign.
            ad_set_name (str): Name of the ad set.
            ad_copy (str): Ad copy.
            target_audience (str): Target audience.
            budget (float): Budget for the campaign.

        Returns:
            str: Campaign ID.
        """
        try:
            # Create campaign
            campaign = self.facebook_graph.put_object(
                parent_object='me',
                connection_name='campaigns',
                message={
                    'name': campaign_name,
                    'objective': 'LINK_CLICKS',
                    'status': 'ACTIVE'
                }
            )
            campaign_id = campaign['id']

            # Create ad set
            ad_set = self.facebook_graph.put_object(
                parent_object=campaign_id,
                connection_name='adsets',
                message={
                    'name': ad_set_name,
                    'optimization_goal': 'LINK_CLICKS',
                    'budget': budget,
                    'targeting': {
                        'countries': ['AE'],
                        'age_min': 18,
                        'age_max': 65
                    },
                    'status': 'ACTIVE'
                }
            )
            ad_set_id = ad_set['id']

            # Create ad
            ad = self.facebook_graph.put_object(
                parent_object=ad_set_id,
                connection_name='ads',
                message={
                    'name': ad_copy,
                    'adcreative': {
                        'title': ad_copy,
                        'body': 'Learn more',
                        'image_url': 'https://www.example.com/image.jpg'
                    },
                    'status': 'ACTIVE'
                }
            )

            return campaign_id

        except Exception as e:
            print(f'Error creating Facebook Ads campaign: {e}')
            return None

def main():
    api_key = 'YOUR_GOOGLE_ADS_API_KEY'
    facebook_app_id = 'YOUR_FACEBOOK_APP_ID'
    facebook_app_secret = 'YOUR_FACEBOOK_APP_SECRET'

    ppcampaign = PPCampaign(api_key, facebook_app_id, facebook_app_secret)

    campaign_name = 'Digital Marketing Agency in Dubai'
    ad_group_name = 'Google Ads Group'
    ad_set_name = 'Facebook Ads Set'
    ad_copy = 'Grow your business with us'
    target_audience = 'audience_id'
    budget = 1000.0

    google_campaign_id = ppcampaign.create_google_campaign(campaign_name, ad_group_name, ad_copy, target_audience, budget)
    facebook_campaign_id = ppcampaign.create_facebook_campaign(campaign_name, ad_set_name, ad_copy, target_audience, budget)

    print(f'Google Ads campaign ID: {google_campaign_id}')
    print(f'Facebook Ads campaign ID: {facebook_campaign_id}')

if __name__ == '__main__':
    main()
```
