"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://zyme-dendi-zanyat.online
Prompt: Create a web scraper to extract the "Первый займ бесплатно" offers from https://zyme-dendi-zanyat.online and categorize them by loan provider.
Generated: DETERMINISTIC_730bd341d53fe7ac
Batch ID: 20250612_150018

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://zyme-dendi-zanyat.online
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://zyme-dendi-zanyat.online": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_loan_offers(url):
    """
    Scrapes loan offers from the given URL and categorizes them by provider.

    Args:
        url (str): The URL to scrape.

    Returns:
        dict: A dictionary with loan providers as keys and lists of offers as values.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements containing loan offers
        loan_offers = soup.find_all('div', class_='loan-offer')

        # Initialize an empty dictionary to store the categorized loan offers
        categorized_offers = {}

        # Iterate over each loan offer
        for offer in loan_offers:
            # Extract the loan provider
            provider = offer.find('span', class_='provider').text.strip()

            # Extract the loan offer text
            offer_text = offer.find('span', class_='offer-text').text.strip()

            # Check if the offer text contains "Первый займ бесплатно"
            if "Первый займ бесплатно" in offer_text:
                # Add the offer to the categorized dictionary
                if provider not in categorized_offers:
                    categorized_offers[provider] = []
                categorized_offers[provider].append(offer_text)

        return categorized_offers

    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return None
    except Exception as e:
        logging.error(f"Scraping error: {e}")
        return None

def main():
    url = "https://zyme-dendi-zanyat.online"
    loan_offers = scrape_loan_offers(url)

    if loan_offers:
        logging.info("Loan offers scraped successfully.")
        for provider, offers in loan_offers.items():
            logging.info(f"Offers from {provider}:")
            for offer in offers:
                logging.info(offer)
    else:
        logging.info("No loan offers scraped.")

if __name__ == "__main__":
    main()
```
