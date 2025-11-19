"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: Generate code to set up an automated lead generation system that targets local clients with paid ads, ensuring immediate results as described in Client Fuel's marketing approach.
Generated: DETERMINISTIC_a0ed33c68eefcdd9
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging
from google.ads.google_ads.client import GoogleAdsClient
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LeadGenerationSystem:
    def __init__(self, config_path: str = 'config.json'):
        """Initialize the lead generation system with configuration."""
        self.config = self._load_config(config_path)
        self._validate_config()
        self._initialize_apis()

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in config file: {config_path}")
            raise

    def _validate_config(self) -> None:
        """Validate the configuration."""
        required_keys = {
            'google_ads': ['developer_token', 'client_id', 'client_secret', 'refresh_token'],
            'facebook_ads': ['app_id', 'app_secret', 'access_token', 'ad_account_id'],
            'targeting': ['locations', 'interests', 'budget', 'lead_form_url']
        }
        
        for section, keys in required_keys.items():
            if section not in self.config:
                raise ValueError(f"Missing section in config: {section}")
            for key in keys:
                if key not in self.config[section]:
                    raise ValueError(f"Missing key in config: {section}.{key}")

    def _initialize_apis(self) -> None:
        """Initialize API clients for Google and Facebook Ads."""
        # Google Ads
        google_creds = {
            'developer_token': self.config['google_ads']['developer_token'],
            'client_id': self.config['google_ads']['client_id'],
            'client_secret': self.config['google_ads']['client_secret'],
            'refresh_token': self.config['google_ads']['refresh_token'],
            'use_proto_plus': True
        }
        self.google_client = GoogleAdsClient.load_from_dict(google_creds)

        # Facebook Ads
        FacebookAdsApi.init(
            self.config['facebook_ads']['app_id'],
            self.config['facebook_ads']['app_secret'],
            self.config['facebook_ads']['access_token']
        )
        self.ad_account = AdAccount(f"act_{self.config['facebook_ads']['ad_account_id']}")

    def create_google_ads_campaign(self, campaign_name: str) -> Optional[int]:
        """Create a Google Ads campaign."""
        try:
            campaign_service = self.google_client.get_service('CampaignService')
            campaign_operation = self.google_client.get_type('CampaignOperation')
            
            campaign = campaign_operation.create
            campaign.name = campaign_name
            campaign.advertising_channel_type = self.google_client.enums.AdvertisingChannelTypeEnum.SEARCH
            campaign.status = self.google_client.enums.CampaignStatusEnum.PAUSED
            campaign.manual_cpc.enhanced_cpc_enabled = True
            
            # Set budget
            campaign.campaign_budget = self._create_google_budget()
            
            # Set targeting
            self._set_google_targeting(campaign)
            
            response = campaign_service.mutate_campaigns(
                customer_id=self.config['google_ads']['client_id'],
                operations=[campaign_operation]
            )
            
            campaign_id = response.results[0].resource_name.split('/')[-1]
            logger.info(f"Created Google Ads campaign with ID: {campaign_id}")
            return int(campaign_id)
            
        except Exception as e:
            logger.error(f"Failed to create Google Ads campaign: {str(e)}")
            return None

    def _create_google_budget(self):
        """Create a Google Ads budget."""
        budget_service = self.google_client.get_service('CampaignBudgetService')
        budget_operation = self.google_client.get_type('CampaignBudgetOperation')
        
        budget = budget_operation.create
        budget.name = f"Budget {datetime.now().strftime('%Y%m%d')}"
        budget.amount_micros = self.config['targeting']['budget'] * 1000000
        budget.delivery_method = self.google_client.enums.BudgetDeliveryMethodEnum.STANDARD
        
        response = budget_service.mutate_campaign_budgets(
            customer_id=self.config['google_ads']['client_id'],
            operations=[budget_operation]
        )
        return response.results[0].resource_name

    def _set_google_targeting(self, campaign):
        """Set targeting for Google Ads campaign."""
        # Location targeting
        location_service = self.google_client.get_service('GeoTargetConstantService')
        for location in self.config['targeting']['locations']:
            response = location_service.suggest_geo_target_constants(
                query=location,
                locale='en',
                country_code='US'
            )
            if response.geo_target_constant_suggestions:
                suggestion = response.geo_target_constant_suggestions[0]
                campaign.network_settings.target_google_search = True
                campaign.network_settings.target_search_network = True
                campaign.network_settings.target_content_network = False
                campaign.network_settings.target_partner_search_network = False

    def create_facebook_ads_campaign(self, campaign_name: str) -> Optional[str]:
        """Create a Facebook Ads campaign."""
        try:
            # Create Campaign
            campaign = Campaign(parent_id=self.ad_account.get_id())
            campaign.update({
                Campaign.Field.name: campaign_name,
                Campaign.Field.objective: 'LEAD_GENERATION',
                Campaign.Field.status: 'PAUSED',
            })
            campaign.remote_create()
            
            # Create Ad Set
            ad_set = AdSet(parent_id=self.ad_account.get_id())
            ad_set.update({
                AdSet.Field.name: f"{campaign_name} AdSet",
                AdSet.Field.campaign_id: campaign.get_id(),
                AdSet.Field.daily_budget: self.config['targeting']['budget'],
                AdSet.Field.billing_event: 'IMPRESSIONS',
                AdSet.Field.optimization_goal: 'LEAD_GENERATION',
                AdSet.Field.bid_strategy: 'LOWEST_COST_WITHOUT_CAP',
                AdSet.Field.targeting: self._get_facebook_targeting(),
            })
            ad_set.remote_create()
            
            # Create Ad
            ad = Ad(parent_id=self.ad_account.get_id())
            ad.update({
                Ad.Field.name: f"{campaign_name} Ad",
                Ad.Field.adset_id: ad_set.get_id(),
                Ad.Field.creative: self._create_facebook_creative(),
                Ad.Field.status: 'PAUSED',
            })
            ad.remote_create()
            
            logger.info(f"Created Facebook Ads campaign with ID: {campaign.get_id()}")
            return campaign.get_id()
            
        except Exception as e:
            logger.error(f"Failed to create Facebook Ads campaign: {str(e)}")
            return None

    def _get_facebook_targeting(self) -> Dict:
        """Get Facebook targeting parameters."""
        return {
            'geo_locations': {
                'countries': ['US'],
                'cities': [{'key': loc} for loc in self.config['targeting']['locations']]
            },
            'interests': [
                {'id': str(interest)} for interest in self.config['targeting']['interests']
            ],
            'publisher_platforms': ['facebook', 'instagram'],
            'facebook_positions': ['feed', 'right_hand_column'],
            'device_platforms': ['mobile', 'desktop']
        }

    def _create_facebook_creative(self) -> Dict:
        """Create Facebook ad creative."""
        return {
            'object_story_spec': {
                'page_id': self.config['facebook_ads']['page_id'],
                'link_data': {
                    'link': self.config['targeting']['lead_form_url'],
                    'message': 'Get started with our exclusive offer today!',
                    'call_to_action': {
                        'type': 'SIGN_UP',
                        'value': {
                            'link': self.config['targeting']['lead_form_url']
                        }
                    }
                }
            }
        }

    def monitor_performance(self, campaign_ids: Dict[str, str]) -> None:
        """Monitor performance of running campaigns."""
        try:
            while True:
                google_perf = self._get_google_performance(campaign_ids.get('google'))
                facebook_perf = self._get_facebook_performance(campaign_ids.get('facebook'))
                
                logger.info(f"Google Ads Performance: {google_perf}")
                logger.info(f"Facebook Ads Performance: {facebook_perf}")
                
                # Check if we need to adjust
