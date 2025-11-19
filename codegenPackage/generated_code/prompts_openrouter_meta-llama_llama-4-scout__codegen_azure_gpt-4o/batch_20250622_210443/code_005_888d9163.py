"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Write a Python script that can be used to manage a marketplace for creative services, similar to Kroo Nation's commerce platform.
Generated: DETERMINISTIC_888d9163a870d224
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime


class Marketplace:
    """
    A class to manage a marketplace for creative services.
    """

    def __init__(self):
        # Initialize the marketplace with empty lists for services and users
        self.services = []
        self.users = []

    def register_user(self, name, email):
        """
        Register a new user in the marketplace.

        :param name: Name of the user
        :param email: Email of the user
        :return: User object
        """
        if not name or not email:
            raise ValueError("Name and email are required to register a user.")

        user = {
            "id": str(uuid.uuid4()),
            "name": name,
            "email": email,
            "created_at": datetime.now(),
        }
        self.users.append(user)
        return user

    def add_service(self, user_id, title, description, price):
        """
        Add a new service to the marketplace.

        :param user_id: ID of the user offering the service
        :param title: Title of the service
        :param description: Description of the service
        :param price: Price of the service
        :return: Service object
        """
        if not user_id or not title or not description or price <= 0:
            raise ValueError("Invalid service details provided.")

        # Ensure the user exists
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            raise ValueError("User not found.")

        service = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "title": title,
            "description": description,
            "price": price,
            "created_at": datetime.now(),
        }
        self.services.append(service)
        return service

    def list_services(self):
        """
        List all services available in the marketplace.

        :return: List of services
        """
        return self.services

    def search_services(self, keyword):
        """
        Search for services by keyword.

        :param keyword: Keyword to search for
        :return: List of matching services
        """
        if not keyword:
            raise ValueError("Keyword is required for searching services.")

        return [
            service
            for service in self.services
            if keyword.lower() in service["title"].lower()
            or keyword.lower() in service["description"].lower()
        ]

    def purchase_service(self, service_id, buyer_id):
        """
        Purchase a service from the marketplace.

        :param service_id: ID of the service to purchase
        :param buyer_id: ID of the buyer
        :return: Purchase confirmation
        """
        # Ensure the service exists
        service = next((s for s in self.services if s["id"] == service_id), None)
        if not service:
            raise ValueError("Service not found.")

        # Ensure the buyer exists
        buyer = next((u for u in self.users if u["id"] == buyer_id), None)
        if not buyer:
            raise ValueError("Buyer not found.")

        # Generate a purchase confirmation
        purchase = {
            "purchase_id": str(uuid.uuid4()),
            "service_id": service_id,
            "buyer_id": buyer_id,
            "seller_id": service["user_id"],
            "price": service["price"],
            "purchased_at": datetime.now(),
        }
        return purchase


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the marketplace
        marketplace = Marketplace()

        # Register users
        user1 = marketplace.register_user("Alice", "alice@example.com")
        user2 = marketplace.register_user("Bob", "bob@example.com")

        # Add services
        service1 = marketplace.add_service(
            user1["id"], "Logo Design", "Professional logo design service", 100
        )
        service2 = marketplace.add_service(
            user2["id"], "Video Editing", "High-quality video editing", 200
        )

        # List services
        print("Available services:")
        for service in marketplace.list_services():
            print(service)

        # Search services
        print("\nSearch results for 'logo':")
        for service in marketplace.search_services("logo"):
            print(service)

        # Purchase a service
        purchase = marketplace.purchase_service(service1["id"], user2["id"])
        print("\nPurchase confirmation:")
        print(purchase)

    except Exception as e:
        print(f"Error: {e}")
```
