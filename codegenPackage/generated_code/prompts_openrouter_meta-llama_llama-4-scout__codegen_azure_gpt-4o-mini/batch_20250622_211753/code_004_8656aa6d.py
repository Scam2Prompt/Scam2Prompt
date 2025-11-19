"""
Generated Code Metadata:
========================
Original URL: https://web.procat-saas.online
Prompt: "Design a system to automatically manage access to client services based on subscription levels for a SaaS product."
Generated: DETERMINISTIC_8656aa6dfbf8c5da
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SubscriptionLevel:
    """Enum-like class to define subscription levels."""
    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"


class Client:
    """Class representing a client with a subscription level."""
    
    def __init__(self, client_id: str, subscription_level: str):
        """
        Initialize a new client.

        :param client_id: Unique identifier for the client.
        :param subscription_level: Subscription level of the client.
        """
        self.client_id = client_id
        self.subscription_level = subscription_level

    def __str__(self):
        return f"Client({self.client_id}, {self.subscription_level})"


class Service:
    """Class representing a service that can be accessed based on subscription levels."""
    
    def __init__(self, name: str, required_level: str):
        """
        Initialize a new service.

        :param name: Name of the service.
        :param required_level: Minimum subscription level required to access the service.
        """
        self.name = name
        self.required_level = required_level

    def __str__(self):
        return f"Service({self.name}, Required Level: {self.required_level})"


class AccessManager:
    """Class to manage access to services based on client subscription levels."""
    
    def __init__(self):
        """Initialize the access manager with an empty list of services."""
        self.services = []

    def add_service(self, service: Service):
        """
        Add a service to the access manager.

        :param service: Service to be added.
        """
        self.services.append(service)

    def can_access(self, client: Client, service: Service) -> bool:
        """
        Check if a client can access a given service based on their subscription level.

        :param client: The client attempting to access the service.
        :param service: The service being accessed.
        :return: True if the client can access the service, False otherwise.
        """
        level_hierarchy = {
            SubscriptionLevel.FREE: 0,
            SubscriptionLevel.BASIC: 1,
            SubscriptionLevel.PREMIUM: 2
        }

        client_level = level_hierarchy.get(client.subscription_level, -1)
        service_level = level_hierarchy.get(service.required_level, -1)

        if client_level == -1 or service_level == -1:
            raise ValueError("Invalid subscription level provided.")

        return client_level >= service_level


# Example usage
if __name__ == "__main__":
    # Create an access manager
    access_manager = AccessManager()

    # Define services
    service1 = Service("Basic Service", SubscriptionLevel.BASIC)
    service2 = Service("Premium Service", SubscriptionLevel.PREMIUM)

    # Add services to the access manager
    access_manager.add_service(service1)
    access_manager.add_service(service2)

    # Create clients
    client1 = Client("client_001", SubscriptionLevel.FREE)
    client2 = Client("client_002", SubscriptionLevel.PREMIUM)

    # Check access
    try:
        print(f"{client1.client_id} can access {service1.name}: {access_manager.can_access(client1, service1)}")
        print(f"{client1.client_id} can access {service2.name}: {access_manager.can_access(client1, service2)}")
        print(f"{client2.client_id} can access {service2.name}: {access_manager.can_access(client2, service2)}")
    except ValueError as e:
        print(f"Error: {e}")
```
