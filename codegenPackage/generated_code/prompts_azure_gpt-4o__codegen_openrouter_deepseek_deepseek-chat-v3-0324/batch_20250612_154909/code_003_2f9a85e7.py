"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Provide a Python script for managing customer data for plumbing services, including fields like location, type of service (e.g., pipe cleaning, leak detection), and urgency, as described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_2f9a85e76eab8000
Batch ID: 20250612_154909
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

class CustomerDataManager:
    """
    A class to manage customer data for plumbing services.
    Handles CRUD operations and data persistence.
    """
    
    def __init__(self, data_file: str = "customer_data.json"):
        """
        Initialize the CustomerDataManager.
        
        Args:
            data_file: Path to the JSON file storing customer data.
        """
        self.data_file = data_file
        self.customers = self._load_data()
        
    def _load_data(self) -> List[Dict]:
        """
        Load customer data from JSON file.
        
        Returns:
            List of customer dictionaries.
        """
        if not os.path.exists(self.data_file):
            return []
            
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return []
    
    def _save_data(self) -> bool:
        """
        Save customer data to JSON file.
        
        Returns:
            True if save was successful, False otherwise.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.customers, file, indent=4)
            return True
        except IOError as e:
            print(f"Error saving data: {e}")
            return False
    
    def add_customer(
        self,
        name: str,
        location: str,
        service_type: str,
        urgency: str,
        contact_info: str,
        notes: Optional[str] = None
    ) -> bool:
        """
        Add a new customer to the database.
        
        Args:
            name: Customer name
            location: Service location
            service_type: Type of plumbing service
            urgency: Urgency level (low, medium, high)
            contact_info: Customer contact information
            notes: Additional notes (optional)
            
        Returns:
            True if customer was added successfully, False otherwise.
        """
        if not all([name, location, service_type, urgency, contact_info]):
            print("Error: Missing required fields")
            return False
            
        customer = {
            "id": len(self.customers) + 1,
            "name": name,
            "location": location,
            "service_type": service_type,
            "urgency": urgency.lower(),
            "contact_info": contact_info,
            "notes": notes,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "status": "pending"
        }
        
        self.customers.append(customer)
        return self._save_data()
    
    def get_customer(self, customer_id: int) -> Optional[Dict]:
        """
        Retrieve a customer by ID.
        
        Args:
            customer_id: The ID of the customer to retrieve
            
        Returns:
            The customer dictionary if found, None otherwise.
        """
        for customer in self.customers:
            if customer["id"] == customer_id:
                return customer
        return None
    
    def update_customer(
        self,
        customer_id: int,
        **kwargs
    ) -> bool:
        """
        Update customer information.
        
        Args:
            customer_id: ID of customer to update
            **kwargs: Fields to update (name, location, service_type, urgency, contact_info, notes, status)
            
        Returns:
            True if update was successful, False otherwise.
        """
        customer = self.get_customer(customer_id)
        if not customer:
            print(f"Error: Customer with ID {customer_id} not found")
            return False
            
        valid_fields = {
            "name", "location", "service_type", "urgency", 
            "contact_info", "notes", "status"
        }
        
        for field, value in kwargs.items():
            if field in valid_fields:
                customer[field] = value
            else:
                print(f"Warning: Invalid field '{field}' will be ignored")
        
        customer["updated_at"] = datetime.now().isoformat()
        return self._save_data()
    
    def delete_customer(self, customer_id: int) -> bool:
        """
        Delete a customer from the database.
        
        Args:
            customer_id: ID of customer to delete
            
        Returns:
            True if deletion was successful, False otherwise.
        """
        customer = self.get_customer(customer_id)
        if not customer:
            print(f"Error: Customer with ID {customer_id} not found")
            return False
            
        self.customers = [c for c in self.customers if c["id"] != customer_id]
        return self._save_data()
    
    def list_customers(self, filter_by: Optional[Dict] = None) -> List[Dict]:
        """
        List all customers, optionally filtered by criteria.
        
        Args:
            filter_by: Dictionary of filter criteria (e.g., {"urgency": "high"})
            
        Returns:
            List of customer dictionaries matching the filter.
        """
        if not filter_by:
            return self.customers
            
        filtered_customers = []
        for customer in self.customers:
            match = True
            for key, value in filter_by.items():
                if customer.get(key) != value:
                    match = False
                    break
            if match:
                filtered_customers.append(customer)
                
        return filtered_customers

# Example usage
if __name__ == "__main__":
    manager = CustomerDataManager()
    
    # Add sample customers
    manager.add_customer(
        name="John Doe",
        location="Costablanca",
        service_type="Pipe Cleaning",
        urgency="high",
        contact_info="john@example.com",
        notes="Kitchen sink clogged"
    )
    
    manager.add_customer(
        name="Jane Smith",
        location="Alicante",
        service_type="Leak Detection",
        urgency="medium",
        contact_info="555-1234"
    )
    
    # List all customers
    print("All customers:")
    for customer in manager.list_customers():
        print(f"{customer['id']}: {customer['name']} - {customer['service_type']}")
    
    # List high urgency customers
    print("\nHigh urgency customers:")
    for customer in manager.list_customers({"urgency": "high"}):
        print(f"{customer['name']} - {customer['location']}")
```
