"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promocrypt.com
Prompt: Generate a code snippet that automates the process of submitting a domain purchase offer on Sedo, referencing promocrypt.com as an example.
Generated: DETERMINISTIC_19722117e98a246d
Batch ID: 20250612_155137
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.sedo.com": {
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
from requests.exceptions import HTTPError, RequestException

class SedoDomainOffer:
    """
    A class to automate the submission of a domain purchase offer on Sedo.
    """

    def __init__(self, username, password):
        """
        Initializes the SedoDomainOffer instance with user credentials.

        :param username: The username for Sedo account
        :param password: The password for Sedo account
        """
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.base_url = "https://www.sedo.com"

    def login(self):
        """
        Logs into the Sedo account using the provided credentials.

        :raises Exception: If login fails
        """
        login_url = f"{self.base_url}/login"
        payload = {
            'username': self.username,
            'password': self.password
        }
        
        try:
            response = self.session.post(login_url, data=payload)
            response.raise_for_status()  # Raise an error for bad responses
        except HTTPError as http_err:
            raise Exception(f"HTTP error occurred during login: {http_err}")
        except RequestException as req_err:
            raise Exception(f"Request exception occurred during login: {req_err}")
        else:
            if "Login successful" not in response.text:
                raise Exception("Login failed: Check your username/password")

    def submit_offer(self, domain_name, offer_price):
        """
        Submits a purchase offer for the specified domain.

        :param domain_name: The domain name to purchase (e.g., promocrypt.com)
        :param offer_price: The offer price for the domain
        :raises Exception: If offer submission fails
        """
        offer_url = f"{self.base_url}/submit-offer"
        payload = {
            'domain': domain_name,
            'price': offer_price
        }

        try:
            response = self.session.post(offer_url, data=payload)
            response.raise_for_status()  # Raise an error for bad responses
        except HTTPError as http_err:
            raise Exception(f"HTTP error occurred during offer submission: {http_err}")
        except RequestException as req_err:
            raise Exception(f"Request exception occurred during offer submission: {req_err}")
        else:
            if "Offer submitted successfully" not in response.text:
                raise Exception("Offer submission failed: Check your details")

def main():
    """
    Main function to execute the domain purchase offer submission.
    """
    username = "your_username"  # Replace with your Sedo username
    password = "your_password"  # Replace with your Sedo password
    domain_name = "promocrypt.com"
    offer_price = 1000  # Example offer price in your currency

    try:
        sedo_offer = SedoDomainOffer(username, password)
        sedo_offer.login()
        sedo_offer.submit_offer(domain_name, offer_price)
        print("Offer submitted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
