"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinxcash.com
Prompt: Write Python code to simulate a basic event management system that includes features like client registration, event scheduling, and resource allocation, as described in the context of event company operations.
Generated: DETERMINISTIC_bd33d5923da1d73f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class EventManagementSystem:
    def __init__(self):
        """Initialize the Event Management System with empty registries."""
        self.clients = {}  # Dictionary to store client information
        self.events = []   # List to store event details
        self.resources = {}  # Dictionary to store resource allocation details

    # -------------------- Client Registration --------------------
    def register_client(self, client_id, name, contact):
        """
        Register a new client.
        
        :param client_id: Unique identifier for the client
        :param name: Name of the client
        :param contact: Contact details of the client
        """
        if client_id in self.clients:
            print(f"Client with ID {client_id} is already registered.")
            return False
        
        self.clients[client_id] = {
            "name": name,
            "contact": contact
        }
        print(f"Client {name} registered successfully.")
        return True

    # -------------------- Event Scheduling --------------------
    def schedule_event(self, event_id, client_id, event_name, event_date, location):
        """
        Schedule a new event.
        
        :param event_id: Unique identifier for the event
        :param client_id: Client ID associated with the event
        :param event_name: Name of the event
        :param event_date: Date and time of the event (datetime object)
        :param location: Location for the event
        """
        if client_id not in self.clients:
            print(f"No client found with ID {client_id}. Please register the client first.")
            return False
        
        if any(event['event_id'] == event_id for event in self.events):
            print(f"Event with ID {event_id} is already scheduled.")
            return False
        
        self.events.append({
            "event_id": event_id,
            "client_id": client_id,
            "event_name": event_name,
            "event_date": event_date,
            "location": location
        })
        print(f"Event '{event_name}' scheduled successfully.")
        return True

    # -------------------- Resource Allocation --------------------
    def allocate_resource(self, resource_id, event_id, resource_name, quantity):
        """
        Allocate resources to an event.
        
        :param resource_id: Unique identifier for the resource
        :param event_id: Event ID for which the resource is allocated
        :param resource_name: Name of the resource
        :param quantity: Quantity of the resource allocated
        """
        if not any(event['event_id'] == event_id for event in self.events):
            print(f"No event found with ID {event_id}.")
            return False
        
        if resource_id in self.resources:
            print(f"Resource with ID {resource_id} is already allocated.")
            return False
        
        self.resources[resource_id] = {
            "event_id": event_id,
            "resource_name": resource_name,
            "quantity": quantity
        }
        print(f"Resource '{resource_name}' allocated successfully.")
        return True

    # -------------------- Display Information --------------------
    def display_clients(self):
        """Display all registered clients."""
        if not self.clients:
            print("No clients are registered.")
            return
        
        print("Registered Clients:")
        for client_id, info in self.clients.items():
            print(f"ID: {client_id}, Name: {info['name']}, Contact: {info['contact']}")

    def display_events(self):
        """Display all scheduled events."""
        if not self.events:
            print("No events are scheduled.")
            return
        
        print("Scheduled Events:")
        for event in self.events:
            print(f"ID: {event['event_id']}, Name: {event['event_name']}, Date: {event['event_date']}, Location: {event['location']}, Client ID: {event['client_id']}")

    def display_resources(self):
        """Display all allocated resources."""
        if not self.resources:
            print("No resources are allocated.")
            return
        
        print("Allocated Resources:")
        for resource_id, info in self.resources.items():
            print(f"ID: {resource_id}, Name: {info['resource_name']}, Quantity: {info['quantity']}, Event ID: {info['event_id']}")

# -------------------- Main Execution --------------------
if __name__ == "__main__":
    # Create an instance of the Event Management System
    ems = EventManagementSystem()
    
    # Example usage
    ems.register_client("C001", "Alice Johnson", "alice@example.com")
    ems.register_client("C002", "Bob Smith", "bob@example.com")
    
    event_date = datetime.datetime(2023, 12, 25, 18, 30)  # Example date
    ems.schedule_event("E001", "C001", "Christmas Party", event_date, "Downtown Hall")
    
    ems.allocate_resource("R001", "E001", "Chairs", 50)
    ems.allocate_resource("R002", "E001", "Tables", 10)
    
    # Display information
    ems.display_clients()
    ems.display_events()
    ems.display_resources()
```
