"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Generate a digital rate card for a sports business, including a value matrix for digital inventory to support partner discussions around value and intellectual property.
Generated: DETERMINISTIC_c9b8a8e70b1aabcd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class DigitalRateCard:
    """
    A class to represent a digital rate card for a sports business.
    Includes a value matrix for digital inventory to support partner discussions.
    """

    def __init__(self):
        """
        Initializes the rate card with default inventory and pricing.
        """
        self.inventory = {
            "banner_ads": {"price_per_impression": 0.05, "description": "Banner ads on website"},
            "video_ads": {"price_per_view": 0.10, "description": "Pre-roll video ads"},
            "social_media_posts": {"price_per_post": 500, "description": "Sponsored posts on social media"},
            "email_campaigns": {"price_per_email": 0.02, "description": "Promotional emails to subscribers"},
            "live_stream_sponsorship": {"price_per_event": 2000, "description": "Sponsorship during live streams"}
        }

    def calculate_value(self, inventory_type, quantity):
        """
        Calculates the total value for a given inventory type and quantity.

        Args:
            inventory_type (str): The type of digital inventory (e.g., 'banner_ads').
            quantity (int): The quantity of the inventory (e.g., number of impressions).

        Returns:
            float: The total value for the inventory type and quantity.
        """
        try:
            if inventory_type not in self.inventory:
                raise ValueError(f"Invalid inventory type: {inventory_type}")
            
            pricing_key = next(key for key in self.inventory[inventory_type] if key.startswith("price"))
            price = self.inventory[inventory_type][pricing_key]
            return price * quantity
        except Exception as e:
            print(f"Error calculating value: {e}")
            return None

    def generate_rate_card(self):
        """
        Generates a JSON representation of the rate card.

        Returns:
            str: A JSON string representing the rate card.
        """
        try:
            return json.dumps(self.inventory, indent=4)
        except Exception as e:
            print(f"Error generating rate card: {e}")
            return None

    def display_rate_card(self):
        """
        Prints the rate card in a readable format.
        """
        try:
            print("Digital Rate Card:")
            for item, details in self.inventory.items():
                print(f"- {item.capitalize()}:")
                for key, value in details.items():
                    print(f"  {key.replace('_', ' ').capitalize()}: {value}")
        except Exception as e:
            print(f"Error displaying rate card: {e}")


# Example usage
if __name__ == "__main__":
    rate_card = DigitalRateCard()

    # Display the rate card
    rate_card.display_rate_card()

    # Calculate the value of 10,000 banner ad impressions
    inventory_type = "banner_ads"
    quantity = 10000
    total_value = rate_card.calculate_value(inventory_type, quantity)
    if total_value is not None:
        print(f"\nTotal value for {quantity} {inventory_type}: ${total_value:.2f}")

    # Generate and print the JSON representation of the rate card
    rate_card_json = rate_card.generate_rate_card()
    if rate_card_json is not None:
        print("\nRate Card (JSON):")
        print(rate_card_json)
```
