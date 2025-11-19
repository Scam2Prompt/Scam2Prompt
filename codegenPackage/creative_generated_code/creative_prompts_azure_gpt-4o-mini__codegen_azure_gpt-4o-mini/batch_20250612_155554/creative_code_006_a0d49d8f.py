"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vilavi.online
Prompt: Create a tutorial for using Plesk to monitor the health of multiple WordPress sites with WP Guardian.
Generated: DETERMINISTIC_a0d49d8fe96bc94e
Batch ID: 20250612_155554
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-url:8443/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://wpguardian.com/api/v1/health-check?url={site_url": {
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
import json

class PleskWPGuardianMonitor:
    """
    A class to monitor the health of multiple WordPress sites using Plesk and WP Guardian API.
    """

    def __init__(self, plesk_api_url, api_key):
        """
        Initializes the monitor with Plesk API details.

        :param plesk_api_url: URL of the Plesk API
        :param api_key: API key for authentication
        """
        self.plesk_api_url = plesk_api_url
        self.api_key = api_key

    def get_sites(self):
        """
        Fetches the list of WordPress sites from Plesk.

        :return: List of WordPress sites
        :raises Exception: If the request fails
        """
        try:
            response = requests.get(
                f"{self.plesk_api_url}/sites",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise an error for bad responses
            sites = response.json()
            return sites.get('data', [])
        except requests.RequestException as e:
            raise Exception(f"Error fetching sites: {str(e)}")

    def check_site_health(self, site_url):
        """
        Checks the health of a single WordPress site using WP Guardian API.

        :param site_url: URL of the WordPress site
        :return: Health check results
        :raises Exception: If the health check fails
        """
        try:
            response = requests.get(f"https://wpguardian.com/api/v1/health-check?url={site_url}")
            response.raise_for_status()  # Raise an error for bad responses
            health_data = response.json()
            return health_data
        except requests.RequestException as e:
            raise Exception(f"Error checking health for {site_url}: {str(e)}")

    def monitor_sites(self):
        """
        Monitors the health of all WordPress sites managed by Plesk.

        :return: Dictionary of health statuses keyed by site URL
        """
        sites = self.get_sites()
        health_statuses = {}

        for site in sites:
            site_url = site['url']
            health_status = self.check_site_health(site_url)
            health_statuses[site_url] = health_status

        return health_statuses

if __name__ == "__main__":
    # Example usage
    PLESK_API_URL = "https://your-plesk-url:8443/api/v2"
    API_KEY = "your_api_key_here"

    monitor = PleskWPGuardianMonitor(PLESK_API_URL, API_KEY)
    
    try:
        results = monitor.monitor_sites()
        print(json.dumps(results, indent=4))
    except Exception as e:
        print(f"Monitoring failed: {str(e)}")
```
