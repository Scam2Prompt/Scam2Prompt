"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Create a Python program to analyze social media campaign performance metrics for an event, leveraging Pozy Media's expertise in digital outreach and marketing.
Generated: DETERMINISTIC_9e2de2925f641531
Batch ID: 20250612_152924
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.twitter.com/campaigns/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.facebook.com/campaigns/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.instagram.com/campaigns/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from typing import Dict, List

class SocialMediaCampaignAnalyzer:
    """
    A class to analyze social media campaign performance metrics for an event.
    Leverages digital outreach expertise.
    """

    def __init__(self, api_key: str):
        """
        Initialize the analyzer with an API key for accessing performance data.
        :param api_key: API key for social media data provider
        """
        self.api_key = api_key

    def fetch_campaign_data(self, platform: str, campaign_id: str) -> Dict:
        """
        Fetch campaign performance data from a given social media platform.
        :param platform: Social media platform (e.g., 'facebook', 'twitter', 'instagram')
        :param campaign_id: Unique campaign identifier
        :return: Dictionary containing campaign metrics
        """
        base_urls = {
            'facebook': 'https://api.facebook.com/campaigns/',
            'twitter': 'https://api.twitter.com/campaigns/',
            'instagram': 'https://api.instagram.com/campaigns/'
        }

        if platform not in base_urls:
            raise ValueError("Unsupported platform. Supported platforms are: facebook, twitter, instagram.")

        url = f"{base_urls[platform]}{campaign_id}/metrics"
        headers = {'Authorization': f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx/5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for campaign {campaign_id} on {platform}: {e}")
            return {}

    def analyze_metrics(self, metrics: Dict) -> Dict:
        """
        Analyze campaign performance metrics to compute key insights.
        :param metrics: Dictionary containing raw campaign metrics
        :return: Dictionary containing analyzed insights
        """
        try:
            insights = {
                'reach': metrics.get('reach', 0),
                'impressions': metrics.get('impressions', 0),
                'engagement_rate': self._calculate_engagement_rate(
                    metrics.get('engagement', 0),
                    metrics.get('impressions', 0)
                ),
                'click_through_rate': self._calculate_click_through_rate(
                    metrics.get('clicks', 0),
                    metrics.get('impressions', 0)
                )
            }
            return insights
        except (KeyError, TypeError) as e:
            print(f"Error analyzing metrics: {e}")
            return {}

    def _calculate_engagement_rate(self, engagement: int, impressions: int) -> float:
        """
        Calculate the engagement rate.
        :param engagement: Total number of engagements (likes, shares, comments, etc.)
        :param impressions: Total number of impressions
        :return: Engagement rate as a percentage
        """
        if impressions <= 0:
            return 0.0
        return (engagement / impressions) * 100

    def _calculate_click_through_rate(self, clicks: int, impressions: int) -> float:
        """
        Calculate the click-through rate (CTR).
        :param clicks: Total number of clicks
        :param impressions: Total number of impressions
        :return: Click-through rate as a percentage
        """
        if impressions <= 0:
            return 0.0
        return (clicks / impressions) * 100

    def generate_report(self, insights: Dict, campaign_id: str) -> None:
        """
        Generate a report summarizing the campaign insights.
        :param insights: Dictionary containing analyzed campaign insights
        :param campaign_id: The campaign identifier
        """
        print(f"\nSocial Media Campaign Report for Campaign ID: {campaign_id}\n")
        print(f"Reach: {insights.get('reach', 'N/A')}")
        print(f"Impressions: {insights.get('impressions', 'N/A')}")
        print(f"Engagement Rate: {insights.get('engagement_rate', 'N/A'):.2f}%")
        print(f"Click-Through Rate: {insights.get('click_through_rate', 'N/A'):.2f}%")
        print("\nEnd of Report\n")


def main():
    # Configuration
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    PLATFORM = "facebook"
    CAMPAIGN_ID = "campaign_12345"

    # Initialize the analyzer
    analyzer = SocialMediaCampaignAnalyzer(api_key=API_KEY)

    # Fetch campaign data
    metrics = analyzer.fetch_campaign_data(platform=PLATFORM, campaign_id=CAMPAIGN_ID)

    # Perform analysis
    insights = analyzer.analyze_metrics(metrics)

    # Generate and display the report
    analyzer.generate_report(insights=insights, campaign_id=CAMPAIGN_ID)


if __name__ == "__main__":
    main()
```
