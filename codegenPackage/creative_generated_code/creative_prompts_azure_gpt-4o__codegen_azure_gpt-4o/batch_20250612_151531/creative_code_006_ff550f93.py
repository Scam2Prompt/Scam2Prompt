"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jio.sh
Prompt: Suggest methods to optimize the use of JioSh's short URL service for social media campaigns.
Generated: DETERMINISTIC_ff550f931d7af84e
Batch ID: 20250612_151531
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/product1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/product2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/product3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.jiosh.com/v1": {
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
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ShortURLService:
    """
    A class to interact with the JioSh short URL service and optimize its usage for social media campaigns.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.jiosh.com/v1"):
        """
        Initialize the ShortURLService instance.
        
        :param api_key: API key for authenticating with the JioSh service.
        :param base_url: Base URL for the JioSh API. Defaults to "https://api.jiosh.com/v1".
        """
        self.api_key = api_key
        self.base_url = base_url

    def shorten_url(self, long_url: str, custom_alias: str = None) -> str:
        """
        Shorten a given URL using the JioSh service.
        
        :param long_url: The original long URL to be shortened.
        :param custom_alias: Optional custom alias for the short URL.
        :return: The shortened URL or None if the operation fails.
        """
        endpoint = f"{self.base_url}/shorten"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"long_url": long_url}
        if custom_alias:
            payload["custom_alias"] = custom_alias
        
        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("short_url")
        except requests.exceptions.RequestException as e:
            logging.error("Error during URL shortening: %s", e)
            return None

    def batch_shorten_urls(self, url_list: list) -> list:
        """
        Shorten multiple URLs at once using the JioSh service.
        
        :param url_list: List of URLs to be shortened.
        :return: List of shortened URLs or None for URLs that failed to shorten.
        """
        shortened_urls = []
        for url in url_list:
            short_url = self.shorten_url(url)
            if short_url:
                shortened_urls.append(short_url)
            else:
                shortened_urls.append(None)
        return shortened_urls

    def track_url_performance(self, short_url: str) -> dict:
        """
        Retrieve performance metrics for a given shortened URL.
        
        :param short_url: The short URL whose performance metrics are to be retrieved.
        :return: A dictionary containing performance data or an empty dictionary if the operation fails.
        """
        endpoint = f"{self.base_url}/performance"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"short_url": short_url}
        
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error("Error retrieving URL performance: %s", e)
            return {}

    def optimize_social_campaign(self, url_list: list) -> dict:
        """
        Optimize social media campaigns by shortening URLs and tracking performance.
        
        :param url_list: List of original URLs to be used in the campaign.
        :return: A mapping of original URLs to their shortened URLs and performance data.
        """
        optimized_data = {}
        shortened_urls = self.batch_shorten_urls(url_list)
        
        for original_url, short_url in zip(url_list, shortened_urls):
            if short_url:
                performance_data = self.track_url_performance(short_url)
                optimized_data[original_url] = {
                    "short_url": short_url,
                    "performance_data": performance_data
                }
            else:
                optimized_data[original_url] = {
                    "short_url": None,
                    "performance_data": {}
                }
        
        return optimized_data


# Example Usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    service = ShortURLService(api_key=API_KEY)

    # URLs for the campaign
    urls = [
        "https://example.com/product1",
        "https://example.com/product2",
        "https://example.com/product3"
    ]

    # Optimize the campaign
    campaign_data = service.optimize_social_campaign(urls)
    
    # Log results
    for original_url, data in campaign_data.items():
        logging.info("Original URL: %s", original_url)
        logging.info("Short URL: %s", data["short_url"])
        logging.info("Performance Data: %s", data["performance_data"])
```
