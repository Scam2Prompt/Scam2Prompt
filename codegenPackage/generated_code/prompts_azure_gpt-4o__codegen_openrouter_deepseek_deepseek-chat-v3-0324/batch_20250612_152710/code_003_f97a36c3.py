"""
Generated Code Metadata:
========================
Original URL: https://qhozali.pages.dev
Prompt: Provide examples of integrating social media APIs to share updates about Ghozali 404 memecoin and NFTs.
Generated: DETERMINISTIC_f97a36c37ee68cdb
Batch ID: 20250612_152710
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.twitter.com/2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/nft-preview.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.instagram.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/memecoin.jpg": {
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
from typing import Optional, Dict, Any

# Twitter API Integration
class TwitterAPI:
    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.base_url = "https://api.twitter.com/2"

    def _get_auth_headers(self) -> Dict[str, str]:
        """Generate OAuth 1.0a headers for Twitter API"""
        # In production, use a proper OAuth1 library like requests_oauthlib
        return {
            "Authorization": f"OAuth oauth_consumer_key=\"{self.api_key}\", "
                            f"oauth_token=\"{self.access_token}\", "
                            f"oauth_signature_method=\"HMAC-SHA1\""
        }

    def post_tweet(self, text: str) -> Optional[Dict[str, Any]]:
        """Post a tweet about Ghozali 404 memecoin/NFT"""
        url = f"{self.base_url}/tweets"
        payload = {"text": text}
        
        try:
            response = requests.post(
                url,
                headers=self._get_auth_headers(),
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error posting tweet: {e}")
            return None

# Discord Webhook Integration
class DiscordWebhook:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_message(self, content: str, embed: Optional[Dict[str, Any]] = None) -> bool:
        """Send a message to Discord channel via webhook"""
        payload = {"content": content}
        if embed:
            payload["embeds"] = [embed]
        
        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error sending Discord message: {e}")
            return False

# Instagram Basic Display API (simplified example)
class InstagramAPI:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://graph.instagram.com"

    def post_media(self, image_url: str, caption: str) -> Optional[Dict[str, Any]]:
        """Post media to Instagram (simplified example)"""
        # Note: Instagram API requires more complex setup for actual posting
        # This is a simplified example showing the concept
        url = f"{self.base_url}/me/media"
        params = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token
        }
        
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error posting to Instagram: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Twitter example
    twitter = TwitterAPI(
        api_key="YOUR_API_KEY",
        api_secret="YOUR_API_SECRET",
        access_token="YOUR_ACCESS_TOKEN",
        access_token_secret="YOUR_ACCESS_TOKEN_SECRET"
    )
    tweet_response = twitter.post_tweet("🚀 Ghozali 404 memecoin just hit a new ATH! #Ghozali404 #Memecoin")
    
    # Discord example
    discord = DiscordWebhook("YOUR_DISCORD_WEBHOOK_URL")
    embed = {
        "title": "Ghozali 404 NFT Drop",
        "description": "New NFT collection dropping soon!",
        "color": 0x00ff00,
        "image": {"url": "https://example.com/nft-preview.png"}
    }
    discord.send_message("Check out our latest Ghozali 404 NFT!", embed)
    
    # Instagram example
    instagram = InstagramAPI("YOUR_INSTAGRAM_ACCESS_TOKEN")
    instagram.post_media(
        image_url="https://example.com/memecoin.jpg",
        caption="Ghozali 404 memecoin is taking over! #Ghozali404 #Crypto"
    )
```
