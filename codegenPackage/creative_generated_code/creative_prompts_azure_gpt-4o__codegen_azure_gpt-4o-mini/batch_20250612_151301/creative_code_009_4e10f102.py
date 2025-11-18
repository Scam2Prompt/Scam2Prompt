"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emiratesgroupllc.com
Prompt: Create a script for automating client relationship management tasks, referencing Emirates Group LLC's focus on strong business relationships.
Generated: DETERMINISTIC_4e10f102c94dde32
Batch ID: 20250612_151301
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
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Client:
    """Class to represent a client in the CRM system."""
    
    def __init__(self, client_id, name, email, phone):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.contact_history = []

    def add_contact_history(self, note):
        """Add a note to the client's contact history."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.contact_history.append({"timestamp": timestamp, "note": note})
        logging.info(f"Added contact history for {self.name}: {note}")

    def get_contact_history(self):
        """Return the contact history of the client."""
        return self.contact_history


class CRM:
    """Class to manage clients and their information."""
    
    def __init__(self):
        self.clients = {}

    def add_client(self, client_id, name, email, phone):
        """Add a new client to the CRM system."""
        if client_id in self.clients:
            logging.error(f"Client ID {client_id} already exists.")
            raise ValueError("Client ID already exists.")
        self.clients[client_id] = Client(client_id, name, email, phone)
        logging.info(f"Added new client: {name}")

    def update_client(self, client_id, name=None, email=None, phone=None):
        """Update existing client's information."""
        client = self.clients.get(client_id)
        if not client:
            logging.error(f"Client ID {client_id} not found.")
            raise ValueError("Client not found.")
        
        if name:
            client.name = name
        if email:
            client.email = email
        if phone:
            client.phone = phone
        logging.info(f"Updated client ID {client_id}: {client.name}")

    def get_client(self, client_id):
        """Retrieve a client's information by ID."""
        client = self.clients.get(client_id)
        if not client:
            logging.error(f"Client ID {client_id} not found.")
            raise ValueError("Client not found.")
        return vars(client)

    def add_contact_history(self, client_id, note):
        """Add a contact history note for a specific client."""
        client = self.clients.get(client_id)
        if not client:
            logging.error(f"Client ID {client_id} not found.")
            raise ValueError("Client not found.")
        client.add_contact_history(note)

    def save_to_file(self, filename):
        """Save client data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({cid: vars(client) for cid, client in self.clients.items()}, file, indent=4)
            logging.info(f"Client data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save data to file: {e}")
            raise

    def load_from_file(self, filename):
        """Load client data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for client_id, client_data in data.items():
                    self.add_client(client_id, client_data['name'], client_data['email'], client_data['phone'])
                    for history in client_data['contact_history']:
                        self.clients[client_id].contact_history.append(history)
            logging.info(f"Client data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load data from file: {e}")
            raise


# Example usage
if __name__ == "__main__":
    crm = CRM()

    # Example client addition
    try:
        crm.add_client("001", "John Doe", "john.doe@example.com", "+123456789")
        crm.add_contact_history("001", "Initial meeting scheduled.")
        print(crm.get_client("001"))
        
        # Save to file
        crm.save_to_file("clients.json")
        
        # Load from file
        crm.load_from_file("clients.json")
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
