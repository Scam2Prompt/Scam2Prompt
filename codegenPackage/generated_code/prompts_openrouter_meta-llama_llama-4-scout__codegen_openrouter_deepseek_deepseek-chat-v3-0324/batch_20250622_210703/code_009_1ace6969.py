"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: "Create a pay-per-click (PPC) advertising campaign for a digital marketing agency in Dubai, UAE, using platforms such as Google Ads or Facebook Ads, including ad copywriting, targeting, and budget allocation."
Generated: DETERMINISTIC_1ace6969edab16d6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from googleads import adwords
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative
from datetime import datetime, timedelta
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PPCCampaignManager:
    """Manages PPC campaigns across Google Ads and Facebook Ads platforms."""
    
    def __init__(self, google_ads_client: dict, facebook_ads_config: dict):
        """Initialize with API credentials."""
        self.google_ads_client = adwords.AdWordsClient.LoadFromDict(google_ads_client)
        self.facebook_ads_config = facebook_ads_config
        FacebookAdsApi.init(
            facebook_ads_config['app_id'],
            facebook_ads_config['app_secret'],
            facebook_ads_config['access_token'],
            facebook_ads_config['account_id']
        )
        self.ad_account = AdAccount(f"act_{facebook_ads_config['account_id']}")

    def create_google_ads_campaign(
        self,
        campaign_name: str,
        budget: float,
        start_date: str,
        end_date: str,
        target_locations: List[str],
        keywords: List[str],
        ad_groups: List[Dict],
        bid_strategy: str = 'MANUAL_CPC'
    ) -> Optional[str]:
        """Create a Google Ads campaign with ad groups and ads."""
        try:
            campaign_service = self.google_ads_client.GetService('CampaignService', version='v201809')
            budget_service = self.google_ads_client.GetService('BudgetService', version='v201809')

            # Create budget
            budget_operation = {
                'operator': 'ADD',
                'operand': {
                    'name': f'Budget for {campaign_name}',
                    'amount': {
                        'microAmount': budget * 1000000
                    },
                    'deliveryMethod': 'STANDARD'
                }
            }
            budget_id = budget_service.mutate([budget_operation])['value'][0]['budgetId']

            # Create campaign
            campaign_operation = {
                'operator': 'ADD',
                'operand': {
                    'name': campaign_name,
                    'status': 'PAUSED',
                    'advertisingChannelType': 'SEARCH',
                    'biddingStrategyConfiguration': {
                        'biddingStrategyType': bid_strategy
                    },
                    'startDate': start_date,
                    'endDate': end_date,
                    'budget': {
                        'budgetId': budget_id
                    },
                    'networkSetting': {
                        'targetGoogleSearch': True,
                        'targetSearchNetwork': True,
                        'targetContentNetwork': False,
                        'targetPartnerSearchNetwork': False
                    },
                    'settings': [{
                        'xsi_type': 'GeoTargetTypeSetting',
                        'positiveGeoTargetType': 'DONT_CARE',
                        'negativeGeoTargetType': 'LOCATION_OF_PRESENCE'
                    }]
                }
            }
            campaign = campaign_service.mutate([campaign_operation])['value'][0]

            # Add locations
            location_service = self.google_ads_client.GetService('LocationCriterionService', version='v201809')
            location_operations = []
            for location in target_locations:
                location_operations.append({
                    'operator': 'ADD',
                    'operand': {
                        'campaignId': campaign['id'],
                        'criterion': {
                            'xsi_type': 'Location',
                            'locationName': location
                        },
                        'bidModifier': 1.0
                    }
                })
            if location_operations:
                self.google_ads_client.GetService('CampaignCriterionService', version='v201809').mutate(location_operations)

            # Create ad groups and ads
            ad_group_service = self.google_ads_client.GetService('AdGroupService', version='v201809')
            ad_group_ad_service = self.google_ads_client.GetService('AdGroupAdService', version='v201809')
            keyword_service = self.google_ads_client.GetService('AdGroupCriterionService', version='v201809')

            for ad_group in ad_groups:
                ad_group_operation = {
                    'operator': 'ADD',
                    'operand': {
                        'campaignId': campaign['id'],
                        'name': ad_group['name'],
                        'status': 'ENABLED',
                        'biddingStrategyConfiguration': {
                            'bids': [{
                                'xsi_type': 'CpcBid',
                                'bid': {
                                    'microAmount': ad_group['bid_amount'] * 1000000
                                }
                            }]
                        }
                    }
                }
                ad_group = ad_group_service.mutate([ad_group_operation])['value'][0]

                # Add keywords
                keyword_operations = []
                for keyword in keywords:
                    keyword_operations.append({
                        'operator': 'ADD',
                        'operand': {
                            'adGroupId': ad_group['id'],
                            'criterion': {
                                'xsi_type': 'Keyword',
                                'text': keyword,
                                'matchType': 'BROAD'
                            },
                            'userStatus': 'ENABLED',
                            'finalUrls': [ad_group['final_url']]
                        }
                    })
                if keyword_operations:
                    keyword_service.mutate(keyword_operations)

                # Add ads
                ad_operations = []
                for ad_copy in ad_group['ads']:
                    ad_operations.append({
                        'operator': 'ADD',
                        'operand': {
                            'adGroupId': ad_group['id'],
                            'ad': {
                                'xsi_type': 'ExpandedTextAd',
                                'headlinePart1': ad_copy['headline1'],
                                'headlinePart2': ad_copy['headline2'],
                                'description': ad_copy['description'],
                                'path1': ad_copy['path1'],
                                'path2': ad_copy['path2'],
                                'finalUrls': [ad_group['final_url']]
                            }
                        }
                    })
                if ad_operations:
                    ad_group_ad_service.mutate(ad_operations)

            logger.info(f"Successfully created Google Ads campaign with ID: {campaign['id']}")
            return campaign['id']
        except Exception as e:
            logger.error(f"Failed to create Google Ads campaign: {str(e)}")
            return None

    def create_facebook_ads_campaign(
        self,
        campaign_name: str,
        objective: str,
        budget: float,
        start_time: datetime,
        end_time: datetime,
        target_locations: List[str],
        interests: List[str],
        ad_sets: List[Dict],
        status: str = 'PAUSED'
    ) -> Optional[str]:
        """Create a Facebook Ads campaign with ad sets and ads."""
        try:
            # Create campaign
            campaign = Campaign(parent_id=self.ad_account.get_id())
            campaign.update({
                'name': campaign_name,
                'objective': objective,
                'status': status,
                'special_ad_categories': []
            })
            campaign.remote_create()

            # Create ad sets
            for ad_set_data in ad_sets:
                ad_set = AdSet(parent_id=self.ad_account.get_id())
                ad_set.update({
                    'name': ad_set_data['name'],
                    'campaign_id': campaign.get_id(),
                    'bid_amount': ad_set_data['bid_amount'],
                    'billing_event': 'IMPRESSIONS',
                    'optimization_goal': 'REACH',
                    'targeting': {
                        'geo_locations': {
                            'countries': ['AE'],
                            'cities': target_locations
                        },
                        'interests': [
                            {'id': interest} for interest in interests
                        ],
                        'age_min': 18,
                        'age_max': 65
                    },
                    'daily_budget': budget,
                    'start_time': start_time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                    'end_time': end_time.strftime('%Y-%m-%dT%H:%M:%S%z')
                })
                ad_set.remote_create()

                # Create ads
                for ad_data in ad_set_data['ads']:
                    creative = AdCreative(parent_id=self.ad_account.get_id())
                    creative.update({
                        'name': f"Creative for {ad_set_data['name']}",
                        'object_story_spec': {
                            'page_id': self.facebook_ads_config['page_id'],
                            'link_data': {
                                'link': ad_data['link'],
                                'message': ad_data['message'],
                                'caption': ad_data['caption'],
                                'description': ad_data['description'],
                                'image_hash': ad_data['image_hash']
                            }
                        }
                    })
                    creative.remote_create()

                    ad = Ad(parent_id=self.ad_account.get_id())
                    ad.update({
                        'name': f"Ad for {ad_set_data['name']}",
                        'adset_id': ad_set.get_id(),
                        'creative': {'creative_id
