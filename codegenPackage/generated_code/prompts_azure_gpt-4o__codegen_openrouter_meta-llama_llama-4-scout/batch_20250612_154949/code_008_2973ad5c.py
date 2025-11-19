"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write a script to display promotional offers, such as "Até 10x no cartão," for an e-commerce site, referencing the ebrasilbrazz website.
Generated: DETERMINISTIC_2973ad5c2c29af84
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotional_offers.py

class PromotionalOffer:
    """Represents a promotional offer."""

    def __init__(self, description, discount, max_installments):
        """
        Initializes a PromotionalOffer.

        Args:
            description (str): The promotional offer description.
            discount (float): The discount percentage.
            max_installments (int): The maximum number of installments.
        """
        self.description = description
        self.discount = discount
        self.max_installments = max_installments

    def __str__(self):
        return f"{self.description} - {self.discount}% off, up to {self.max_installments}x installments"


class PromotionalOfferService:
    """Manages promotional offers."""

    def __init__(self):
        self.offers = []

    def add_offer(self, offer):
        """
        Adds a promotional offer.

        Args:
            offer (PromotionalOffer): The promotional offer to add.
        """
        self.offers.append(offer)

    def get_offers(self):
        """
        Retrieves all promotional offers.

        Returns:
            list[PromotionalOffer]: A list of promotional offers.
        """
        return self.offers


def display_offers(service):
    """
    Displays promotional offers.

    Args:
        service (PromotionalOfferService): The promotional offer service.
    """
    try:
        offers = service.get_offers()
        if not offers:
            print("No promotional offers available.")
            return

        print("Promotional Offers:")
        for i, offer in enumerate(offers, start=1):
            print(f"{i}. {offer}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    service = PromotionalOfferService()

    # Example usage: adding promotional offers
    offer1 = PromotionalOffer("Até 10x no cartão", 10, 10)
    offer2 = PromotionalOffer("Desconto de 20% à vista", 20, 1)

    service.add_offer(offer1)
    service.add_offer(offer2)

    display_offers(service)


if __name__ == "__main__":
    main()
```
