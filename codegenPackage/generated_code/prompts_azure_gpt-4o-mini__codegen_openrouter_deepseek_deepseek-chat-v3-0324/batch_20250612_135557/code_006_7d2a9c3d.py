"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Develop a marketing strategy that includes live streaming and social media engagement, utilizing Cara Productions' services to maximize audience reach in Kenya.
Generated: DETERMINISTIC_7d2a9c3d77264976
Batch ID: 20250612_135557
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/youtube/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.twitter.com/2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0": {
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
import datetime
import json
import requests
from typing import Dict, List, Optional

class SocialMediaPlatform:
    """Base class for social media platform integrations."""
    
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = ""
        
    def authenticate(self) -> bool:
        """Authenticate with the platform's API."""
        raise NotImplementedError
        
    def post_content(self, content: str, image_url: Optional[str] = None) -> Dict:
        """Post content to the platform."""
        raise NotImplementedError
        
    def schedule_post(self, content: str, post_time: datetime.datetime, image_url: Optional[str] = None) -> Dict:
        """Schedule a post for future publishing."""
        raise NotImplementedError
        
    def get_analytics(self) -> Dict:
        """Get performance analytics for the account."""
        raise NotImplementedError


class Facebook(SocialMediaPlatform):
    """Facebook platform integration."""
    
    def __init__(self, api_key: str, api_secret: str, page_id: str):
        super().__init__(api_key, api_secret)
        self.base_url = "https://graph.facebook.com/v12.0"
        self.page_id = page_id
        self.access_token = None
        
    def authenticate(self) -> bool:
        """Authenticate with Facebook Graph API."""
        try:
            auth_url = f"{self.base_url}/oauth/access_token"
            params = {
                "client_id": self.api_key,
                "client_secret": self.api_secret,
                "grant_type": "client_credentials"
            }
            response = requests.get(auth_url, params=params)
            response.raise_for_status()
            self.access_token = response.json().get("access_token")
            return True
        except Exception as e:
            print(f"Facebook authentication failed: {str(e)}")
            return False
            
    def post_content(self, content: str, image_url: Optional[str] = None) -> Dict:
        """Post content to Facebook page."""
        if not self.access_token:
            raise ValueError("Not authenticated. Call authenticate() first.")
            
        try:
            post_url = f"{self.base_url}/{self.page_id}/feed"
            params = {
                "message": content,
                "access_token": self.access_token
            }
            
            if image_url:
                params["url"] = image_url
                
            response = requests.post(post_url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Facebook post failed: {str(e)}")
            return {"error": str(e)}
            
    def go_live(self, title: str, description: str) -> Dict:
        """Start a live stream on Facebook."""
        if not self.access_token:
            raise ValueError("Not authenticated. Call authenticate() first.")
            
        try:
            live_url = f"{self.base_url}/{self.page_id}/live_videos"
            params = {
                "title": title,
                "description": description,
                "access_token": self.access_token,
                "status": "LIVE_NOW"
            }
            response = requests.post(live_url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Facebook live stream failed: {str(e)}")
            return {"error": str(e)}


class Twitter(SocialMediaPlatform):
    """Twitter platform integration."""
    
    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        super().__init__(api_key, api_secret)
        self.base_url = "https://api.twitter.com/2"
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
    def authenticate(self) -> bool:
        """Twitter uses OAuth 1.0a which requires tokens during initialization."""
        return True
        
    def post_content(self, content: str, image_url: Optional[str] = None) -> Dict:
        """Post a tweet."""
        try:
            tweet_url = f"{self.base_url}/tweets"
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            }
            payload = {"text": content}
            
            response = requests.post(tweet_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Twitter post failed: {str(e)}")
            return {"error": str(e)}


class Instagram(SocialMediaPlatform):
    """Instagram platform integration."""
    
    def __init__(self, api_key: str, api_secret: str, business_account_id: str):
        super().__init__(api_key, api_secret)
        self.base_url = "https://graph.facebook.com/v12.0"
        self.business_account_id = business_account_id
        self.access_token = None
        
    def authenticate(self) -> bool:
        """Authenticate with Facebook Graph API (Instagram uses Facebook's API)."""
        try:
            auth_url = f"{self.base_url}/oauth/access_token"
            params = {
                "client_id": self.api_key,
                "client_secret": self.api_secret,
                "grant_type": "client_credentials"
            }
            response = requests.get(auth_url, params=params)
            response.raise_for_status()
            self.access_token = response.json().get("access_token")
            return True
        except Exception as e:
            print(f"Instagram authentication failed: {str(e)}")
            return False
            
    def post_content(self, content: str, image_url: str) -> Dict:
        """Post content to Instagram."""
        if not self.access_token:
            raise ValueError("Not authenticated. Call authenticate() first.")
            
        try:
            # Step 1: Create media container
            container_url = f"{self.base_url}/{self.business_account_id}/media"
            params = {
                "image_url": image_url,
                "caption": content,
                "access_token": self.access_token
            }
            response = requests.post(container_url, params=params)
            response.raise_for_status()
            container_id = response.json().get("id")
            
            # Step 2: Publish the container
            publish_url = f"{self.base_url}/{self.business_account_id}/media_publish"
            params = {
                "creation_id": container_id,
                "access_token": self.access_token
            }
            response = requests.post(publish_url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Instagram post failed: {str(e)}")
            return {"error": str(e)}


class YouTube:
    """YouTube live streaming integration."""
    
    def __init__(self, api_key: str, client_secret_file: str):
        self.api_key = api_key
        self.client_secret_file = client_secret_file
        self.base_url = "https://www.googleapis.com/youtube/v3"
        self.credentials = None
        
    def authenticate(self) -> bool:
        """Authenticate with YouTube API."""
        try:
            # In a real implementation, this would use OAuth 2.0
            # For simplicity, we're just checking the API key
            test_url = f"{self.base_url}/videos?part=snippet&id=test&key={self.api_key}"
            response = requests.get(test_url)
            if response.status_code == 200:
                self.credentials = {"api_key": self.api_key}
                return True
            return False
        except Exception as e:
            print(f"YouTube authentication failed: {str(e)}")
            return False
            
    def create_live_event(self, title: str, description: str, scheduled_start_time: datetime.datetime) -> Dict:
        """Create a scheduled live streaming event."""
        if not self.credentials:
            raise ValueError("Not authenticated. Call authenticate() first.")
            
        try:
            live_url = f"{self.base_url}/liveBroadcasts"
            params = {
                "part": "snippet,status",
                "key": self.api_key
            }
            payload = {
                "snippet": {
                    "title": title,
                    "description": description,
                    "scheduledStartTime": scheduled_start_time.isoformat()
                },
                "status": {
                    "privacyStatus": "public"
                }
            }
            response = requests.post(live_url, params=params, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"YouTube live event creation failed: {str(e)}")
            return {"error": str(e)}


class MarketingStrategy:
    """Marketing strategy implementation for Kenya market."""
    
    def __init__(self):
        self.platforms = []
        self.scheduled_content = []
        
    def add_platform(self, platform: SocialMediaPlatform) -> None:
        """Add a social media platform to the strategy."""
        if platform.authenticate():
            self.platforms.append(platform)
            
    def schedule_content(self, content: str, platforms: List[str], post_time: datetime.datetime, image_url: Optional[str] = None) -> None:
        """Schedule content across multiple platforms."""
        self
