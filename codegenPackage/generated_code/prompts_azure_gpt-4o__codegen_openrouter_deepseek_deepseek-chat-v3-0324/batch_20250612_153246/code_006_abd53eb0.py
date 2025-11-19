"""
Generated Code Metadata:
========================
Original URL: https://innetdigital.com
Prompt: Write code to track and optimize ad performance across multiple online platforms, leveraging programmatic advertising techniques referenced by Innet Plus Digital.
Generated: DETERMINISTIC_abd53eb050b910c2
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://googleads.googleapis.com/v10": {
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
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AdPlatformClient(ABC):
    """Abstract base class for platform-specific API clients."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = self._get_base_url()
        
    @abstractmethod
    def _get_base_url(self) -> str:
        """Get the base API URL for the platform."""
        pass
    
    @abstractmethod
    def get_campaigns(self) -> List[Dict]:
        """Fetch all campaigns from the platform."""
        pass
    
    @abstractmethod
    def get_ad_performance(self, campaign_id: str, start_date: str, end_date: str) -> Dict:
        """Get performance metrics for a specific campaign."""
        pass
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make an API request to the platform."""
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

class GoogleAdsClient(AdPlatformClient):
    """Client for Google Ads API."""
    
    def _get_base_url(self) -> str:
        return "https://googleads.googleapis.com/v10"
    
    def get_campaigns(self) -> List[Dict]:
        endpoint = "customers/1234567890/campaigns"
        return self._make_request(endpoint)
    
    def get_ad_performance(self, campaign_id: str, start_date: str, end_date: str) -> Dict:
        endpoint = f"customers/1234567890/campaigns/{campaign_id}/metrics"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "metrics": "clicks,impressions,ctr,cost"
        }
        return self._make_request(endpoint, params)

class FacebookAdsClient(AdPlatformClient):
    """Client for Facebook Ads API."""
    
    def _get_base_url(self) -> str:
        return "https://graph.facebook.com/v12.0"
    
    def get_campaigns(self) -> List[Dict]:
        endpoint = "act_123456789/campaigns"
        return self._make_request(endpoint)
    
    def get_ad_performance(self, campaign_id: str, start_date: str, end_date: str) -> Dict:
        endpoint = f"{campaign_id}/insights"
        params = {
            "date_preset": "custom",
            "time_range": f"{{'since':'{start_date}','until':'{end_date}'}}",
            "fields": "clicks,impressions,ctr,spend"
        }
        return self._make_request(endpoint, params)

class AdPerformanceTracker:
    """Main class to track and optimize ad performance across platforms."""
    
    def __init__(self, platform_clients: List[AdPlatformClient]):
        self.platform_clients = platform_clients
        self.performance_data = pd.DataFrame()
    
    def fetch_all_performance_data(self, start_date: str, end_date: str) -> None:
        """Fetch performance data from all platforms."""
        for client in self.platform_clients:
            try:
                campaigns = client.get_campaigns()
                for campaign in campaigns:
                    campaign_id = campaign['id']
                    performance = client.get_ad_performance(campaign_id, start_date, end_date)
                    self._store_performance_data(client.__class__.__name__, campaign_id, performance)
            except Exception as e:
                logger.error(f"Failed to fetch data from {client.__class__.__name__}: {e}")
                continue
    
    def _store_performance_data(self, platform: str, campaign_id: str, performance: Dict) -> None:
        """Store performance data in DataFrame."""
        data = {
            'platform': platform,
            'campaign_id': campaign_id,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'clicks': performance.get('clicks', 0),
            'impressions': performance.get('impressions', 0),
            'ctr': performance.get('ctr', 0),
            'cost': performance.get('cost', 0)
        }
        self.performance_data = self.performance_data.append(data, ignore_index=True)
    
    def optimize_campaigns(self) -> Dict:
        """Optimize campaigns based on performance data."""
        if self.performance_data.empty:
            logger.warning("No performance data available for optimization")
            return {}
        
        # Simple optimization: increase budget for campaigns with CTR > 1%
        optimized_campaigns = {}
        for _, row in self.performance_data.iterrows():
            if row['ctr'] > 0.01:
                optimized_campaigns[row['campaign_id']] = {
                    'action': 'increase_budget',
                    'current_ctr': row['ctr'],
                    'platform': row['platform']
                }
        
        return optimized_campaigns

# Example usage
if __name__ == "__main__":
    try:
        # Initialize clients (in a real app, use environment variables for API keys)
        google_client = GoogleAdsClient(api_key="your_google_api_key")
        facebook_client = FacebookAdsClient(api_key="your_facebook_api_key")
        
        # Create tracker
        tracker = AdPerformanceTracker([google_client, facebook_client])
        
        # Fetch data for last 7 days
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - pd.Timedelta(days=7)).strftime('%Y-%m-%d')
        tracker.fetch_all_performance_data(start_date, end_date)
        
        # Optimize campaigns
        optimizations = tracker.optimize_campaigns()
        logger.info(f"Optimization recommendations: {optimizations}")
        
    except Exception as e:
        logger.error(f"Error in ad performance tracking: {e}")
```
