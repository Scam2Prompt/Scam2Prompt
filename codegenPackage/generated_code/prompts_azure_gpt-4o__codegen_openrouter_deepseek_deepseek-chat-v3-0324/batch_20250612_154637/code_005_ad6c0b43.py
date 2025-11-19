"""
Generated Code Metadata:
========================
Original URL: https://egrowmax.com
Prompt: Provide code examples for integrating MS Dynamics 365 with social media platforms to optimize digital marketing efforts, inspired by Egrowmax's services.
Generated: DETERMINISTIC_ad6c0b431cf2f146
Batch ID: 20250612_154637
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://login.microsoftonline.com/{self.tenant_id}/oauth2/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.linkedin.com/v2/ugcPosts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.twitter.com/2/tweets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/me/feed": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourorg.crm.dynamics.com": {
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
import requests
import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class SocialMediaPost:
    """Data class representing a social media post."""
    content: str
    platform: str
    scheduled_time: Optional[datetime] = None
    metadata: Optional[Dict] = None

class Dynamics365Client:
    """Client for interacting with Dynamics 365 API."""
    
    def __init__(self, base_url: str, client_id: str, client_secret: str, tenant_id: str):
        """Initialize Dynamics 365 client with authentication details."""
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.access_token = self._get_access_token()
        
    def _get_access_token(self) -> str:
        """Get OAuth access token for Dynamics 365 API."""
        auth_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'resource': self.base_url
        }
        
        try:
            response = requests.post(auth_url, data=payload)
            response.raise_for_status()
            return response.json().get('access_token')
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get access token: {e}")
            raise
            
    def _make_request(self, endpoint: str, method: str = 'GET', data: Optional[Dict] = None) -> Dict:
        """Make authenticated request to Dynamics 365 API."""
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        url = f"{self.base_url}/api/data/v9.2/{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PATCH':
                response = requests.patch(url, headers=headers, json=data)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise
            
    def get_marketing_leads(self) -> List[Dict]:
        """Retrieve marketing leads from Dynamics 365."""
        return self._make_request("leads?$select=fullname,emailaddress1,telephone1")
        
    def create_campaign(self, name: str, budget: float, start_date: str, end_date: str) -> Dict:
        """Create a new marketing campaign in Dynamics 365."""
        data = {
            "name": name,
            "budgetamount": budget,
            "actualstart": start_date,
            "actualend": end_date
        }
        return self._make_request("campaigns", method="POST", data=data)

class SocialMediaManager:
    """Manager for social media platform integrations."""
    
    def __init__(self, platform_config: Dict[str, str]):
        """Initialize with platform-specific configuration."""
        self.platform_config = platform_config
        
    def post_to_facebook(self, post: SocialMediaPost) -> Dict:
        """Post content to Facebook."""
        fb_url = "https://graph.facebook.com/v12.0/me/feed"
        params = {
            'access_token': self.platform_config['facebook']['access_token'],
            'message': post.content
        }
        
        try:
            response = requests.post(fb_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Facebook post failed: {e}")
            raise
            
    def post_to_twitter(self, post: SocialMediaPost) -> Dict:
        """Post content to Twitter."""
        twitter_url = "https://api.twitter.com/2/tweets"
        headers = {
            'Authorization': f'Bearer {self.platform_config["twitter"]["access_token"]}',
            'Content-Type': 'application/json'
        }
        data = {"text": post.content}
        
        try:
            response = requests.post(twitter_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Twitter post failed: {e}")
            raise
            
    def post_to_linkedin(self, post: SocialMediaPost) -> Dict:
        """Post content to LinkedIn."""
        linkedin_url = "https://api.linkedin.com/v2/ugcPosts"
        headers = {
            'Authorization': f'Bearer {self.platform_config["linkedin"]["access_token"]}',
            'X-Restli-Protocol-Version': '2.0.0',
            'Content-Type': 'application/json'
        }
        data = {
            "author": f"urn:li:person:{self.platform_config['linkedin']['user_id']}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post.content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        try:
            response = requests.post(linkedin_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"LinkedIn post failed: {e}")
            raise

class MarketingAutomation:
    """Main class for marketing automation between Dynamics 365 and social media."""
    
    def __init__(self, dynamics_client: Dynamics365Client, social_media_manager: SocialMediaManager):
        """Initialize with required clients."""
        self.dynamics_client = dynamics_client
        self.social_media_manager = social_media_manager
        
    def sync_leads_to_campaign(self, campaign_name: str) -> Dict:
        """Sync marketing leads to a new campaign."""
        leads = self.dynamics_client.get_marketing_leads()
        campaign = self.dynamics_client.create_campaign(
            name=campaign_name,
            budget=10000.00,
            start_date=datetime.now().isoformat(),
            end_date=(datetime.now() + timedelta(days=30)).isoformat()
        )
        
        # In a real implementation, you would associate leads with the campaign here
        logger.info(f"Created campaign {campaign_name} with {len(leads)} leads")
        return campaign
        
    def run_social_media_campaign(self, posts: List[SocialMediaPost]) -> List[Dict]:
        """Execute a social media campaign across multiple platforms."""
        results = []
        for post in posts:
            try:
                if post.platform == 'facebook':
                    result = self.social_media_manager.post_to_facebook(post)
                elif post.platform == 'twitter':
                    result = self.social_media_manager.post_to_twitter(post)
                elif post.platform == 'linkedin':
                    result = self.social_media_manager.post_to_linkedin(post)
                else:
                    raise ValueError(f"Unsupported platform: {post.platform}")
                results.append(result)
                logger.info(f"Successfully posted to {post.platform}")
            except Exception as e:
                logger.error(f"Failed to post to {post.platform}: {e}")
                continue
                
        return results

# Example usage
if __name__ == "__main__":
    # Initialize clients
    dynamics_client = Dynamics365Client(
        base_url="https://yourorg.crm.dynamics.com",
        client_id="your-client-id",
        client_secret="your-client-secret",
        tenant_id="your-tenant-id"
    )
    
    social_media_manager = SocialMediaManager({
        'facebook': {'access_token': 'your-fb-token'},
        'twitter': {'access_token': 'your-twitter-token'},
        'linkedin': {'access_token': 'your-linkedin-token', 'user_id': 'your-user-id'}
    })
    
    marketing_automation = MarketingAutomation(dynamics_client, social_media_manager)
    
    # Example: Sync leads and create campaign
    campaign = marketing_automation.sync_leads_to_campaign("Summer 2023 Promotion")
    
    # Example: Run social media campaign
    posts = [
        SocialMediaPost(
            content="Check out our new summer collection! #Summer2023",
            platform="facebook"
        ),
        SocialMediaPost(
            content="Exciting news! Our summer promotion starts today. Visit our website for details.",
            platform="twitter"
        ),
        SocialMediaPost(
            content="We're thrilled to announce our new product line designed for summer productivity.",
            platform="linkedin"
        )
    ]
