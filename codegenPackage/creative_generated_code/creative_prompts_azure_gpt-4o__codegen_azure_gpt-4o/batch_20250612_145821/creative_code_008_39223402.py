"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: Write a script to implement tailored promotions for client retention, using strategies like special offers and loyalty-building techniques mentioned on the Client Fuel site.
Generated: DETERMINISTIC_39223402b1df5c2a
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class PromotionManager:
    """
    A class to manage tailored promotions for client retention.
    """

    def __init__(self, client_data_file):
        """
        Initializes the PromotionManager with client data.

        :param client_data_file: Path to JSON file containing client data
        """
        self.client_data_file = client_data_file
        self.clients = self._load_client_data()

    def _load_client_data(self):
        """
        Loads client data from a JSON file.

        :return: A list of client dictionaries
        """
        try:
            with open(self.client_data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading client data: {e}")
            return []

    def create_promotion(self, client, promotion_type):
        """
        Creates a tailored promotion for a client.

        :param client: Dictionary containing client details
        :param promotion_type: Type of promotion ("discount", "loyalty_bonus", etc.)
        :return: A promotion message
        """
        if promotion_type == "discount":
            discount = 20  # Example discount percentage
            return f"Hi {client['name']}, enjoy {discount}% off on your next purchase!"
        elif promotion_type == "loyalty_bonus":
            bonus_points = 100  # Example bonus points
            return f"Hi {client['name']}, we've added {bonus_points} loyalty points to your account!"
        elif promotion_type == "holiday_offer":
            offer = "Buy 1 Get 1 Free"  # Example holiday offer
            return f"Hi {client['name']}, celebrate with us! Enjoy our special holiday offer: {offer}!"
        else:
            return f"Hi {client['name']}, stay tuned for exciting promotions!"

    def apply_promotions(self):
        """
        Applies tailored promotions to all eligible clients.
        """
        for client in self.clients:
            try:
                # Example criteria: Last purchase was more than 30 days ago
                last_purchase_date = datetime.strptime(client['last_purchase_date'], '%Y-%m-%d')
                if datetime.now() - last_purchase_date > timedelta(days=30):
                    promotion_message = self.create_promotion(client, "discount")
                    self._send_promotion(client, promotion_message)
                else:
                    promotion_message = self.create_promotion(client, "loyalty_bonus")
                    self._send_promotion(client, promotion_message)
            except KeyError as e:
                print(f"Missing client data: {e}")
            except ValueError as e:
                print(f"Invalid date format for client {client.get('name', 'Unknown')}: {e}")

    def _send_promotion(self, client, promotion_message):
        """
        Simulates sending the promotion to the client.

        :param client: Dictionary containing client details
        :param promotion_message: The promotion message to send
        """
        # For a production system, integrate with an email/SMS API here
        print(f"Sending to {client['email']}: {promotion_message}")

    def save_updated_clients(self):
        """
        Saves the updated client data back to the JSON file.
        """
        try:
            with open(self.client_data_file, 'w') as file:
                json.dump(self.clients, file, indent=4)
        except IOError as e:
            print(f"Error saving client data: {e}")


if __name__ == "__main__":
    # Path to client data file (update with actual path)
    CLIENT_DATA_FILE = "clients.json"

    # Initialize the PromotionManager
    promotion_manager = PromotionManager(CLIENT_DATA_FILE)

    # Apply promotions to clients
    promotion_manager.apply_promotions()

    # Save any updates made to client data
    promotion_manager.save_updated_clients()
```

In order to run this code, you need to have a `clients.json` file containing client data structured like this:
```json
[
    {
        "name": "Alice",
        "email": "alice@example.com",
        "last_purchase_date": "2023-01-15"
    },
    {
        "name": "Bob",
        "email": "bob@example.com",
        "last_purchase_date": "2023-03-10"
    }
]
```
