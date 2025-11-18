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
import random
from datetime import datetime, timedelta

class Client:
    def __init__(self, client_id, name, email, loyalty_points, last_purchase_date):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.loyalty_points = loyalty_points
        self.last_purchase_date = last_purchase_date

    def __repr__(self):
        return f"Client({self.client_id}, {self.name}, {self.email}, {self.loyalty_points}, {self.last_purchase_date})"


class Promotion:
    def __init__(self, promotion_id, description, discount, expiration_date):
        self.promotion_id = promotion_id
        self.description = description
        self.discount = discount
        self.expiration_date = expiration_date

    def is_valid(self):
        """Check if the promotion is still valid based on the expiration date."""
        return datetime.now() < self.expiration_date

    def __repr__(self):
        return f"Promotion({self.promotion_id}, {self.description}, {self.discount}, {self.expiration_date})"


class ClientRetentionProgram:
    def __init__(self):
        self.clients = []
        self.promotions = []

    def add_client(self, client):
        """Add a new client to the retention program."""
        self.clients.append(client)

    def add_promotion(self, promotion):
        """Add a new promotion to the retention program."""
        self.promotions.append(promotion)

    def generate_loyalty_offer(self, client):
        """Generate a tailored loyalty offer based on the client's loyalty points."""
        if client.loyalty_points >= 100:
            return f"Exclusive 20% off your next purchase, {client.name}!"
        elif client.loyalty_points >= 50:
            return f"Enjoy a 10% discount on your next order, {client.name}!"
        else:
            return "Join our loyalty program to start earning points!"

    def send_promotions(self):
        """Send valid promotions to clients based on their last purchase date."""
        for client in self.clients:
            days_since_last_purchase = (datetime.now() - client.last_purchase_date).days
            
            # Tailored promotion based on inactivity
            if days_since_last_purchase > 30:
                promotion_message = self.generate_loyalty_offer(client)
                print(f"Sending promotion to {client.email}: {promotion_message}")

            # Send available promotions
            valid_promotions = [promo for promo in self.promotions if promo.is_valid()]
            if valid_promotions:
                selected_promo = random.choice(valid_promotions)
                print(f"Sending promotion to {client.email}: {selected_promo.description} - Discount: {selected_promo.discount}")


def main():
    """Main function to run the client retention program."""
    retention_program = ClientRetentionProgram()

    # Sample data for clients
    retention_program.add_client(Client(1, "Alice Johnson", "alice@example.com", 120, datetime.now() - timedelta(days=45)))
    retention_program.add_client(Client(2, "Bob Smith", "bob@example.com", 30, datetime.now() - timedelta(days=15)))
    retention_program.add_client(Client(3, "Charlie Brown", "charlie@example.com", 75, datetime.now() - timedelta(days=60)))

    # Sample promotions
    retention_program.add_promotion(Promotion(1, "Spring Sale: Get 15% off!", 15, datetime.now() + timedelta(days=60)))
    retention_program.add_promotion(Promotion(2, "Refer a Friend: Get $20!", 20, datetime.now() + timedelta(days=30)))

    # Send promotions to clients
    retention_program.send_promotions()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
