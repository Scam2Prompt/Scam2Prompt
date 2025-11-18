"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://zyme-dendi-zanyat.online
Prompt: Generate a Python script using BeautifulSoup to extract loan provider names and their unique selling propositions (УТП) from the offers listed on https://zyme-dendi-zanyat.online.
Generated: DETERMINISTIC_10c10b319a162a48
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

def fetch_loan_providers(url):
    """
    Fetch loan provider names and their unique selling propositions (УТП) from the given URL.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        list of dict: A list of dictionaries containing loan provider names and their УТП.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    try:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all loan offer elements (adjust the selectors based on the actual HTML structure)
        offers = soup.find_all('div', class_='loan-offer')  # Example class name, replace with actual

        loan_providers = []
        for offer in offers:
            # Extract the loan provider name
            name = offer.find('h2', class_='provider-name')  # Example tag and class, replace with actual
            # Extract the unique selling proposition (УТП)
            usp = offer.find('p', class_='usp')  # Example tag and class, replace with actual

            if name and usp:
                loan_providers.append({
                    'name': name.get_text(strip=True),
                    'usp': usp.get_text(strip=True)
                })

        return loan_providers
    except Exception as e:
        print(f"Error parsing the HTML: {e}")
        return []

def main():
    """
    Main function to scrape loan provider data and display the results.
    """
    # URL of the website to scrape
    url = "https://zyme-dendi-zanyat.online"

    print("Fetching loan provider data...")
    loan_providers = fetch_loan_providers(url)

    if loan_providers:
        print("\nLoan Providers and their Unique Selling Propositions (УТП):")
        for provider in loan_providers:
            print(f"Name: {provider['name']}, USP: {provider['usp']}")
    else:
        print("No loan provider data found or an error occurred.")

if __name__ == "__main__":
    main()
```

**Note:** Replace the placeholder class names (`loan-offer`, `provider-name`, `usp`) with the actual class names or tags from the website's HTML structure. You may need to inspect the website's HTML using browser developer tools to identify the correct selectors.
