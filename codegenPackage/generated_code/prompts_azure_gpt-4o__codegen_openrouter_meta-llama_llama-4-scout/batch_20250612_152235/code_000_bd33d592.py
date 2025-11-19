"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Write Python code to simulate a basic event management system that includes features like client registration, event scheduling, and resource allocation, as described in the context of event company operations.
Generated: DETERMINISTIC_bd33d5923da1d73f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class Client:
    """Represents a client in the event management system."""

    def __init__(self, client_id, name, email, phone):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Client's name.
            email (str): Client's email address.
            phone (str): Client's phone number.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class Event:
    """Represents an event in the event management system."""

    def __init__(self, event_id, client, date, time, location):
        """
        Initializes an Event object.

        Args:
            event_id (int): Unique identifier for the event.
            client (Client): Client object associated with the event.
            date (str): Date of the event (YYYY-MM-DD).
            time (str): Time of the event (HH:MM).
            location (str): Location of the event.
        """
        self.event_id = event_id
        self.client = client
        self.date = date
        self.time = time
        self.location = location
        self.resources = []

    def add_resource(self, resource):
        """Adds a resource to the event."""
        self.resources.append(resource)

    def __str__(self):
        return f"Event ID: {self.event_id}, Client: {self.client.name}, Date: {self.date}, Time: {self.time}, Location: {self.location}"


class Resource:
    """Represents a resource in the event management system."""

    def __init__(self, resource_id, name, quantity):
        """
        Initializes a Resource object.

        Args:
            resource_id (int): Unique identifier for the resource.
            name (str): Name of the resource.
            quantity (int): Quantity of the resource available.
        """
        self.resource_id = resource_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Resource ID: {self.resource_id}, Name: {self.name}, Quantity: {self.quantity}"


class EventManagementSystem:
    """Manages clients, events, and resources."""

    def __init__(self):
        self.clients = []
        self.events = []
        self.resources = []

    def register_client(self, client_id, name, email, phone):
        """
        Registers a new client.

        Args:
            client_id (int): Unique identifier for the client.
            name (str): Client's name.
            email (str): Client's email address.
            phone (str): Client's phone number.

        Returns:
            Client: The newly created Client object.
        """
        client = Client(client_id, name, email, phone)
        self.clients.append(client)
        return client

    def schedule_event(self, event_id, client_id, date, time, location):
        """
        Schedules a new event.

        Args:
            event_id (int): Unique identifier for the event.
            client_id (int): Unique identifier for the client.
            date (str): Date of the event (YYYY-MM-DD).
            time (str): Time of the event (HH:MM).
            location (str): Location of the event.

        Returns:
            Event: The newly created Event object.

        Raises:
            ValueError: If the client is not found.
        """
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client is None:
            raise ValueError("Client not found")

        event = Event(event_id, client, date, time, location)
        self.events.append(event)
        return event

    def allocate_resource(self, event_id, resource_id, quantity):
        """
        Allocates a resource to an event.

        Args:
            event_id (int): Unique identifier for the event.
            resource_id (int): Unique identifier for the resource.
            quantity (int): Quantity of the resource to allocate.

        Raises:
            ValueError: If the event or resource is not found.
        """
        event = next((e for e in self.events if e.event_id == event_id), None)
        if event is None:
            raise ValueError("Event not found")

        resource = next((r for r in self.resources if r.resource_id == resource_id), None)
        if resource is None:
            raise ValueError("Resource not found")

        if quantity > resource.quantity:
            raise ValueError("Insufficient quantity of resource")

        resource.quantity -= quantity
        event.add_resource((resource_id, quantity))

    def add_resource(self, resource_id, name, quantity):
        """
        Adds a new resource.

        Args:
            resource_id (int): Unique identifier for the resource.
            name (str): Name of the resource.
            quantity (int): Quantity of the resource available.

        Returns:
            Resource: The newly created Resource object.
        """
        resource = Resource(resource_id, name, quantity)
        self.resources.append(resource)
        return resource

    def __str__(self):
        output = "Clients:\n"
        for client in self.clients:
            output += str(client) + "\n"

        output += "\nEvents:\n"
        for event in self.events:
            output += str(event) + "\n"

        output += "\nResources:\n"
        for resource in self.resources:
            output += str(resource) + "\n"

        return output


def main():
    ems = EventManagementSystem()

    # Register clients
    client1 = ems.register_client(1, "John Doe", "john@example.com", "123-456-7890")
    client2 = ems.register_client(2, "Jane Doe", "jane@example.com", "987-654-3210")

    # Add resources
    ems.add_resource(1, "Audio Equipment", 10)
    ems.add_resource(2, "Lighting Equipment", 5)

    # Schedule events
    event1 = ems.schedule_event(1, 1, "2024-09-20", "10:00", "New York")
    event2 = ems.schedule_event(2, 2, "2024-09-25", "14:00", "Los Angeles")

    # Allocate resources
    ems.allocate_resource(1, 1, 2)
    ems.allocate_resource(2, 2, 1)

    print(ems)


if __name__ == "__main__":
    main()
```
