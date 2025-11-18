"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malinky.pages.dev
Prompt: Create a Python script to filter SwapSpace exchange offers for Anyswap (ANY) based on privacy policies, such as no KYC requirements.
Generated: DETERMINISTIC_761551270581d39b
Batch ID: 20250612_145626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.swapspace.co/v1/offers": {
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

def fetch_swapspace_offers():
    """
    Fetches exchange offers from the SwapSpace API for Anyswap (ANY).

    Returns:
        list: A list of offers in JSON format.
    """
    api_url = "https://api.swapspace.co/v1/offers"
    payload = {
        "from": "ANY",  # Source currency
        "to": "ANY",    # Destination currency (can be adjusted as needed)
        "amount": 1     # Test amount to retrieve offers
    }
    headers = {
        "Accept": "application/json"
    }

    try:
        response = requests.get(api_url, params=payload, headers=headers)
        response.raise_for_status()  # Raise HTTP error if response code is not 200
        return response.json().get("offers", [])
    except requests.RequestException as e:
        print(f"Error fetching offers from SwapSpace API: {e}")
        return []

def filter_offers_by_privacy(offers):
    """
    Filters the exchange offers based on privacy policy, i.e., no KYC required.

    Args:
        offers (list): A list of exchange offers.

    Returns:
        list: A list of offers that do not require KYC.
    """
    # Filtering offers where "noKYC" flag is True
    return [offer for offer in offers if offer.get("noKYC")]

def display_offers(offers):
    """
    Displays the filtered exchange offers in a user-friendly way.

    Args:
        offers (list): A list of exchange offers.
    """
    if not offers:
        print("No offers available that meet the privacy policy criteria (no KYC).")
        return

    print("Filtered Offers (No KYC Required):\n")
    for offer in offers:
        print(f"Exchange: {offer.get('exchange')}")
        print(f"Rate: {offer.get('rate')} {offer.get('to')}/{offer.get('from')}")
        print(f"Minimum Amount: {offer.get('minAmount')} {offer.get('from')}")
        print(f"Maximum Amount: {offer.get('maxAmount')} {offer.get('from')}")
        print(f"Fee: {offer.get('fee')} {offer.get('from')}")
        print("-" * 40)

def main():
    """
    Main function to fetch, filter, and display SwapSpace exchange offers for Anyswap (ANY).
    """
    print("Fetching SwapSpace offers for Anyswap (ANY)...")
    offers = fetch_swapspace_offers()

    if not offers:
        print("No offers retrieved from the API.")
        return

    print("Filtering offers based on privacy (no KYC requirements)...")
    filtered_offers = filter_offers_by_privacy(offers)

    display_offers(filtered_offers)

if __name__ == "__main__":
    main()
```
