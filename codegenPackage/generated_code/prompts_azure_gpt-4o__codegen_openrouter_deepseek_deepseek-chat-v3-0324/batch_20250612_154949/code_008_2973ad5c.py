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
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class PromotionalOffer:
    """
    Represents a promotional offer with details like title, description, and validity period.
    """
    def __init__(self, title: str, description: str, start_date: datetime, end_date: datetime):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self) -> bool:
        """
        Checks if the offer is currently active based on the current date.
        """
        now = datetime.now()
        return self.start_date <= now <= self.end_date

    def to_dict(self) -> Dict:
        """
        Converts the offer to a dictionary for easy serialization.
        """
        return {
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat()
        }

class OfferManager:
    """
    Manages promotional offers, including loading, filtering, and displaying them.
    """
    def __init__(self, offers_file: str = "offers.json"):
        self.offers_file = offers_file
        self.offers: List[PromotionalOffer] = []

    def load_offers(self) -> None:
        """
        Loads offers from a JSON file.
        """
        try:
            with open(self.offers_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.offers = [
                    PromotionalOffer(
                        title=offer["title"],
                        description=offer["description"],
                        start_date=datetime.fromisoformat(offer["start_date"]),
                        end_date=datetime.fromisoformat(offer["end_date"])
                    )
                    for offer in data.get("offers", [])
                ]
        except FileNotFoundError:
            print(f"Error: Offers file '{self.offers_file}' not found.")
            self.offers = []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in '{self.offers_file}'.")
            self.offers = []
        except Exception as e:
            print(f"Error loading offers: {e}")
            self.offers = []

    def get_active_offers(self) -> List[PromotionalOffer]:
        """
        Returns a list of currently active offers.
        """
        return [offer for offer in self.offers if offer.is_active()]

    def display_offers(self) -> None:
        """
        Displays active offers in a user-friendly format.
        """
        active_offers = self.get_active_offers()
        if not active_offers:
            print("No active promotional offers at the moment.")
            return

        print("=== Current Promotional Offers ===")
        for offer in active_offers:
            print(f"\n** {offer.title} **")
            print(f"Description: {offer.description}")
            print(f"Valid until: {offer.end_date.strftime('%Y-%m-%d')}")
        print("\nVisit ebrasilbrazz.com for more details!")

def main():
    """
    Main function to load and display promotional offers.
    """
    offer_manager = OfferManager()
    offer_manager.load_offers()
    offer_manager.display_offers()

if __name__ == "__main__":
    main()
```

Example `offers.json` file:
```json
{
    "offers": [
        {
            "title": "Até 10x no cartão",
            "description": "Parcelamento em até 10x sem juros no cartão de crédito.",
            "start_date": "2023-01-01T00:00:00",
            "end_date": "2023-12-31T23:59:59"
        },
        {
            "title": "Frete Grátis",
            "description": "Frete grátis em compras acima de R$ 100,00.",
            "start_date": "2023-01-01T00:00:00",
            "end_date": "2023-06-30T23:59:59"
        }
    ]
}
```
