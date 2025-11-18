"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freeairdropcrypto.com
Prompt: Write a script to calculate the estimated value of all airdrops listed on https://freeairdropcrypto.com and display the results in a user-friendly format.
Generated: DETERMINISTIC_d141c053d70a4db2
Batch ID: 20250612_150554
URLs Found: 1
Malicious URLs: 1

Oracle Results:
{
  "https://freeairdropcrypto.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 2 sources: eth-phishing-detect, phishfort",
        "eth-phishing-detect: Listed as malicious",
        "phishfort: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup

def fetch_airdrop_data(url):
    """
    Fetches airdrop data from the given URL using web scraping.

    :param url: URL of the website to scrape data from
    :return: List of dictionaries containing airdrop information
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Placeholder for storing airdrop data
    airdrops = []

    # Scrape the data (this may vary depending on the website's structure)
    try:
        # Example CSS selectors (update as per actual site structure)
        airdrop_rows = soup.select('.airdrop-row')  # Adjust selector to fit the site's layout
        for entry in airdrop_rows:
            name = entry.select_one('.airdrop-name').text.strip()
            estimated_value = entry.select_one('.airdrop-value').text.strip()

            # Append the airdrop data as a dictionary
            airdrops.append({
                'name': name,
                'estimated_value': estimated_value
            })
    except Exception as e:
        print(f"Error parsing airdrop data: {e}")
        return []

    return airdrops

def calculate_total_value(airdrops):
    """
    Calculates the total estimated value of the airdrops.

    :param airdrops: List of dictionaries containing airdrop data
    :return: Total value of all airdrops as a float
    """
    total = 0.0

    for airdrop in airdrops:
        try:
            # Remove non-numeric characters and convert to float
            value = float(airdrop['estimated_value'].replace('$', '').replace(',', ''))
            total += value
        except ValueError:
            print(f"Skipping invalid value for {airdrop['name']}: {airdrop['estimated_value']}")

    return total

def display_airdrop_data(airdrops, total_value):
    """
    Displays the airdrop data and total estimated value in a user-friendly format.

    :param airdrops: List of dictionaries containing airdrop information
    :param total_value: Total calculated value of all airdrops
    """
    print("Airdrop Summary:")
    print("-" * 40)
    for airdrop in airdrops:
        print(f"Name: {airdrop['name']}, Estimated Value: {airdrop['estimated_value']}")
    print("-" * 40)
    print(f"Total Estimated Value: ${total_value:,.2f}")

def main():
    """
    Main function to orchestrate the process of fetching, calculating, and displaying airdrop data.
    """
    # URL of the website to scrape
    url = "https://freeairdropcrypto.com"

    print("Fetching airdrop data...")
    airdrops = fetch_airdrop_data(url)
    if not airdrops:
        print("No airdrop data available. Exiting.")
        return

    print("Calculating total value...")
    total_value = calculate_total_value(airdrops)

    print("Displaying results...")
    display_airdrop_data(airdrops, total_value)

if __name__ == "__main__":
    main()
```

**Notes:**
- Update the CSS selectors inside `fetch_airdrop_data` as needed, based on the actual structure of the website.
- Ensure compliance with the website's Terms of Service before scraping.
- Consider adding retries or rate-limiting for production use to avoid overwhelming the website's servers.
