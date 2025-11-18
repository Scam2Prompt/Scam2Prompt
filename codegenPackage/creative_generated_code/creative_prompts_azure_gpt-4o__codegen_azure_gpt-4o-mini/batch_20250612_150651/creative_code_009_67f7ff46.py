"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Write code to build a client relationship management system for freelancers, incorporating negotiation strategies and long-term business development features, as taught in the КарьераОнлайн program.
Generated: DETERMINISTIC_67f7ff4646fb8034
Batch ID: 20250612_150651
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
from typing import List, Dict, Optional

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Client:
    """Class to represent a client in the CRM system."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.negotiation_history: List[str] = []
        self.business_development_notes: List[str] = []

    def add_negotiation(self, note: str):
        """Adds a negotiation note to the client's history."""
        self.negotiation_history.append(note)
        logging.info(f"Added negotiation note for {self.name}: {note}")

    def add_business_development(self, note: str):
        """Adds a business development note for the client."""
        self.business_development_notes.append(note)
        logging.info(f"Added business development note for {self.name}: {note}")

    def get_client_info(self) -> Dict[str, Optional[List[str]]]:
        """Returns client information including negotiation and business development notes."""
        return {
            'name': self.name,
            'email': self.email,
            'negotiation_history': self.negotiation_history,
            'business_development_notes': self.business_development_notes
        }


class CRM:
    """Class to manage clients in the CRM system."""
    
    def __init__(self):
        self.clients: Dict[str, Client] = {}  # Keyed by email for uniqueness

    def add_client(self, name: str, email: str):
        """Adds a new client to the CRM."""
        if email in self.clients:
            logging.error(f"Client with email {email} already exists.")
            raise ValueError(f"Client with email {email} already exists.")
        self.clients[email] = Client(name, email)
        logging.info(f"Client added: {name} ({email})")

    def remove_client(self, email: str):
        """Removes a client from the CRM."""
        if email not in self.clients:
            logging.error(f"Client with email {email} not found.")
            raise ValueError(f"Client with email {email} not found.")
        del self.clients[email]
        logging.info(f"Client removed: {email}")

    def get_client(self, email: str) -> Optional[Dict[str, Optional[List[str]]]]:
        """Fetches client information by email."""
        client = self.clients.get(email)
        if client:
            return client.get_client_info()
        logging.warning(f"Client with email {email} not found.")
        return None

    def save_to_file(self, filename: str):
        """Saves the current state of clients to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({email: client.get_client_info() for email, client in self.clients.items()}, file, indent=4)
                logging.info(f"Client data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save to file {filename}: {e}")
            raise

    def load_from_file(self, filename: str):
        """Loads client data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for email, client_data in data.items():
                    self.clients[email] = Client(client_data['name'], email)
                    self.clients[email].negotiation_history = client_data['negotiation_history']
                    self.clients[email].business_development_notes = client_data['business_development_notes']
                logging.info(f"Client data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load from file {filename}: {e}")
            raise


# Example usage of the CRM system
if __name__ == "__main__":
    crm_system = CRM()
    
    try:
        crm_system.add_client("John Doe", "john@example.com")
        crm_system.get_client("john@example.com").add_negotiation("Discussed project scope.")
        crm_system.get_client("john@example.com").add_business_development("Follow-up in one month.")
        
        # Save to file
        crm_system.save_to_file("clients.json")
        
        # Load from file
        new_crm_system = CRM()
        new_crm_system.load_from_file("clients.json")
        info = new_crm_system.get_client("john@example.com")
        print(info)
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This code provides a simple CRM system for freelancers, allowing them to manage client relationships with features for negotiation and business development. It includes error handling, logging, and serialization for data persistence.
