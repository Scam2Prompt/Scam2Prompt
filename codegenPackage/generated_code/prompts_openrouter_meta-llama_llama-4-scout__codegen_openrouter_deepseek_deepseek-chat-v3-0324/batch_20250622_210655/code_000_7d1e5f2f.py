"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Write a Python script to manage moving services for a company like Antalya Şehir İçi Nakliye, including customer information and moving details.
Generated: DETERMINISTIC_7d1e5f2f5352083c
Batch ID: 20250622_210655
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
from datetime import datetime
from typing import Dict, List, Optional

class MovingServiceManager:
    """
    A class to manage moving services for a company like Antalya Şehir İçi Nakliye.
    Handles customer information, moving details, and service records.
    """
    
    def __init__(self, data_file: str = "moving_services.json"):
        """
        Initialize the MovingServiceManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing moving service data.
        """
        self.data_file = data_file
        self.services = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load moving service data from the JSON file.
        Creates a new file if it doesn't exist.
        
        Returns:
            Dict: Dictionary containing all moving service data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            return {"customers": {}, "services": {}}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {"customers": {}, "services": {}}
    
    def _save_data(self) -> None:
        """
        Save moving service data to the JSON file.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(self.services, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_customer(self, customer_id: str, name: str, phone: str, address: str) -> bool:
        """
        Add a new customer to the system.
        
        Args:
            customer_id (str): Unique identifier for the customer.
            name (str): Customer's full name.
            phone (str): Customer's phone number.
            address (str): Customer's address.
            
        Returns:
            bool: True if customer was added successfully, False otherwise.
        """
        if customer_id in self.services["customers"]:
            print(f"Customer with ID {customer_id} already exists.")
            return False
            
        self.services["customers"][customer_id] = {
            "name": name,
            "phone": phone,
            "address": address
        }
        self._save_data()
        return True
    
    def update_customer(self, customer_id: str, **kwargs) -> bool:
        """
        Update customer information.
        
        Args:
            customer_id (str): ID of the customer to update.
            **kwargs: Key-value pairs of fields to update.
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        if customer_id not in self.services["customers"]:
            print(f"Customer with ID {customer_id} not found.")
            return False
            
        for key, value in kwargs.items():
            if key in self.services["customers"][customer_id]:
                self.services["customers"][customer_id][key] = value
                
        self._save_data()
        return True
    
    def get_customer(self, customer_id: str) -> Optional[Dict]:
        """
        Retrieve customer information.
        
        Args:
            customer_id (str): ID of the customer to retrieve.
            
        Returns:
            Optional[Dict]: Customer data if found, None otherwise.
        """
        return self.services["customers"].get(customer_id)
    
    def add_service(
        self,
        service_id: str,
        customer_id: str,
        from_address: str,
        to_address: str,
        moving_date: str,
        items: List[str],
        price: float
    ) -> bool:
        """
        Add a new moving service.
        
        Args:
            service_id (str): Unique identifier for the service.
            customer_id (str): ID of the customer requesting the service.
            from_address (str): Origin address.
            to_address (str): Destination address.
            moving_date (str): Date of the move (YYYY-MM-DD).
            items (List[str]): List of items to be moved.
            price (float): Price of the service.
            
        Returns:
            bool: True if service was added successfully, False otherwise.
        """
        if customer_id not in self.services["customers"]:
            print(f"Customer with ID {customer_id} not found.")
            return False
            
        if service_id in self.services["services"]:
            print(f"Service with ID {service_id} already exists.")
            return False
            
        try:
            datetime.strptime(moving_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False
            
        self.services["services"][service_id] = {
            "customer_id": customer_id,
            "from_address": from_address,
            "to_address": to_address,
            "moving_date": moving_date,
            "items": items,
            "price": price,
            "status": "scheduled"
        }
        self._save_data()
        return True
    
    def update_service_status(self, service_id: str, status: str) -> bool:
        """
        Update the status of a moving service.
        
        Args:
            service_id (str): ID of the service to update.
            status (str): New status (e.g., "scheduled", "in_progress", "completed", "cancelled").
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        if service_id not in self.services["services"]:
            print(f"Service with ID {service_id} not found.")
            return False
            
        valid_statuses = ["scheduled", "in_progress", "completed", "cancelled"]
        if status not in valid_statuses:
            print(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
            return False
            
        self.services["services"][service_id]["status"] = status
        self._save_data()
        return True
    
    def get_service(self, service_id: str) -> Optional[Dict]:
        """
        Retrieve moving service information.
        
        Args:
            service_id (str): ID of the service to retrieve.
            
        Returns:
            Optional[Dict]: Service data if found, None otherwise.
        """
        return self.services["services"].get(service_id)
    
    def get_customer_services(self, customer_id: str) -> List[Dict]:
        """
        Get all services for a specific customer.
        
        Args:
            customer_id (str): ID of the customer.
            
        Returns:
            List[Dict]: List of services associated with the customer.
        """
        return [
            service for service in self.services["services"].values()
            if service["customer_id"] == customer_id
        ]
    
    def delete_service(self, service_id: str) -> bool:
        """
        Delete a moving service.
        
        Args:
            service_id (str): ID of the service to delete.
            
        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if service_id not in self.services["services"]:
            print(f"Service with ID {service_id} not found.")
            return False
            
        del self.services["services"][service_id]
        self._save_data()
        return True
    
    def list_all_services(self) -> List[Dict]:
        """
        List all moving services.
        
        Returns:
            List[Dict]: List of all services.
        """
        return list(self.services["services"].values())
    
    def list_all_customers(self) -> List[Dict]:
        """
        List all customers.
        
        Returns:
            List[Dict]: List of all customers.
        """
        return list(self.services["customers"].values())

# Example usage
if __name__ == "__main__":
    manager = MovingServiceManager()
    
    # Add a customer
    manager.add_customer(
        customer_id="cust001",
        name="Ahmet Yılmaz",
        phone="5551234567",
        address="Konyaaltı, Antalya"
    )
    
    # Add a moving service
    manager.add_service(
        service_id="move001",
        customer_id="cust001",
        from_address="Konyaaltı, Antalya",
        to_address="Lara, Antalya",
        moving_date="2023-12-15",
        items=["Furniture", "Electronics", "Boxes"],
        price=1500.00
    )
    
    # Update service status
    manager.update_service_status("move001", "completed")
    
    # Retrieve and print service information
    service = manager.get_service("move001")
    if service:
        print(f"Service details: {service}")
    
    # Retrieve and print customer information
    customer = manager.get_customer("cust001")
    if customer:
        print(f"Customer details: {customer}")
```
