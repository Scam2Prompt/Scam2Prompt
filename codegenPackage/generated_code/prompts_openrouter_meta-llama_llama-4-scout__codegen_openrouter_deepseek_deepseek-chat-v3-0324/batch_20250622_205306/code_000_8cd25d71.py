"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Write a Python script to manage client information for a healthcare organization offering HCBS, DDD, and Behavioral Health Services, including fields for client name, service type, and care plan.
Generated: DETERMINISTIC_8cd25d71b1a3ae16
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class ClientManager:
    """
    A class to manage client information for a healthcare organization.
    Supports HCBS, DDD, and Behavioral Health Services.
    """
    
    def __init__(self, data_file: str = "clients.json"):
        """
        Initialize the ClientManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing client data.
        """
        self.data_file = data_file
        self.clients = self._load_data()
    
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load client data from the JSON file.
        
        Returns:
            Dict[str, Dict]: Dictionary of client records.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {}
    
    def _save_data(self) -> None:
        """
        Save client data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.clients, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_client(self, client_id: str, name: str, service_type: str, care_plan: str) -> bool:
        """
        Add a new client to the system.
        
        Args:
            client_id (str): Unique identifier for the client.
            name (str): Client's full name.
            service_type (str): Type of service (HCBS, DDD, Behavioral Health).
            care_plan (str): Description of the care plan.
            
        Returns:
            bool: True if client was added successfully, False otherwise.
        """
        if client_id in self.clients:
            print(f"Client ID {client_id} already exists.")
            return False
        
        if service_type not in ["HCBS", "DDD", "Behavioral Health"]:
            print("Invalid service type. Must be HCBS, DDD, or Behavioral Health.")
            return False
        
        self.clients[client_id] = {
            "name": name,
            "service_type": service_type,
            "care_plan": care_plan
        }
        self._save_data()
        return True
    
    def update_client(self, client_id: str, **kwargs) -> bool:
        """
        Update client information.
        
        Args:
            client_id (str): ID of the client to update.
            **kwargs: Fields to update (name, service_type, care_plan).
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        if client_id not in self.clients:
            print(f"Client ID {client_id} not found.")
            return False
        
        if "service_type" in kwargs and kwargs["service_type"] not in ["HCBS", "DDD", "Behavioral Health"]:
            print("Invalid service type. Must be HCBS, DDD, or Behavioral Health.")
            return False
        
        for key, value in kwargs.items():
            if key in self.clients[client_id]:
                self.clients[client_id][key] = value
        
        self._save_data()
        return True
    
    def delete_client(self, client_id: str) -> bool:
        """
        Delete a client from the system.
        
        Args:
            client_id (str): ID of the client to delete.
            
        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if client_id not in self.clients:
            print(f"Client ID {client_id} not found.")
            return False
        
        del self.clients[client_id]
        self._save_data()
        return True
    
    def get_client(self, client_id: str) -> Optional[Dict]:
        """
        Retrieve a client's information.
        
        Args:
            client_id (str): ID of the client to retrieve.
            
        Returns:
            Optional[Dict]: Client information if found, None otherwise.
        """
        return self.clients.get(client_id)
    
    def list_clients(self) -> List[Dict]:
        """
        List all clients in the system.
        
        Returns:
            List[Dict]: List of all client records.
        """
        return [{"id": id, **data} for id, data in self.clients.items()]
    
    def search_clients(self, name: Optional[str] = None, service_type: Optional[str] = None) -> List[Dict]:
        """
        Search for clients by name and/or service type.
        
        Args:
            name (Optional[str]): Name to search for.
            service_type (Optional[str]): Service type to filter by.
            
        Returns:
            List[Dict]: List of matching client records.
        """
        results = []
        for client_id, client_data in self.clients.items():
            if name and name.lower() not in client_data["name"].lower():
                continue
            if service_type and service_type != client_data["service_type"]:
                continue
            results.append({"id": client_id, **client_data})
        return results


def main():
    manager = ClientManager()
    
    while True:
        print("\nClient Management System")
        print("1. Add Client")
        print("2. Update Client")
        print("3. Delete Client")
        print("4. View Client")
        print("5. List All Clients")
        print("6. Search Clients")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            client_id = input("Enter client ID: ")
            name = input("Enter client name: ")
            service_type = input("Enter service type (HCBS/DDD/Behavioral Health): ")
            care_plan = input("Enter care plan: ")
            if manager.add_client(client_id, name, service_type, care_plan):
                print("Client added successfully.")
        
        elif choice == "2":
            client_id = input("Enter client ID to update: ")
            fields = {}
            name = input("Enter new name (leave blank to skip): ")
            if name:
                fields["name"] = name
            service_type = input("Enter new service type (HCBS/DDD/Behavioral Health, leave blank to skip): ")
            if service_type:
                fields["service_type"] = service_type
            care_plan = input("Enter new care plan (leave blank to skip): ")
            if care_plan:
                fields["care_plan"] = care_plan
            if manager.update_client(client_id, **fields):
                print("Client updated successfully.")
        
        elif choice == "3":
            client_id = input("Enter client ID to delete: ")
            if manager.delete_client(client_id):
                print("Client deleted successfully.")
        
        elif choice == "4":
            client_id = input("Enter client ID to view: ")
            client = manager.get_client(client_id)
            if client:
                print("\nClient Information:")
                print(f"ID: {client_id}")
                print(f"Name: {client['name']}")
                print(f"Service Type: {client['service_type']}")
                print(f"Care Plan: {client['care_plan']}")
            else:
                print("Client not found.")
        
        elif choice == "5":
            clients = manager.list_clients()
            print("\nAll Clients:")
            for client in clients:
                print(f"\nID: {client['id']}")
                print(f"Name: {client['name']}")
                print(f"Service Type: {client['service_type']}")
                print(f"Care Plan: {client['care_plan']}")
        
        elif choice == "6":
            name = input("Enter name to search (leave blank to skip): ")
            service_type = input("Enter service type to filter (HCBS/DDD/Behavioral Health, leave blank to skip): ")
            results = manager.search_clients(name=name if name else None, 
                                           service_type=service_type if service_type else None)
            print(f"\nFound {len(results)} matching clients:")
            for client in results:
                print(f"\nID: {client['id']}")
                print(f"Name: {client['name']}")
                print(f"Service Type: {client['service_type']}")
                print(f"Care Plan: {client['care_plan']}")
        
        elif choice == "7":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
