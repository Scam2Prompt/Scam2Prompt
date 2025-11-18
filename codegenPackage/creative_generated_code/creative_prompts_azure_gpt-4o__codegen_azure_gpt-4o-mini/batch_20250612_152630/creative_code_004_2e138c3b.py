"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w3.toonanime.co
Prompt: Create an API client in Python to interact with Toonanime's sitemap and retrieve metadata for anime episodes categorized under "Action" and "Adventure."
Generated: DETERMINISTIC_2e138c3b7371d8ab
Batch ID: 20250612_152630
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://toonanime.com/sitemap.xml": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.sitemaps.org/schemas/sitemap-image/1.1}loc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.sitemaps.org/schemas/sitemap-image/1.1}category": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.sitemaps.org/schemas/sitemap-image/1.1}url": {
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
from xml.etree import ElementTree as ET

class ToonanimeAPIClient:
    """
    A client for interacting with Toonanime's sitemap to retrieve metadata
    for anime episodes categorized under "Action" and "Adventure".
    """

    def __init__(self, sitemap_url):
        """
        Initializes the Toonanime API client with the sitemap URL.

        Args:
            sitemap_url (str): The URL of the Toonanime sitemap.
        """
        self.sitemap_url = sitemap_url

    def fetch_sitemap(self):
        """
        Fetches the sitemap XML from the specified URL.

        Returns:
            str: The raw XML content of the sitemap.
        
        Raises:
            requests.RequestException: If the HTTP request to fetch the sitemap fails.
        """
        try:
            response = requests.get(self.sitemap_url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.text
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch sitemap: {e}")

    def parse_sitemap(self, xml_content):
        """
        Parses the sitemap XML content to extract episode URLs categorized as 
        "Action" or "Adventure".

        Args:
            xml_content (str): The raw XML content of the sitemap.

        Returns:
            list: A list of episode URLs categorized under "Action" and "Adventure".
        """
        try:
            root = ET.fromstring(xml_content)
            episode_urls = []

            # Iterate over sitemap entries
            for url in root.findall('{http://www.sitemaps.org/schemas/sitemap-image/1.1}url'):
                loc = url.find('{http://www.sitemaps.org/schemas/sitemap-image/1.1}loc')
                category = url.find('{http://www.sitemaps.org/schemas/sitemap-image/1.1}category')

                if loc is not None and category is not None:
                    category_text = category.text.lower()
                    if category_text in ["action", "adventure"]:
                        episode_urls.append(loc.text)
            
            return episode_urls

        except ET.ParseError as e:
            raise RuntimeError(f"Failed to parse sitemap XML: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while parsing the sitemap: {e}")

    def get_action_adventure_episodes(self):
        """
        Retrieves episode URLs categorized under "Action" and "Adventure".

        Returns:
            list: A list of episode URLs under the specified categories.
        """
        xml_content = self.fetch_sitemap()
        return self.parse_sitemap(xml_content)

# Example usage (this would normally be in a separate script)
if __name__ == "__main__":
    sitemap_url = "https://toonanime.com/sitemap.xml"  # Replace with the actual sitemap URL
    client = ToonanimeAPIClient(sitemap_url)

    try:
        episodes = client.get_action_adventure_episodes()
        print("Action and Adventure Episodes:")
        for episode in episodes:
            print(episode)
    except RuntimeError as e:
        print(f"Error: {e}")
```
