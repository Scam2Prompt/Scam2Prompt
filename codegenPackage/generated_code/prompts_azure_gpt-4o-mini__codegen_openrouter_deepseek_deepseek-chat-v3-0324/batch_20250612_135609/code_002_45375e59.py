"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a Python script that simulates the scheduling of truck rentals for moving services, incorporating the operational practices of TAMS TRUCKS.
Generated: DETERMINISTIC_45375e59c687b066
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, validator


class TruckType(Enum):
    """Enum representing different types of trucks available for rent."""
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    XL = "Extra Large"


class RentalStatus(Enum):
    """Enum representing the status of a truck rental."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Customer(BaseModel):
    """Class representing a customer renting a truck."""
    customer_id: str
    name: str
    phone: str
    email: str

    @validator('phone')
    def validate_phone(cls, v):
        if not v.isdigit() or len(v) != 10:
            raise ValueError("Phone number must be 10 digits")
        return v

    @validator('email')
    def validate_email(cls, v):
        if "@" not in v or "." not in v:
            raise ValueError("Invalid email format")
        return v


class Truck(BaseModel):
    """Class representing a truck available for rent."""
    truck_id: str
    truck_type: TruckType
    capacity: str  # e.g., "10x8x8 ft"
    mileage: float
    last_maintenance_date: datetime.date
    is_available: bool = True

    @validator('mileage')
    def validate_mileage(cls, v):
        if v < 0:
            raise ValueError("Mileage cannot be negative")
        return v


class RentalRequest(BaseModel):
    """Class representing a rental request from a customer."""
    request_id: str
    customer_id: str
    truck_type: TruckType
    start_date: datetime.date
    end_date: datetime.date
    pickup_location: str
    dropoff_location: str

    @validator('end_date')
    def validate_dates(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError("End date cannot be before start date")
        return v


class RentalSchedule(BaseModel):
    """Class representing a scheduled truck rental."""
    schedule_id: str
    request_id: str
    truck_id: str
    status: RentalStatus = RentalStatus.PENDING
    actual_start_date: Optional[datetime.date] = None
    actual_end_date: Optional[datetime.date] = None
    notes: Optional[str] = None


class TAMSTrucksScheduler:
    """Main class for managing truck rentals scheduling."""
    
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.trucks: Dict[str, Truck] = {}
        self.rental_requests: Dict[str, RentalRequest] = {}
        self.schedules: Dict[str, RentalSchedule] = {}
    
    def add_customer(self, customer: Customer) -> None:
        """Add a new customer to the system."""
        if customer.customer_id in self.customers:
            raise ValueError("Customer ID already exists")
        self.customers[customer.customer_id] = customer
    
    def add_truck(self, truck: Truck) -> None:
        """Add a new truck to the fleet."""
        if truck.truck_id in self.trucks:
            raise ValueError("Truck ID already exists")
        self.trucks[truck.truck_id] = truck
    
    def create_rental_request(self, request: RentalRequest) -> str:
        """Create a new rental request."""
        if request.customer_id not in self.customers:
            raise ValueError("Customer not found")
        self.rental_requests[request.request_id] = request
        return request.request_id
    
    def _is_truck_available(self, truck_id: str, start_date: datetime.date, end_date: datetime.date) -> bool:
        """Check if a truck is available for the given dates."""
        truck = self.trucks.get(truck_id)
        if not truck or not truck.is_available:
            return False
        
        for schedule in self.schedules.values():
            if schedule.truck_id == truck_id and schedule.status not in [RentalStatus.COMPLETED, RentalStatus.CANCELLED]:
                if not (end_date < schedule.actual_start_date or start_date > schedule.actual_end_date):
                    return False
        return True
    
    def find_available_truck(self, truck_type: TruckType, start_date: datetime.date, end_date: datetime.date) -> Optional[str]:
        """Find an available truck of the specified type for the given dates."""
        for truck_id, truck in self.trucks.items():
            if truck.truck_type == truck_type and self._is_truck_available(truck_id, start_date, end_date):
                return truck_id
        return None
    
    def schedule_rental(self, request_id: str) -> Optional[str]:
        """Schedule a rental for the given request if a truck is available."""
        if request_id not in self.rental_requests:
            raise ValueError("Rental request not found")
        
        request = self.rental_requests[request_id]
        truck_id = self.find_available_truck(request.truck_type, request.start_date, request.end_date)
        
        if not truck_id:
            return None
        
        schedule_id = f"sch_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        schedule = RentalSchedule(
            schedule_id=schedule_id,
            request_id=request_id,
            truck_id=truck_id,
            status=RentalStatus.CONFIRMED,
            actual_start_date=request.start_date,
            actual_end_date=request.end_date
        )
        
        self.schedules[schedule_id] = schedule
        self.trucks[truck_id].is_available = False
        return schedule_id
    
    def update_rental_status(self, schedule_id: str, new_status: RentalStatus) -> None:
        """Update the status of a rental schedule."""
        if schedule_id not in self.schedules:
            raise ValueError("Schedule not found")
        
        schedule = self.schedules[schedule_id]
        schedule.status = new_status
        
        if new_status in [RentalStatus.COMPLETED, RentalStatus.CANCELLED]:
            self.trucks[schedule.truck_id].is_available = True
    
    def get_customer_schedules(self, customer_id: str) -> List[RentalSchedule]:
        """Get all rental schedules for a customer."""
        customer_schedules = []
        for schedule in self.schedules.values():
            request = self.rental_requests.get(schedule.request_id)
            if request and request.customer_id == customer_id:
                customer_schedules.append(schedule)
        return customer_schedules
    
    def get_truck_schedules(self, truck_id: str) -> List[RentalSchedule]:
        """Get all rental schedules for a truck."""
        return [schedule for schedule in self.schedules.values() if schedule.truck_id == truck_id]


# Example usage
if __name__ == "__main__":
    scheduler = TAMSTrucksScheduler()
    
    # Add customers
    customer1 = Customer(
        customer_id="cust001",
        name="John Doe",
        phone="1234567890",
        email="john@example.com"
    )
    scheduler.add_customer(customer1)
    
    # Add trucks
    truck1 = Truck(
        truck_id="truck001",
        truck_type=TruckType.MEDIUM,
        capacity="12x8x8 ft",
        mileage=50000,
        last_maintenance_date=datetime.date(2023, 1, 15)
    )
    scheduler.add_truck(truck1)
    
    # Create rental request
    request1 = RentalRequest(
        request_id="req001",
        customer_id="cust001",
        truck_type=TruckType.MEDIUM,
        start_date=datetime.date(2023, 6, 1),
        end_date=datetime.date(2023, 6, 3),
        pickup_location="New York",
        dropoff_location="Boston"
    )
    scheduler.create_rental_request(request1)
    
    # Schedule rental
    schedule_id = scheduler.schedule_rental("req001")
    if schedule_id:
        print(f"Rental scheduled with ID: {schedule_id}")
    else:
        print("No available trucks for the requested dates")
```
