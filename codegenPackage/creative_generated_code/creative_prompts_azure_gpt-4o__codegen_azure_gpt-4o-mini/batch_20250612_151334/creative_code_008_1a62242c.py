"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namestajnovidom.com
Prompt: Write a script to detect 먹튀 sites by monitoring sudden closures and tracking user complaints, as warned in the 토토플레이 site's cautionary section.
Generated: DETERMINISTIC_1a62242c4c413bad
Batch ID: 20250612_151334
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://testsite.com": {
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
import time
import logging
from datetime import datetime
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO, filename='site_monitor.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SiteMonitor:
    def __init__(self, sites, check_interval=60):
        """
        Initialize the SiteMonitor with a list of sites to monitor and the check interval.

        :param sites: List of URLs to monitor.
        :param check_interval: Time in seconds between checks.
        """
        self.sites = sites
        self.check_interval = check_interval
        self.site_status = defaultdict(list)  # Store status history for each site.

    def check_site(self, url):
        """
        Check the status of a site and log any issues.

        :param url: The URL of the site to check.
        :return: Boolean indicating if the site is up.
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an error for bad status codes
            logging.info(f'Site {url} is up.')
            return True
        except requests.RequestException as e:
            logging.error(f'Site {url} is down: {e}')
            return False

    def track_complaints(self):
        """
        Simulate tracking user complaints against sites (stub function).
        This should be replaced with actual logic to fetch complaints.
        """
        # Placeholder for complaints tracking logic.
        # In a real implementation, this might involve querying a database or an API.
        return {"example.com": 5, "testsite.com": 10}  # Mocked complaints data

    def monitor_sites(self):
        """
        Monitor each site at the specified intervals and log any closures or complaints.
        """
        while True:
            for url in self.sites:
                site_up = self.check_site(url)
                timestamp = datetime.now().isoformat()

                # Record the site's status
                self.site_status[url].append((timestamp, site_up))

                # Check for user complaints
                complaints = self.track_complaints()
                if url in complaints and complaints[url] > 0:
                    logging.warning(f'Site {url} has {complaints[url]} user complaints.')

            time.sleep(self.check_interval)

if __name__ == "__main__":
    # List of sites to monitor - replace with actual sites you want to track
    sites_to_monitor = ['http://example.com', 'http://testsite.com']

    # Initialize the SiteMonitor
    site_monitor = SiteMonitor(sites=sites_to_monitor)
    
    # Start monitoring the sites
    try:
        site_monitor.monitor_sites()
    except KeyboardInterrupt:
        logging.info("Site monitoring stopped by user.")
```
