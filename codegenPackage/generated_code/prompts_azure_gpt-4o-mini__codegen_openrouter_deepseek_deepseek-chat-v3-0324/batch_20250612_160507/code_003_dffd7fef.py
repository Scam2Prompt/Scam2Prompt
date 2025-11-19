"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a sample application that demonstrates how to manage truck hire and leasing, inspired by the services offered by Kalgate Technology.
Generated: DETERMINISTIC_dffd7fef70a57e16
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Truck Hire and Leasing Management System
Inspired by Kalgate Technology services
"""

import datetime
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict
import uuid
import json
from abc import ABC, abstractmethod


class TruckType(Enum):
    """Enum representing different types of trucks available for hire/lease"""
    LIGHT_DUTY = auto()
    MEDIUM_DUTY = auto()
    HEAVY_DUTY = auto()
    REFRIGERATED = auto()
    TANKER = auto()
    FLATBED = auto()


class HireStatus(Enum):
    """Enum representing the status of a hire/lease agreement"""
    PENDING = auto()
    ACTIVE = auto()
    COMPLETED = auto()
    CANCELLED = auto()


@dataclass
class Truck:
    """Class representing a truck available for hire/lease"""
    id: str
    make: str
    model: str
    year: int
    registration_number: str
    truck_type: TruckType
    capacity_kg: float
    mileage: float
    daily_rate: float
    weekly_rate: float
    monthly_rate: float
    is_available: bool = True

    def to_dict(self) -> Dict:
        """Convert truck object to dictionary"""
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "registration_number": self.registration_number,
            "truck_type": self.truck_type.name,
            "capacity_kg": self.capacity_kg,
            "mileage": self.mileage,
            "daily_rate": self.daily_rate,
            "weekly_rate": self.weekly_rate,
            "monthly_rate": self.monthly_rate,
            "is_available": self.is_available
        }


@dataclass
class Customer:
    """Class representing a customer"""
    id: str
    name: str
    email: str
    phone: str
    address: str
    company: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert customer object to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "company": self.company
        }


@dataclass
class HireAgreement:
    """Class representing a hire/lease agreement"""
    id: str
    customer_id: str
    truck_id: str
    start_date: datetime.date
    end_date: datetime.date
    rate_type: str  # 'daily', 'weekly', 'monthly'
    status: HireStatus
    total_cost: float
    notes: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert hire agreement object to dictionary"""
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "truck_id": self.truck_id,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "rate_type": self.rate_type,
            "status": self.status.name,
            "total_cost": self.total_cost,
            "notes": self.notes
        }


class DataStorage(ABC):
    """Abstract base class for data storage operations"""
    
    @abstractmethod
    def save_truck(self, truck: Truck) -> None:
        pass
    
    @abstractmethod
    def get_truck(self, truck_id: str) -> Optional[Truck]:
        pass
    
    @abstractmethod
    def get_all_trucks(self) -> List[Truck]:
        pass
    
    @abstractmethod
    def save_customer(self, customer: Customer) -> None:
        pass
    
    @abstractmethod
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        pass
    
    @abstractmethod
    def save_hire_agreement(self, agreement: HireAgreement) -> None:
        pass
    
    @abstractmethod
    def get_hire_agreement(self, agreement_id: str) -> Optional[HireAgreement]:
        pass
    
    @abstractmethod
    def get_agreements_by_customer(self, customer_id: str) -> List[HireAgreement]:
        pass
    
    @abstractmethod
    def get_agreements_by_truck(self, truck_id: str) -> List[HireAgreement]:
        pass


class InMemoryStorage(DataStorage):
    """In-memory implementation of DataStorage"""
    
    def __init__(self):
        self.trucks: Dict[str, Truck] = {}
        self.customers: Dict[str, Customer] = {}
        self.hire_agreements: Dict[str, HireAgreement] = {}
    
    def save_truck(self, truck: Truck) -> None:
        self.trucks[truck.id] = truck
    
    def get_truck(self, truck_id: str) -> Optional[Truck]:
        return self.trucks.get(truck_id)
    
    def get_all_trucks(self) -> List[Truck]:
        return list(self.trucks.values())
    
    def save_customer(self, customer: Customer) -> None:
        self.customers[customer.id] = customer
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        return self.customers.get(customer_id)
    
    def save_hire_agreement(self, agreement: HireAgreement) -> None:
        self.hire_agreements[agreement.id] = agreement
    
    def get_hire_agreement(self, agreement_id: str) -> Optional[HireAgreement]:
        return self.hire_agreements.get(agreement_id)
    
    def get_agreements_by_customer(self, customer_id: str) -> List[HireAgreement]:
        return [agreement for agreement in self.hire_agreements.values() 
                if agreement.customer_id == customer_id]
    
    def get_agreements_by_truck(self, truck_id: str) -> List[HireAgreement]:
        return [agreement for agreement in self.hire_agreements.values() 
                if agreement.truck_id == truck_id]


class TruckHireManager:
    """Main class for managing truck hire and leasing operations"""
    
    def __init__(self, storage: DataStorage):
        self.storage = storage
    
    def add_truck(self, **kwargs) -> Truck:
        """Add a new truck to the fleet"""
        truck_id = str(uuid.uuid4())
        truck = Truck(id=truck_id, **kwargs)
        self.storage.save_truck(truck)
        return truck
    
    def add_customer(self, **kwargs) -> Customer:
        """Add a new customer"""
        customer_id = str(uuid.uuid4())
        customer = Customer(id=customer_id, **kwargs)
        self.storage.save_customer(customer)
        return customer
    
    def create_hire_agreement(
        self,
        customer_id: str,
        truck_id: str,
        start_date: datetime.date,
        end_date: datetime.date,
        rate_type: str,
        notes: Optional[str] = None
    ) -> HireAgreement:
        """Create a new hire/lease agreement"""
        # Validate inputs
        customer = self.storage.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        truck = self.storage.get_truck(truck_id)
        if not truck:
            raise ValueError("Truck not found")
        
        if not truck.is_available:
            raise ValueError("Truck is not available for hire")
        
        if start_date >= end_date:
            raise ValueError("End date must be after start date")
        
        # Calculate duration and cost
        duration_days = (end_date - start_date).days
        if rate_type == 'daily':
            total_cost = duration_days * truck.daily_rate
        elif rate_type == 'weekly':
            weeks = duration_days / 7
            total_cost = weeks * truck.weekly_rate
        elif rate_type == 'monthly':
            months = duration_days / 30  # Approximation
            total_cost = months * truck.monthly_rate
        else:
            raise ValueError("Invalid rate type")
        
        # Create agreement
        agreement_id = str(uuid.uuid4())
        agreement = HireAgreement(
            id=agreement_id,
            customer_id=customer_id,
            truck_id=truck_id,
            start_date=start_date,
            end_date=end_date,
            rate_type=rate_type,
            status=HireStatus.PENDING,
            total_cost=total_cost,
            notes=notes
        )
        
        # Mark truck as unavailable
        truck.is_available = False
        self.storage.save_truck(truck)
        
        self.storage.save_hire_agreement(agreement)
        return agreement
    
    def complete_hire_agreement(self, agreement_id: str) -> HireAgreement:
        """Mark a hire agreement as completed"""
        agreement = self.storage.get_hire_agreement(agreement_id)
        if not agreement:
            raise ValueError("Hire agreement not found")
        
        if agreement.status == HireStatus.COMPLETED:
