"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fusionjiujitsu.com.br
Prompt: Write a Python script to scrape the Fusion Jiu Jitsu School's contact information, including phone number, address, and social media links.
Generated: DETERMINISTIC_dea740d516b3bbf6
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.fusionjiujitsu.com/contact": {
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

class FusionJiuJitsuScraper:
    def __init__(self, url):
        self.url = url
        self.contact_info = {}

    def fetch_page(self):
        """Fetch the webpage content using GET request."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            return None

    def parse_contact_info(self, html):
        """Parse the contact information from the HTML content."""
        soup = BeautifulSoup(html, 'html.parser')

        # Extract phone number
        phone = soup.find('a', href=lambda href: href and "tel:" in href)
        self.contact_info['phone'] = phone.text.strip() if phone else "Phone not found"

        # Extract address
        address = soup.find('address')
        self.contact_info['address'] = address.get_text(strip=True) if address else "Address not found"

        # Extract social media links
        social_links = {
            'facebook': None,
            'instagram': None,
            'twitter': None
        }
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'facebook.com' in href:
                social_links['facebook'] = href
            elif 'instagram.com' in href:
                social_links['instagram'] = href
            elif 'twitter.com' in href:
                social_links['twitter'] = href

        self.contact_info['social_media'] = social_links

    def scrape(self):
        """Main method to scrape contact information."""
        html_content = self.fetch_page()
        if html_content:
            self.parse_contact_info(html_content)
            return self.contact_info
        return None

if __name__ == "__main__":
    # URL of the Fusion Jiu Jitsu School's contact page
    URL = "https://www.fusionjiujitsu.com/contact"  # Replace with the actual URL

    # Create a scraper instance and scrape contact info
    scraper = FusionJiuJitsuScraper(URL)
    contact_info = scraper.scrape()

    # Print the scraped contact information
    if contact_info:
        print("Contact Information:")
        for key, value in contact_info.items():
            print(f"{key.capitalize()}: {value}")
```

Make sure to replace the URL in the `URL` variable with the actual contact page URL of Fusion Jiu Jitsu School before running the script.
