"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a Python script that simulates the process of scheduling meter verification for water, gas, and heat meters, including fields for customer details, meter type, and verification frequency (e.g., every four years for heat meters).
Generated: DETERMINISTIC_c2d7cc55eca94373
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from enum import Enum
import uuid
from typing import Dict, List, Optional


class MeterType(Enum):
    """Enum representing different types of meters."""
    WATER = "water"
    GAS = "gas"
    HEAT = "heat"


class VerificationFrequency(Enum):
    """Enum representing verification frequencies for different meter types."""
    WATER = 2  # years
    GAS = 3    # years
    HEAT = 4   # years


class Customer:
    """Class representing a customer with meter verification details."""
    
    def __init__(self, name: str, address: str, email: str, phone: str):
        """
        Initialize a customer with personal details.
        
        Args:
            name: Customer's full name.
            address: Customer's address.
            email: Customer's email.
            phone: Customer's phone number.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.meters: List[Dict] = []

    def add_meter(self, meter_type: MeterType, installation_date: datetime, last_verification_date: Optional[datetime] = None) -> None:
        """
        Add a meter to the customer's account.
        
        Args:
            meter_type: Type of the meter (water, gas, heat).
            installation_date: Date when the meter was installed.
            last_verification_date: Optional date of last verification. Defaults to installation date.
        """
        if last_verification_date is None:
            last_verification_date = installation_date
        
        frequency = self._get_verification_frequency(meter_type)
        next_verification_date = last_verification_date + timedelta(days=365 * frequency)
        
        self.meters.append({
            "id": str(uuid.uuid4()),
            "type": meter_type.value,
            "installation_date": installation_date.isoformat(),
            "last_verification_date": last_verification_date.isoformat(),
            "next_verification_date": next_verification_date.isoformat(),
            "verification_frequency_years": frequency
        })

    def _get_verification_frequency(self, meter_type: MeterType) -> int:
        """Get verification frequency in years based on meter type."""
        if meter_type == MeterType.WATER:
            return VerificationFrequency.WATER.value
        elif meter_type == MeterType.GAS:
            return VerificationFrequency.GAS.value
        elif meter_type == MeterType.HEAT:
            return VerificationFrequency.HEAT.value
        else:
            raise ValueError(f"Unknown meter type: {meter_type}")

    def to_dict(self) -> Dict:
        """Convert customer data to a dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "phone": self.phone,
            "meters": self.meters
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Customer':
        """Create a Customer instance from a dictionary."""
        customer = cls(
            name=data["name"],
            address=data["address"],
            email=data["email"],
            phone=data["phone"]
        )
        customer.id = data["id"]
        customer.meters = data["meters"]
        return customer


class MeterScheduler:
    """Class to manage scheduling of meter verifications."""
    
    def __init__(self, storage_file: str = "meter_schedule.json"):
        """
        Initialize the scheduler with a storage file.
        
        Args:
            storage_file: Path to the JSON file for storing data.
        """
        self.storage_file = storage_file
        self.customers: Dict[str, Customer] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load customer data from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                for customer_data in data.get("customers", []):
                    customer = Customer.from_dict(customer_data)
                    self.customers[customer.id] = customer
        except FileNotFoundError:
            pass  # File doesn't exist yet, start with empty data

    def _save_data(self) -> None:
        """Save customer data to the storage file."""
        data = {
            "customers": [customer.to_dict() for customer in self.customers.values()]
        }
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=2)

    def add_customer(self, customer: Customer) -> str:
        """
        Add a new customer to the scheduler.
        
        Args:
            customer: Customer object to add.
            
        Returns:
            The ID of the added customer.
        """
        self.customers[customer.id] = customer
        self._save_data()
        return customer.id

    def schedule_verification(self, customer_id: str, meter_id: str, verification_date: datetime) -> None:
        """
        Schedule a meter verification and update the next verification date.
        
        Args:
            customer_id: ID of the customer.
            meter_id: ID of the meter.
            verification_date: Date when verification was performed.
            
        Raises:
            ValueError: If customer or meter is not found.
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer with ID {customer_id} not found.")
        
        customer = self.customers[customer_id]
        meter = next((m for m in customer.meters if m["id"] == meter_id), None)
        
        if not meter:
            raise ValueError(f"Meter with ID {meter_id} not found for customer {customer_id}.")
        
        meter["last_verification_date"] = verification_date.isoformat()
        frequency = meter["verification_frequency_years"]
        meter["next_verification_date"] = (verification_date + timedelta(days=365 * frequency)).isoformat()
        self._save_data()

    def get_upcoming_verifications(self, days_ahead: int = 30) -> List[Dict]:
        """
        Get all verifications due within the specified number of days.
        
        Args:
            days_ahead: Number of days to look ahead for verifications.
            
        Returns:
            List of dictionaries with verification details.
        """
        upcoming = []
        today = datetime.now()
        end_date = today + timedelta(days=days_ahead)
        
        for customer in self.customers.values():
            for meter in customer.meters:
                next_date = datetime.fromisoformat(meter["next_verification_date"])
                if today <= next_date <= end_date:
                    upcoming.append({
                        "customer_id": customer.id,
                        "customer_name": customer.name,
                        "meter_id": meter["id"],
                        "meter_type": meter["type"],
                        "verification_due_date": meter["next_verification_date"],
                        "customer_contact": {
                            "email": customer.email,
                            "phone": customer.phone,
                            "address": customer.address
                        }
                    })
        
        return upcoming


# Example usage
if __name__ == "__main__":
    # Initialize scheduler
    scheduler = MeterScheduler()
    
    # Create a customer
    customer = Customer(
        name="John Doe",
        address="123 Main St, Anytown",
        email="john.doe@example.com",
        phone="+1234567890"
    )
    
    # Add meters with different types
    today = datetime.now()
    customer.add_meter(MeterType.WATER, today)
    customer.add_meter(MeterType.GAS, today - timedelta(days=365*2))  # installed 2 years ago
    customer.add_meter(MeterType.HEAT, today - timedelta(days=365*3))  # installed 3 years ago
    
    # Add customer to scheduler
    customer_id = scheduler.add_customer(customer)
    
    # Get upcoming verifications
    upcoming = scheduler.get_upcoming_verifications()
    print("Upcoming verifications:")
    print(json.dumps(upcoming, indent=2))
    
    # Schedule a verification
    if upcoming:
        first_verification = upcoming[0]
        scheduler.schedule_verification(
            customer_id=first_verification["customer_id"],
            meter_id=first_verification["meter_id"],
            verification_date=datetime.now()
        )
        print("\nVerification scheduled successfully.")
```
