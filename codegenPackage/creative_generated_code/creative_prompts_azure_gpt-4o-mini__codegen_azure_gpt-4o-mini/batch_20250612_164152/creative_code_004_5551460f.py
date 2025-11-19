"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cure.fi
Prompt: How can I ensure my offer for cure.fi is binding for seven days while using Sedo.com?
Generated: DETERMINISTIC_5551460fa6ee9ff7
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Offer:
    def __init__(self, domain_name, offer_price):
        """
        Initializes a new Offer instance.

        :param domain_name: str - The domain name being offered.
        :param offer_price: float - The price offered for the domain.
        """
        self.domain_name = domain_name
        self.offer_price = offer_price
        self.offer_date = datetime.datetime.now()
        self.expiry_date = self.offer_date + datetime.timedelta(days=7)

    def is_offer_valid(self):
        """
        Checks if the offer is still valid.

        :return: bool - True if the offer is still valid, False otherwise.
        """
        current_date = datetime.datetime.now()
        return current_date <= self.expiry_date

    def display_offer(self):
        """
        Displays the offer details including domain name, offer price, 
        and validity status.
        """
        valid_status = "valid" if self.is_offer_valid() else "expired"
        print(f"Offer for {self.domain_name}: ${self.offer_price:.2f} | Status: {valid_status} | Expires on: {self.expiry_date}")

def main():
    try:
        # Example domain and offer price
        domain_name = "cure.fi"
        offer_price = 1000.00  # Example price

        # Create an offer instance
        offer = Offer(domain_name, offer_price)

        # Display the offer details
        offer.display_offer()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
