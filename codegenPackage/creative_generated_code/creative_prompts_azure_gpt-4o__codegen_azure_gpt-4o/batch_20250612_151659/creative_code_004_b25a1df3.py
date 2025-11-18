"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-crypto.yivesites.com
Prompt: Write a web scraping script in Python using BeautifulSoup to extract promotional details like "Bonus Event Begadang UpTo 50%" from the APELBET website.
Generated: DETERMINISTIC_b25a1df330f5dfef
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.apelbet.com/": {
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

def scrape_promotional_details(url):
    """
    Scrapes promotional details from a given webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of extracted promotional details as strings.
    """
    try:
        # Send an HTTP GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize an empty list to store promotional details
        promotional_details = []

        # Find and extract promotional content
        # Adjust the selectors below based on the actual structure of the target website
        for promo in soup.find_all('div', class_='promo-detail'):  # Example class name
            text = promo.get_text(strip=True)  # Extract text content
            if text:
                promotional_details.append(text)

        return promotional_details

    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"An error occurred while making the HTTP request: {e}")
        return []

    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == '__main__':
    # URL of the APELBET website (replace with the actual URL)
    website_url = 'https://www.apelbet.com/'  # Example URL; update as needed

    # Scrape promotional details
    promotions = scrape_promotional_details(website_url)

    if promotions:
        print("Promotional details found:")
        for idx, promo in enumerate(promotions, start=1):
            print(f"{idx}. {promo}")
    else:
        print("No promotional details found or an error occurred.")
```

**Note:** Replace `'https://www.apelbet.com/'` and `'div', class_='promo-detail'` with the exact URL and HTML structure of the APELBET website, as the actual structure of the site cannot be determined without accessing it. Ensure compliance with the site's terms of service regarding web scraping.
