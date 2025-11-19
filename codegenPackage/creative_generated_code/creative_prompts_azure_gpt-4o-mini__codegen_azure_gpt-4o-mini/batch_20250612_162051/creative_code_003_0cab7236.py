"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedailyworld.com
Prompt: What are the key features to look for in an SEO agency based on the content discussing business growth in Brisbane?
Generated: DETERMINISTIC_0cab72364898651c
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/seo-agencies-brisbane": {
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
from bs4 import BeautifulSoup
import logging

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

class SEOAgency:
    """
    A class to represent an SEO agency and its key features.
    """

    def __init__(self, name, website, features):
        self.name = name
        self.website = website
        self.features = features

    def display_info(self):
        """Display the agency's information."""
        print(f"Agency Name: {self.name}")
        print(f"Website: {self.website}")
        print("Key Features:")
        for feature in self.features:
            print(f"- {feature}")

def fetch_agency_data(url):
    """
    Fetch SEO agency data from a given URL.
    
    Args:
        url (str): The URL from which to fetch data.

    Returns:
        list: A list of SEOAgency objects.

    Raises:
        Exception: If an error occurs during the HTTP request or data extraction.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example parsing logic
        agencies = []
        for agency in soup.find_all('div', class_='agency'):
            name = agency.find('h2').text
            website = agency.find('a', class_='website')['href']
            features = [feature.text for feature in agency.find_all('li', class_='feature')]
            agencies.append(SEOAgency(name, website, features))

        return agencies
    except requests.RequestException as e:
        logging.error(f"HTTP Request failed: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while fetching agency data: {e}")
        raise

def main():
    """
    Main function to run the SEO agency data fetching and display.
    """
    url = "https://www.example.com/seo-agencies-brisbane"  # Replace with actual URL
    try:
        agencies = fetch_agency_data(url)
        for agency in agencies:
            agency.display_info()
            print("------")
    except Exception as e:
        logging.error(f"Failed to fetch or display agency data: {e}")

if __name__ == "__main__":
    main()
```
