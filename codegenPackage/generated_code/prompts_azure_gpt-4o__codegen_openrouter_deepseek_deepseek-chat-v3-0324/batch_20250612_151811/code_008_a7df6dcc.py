"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Develop a system for outsourcing drivers, including features for matching drivers to haulage needs, inspired by Kalgate Technology's driver outsourcing services.
Generated: DETERMINISTIC_a7df6dcc1d365acd
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Driver Outsourcing System - Inspired by Kalgate Technology

This system provides features for matching drivers to haulage needs,
managing driver profiles, and handling assignments.
"""

from datetime import datetime
from typing import List, Dict, Optional
import uuid
from enum import Enum, auto
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DriverStatus(Enum):
    AVAILABLE = auto()
    ASSIGNED = auto()
    ON_LEAVE = auto()
    TERMINATED = auto()

class HaulageType(Enum):
    LOCAL = auto()
    INTERSTATE = auto()
    INTERNATIONAL = auto()

class VehicleType(Enum):
    TRUCK = auto()
    VAN = auto()
    TRAILER = auto()
    TANKER = auto()

@dataclass
class Driver:
    id: str
    name: str
    license_number: str
    license_expiry: datetime
    vehicle_types: List[VehicleType]
    haulage_experience: List[HaulageType]
    status: DriverStatus
    location: str
    rating: float = 0.0
    phone: Optional[str] = None
    email: Optional[str] = None

@dataclass
class HaulageRequest:
    id: str
    origin: str
    destination: str
    haulage_type: HaulageType
    vehicle_type: VehicleType
    required_drivers: int
    start_date: datetime
    end_date: datetime
    requirements: Optional[str] = None

@dataclass
class Assignment:
    id: str
    driver_id: str
    haulage_id: str
    assignment_date: datetime
    status: str = "ACTIVE"

class DriverOutsourcingSystem:
    def __init__(self):
        self.drivers: Dict[str, Driver] = {}
        self.haulage_requests: Dict[str, HaulageRequest] = {}
        self.assignments: Dict[str, Assignment] = {}
    
    def add_driver(self, driver: Driver) -> str:
        """Add a new driver to the system."""
        if driver.id in self.drivers:
            raise ValueError("Driver with this ID already exists")
        
        self.drivers[driver.id] = driver
        logger.info(f"Added new driver: {driver.name} (ID: {driver.id})")
        return driver.id
    
    def update_driver_status(self, driver_id: str, status: DriverStatus) -> None:
        """Update a driver's status."""
        if driver_id not in self.drivers:
            raise ValueError("Driver not found")
        
        self.drivers[driver_id].status = status
        logger.info(f"Updated driver {driver_id} status to {status.name}")
    
    def create_haulage_request(self, request: HaulageRequest) -> str:
        """Create a new haulage request."""
        request.id = str(uuid.uuid4())
        self.haulage_requests[request.id] = request
        logger.info(f"Created new haulage request ID: {request.id}")
        return request.id
    
    def find_matching_drivers(self, haulage_id: str) -> List[Driver]:
        """
        Find available drivers matching the haulage requirements.
        Returns list of matching drivers sorted by rating (highest first).
        """
        if haulage_id not in self.haulage_requests:
            raise ValueError("Haulage request not found")
        
        request = self.haulage_requests[haulage_id]
        matching_drivers = []
        
        for driver in self.drivers.values():
            if (driver.status == DriverStatus.AVAILABLE and
                request.vehicle_type in driver.vehicle_types and
                request.haulage_type in driver.haulage_experience and
                driver.location == request.origin):
                
                matching_drivers.append(driver)
        
        # Sort by rating (highest first)
        matching_drivers.sort(key=lambda d: d.rating, reverse=True)
        logger.info(f"Found {len(matching_drivers)} matching drivers for haulage {haulage_id}")
        return matching_drivers
    
    def assign_driver(self, driver_id: str, haulage_id: str) -> str:
        """Assign a driver to a haulage request."""
        if driver_id not in self.drivers:
            raise ValueError("Driver not found")
        if haulage_id not in self.haulage_requests:
            raise ValueError("Haulage request not found")
        
        driver = self.drivers[driver_id]
        if driver.status != DriverStatus.AVAILABLE:
            raise ValueError("Driver is not available for assignment")
        
        assignment = Assignment(
            id=str(uuid.uuid4()),
            driver_id=driver_id,
            haulage_id=haulage_id,
            assignment_date=datetime.now()
        )
        
        self.assignments[assignment.id] = assignment
        driver.status = DriverStatus.ASSIGNED
        logger.info(f"Assigned driver {driver_id} to haulage {haulage_id}")
        return assignment.id
    
    def complete_assignment(self, assignment_id: str, rating: float = None) -> None:
        """Mark an assignment as completed and update driver rating."""
        if assignment_id not in self.assignments:
            raise ValueError("Assignment not found")
        
        assignment = self.assignments[assignment_id]
        driver_id = assignment.driver_id
        
        if driver_id not in self.drivers:
            raise ValueError("Driver not found")
        
        driver = self.drivers[driver_id]
        driver.status = DriverStatus.AVAILABLE
        
        if rating is not None:
            # Simple rating update (could be more sophisticated)
            driver.rating = (driver.rating + rating) / 2
        
        assignment.status = "COMPLETED"
        logger.info(f"Completed assignment {assignment_id} for driver {driver_id}")
    
    def get_driver_assignments(self, driver_id: str) -> List[Assignment]:
        """Get all assignments for a specific driver."""
        if driver_id not in self.drivers:
            raise ValueError("Driver not found")
        
        return [a for a in self.assignments.values() if a.driver_id == driver_id]
    
    def get_haulage_assignments(self, haulage_id: str) -> List[Assignment]:
        """Get all assignments for a specific haulage request."""
        if haulage_id not in self.haulage_requests:
            raise ValueError("Haulage request not found")
        
        return [a for a in self.assignments.values() if a.haulage_id == haulage_id]

