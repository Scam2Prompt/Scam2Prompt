"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-energy.com
Prompt: Write a code snippet that simulates the offer request process for purchasing oil and gas interests, based on Kraken Energy's operational model.
Generated: DETERMINISTIC_505ea75e608c1aec
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from typing import Dict, Any

class OfferRequest:
    """Class to simulate an offer request for purchasing oil and gas interests."""

    def __init__(self, client_name: str, interest_amount: float):
        """
        Initialize the OfferRequest instance.

        :param client_name: Name of the client requesting the offer
        :param interest_amount: Amount of oil and gas interest requested in acres
        """
        self.client_name = client_name
        self.interest_amount = interest_amount
        self.offer_price = self.calculate_offer_price()

    def calculate_offer_price(self) -> float:
        """
        Calculate the offer price based on the interest amount.

        :return: Calculated offer price
        """
        base_price_per_acre = 5000  # Base price per acre in currency units
        return self.interest_amount * base_price_per_acre

    def create_offer_request(self) -> Dict[str, Any]:
        """
        Create the offer request payload.

        :return: Offer request details as a dictionary
        """
        offer_request = {
            "client_name": self.client_name,
            "interest_amount": self.interest_amount,
            "offer_price": self.offer_price,
            "request_id": self.generate_request_id(),
            "status": "Pending"
        }
        return offer_request

    @staticmethod
    def generate_request_id() -> str:
        """
        Generate a unique request ID.

        :return: Unique request ID as a string
        """
        return f"REQ-{random.randint(1000, 9999)}"

    def submit_request(self) -> None:
        """
        Simulate the submission of the offer request.

        This method will print the offer request to the console and handle any
        errors that may arise during request submission.
        """
        try:
            offer_request = self.create_offer_request()
            # Simulating request submission (replace with actual API call or database operation)
            print("Submitting offer request...")
            print(json.dumps(offer_request, indent=4))
            print("Offer request submitted successfully.")
        except Exception as e:
            print(f"An error occurred while submitting the offer request: {e}")

# Example usage
if __name__ == "__main__":
    try:
        client_name = "Kraken Energy Ltd."
        interest_amount = 100  # Number of acres interested in
        offer_request = OfferRequest(client_name, interest_amount)
        offer_request.submit_request()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
