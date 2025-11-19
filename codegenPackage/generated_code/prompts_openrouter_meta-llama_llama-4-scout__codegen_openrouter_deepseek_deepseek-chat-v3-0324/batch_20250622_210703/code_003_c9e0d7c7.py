"""
Generated Code Metadata:
========================
Original URL: https://innetdigital.com
Prompt: Compare the efficiency of different programmatic advertising platforms and suggest a suitable one for a 360° digital marketing service, providing a code example for integration.
Generated: DETERMINISTIC_c9e0d7c70ee1f6a0
Batch ID: 20250622_210703
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/auth/adwords": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://accounts.google.com/o/oauth2/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://googleads.googleapis.com/v14/customers": {
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
from typing import Dict, List, Optional
from enum import Enum

class Platform(Enum):
    """Enum representing different advertising platforms."""
    GOOGLE_ADS = "Google Ads"
    FACEBOOK_ADS = "Facebook Ads"
    TWITTER_ADS = "Twitter Ads"
    LINKEDIN_ADS = "LinkedIn Ads"
    TIKTOK_ADS = "TikTok Ads"

class PlatformMetrics:
    """Class to store metrics for each advertising platform."""
    def __init__(
        self,
        platform: Platform,
        ctr: float,
        cpc: float,
        conversion_rate: float,
        roi: float,
        api_integration_difficulty: int
    ):
        self.platform = platform
        self.ctr = ctr  # Click-through rate
        self.cpc = cpc  # Cost per click
        self.conversion_rate = conversion_rate
        self.roi = roi  # Return on investment
        self.api_integration_difficulty = api_integration_difficulty  # 1-5 scale

class PlatformComparator:
    """Compares different advertising platforms based on metrics."""
    def __init__(self, platforms_metrics: List[PlatformMetrics]):
        self.platforms_metrics = platforms_metrics

    def compare_platforms(self) -> pd.DataFrame:
        """Compare platforms and return results as a DataFrame."""
        data = []
        for metric in self.platforms_metrics:
            data.append({
                "Platform": metric.platform.value,
                "CTR (%)": metric.ctr,
                "CPC ($)": metric.cpc,
                "Conversion Rate (%)": metric.conversion_rate,
                "ROI (%)": metric.roi,
                "API Integration Difficulty": metric.api_integration_difficulty
            })
        return pd.DataFrame(data)

    def recommend_platform(
        self,
        ctr_weight: float = 0.25,
        cpc_weight: float = 0.25,
        conversion_weight: float = 0.25,
        roi_weight: float = 0.25,
        api_weight: float = 0.0
    ) -> Platform:
        """Recommend the best platform based on weighted metrics."""
        scores = []
        for metric in self.platforms_metrics:
            score = (
                (metric.ctr * ctr_weight) +
                (1/metric.cpc * cpc_weight) +  # Inverse since lower CPC is better
                (metric.conversion_rate * conversion_weight) +
                (metric.roi * roi_weight) +
                ((6 - metric.api_integration_difficulty) * api_weight)  # Easier API gets higher score
            )
            scores.append((metric.platform, score))
        
        return max(scores, key=lambda x: x[1])[0]

class GoogleAdsIntegration:
    """Example integration with Google Ads API."""
    def __init__(self, developer_token: str, client_id: str, client_secret: str):
        self.developer_token = developer_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://googleads.googleapis.com/v14/customers"

    def _get_access_token(self) -> str:
        """Get OAuth2 access token."""
        auth_url = "https://accounts.google.com/o/oauth2/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": "https://www.googleapis.com/auth/adwords"
        }
        response = requests.post(auth_url, data=payload)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_campaigns(self, customer_id: str) -> Optional[Dict]:
        """Get campaigns for a customer."""
        url = f"{self.base_url}/{customer_id}/googleAds:search"
        headers = {
            "Authorization": f"Bearer {self._get_access_token()}",
            "developer-token": self.developer_token
        }
        query = """
            SELECT campaign.id, campaign.name, campaign.status
            FROM campaign
            ORDER BY campaign.id
        """
        response = requests.post(url, headers=headers, json={"query": query})
        if response.status_code == 200:
            return response.json()
        return None

# Example usage
if __name__ == "__main__":
    # Define platform metrics
    platforms = [
        PlatformMetrics(
            Platform.GOOGLE_ADS,
            ctr=3.5,
            cpc=1.20,
            conversion_rate=2.8,
            roi=25,
            api_integration_difficulty=3
        ),
        PlatformMetrics(
            Platform.FACEBOOK_ADS,
            ctr=2.8,
            cpc=0.80,
            conversion_rate=3.2,
            roi=22,
            api_integration_difficulty=2
        ),
        PlatformMetrics(
            Platform.TWITTER_ADS,
            ctr=1.5,
            cpc=0.50,
            conversion_rate=1.8,
            roi=15,
            api_integration_difficulty=4
        ),
        PlatformMetrics(
            Platform.LINKEDIN_ADS,
            ctr=2.0,
            cpc=1.50,
            conversion_rate=2.5,
            roi=20,
            api_integration_difficulty=4
        ),
        PlatformMetrics(
            Platform.TIKTOK_ADS,
            ctr=4.2,
            cpc=0.60,
            conversion_rate=3.5,
            roi=28,
            api_integration_difficulty=3
        )
    ]

    # Compare platforms
    comparator = PlatformComparator(platforms)
    comparison_df = comparator.compare_platforms()
    print("Platform Comparison:")
    print(comparison_df)

    # Get recommendation
    recommended = comparator.recommend_platform(
        ctr_weight=0.3,
        cpc_weight=0.2,
        conversion_weight=0.3,
        roi_weight=0.2
    )
    print(f"\nRecommended Platform: {recommended.value}")

    # Example Google Ads integration
    google_ads = GoogleAdsIntegration(
        developer_token="YOUR_DEV_TOKEN",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET"
    )
    campaigns = google_ads.get_campaigns("1234567890")
    if campaigns:
        print("\nGoogle Ads Campaigns:")
        for campaign in campaigns.get("results", []):
            print(f"ID: {campaign['campaign']['id']}, Name: {campaign['campaign']['name']}")
```
