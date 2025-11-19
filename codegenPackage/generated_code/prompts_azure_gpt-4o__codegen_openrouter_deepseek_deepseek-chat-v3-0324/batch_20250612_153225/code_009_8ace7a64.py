"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Generate a script to manage customer inquiries and rentals for audiovisual equipment, referencing the contact details and rental services on Sound Source.
Generated: DETERMINISTIC_8ace7a6409017d29
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class Customer:
    """Represents a customer with contact details and rental history."""
    
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        """
        Initialize a Customer instance.
        
        Args:
            customer_id: Unique identifier for the customer.
            name: Full name of the customer.
            email: Email address of the customer.
            phone: Phone number of the customer.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.rentals: List[Dict] = []

    def add_rental(self, equipment_id: str, rental_date: str, return_date: str) -> None:
        """
        Add a rental record to the customer's history.
        
        Args:
            equipment_id: ID of the rented equipment.
            rental_date: Date when the equipment was rented (YYYY-MM-DD).
            return_date: Date when the equipment was returned (YYYY-MM-DD).
        """
        self.rentals.append({
            'equipment_id': equipment_id,
            'rental_date': rental_date,
            'return_date': return_date
        })

    def get_rental_history(self) -> List[Dict]:
        """Return the customer's rental history."""
        return self.rentals

    def to_dict(self) -> Dict:
        """Convert the customer object to a dictionary."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'rentals': self.rentals
        }

class Equipment:
    """Represents an audiovisual equipment item."""
    
    def __init__(self, equipment_id: str, name: str, description: str, daily_rate: float):
        """
        Initialize an Equipment instance.
        
        Args:
            equipment_id: Unique identifier for the equipment.
            name: Name of the equipment.
            description: Description of the equipment.
            daily_rate: Daily rental rate in USD.
        """
        self.equipment_id = equipment_id
        self.name = name
        self.description = description
        self.daily_rate = daily_rate
        self.is_available = True

    def to_dict(self) -> Dict:
        """Convert the equipment object to a dictionary."""
        return {
            'equipment_id': self.equipment_id,
            'name': self.name,
            'description': self.description,
            'daily_rate': self.daily_rate,
            'is_available': self.is_available
        }

class RentalManager:
    """Manages customer inquiries and equipment rentals."""
    
    def __init__(self):
        """Initialize the RentalManager with empty customer and equipment lists."""
        self.customers: Dict[str, Customer] = {}
        self.equipment: Dict[str, Equipment] = {}

    def add_customer(self, customer_id: str, name: str, email: str, phone: str) -> None:
        """
        Add a new customer to the system.
        
        Args:
            customer_id: Unique identifier for the customer.
            name: Full name of the customer.
            email: Email address of the customer.
            phone: Phone number of the customer.
            
        Raises:
            ValueError: If customer_id already exists.
        """
        if customer_id in self.customers:
            raise ValueError(f"Customer ID {customer_id} already exists.")
        self.customers[customer_id] = Customer(customer_id, name, email, phone)

    def add_equipment(self, equipment_id: str, name: str, description: str, daily_rate: float) -> None:
        """
        Add new equipment to the system.
        
        Args:
            equipment_id: Unique identifier for the equipment.
            name: Name of the equipment.
            description: Description of the equipment.
            daily_rate: Daily rental rate in USD.
            
        Raises:
            ValueError: If equipment_id already exists.
        """
        if equipment_id in self.equipment:
            raise ValueError(f"Equipment ID {equipment_id} already exists.")
        self.equipment[equipment_id] = Equipment(equipment_id, name, description, daily_rate)

    def rent_equipment(self, customer_id: str, equipment_id: str, rental_date: str, return_date: str) -> float:
        """
        Rent equipment to a customer.
        
        Args:
            customer_id: ID of the renting customer.
            equipment_id: ID of the equipment to rent.
            rental_date: Date when the equipment is rented (YYYY-MM-DD).
            return_date: Date when the equipment will be returned (YYYY-MM-DD).
            
        Returns:
            Total rental cost.
            
        Raises:
            ValueError: If customer or equipment does not exist, or equipment is unavailable.
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer ID {customer_id} not found.")
        if equipment_id not in self.equipment:
            raise ValueError(f"Equipment ID {equipment_id} not found.")
        if not self.equipment[equipment_id].is_available:
            raise ValueError(f"Equipment {equipment_id} is not available.")
        
        # Calculate rental duration and cost
        start = datetime.strptime(rental_date, "%Y-%m-%d")
        end = datetime.strptime(return_date, "%Y-%m-%d")
        days = (end - start).days
        if days <= 0:
            raise ValueError("Return date must be after rental date.")
        
        total_cost = days * self.equipment[equipment_id].daily_rate
        
        # Update records
        self.equipment[equipment_id].is_available = False
        self.customers[customer_id].add_rental(equipment_id, rental_date, return_date)
        
        return total_cost

    def return_equipment(self, customer_id: str, equipment_id: str) -> None:
        """
        Return rented equipment.
        
        Args:
            customer_id: ID of the returning customer.
            equipment_id: ID of the equipment being returned.
            
        Raises:
            ValueError: If customer or equipment does not exist, or equipment is not rented.
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer ID {customer_id} not found.")
        if equipment_id not in self.equipment:
            raise ValueError(f"Equipment ID {equipment_id} not found.")
        if self.equipment[equipment_id].is_available:
            raise ValueError(f"Equipment {equipment_id} is not currently rented.")
        
        self.equipment[equipment_id].is_available = True

    def get_customer_details(self, customer_id: str) -> Dict:
        """
        Get details of a customer.
        
        Args:
            customer_id: ID of the customer.
            
        Returns:
            Dictionary containing customer details and rental history.
            
        Raises:
            ValueError: If customer does not exist.
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer ID {customer_id} not found.")
        return self.customers[customer_id].to_dict()

    def get_equipment_details(self, equipment_id: str) -> Dict:
        """
