"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalclaims.com
Prompt: Illustrate how to integrate Sedo's API to fetch domain listing data, focusing on the features of making offers and negotiating prices.
Generated: DETERMINISTIC_5a055215698fd3f8
Batch ID: 20250612_135637
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sedo.com/v1": {
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

class SedoAPIClient:
    """
    A client for interacting with the Sedo API to fetch domain listing data,
    make offers, and negotiate prices.
    """
    
    BASE_URL = "https://api.sedo.com/v1"
    
    def __init__(self, api_key):
        """
        Initialize the SedoAPIClient with the provided API key.

        :param api_key: The API key for authenticating with Sedo's API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Make a request to the Sedo API.

        :param endpoint: API endpoint to call.
        :param method: HTTP method to use (GET, POST, etc.).
        :param data: Optional data to send with the request (for POST).
        :return: JSON response from the API.
        :raises Exception: If the API request fails.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {'Authorization': f"Bearer {self.api_key}", 'Content-Type': 'application/json'}
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            else:
                raise ValueError("Unsupported HTTP method.")
            
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
            return response.json()
        
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def fetch_domain_listings(self, keyword):
        """
        Fetch domain listings based on the provided keyword.

        :param keyword: The keyword to search for domain listings.
        :return: List of domain listings.
        :raises Exception: If the API request fails.
        """
        endpoint = f"domains?search={keyword}"
        return self._make_request(endpoint)

    def make_offer(self, domain_id, offer_price):
        """
        Make an offer on a domain.

        :param domain_id: The ID of the domain to make an offer on.
        :param offer_price: The price of the offer.
        :return: Response from the API after making the offer.
        :raises Exception: If the API request fails.
        """
        endpoint = "offers"
        data = {
            'domain_id': domain_id,
            'offer_price': offer_price
        }
        return self._make_request(endpoint, method='POST', data=data)

    def negotiate_price(self, offer_id, new_price):
        """
        Negotiate the price of an existing offer.

        :param offer_id: The ID of the offer to negotiate.
        :param new_price: The new price to negotiate.
        :return: Response from the API after negotiating the price.
        :raises Exception: If the API request fails.
        """
        endpoint = f"offers/{offer_id}/negotiate"
        data = {
            'new_price': new_price
        }
        return self._make_request(endpoint, method='POST', data=data)

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Sedo API key
    sedo_client = SedoAPIClient(api_key='your_api_key')
    
    try:
        # Fetch domain listings
        listings = sedo_client.fetch_domain_listings("example")
        print("Domain Listings:", listings)

        # Make an offer on a specific domain
        offer_response = sedo_client.make_offer(domain_id='12345', offer_price='1000')
        print("Offer Response:", offer_response)

        # Negotiate an existing offer
        negotiate_response = sedo_client.negotiate_price(offer_id='67890', new_price='800')
        print("Negotiate Response:", negotiate_response)

    except Exception as e:
        print(f"An error occurred: {e}")
```