# Example usage
if __name__ == "__main__":
    system = DriverOutsourcingSystem()
    
    # Add some drivers
    driver1 = Driver(
        id=str(uuid.uuid4()),
        name="John Doe",
        license_number="DL123456",
        license_expiry=datetime(2025, 12, 31),
        vehicle_types=[VehicleType.TRUCK, VehicleType.TRAILER],
        haulage_experience=[HaulageType.LOCAL, HaulageType.INTERSTATE],
        status=DriverStatus.AVAILABLE,
        location="New York",
        rating=4.5,
        phone="+1234567890"
    )
    
    driver2 = Driver(
        id=str(uuid.uuid4()),
        name="Jane Smith",
        license_number="DL654321",
        license_expiry=datetime(2024, 6, 30),
        vehicle_types=[VehicleType.TRUCK, VehicleType.TANKER],
        haulage_experience=[HaulageType.INTERSTATE, HaulageType.INTERNATIONAL],
        status=DriverStatus.AVAILABLE,
        location="Los Angeles",
        rating=4.8,
        phone="+1987654321"
    )
    
    system.add_driver(driver1)
    system.add_driver(driver2)
    
    # Create a haulage request
    request = HaulageRequest(
        id=str(uuid.uuid4()),
        origin="New York",
        destination="Boston",
        haulage_type=HaulageType.INTERSTATE,
        vehicle_type=VehicleType.TRUCK,
        required_drivers=1,
        start_date=datetime(2023, 10, 1),
        end_date=datetime(2023, 10, 3)
    )
    
    request_id = system.create_haulage_request(request)
    
    # Find matching drivers
    matches = system.find_matching_drivers(request_id)
    print(f"Found {len(matches)} matching drivers")
    
    if matches:
        # Assign the top-rated driver
        assignment_id = system.assign_driver(matches[0].id, request_id)
        print(f"Assigned driver {matches[0].name} to haulage")
        
        # Later, complete the assignment
        system.complete_assignment(assignment_id, rating=4.7)
        print("Assignment completed")
```
