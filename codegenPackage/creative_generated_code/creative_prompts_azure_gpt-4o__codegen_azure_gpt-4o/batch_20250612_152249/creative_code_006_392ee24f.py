"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whales-market-8x5.pages.dev
Prompt: Develop a script to reset and apply filters on Whales Market offers, ensuring compatibility with the platform's filtering system.
Generated: DETERMINISTIC_392ee24f34f71ca9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WhalesMarket:
    def __init__(self):
        """
        Initialize the Whales Market with an empty list of offers and filters.
        """
        self.offers = []  # List to hold market offers
        self.filters = {}  # Dictionary to hold filters

    def reset_offers(self):
        """
        Clears all offers from the market.
        """
        try:
            self.offers.clear()
            logging.info("Market offers have been reset successfully.")
        except Exception as e:
            logging.error("Failed to reset market offers: %s", str(e))
            raise

    def reset_filters(self):
        """
        Clears all filters applied to the market.
        """
        try:
            self.filters.clear()
            logging.info("Market filters have been reset successfully.")
        except Exception as e:
            logging.error("Failed to reset market filters: %s", str(e))
            raise

    def apply_filters(self, filters):
        """
        Applies the specified filters to the market.

        Args:
            filters (dict): Dictionary containing filter criteria.
        """
        if not isinstance(filters, dict):
            raise ValueError("Filters must be provided as a dictionary.")

        try:
            self.filters = filters
            logging.info("Filters have been successfully applied: %s", filters)
        except Exception as e:
            logging.error("Failed to apply filters: %s", str(e))
            raise

    def get_filtered_offers(self):
        """
        Retrieves offers filtered based on the current filters.

        Returns:
            list: Filtered offers.
        """
        try:
            if not self.filters:
                logging.warning("No filters applied. Returning all offers.")
                return self.offers
            
            filtered_offers = [
                offer for offer in self.offers
                if all(offer.get(key) == value for key, value in self.filters.items())
            ]

            logging.info("Filtered offers retrieved successfully.")
            return filtered_offers
        except Exception as e:
            logging.error("Failed to retrieve filtered offers: %s", str(e))
            raise

    def add_offer(self, offer):
        """
        Adds a new offer to the market.

        Args:
            offer (dict): Dictionary representing the offer details.
        """
        if not isinstance(offer, dict):
            raise ValueError("Offer must be provided as a dictionary.")

        try:
            self.offers.append(offer)
            logging.info("Offer added successfully: %s", offer)
        except Exception as e:
            logging.error("Failed to add offer: %s", str(e))
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Whales Market
        market = WhalesMarket()

        # Add some offers to the market
        market.add_offer({"id": 1, "type": "buy", "price": 100})
        market.add_offer({"id": 2, "type": "sell", "price": 200})
        market.add_offer({"id": 3, "type": "buy", "price": 150})

        # Apply filters
        filters_to_apply = {"type": "buy"}
        market.apply_filters(filters_to_apply)

        # Retrieve filtered offers
        filtered_offers = market.get_filtered_offers()
        print("Filtered Offers:", filtered_offers)

        # Reset offers and filters
        market.reset_offers()
        market.reset_filters()

    except Exception as main_error:
        logging.critical("An unexpected error occurred: %s", str(main_error))
```
