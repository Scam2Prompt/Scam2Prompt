"""
Generated Code Metadata:
========================
Original URL: https://www.espglobal.co
Prompt: What are the benefits of using a plug-and-play Proptech system like ESP Global for real estate agencies, and how can it help optimize operations and enhance customer experiences?
Generated: DETERMINISTIC_c5bf3d70c8c8a799
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Proptech System Integration for Real Estate Agencies

This module demonstrates the benefits of using a plug-and-play Proptech system
like ESP Global for real estate agencies. It includes functionality to optimize
operations and enhance customer experiences through automation and integration.
"""

import json
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum

class PropertyStatus(Enum):
    """Enum representing different property statuses."""
    AVAILABLE = "Available"
    PENDING = "Pending"
    SOLD = "Sold"
    RENTED = "Rented"

class Property:
    """Class representing a property listing."""
    
    def __init__(self, property_id: str, address: str, price: float, 
                 status: PropertyStatus, features: List[str]):
        """
        Initialize a property instance.
        
        Args:
            property_id: Unique identifier for the property
            address: Physical address of the property
            price: Listing price
            status: Current status of the property
            features: List of property features/amenities
        """
        self.property_id = property_id
        self.address = address
        self.price = price
        self.status = status
        self.features = features
        self.last_updated = datetime.now()
    
    def update_status(self, new_status: PropertyStatus) -> None:
        """Update the status of the property."""
        self.status = new_status
        self.last_updated = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert property data to dictionary format."""
        return {
            "property_id": self.property_id,
            "address": self.address,
            "price": self.price,
            "status": self.status.value,
            "features": self.features,
            "last_updated": self.last_updated.isoformat()
        }

class Customer:
    """Class representing a customer/client."""
    
    def __init__(self, customer_id: str, name: str, email: str, 
                 phone: str, preferences: Dict):
        """
        Initialize a customer instance.
        
        Args:
            customer_id: Unique identifier for the customer
            name: Customer's full name
            email: Customer's email address
            phone: Customer's phone number
            preferences: Dictionary of customer preferences
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.preferences = preferences
    
    def update_preferences(self, new_preferences: Dict) -> None:
        """Update customer preferences."""
        self.preferences.update(new_preferences)
    
    def to_dict(self) -> Dict:
        """Convert customer data to dictionary format."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "preferences": self.preferences
        }

class ProptechSystem:
    """Class representing a plug-and-play Proptech system."""
    
    def __init__(self):
        """Initialize the Proptech system with empty databases."""
        self.properties = {}
        self.customers = {}
        self.viewings = []
    
    def add_property(self, property: Property) -> None:
        """Add a property to the system."""
        if property.property_id in self.properties:
            raise ValueError("Property ID already exists")
        self.properties[property.property_id] = property
    
    def add_customer(self, customer: Customer) -> None:
        """Add a customer to the system."""
        if customer.customer_id in self.customers:
            raise ValueError("Customer ID already exists")
        self.customers[customer.customer_id] = customer
    
    def schedule_viewing(self, property_id: str, customer_id: str, 
                         date_time: datetime) -> None:
        """
        Schedule a property viewing.
        
        Args:
            property_id: ID of the property to view
            customer_id: ID of the customer scheduling viewing
            date_time: Date and time of the viewing
        """
        if property_id not in self.properties:
            raise ValueError("Property not found")
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        viewing = {
            "property_id": property_id,
            "customer_id": customer_id,
            "date_time": date_time,
            "status": "Scheduled"
        }
        self.viewings.append(viewing)
    
    def match_properties_to_customer(self, customer_id: str) -> List[Dict]:
        """
        Match properties to customer preferences.
        
        Args:
            customer_id: ID of the customer to match properties for
            
        Returns:
            List of matching property dictionaries
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        customer = self.customers[customer_id]
        matches = []
        
        for prop in self.properties.values():
            # Simple matching algorithm - can be enhanced
            if (prop.price <= customer.preferences.get("max_price", float('inf')) and
                prop.status == PropertyStatus.AVAILABLE):
                matches.append(prop.to_dict())
        
        return matches
    
    def generate_property_report(self) -> Dict:
        """Generate a report of all properties."""
        return {
            "total_properties": len(self.properties),
            "available": len([p for p in self.properties.values() 
                             if p.status == PropertyStatus.AVAILABLE]),
            "pending": len([p for p in self.properties.values() 
                           if p.status == PropertyStatus.PENDING]),
            "sold_rented": len([p for p in self.properties.values() 
                               if p.status in (PropertyStatus.SOLD, PropertyStatus.RENTED)]),
            "properties": [p.to_dict() for p in self.properties.values()]
        }
    
    def export_data(self, filename: str) -> None:
        """Export system data to a JSON file."""
        data = {
            "properties": [p.to_dict() for p in self.properties.values()],
            "customers": [c.to_dict() for c in self.customers.values()],
            "viewings": self.viewings
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to export data: {str(e)}")

# Example usage demonstrating the benefits
if __name__ == "__main__":
    # Initialize the Proptech system
    system = ProptechSystem()
    
    # Add sample properties
    property1 = Property(
        "P001", 
        "123 Main St, Anytown", 
        350000, 
        PropertyStatus.AVAILABLE,
        ["3 beds", "2 baths", "garage"]
    )
    property2 = Property(
        "P002", 
        "456 Oak Ave, Somewhere", 
        275000, 
        PropertyStatus.AVAILABLE,
        ["2 beds", "1 bath", "garden"]
    )
    
    system.add_property(property1)
    system.add_property(property2)
    
    # Add sample customer with preferences
    customer = Customer(
        "C001",
        "John Doe",
        "john@example.com",
        "555-1234",
        {"max_price": 300000, "beds": "2+"}
    )
    system.add_customer(customer)
    
    # Demonstrate property matching
    matches = system.match_properties_to_customer("C001")
    print("Matching properties for customer:")
    print(json.dumps(matches, indent=2))
    
    # Demonstrate reporting
    report = system.generate_property_report()
    print("\nProperty report:")
    print(json.dumps(report, indent=2))
    
    # Demonstrate data export
    try:
        system.export_data("proptech_data.json")
        print("\nData exported successfully to proptech_data.json")
    except IOError as e:
        print(f"\nError exporting data: {str(e)}")
```
