"""
Generated Code Metadata:
========================
Original URL: https://pepecoin.blog
Prompt: Create a script to monitor Pepecoin's community activity on Discord and Reddit, leveraging APIs for community engagement tracking.
Generated: DETERMINISTIC_c5e2c661705eac5a
Batch ID: 20250612_154412
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.reddit.com/r": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.com/api/v9": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.reddit.com/api/v1/access_token": {
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
import os
import time
import requests
import json
from datetime import datetime
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pepecoin_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
CONFIG = {
    'DISCORD_API_URL': 'https://discord.com/api/v9',
    'REDDIT_API_URL': 'https://www.reddit.com/r',
    'SUBREDDIT': 'pepecoin',
    'DISCORD_SERVER_ID': 'pepecoin_discord_server_id',  # Replace with actual server ID
    'POLL_INTERVAL': 300,  # 5 minutes in seconds
    'MAX_RETRIES': 3,
    'RETRY_DELAY': 5
}

# Environment variables for API keys
DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = 'PepecoinCommunityMonitor/1.0'

class APIClient:
    """Base API client with common request handling."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'PepecoinCommunityMonitor/1.0'})
    
    def make_request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict] = None,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        retries: int = CONFIG['MAX_RETRIES']
    ) -> Optional[Dict]:
        """Make an HTTP request with retry logic."""
        for attempt in range(retries):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=data,
                    timeout=10
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < retries - 1:
                    time.sleep(CONFIG['RETRY_DELAY'])
                else:
                    logger.error(f"Max retries reached for {url}")
                    return None

class DiscordClient(APIClient):
    """Client for interacting with Discord API."""
    
    def __init__(self):
        super().__init__()
        self.base_url = CONFIG['DISCORD_API_URL']
        self.session.headers.update({'Authorization': f'Bot {DISCORD_TOKEN}'})
    
    def get_server_info(self) -> Optional[Dict]:
        """Get information about the Discord server."""
        url = f"{self.base_url}/guilds/{CONFIG['DISCORD_SERVER_ID']}"
        return self.make_request('GET', url)
    
    def get_channels(self) -> Optional[List[Dict]]:
        """Get list of channels in the server."""
        url = f"{self.base_url}/guilds/{CONFIG['DISCORD_SERVER_ID']}/channels"
        return self.make_request('GET', url)
    
    def get_channel_messages(self, channel_id: str, limit: int = 50) -> Optional[List[Dict]]:
        """Get recent messages from a channel."""
        url = f"{self.base_url}/channels/{channel_id}/messages"
        params = {'limit': limit}
        return self.make_request('GET', url, params=params)
    
    def get_member_count(self) -> Optional[int]:
        """Get approximate member count of the server."""
        server_info = self.get_server_info()
        return server_info.get('approximate_member_count') if server_info else None

class RedditClient(APIClient):
    """Client for interacting with Reddit API."""
    
    def __init__(self):
        super().__init__()
        self.base_url = CONFIG['REDDIT_API_URL']
        self.access_token = None
        self.token_expires = 0
    
    def authenticate(self) -> bool:
        """Authenticate with Reddit API using OAuth2."""
        auth_url = 'https://www.reddit.com/api/v1/access_token'
        auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET)
        data = {
            'grant_type': 'client_credentials',
            'scope': 'read'
        }
        headers = {'User-Agent': REDDIT_USER_AGENT}
        
        try:
            response = requests.post(
                auth_url,
                auth=auth,
                data=data,
                headers=headers,
                timeout=10
            )
            response.raise_for_status()
            token_data = response.json()
            self.access_token = token_data['access_token']
            self.token_expires = time.time() + token_data['expires_in']
            self.session.headers.update({'Authorization': f'bearer {self.access_token}'})
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Reddit authentication failed: {str(e)}")
            return False
    
    def ensure_auth(self) -> bool:
        """Ensure we have a valid auth token."""
        if not self.access_token or time.time() >= self.token_expires:
            return self.authenticate()
        return True
    
    def get_subreddit_posts(self, limit: int = 25, sort: str = 'new') -> Optional[List[Dict]]:
        """Get posts from the subreddit."""
        if not self.ensure_auth():
            return None
        
        url = f"{self.base_url}/{CONFIG['SUBREDDIT']}/{sort}.json"
        params = {'limit': limit}
        return self.make_request('GET', url, params=params)
    
    def get_subreddit_info(self) -> Optional[Dict]:
        """Get information about the subreddit."""
        if not self.ensure_auth():
            return None
        
        url = f"{self.base_url}/{CONFIG['SUBREDDIT']}/about.json"
        return self.make_request('GET', url)

class CommunityMonitor:
    """Main class for monitoring Pepecoin community activity."""
    
    def __init__(self):
        self.discord = DiscordClient()
        self.reddit = RedditClient()
        self.last_run = None
    
    def run(self):
        """Run the monitoring process."""
        logger.info("Starting Pepecoin community monitoring...")
        self.last_run = datetime.utcnow()
        
        try:
            # Discord monitoring
            discord_data = self.monitor_discord()
            
            # Reddit monitoring
            reddit_data = self.monitor_reddit()
            
            # Process and store results
            self.process_results(discord_data, reddit_data)
            
        except Exception as e:
            logger.error(f"Monitoring failed: {str(e)}", exc_info=True)
    
    def monitor_discord(self) -> Dict:
        """Monitor Discord activity."""
        logger.info("Checking Discord activity...")
        data = {}
        
        # Get server info
        server_info = self.discord.get_server_info()
        if server_info:
            data['member_count'] = server_info.get('approximate_member_count')
            logger.info(f"Discord server has {data['member_count']} members")
        
        # Get channel messages
        channels = self.discord.get_channels()
        if channels:
            text_channels = [c for c in channels if c.get('type') == 0]  # Type 0 is text channel
            for channel in text_channels[:3]:  # Limit to first 3 channels
                messages = self.discord.get_channel_messages(channel['id'])
                if messages:
                    data[f"channel_{channel['id']}_recent_messages"] = len(messages)
        
        return data
    
    def monitor_reddit(self) -> Dict:
        """Monitor Reddit activity."""
        logger.info("Checking Reddit activity...")
        data = {}
        
        # Get subreddit info
        subreddit_info = self.reddit.get_subreddit_info()
        if subreddit_info and 'data' in subreddit_info:
            data['subscribers'] = subreddit_info['data'].get('subscribers')
            logger.info(f"Subreddit has {data['subscribers']} subscribers")
        
        # Get recent posts
        posts = self.reddit.get_subreddit_posts()
        if posts and 'data' in posts and 'children' in posts['data']:
            data['recent_posts'] = len(posts['data']['children'])
            data['post_titles'] = [post['data']['title'] for post in posts['data']['children']]
        
        return data
    
    def process_results(self, discord_data: Dict, reddit_data: Dict):
        """Process and store monitoring results."""
        timestamp = datetime.ut
