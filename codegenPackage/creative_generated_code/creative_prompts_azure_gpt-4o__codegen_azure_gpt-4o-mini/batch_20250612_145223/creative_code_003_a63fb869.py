"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Create a script to integrate brand-specific offers (e.g., WMF, Sky, SIXT rent a car) into a corporate benefits portal, ensuring proper categorization and display.
Generated: DETERMINISTIC_a63fb869f2e11a43
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Offer:
    """Class to represent a brand-specific offer."""
    
    def __init__(self, brand: str, description: str, discount: float, category: str):
        self.brand = brand
        self.description = description
        self.discount = discount
        self.category = category

    def to_dict(self) -> Dict[str, Any]:
        """Convert the offer to a dictionary for JSON serialization."""
        return {
            "brand": self.brand,
            "description": self.description,
            "discount": self.discount,
            "category": self.category
        }


class OffersManager:
    """Class to manage the integration of offers into the corporate benefits portal."""
    
    def __init__(self):
        # Store offers in a dictionary categorized by brand
        self.offers: Dict[str, List[Offer]] = {}

    def add_offer(self, brand: str, description: str, discount: float, category: str):
        """Add a new offer to the manager."""
        if discount < 0:
            logging.error("Discount cannot be negative.")
            raise ValueError("Discount must be a non-negative value.")
        
        offer = Offer(brand, description, discount, category)
        if brand not in self.offers:
            self.offers[brand] = []
        self.offers[brand].append(offer)
        logging.info(f"Added offer: {offer.to_dict()}")

    def get_offers(self) -> List[Dict[str, Any]]:
        """Retrieve all offers as a list of dictionaries."""
        all_offers = [offer.to_dict() for brand_offers in self.offers.values() for offer in brand_offers]
        logging.info(f"Retrieved offers: {all_offers}")
        return all_offers

    def save_offers_to_file(self, filename: str):
        """Save the offers to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_offers(), file, indent=4)
            logging.info(f"Offers saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to write to {filename}: {e}")
            raise RuntimeError(f"Could not save offers to file {filename}.") from e

def main():
    """Main function to demonstrate the OffersManager functionality."""
    try:
        manager = OffersManager()
        # Adding sample offers
        manager.add_offer("WMF", "20% off kitchenware", 20.0, "Home & Kitchen")
        manager.add_offer("Sky", "Free first month subscription", 100.0, "Entertainment")
        manager.add_offer("SIXT", "15% off car rentals", 15.0, "Transportation")

        # Retrieve and save offers
        offers = manager.get_offers()
        manager.save_offers_to_file("offers.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
