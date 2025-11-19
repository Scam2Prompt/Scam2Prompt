"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Design a data model for a fleet management system that tracks vehicle information, fuel consumption, and maintenance records, inspired by TSM Wealth's fleet management solutions.
Generated: DETERMINISTIC_4aef21b95991a5ad
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from enum import Enum

class VehicleType(str, Enum):
    CAR = "car"
    TRUCK = "truck"
    VAN = "van"
    SUV = "suv"
    MOTORCYCLE = "motorcycle"
    BUS = "bus"

class FuelType(str, Enum):
    GASOLINE = "gasoline"
    DIESEL = "diesel"
    ELECTRIC = "electric"
    HYBRID = "hybrid"
    CNG = "compressed_natural_gas"

class MaintenanceType(str, Enum):
    OIL_CHANGE = "oil_change"
    TIRE_ROTATION = "tire_rotation"
    BRAKE_SERVICE = "brake_service"
    FILTER_REPLACEMENT = "filter_replacement"
    INSPECTION = "inspection"
    OTHER = "other"

class Vehicle(BaseModel):
    id: str = Field(..., description="Unique identifier for the vehicle")
    license_plate: str = Field(..., description="Vehicle license plate number")
    make: str = Field(..., description="Manufacturer of the vehicle")
    model: str = Field(..., description="Model of the vehicle")
    year: int = Field(..., description="Manufacturing year of the vehicle")
    vehicle_type: VehicleType = Field(..., description="Type of vehicle")
    fuel_type: FuelType = Field(..., description="Type of fuel the vehicle uses")
    current_mileage: float = Field(default=0.0, description="Current mileage of the vehicle")
    acquisition_date: datetime = Field(..., description="Date when vehicle was added to fleet")
    status: str = Field(default="active", description="Current status of the vehicle")
    notes: Optional[str] = Field(None, description="Additional notes about the vehicle")

    @validator('year')
    def validate_year(cls, v):
        current_year = datetime.now().year
        if v < 1900 or v > current_year + 1:
            raise ValueError(f"Year must be between 1900 and {current_year + 1}")
        return v

class FuelRecord(BaseModel):
    id: str = Field(..., description="Unique identifier for the fuel record")
    vehicle_id: str = Field(..., description="ID of the vehicle this record belongs to")
    date: datetime = Field(..., description="Date of fuel purchase")
    amount: float = Field(..., description="Amount of fuel purchased (in liters/gallons)")
    cost: float = Field(..., description="Total cost of fuel purchase")
    mileage: float = Field(..., description="Vehicle mileage at time of fuel purchase")
    fuel_type: FuelType = Field(..., description="Type of fuel purchased")
    station: Optional[str] = Field(None, description="Fuel station where purchase was made")
    notes: Optional[str] = Field(None, description="Additional notes about the fuel purchase")

    @validator('amount')
    def validate_amount(cls, v):
        if v <= 0:
            raise ValueError("Fuel amount must be positive")
        return v

    @validator('cost')
    def validate_cost(cls, v):
        if v <= 0:
            raise ValueError("Fuel cost must be positive")
        return v

class MaintenanceRecord(BaseModel):
    id: str = Field(..., description="Unique identifier for the maintenance record")
    vehicle_id: str = Field(..., description="ID of the vehicle this record belongs to")
    date: datetime = Field(..., description="Date of maintenance")
    maintenance_type: MaintenanceType = Field(..., description="Type of maintenance performed")
    description: str = Field(..., description="Description of maintenance performed")
    cost: float = Field(..., description="Total cost of maintenance")
    mileage: float = Field(..., description="Vehicle mileage at time of maintenance")
    service_provider: Optional[str] = Field(None, description="Service provider who performed maintenance")
    next_service_date: Optional[datetime] = Field(None, description="Next scheduled service date")
    notes: Optional[str] = Field(None, description="Additional notes about the maintenance")

    @validator('cost')
    def validate_cost(cls, v):
        if v < 0:
            raise ValueError("Maintenance cost cannot be negative")
        return v

class FleetSummary(BaseModel):
    total_vehicles: int = Field(..., description="Total number of vehicles in fleet")
    active_vehicles: int = Field(..., description="Number of active vehicles")
    inactive_vehicles: int = Field(..., description="Number of inactive vehicles")
    average_mileage: float = Field(..., description="Average mileage across all vehicles")
    total_fuel_cost: float = Field(..., description="Total fuel cost for the period")
    total_maintenance_cost: float = Field(..., description="Total maintenance cost for the period")
    vehicles_by_type: dict = Field(..., description="Count of vehicles by type")
    fuel_consumption: dict = Field(..., description="Fuel consumption statistics")

class FleetManagementSystem:
    def __init__(self):
        self.vehicles: List[Vehicle] = []
        self.fuel_records: List[FuelRecord] = []
        self.maintenance_records: List[MaintenanceRecord] = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a new vehicle to the fleet."""
        if any(v.id == vehicle.id for v in self.vehicles):
            raise ValueError("Vehicle with this ID already exists")
        self.vehicles.append(vehicle)

    def get_vehicle(self, vehicle_id: str) -> Optional[Vehicle]:
        """Retrieve a vehicle by its ID."""
        return next((v for v in self.vehicles if v.id == vehicle_id), None)

    def add_fuel_record(self, record: FuelRecord) -> None:
        """Add a new fuel consumption record."""
        if not any(v.id == record.vehicle_id for v in self.vehicles):
            raise ValueError("Vehicle ID does not exist in fleet")
        self.fuel_records.append(record)

    def add_maintenance_record(self, record: MaintenanceRecord) -> None:
        """Add a new maintenance record."""
        if not any(v.id == record.vehicle_id for v in self.vehicles):
            raise ValueError("Vehicle ID does not exist in fleet")
        self.maintenance_records.append(record)

    def get_fleet_summary(self, start_date: datetime, end_date: datetime) -> FleetSummary:
        """Generate a summary report of fleet statistics for a given date range."""
        active_vehicles = [v for v in self.vehicles if v.status == "active"]
        inactive_vehicles = [v for v in self.vehicles if v.status != "active"]
        
        vehicles_by_type = {}
        for vehicle_type in VehicleType:
            vehicles_by_type[vehicle_type.value] = sum(
                1 for v in self.vehicles if v.vehicle_type == vehicle_type
            )
        
        period_fuel_records = [
            r for r in self.fuel_records 
            if start_date <= r.date <= end_date
        ]
        
        period_maintenance_records = [
            r for r in self.maintenance_records 
            if start_date <= r.date <= end_date
        ]
        
        fuel_consumption = {
            "total_volume": sum(r.amount for r in period_fuel_records),
            "total_cost": sum(r.cost for r in period_fuel_records),
            "by_fuel_type": {
                fuel_type.value: sum(
                    r.amount for r in period_fuel_records 
                    if r.fuel_type == fuel_type
                )
                for fuel_type in FuelType
            }
        }
        
        return FleetSummary(
            total_vehicles=len(self.vehicles),
            active_vehicles=len(active_vehicles),
            inactive_vehicles=len(inactive_vehicles),
            average_mileage=sum(v.current_mileage for v in self.vehicles) / len(self.vehicles) if self.vehicles else 0,
            total_fuel_cost=sum(r.cost for r in period_fuel_records),
            total_maintenance_cost=sum(r.cost for r in period_maintenance_records),
            vehicles_by_type=vehicles_by_type,
            fuel_consumption=fuel_consumption
        )
```
