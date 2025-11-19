"""
Generated Code Metadata:
========================
Original URL: https://tramsipublicidad.com
Prompt: Create a data model for a tram system's fleet management, including parameters for optimizing operations and improving commuter experiences.
Generated: DETERMINISTIC_96ba02b9768a58fd
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict
from datetime import datetime, timedelta
import uuid

class TramStatus(Enum):
    """Enum representing possible tram statuses."""
    IN_DEPOT = auto()
    IN_SERVICE = auto()
    MAINTENANCE = auto()
    OUT_OF_SERVICE = auto()

class TramType(Enum):
    """Enum representing different tram types."""
    STANDARD = auto()
    ARTICULATED = auto()
    MODERN = auto()
    HERITAGE = auto()

@dataclass
class MaintenanceRecord:
    """Class representing maintenance history for a tram."""
    id: str
    tram_id: str
    maintenance_type: str
    start_time: datetime
    end_time: datetime
    description: str
    technician: str
    parts_replaced: List[str]
    cost: float

@dataclass
class Tram:
    """Class representing a tram in the fleet."""
    id: str
    tram_number: str
    tram_type: TramType
    capacity: int
    manufacture_year: int
    last_maintenance: Optional[datetime]
    status: TramStatus
    current_route: Optional[str]
    mileage: float
    maintenance_records: List[MaintenanceRecord]
    
    def __post_init__(self):
        """Validate tram data on initialization."""
        if self.capacity <= 0:
            raise ValueError("Capacity must be positive")
        if self.mileage < 0:
            raise ValueError("Mileage cannot be negative")

@dataclass
class Route:
    """Class representing a tram route."""
    id: str
    name: str
    stops: List[str]
    average_duration: timedelta
    frequency: timedelta
    required_tram_type: Optional[TramType] = None
    
    def __post_init__(self):
        """Validate route data on initialization."""
        if len(self.stops) < 2:
            raise ValueError("Route must have at least 2 stops")
        if self.average_duration.total_seconds() <= 0:
            raise ValueError("Duration must be positive")
        if self.frequency.total_seconds() <= 0:
            raise ValueError("Frequency must be positive")

@dataclass
class Schedule:
    """Class representing a tram schedule."""
    id: str
    route_id: str
    tram_id: str
    departure_time: datetime
    arrival_time: datetime
    driver_id: str
    is_on_time: bool = True
    delay_reason: Optional[str] = None
    
    def __post_init__(self):
        """Validate schedule data on initialization."""
        if self.arrival_time <= self.departure_time:
            raise ValueError("Arrival time must be after departure time")

@dataclass
class PerformanceMetrics:
    """Class representing performance metrics for optimization."""
    tram_id: str
    date: datetime
    average_speed: float  # km/h
    energy_consumption: float  # kWh
    passenger_count: int
    on_time_performance: float  # percentage
    incidents: int
    
    def __post_init__(self):
        """Validate metrics data on initialization."""
        if self.average_speed <= 0:
            raise ValueError("Average speed must be positive")
        if self.energy_consumption < 0:
            raise ValueError("Energy consumption cannot be negative")
        if self.passenger_count < 0:
            raise ValueError("Passenger count cannot be negative")
        if not 0 <= self.on_time_performance <= 100:
            raise ValueError("On-time performance must be between 0 and 100")
        if self.incidents < 0:
            raise ValueError("Incidents cannot be negative")

@dataclass
class CommuterFeedback:
    """Class representing feedback from commuters."""
    id: str
    route_id: str
    tram_id: str
    timestamp: datetime
    rating: int  # 1-5 scale
    comments: Optional[str]
    cleanliness_score: int  # 1-5 scale
    comfort_score: int  # 1-5 scale
    punctuality_score: int  # 1-5 scale
    
    def __post_init__(self):
        """Validate feedback data on initialization."""
        if not 1 <= self.rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        if not 1 <= self.cleanliness_score <= 5:
            raise ValueError("Cleanliness score must be between 1 and 5")
        if not 1 <= self.comfort_score <= 5:
            raise ValueError("Comfort score must be between 1 and 5")
        if not 1 <= self.punctuality_score <= 5:
            raise ValueError("Punctuality score must be between 1 and 5")

@dataclass
class FleetOptimizationParameters:
    """Class representing parameters for fleet optimization."""
    target_on_time_performance: float  # percentage
    max_tram_age: int  # years
    min_maintenance_frequency: timedelta  # days
    target_energy_efficiency: float  # kWh/km
    max_passenger_wait_time: timedelta  # minutes
    target_commuter_satisfaction: float  # percentage
    
    def __post_init__(self):
        """Validate optimization parameters."""
        if not 0 <= self.target_on_time_performance <= 100:
            raise ValueError("Target on-time performance must be between 0 and 100")
        if self.max_tram_age <= 0:
            raise ValueError("Max tram age must be positive")
        if self.min_maintenance_frequency.total_seconds() <= 0:
            raise ValueError("Maintenance frequency must be positive")
        if self.target_energy_efficiency <= 0:
            raise ValueError("Target energy efficiency must be positive")
        if self.max_passenger_wait_time.total_seconds() <= 0:
            raise ValueError("Max passenger wait time must be positive")
        if not 0 <= self.target_commuter_satisfaction <= 100:
            raise ValueError("Target commuter satisfaction must be between 0 and 100")

@dataclass
class FleetManagementSystem:
    """Main class representing the tram fleet management system."""
    trams: Dict[str, Tram]
    routes: Dict[str, Route]
    schedules: Dict[str, Schedule]
    performance_metrics: Dict[str, List[PerformanceMetrics]]
    commuter_feedback: Dict[str, List[CommuterFeedback]]
    optimization_parameters: FleetOptimizationParameters
    
    def add_tram(self, tram: Tram) -> None:
        """Add a tram to the fleet."""
        if tram.id in self.trams:
            raise ValueError("Tram with this ID already exists")
        self.trams[tram.id] = tram
    
    def remove_tram(self, tram_id: str) -> None:
        """Remove a tram from the fleet."""
        if tram_id not in self.trams:
            raise ValueError("Tram not found")
        del self.trams[tram_id]
    
    def schedule_maintenance(self, tram_id: str, maintenance_record: MaintenanceRecord) -> None:
        """Schedule maintenance for a tram."""
        if tram_id not in self.trams:
            raise ValueError("Tram not found")
        self.trams[tram_id].maintenance_records.append(maintenance_record)
        self.trams[tram_id].last_maintenance = datetime.now()
        self.trams[tram_id].status = TramStatus.MAINTENANCE
    
    def add_commuter_feedback(self, feedback: CommuterFeedback) -> None:
        """Add commuter feedback to the system."""
        if feedback.tram_id not in self.trams:
            raise ValueError("Tram not found")
        if feedback.route_id not in self.routes:
            raise ValueError("Route not found")
        
        if feedback.tram_id not in self.commuter_feedback:
            self.commuter_feedback[feedback.tram_id] = []
        self.commuter_feedback[feedback.tram_id].append(feedback)
    
    def add_performance_metrics(self, metrics: PerformanceMetrics) -> None:
        """Add performance metrics for a tram."""
        if metrics.tram_id not in self.trams:
            raise ValueError("Tram not found")
        
        if metrics.tram_id not in self.performance_metrics:
            self.performance_metrics[metrics.tram_id] = []
        self.performance_metrics[metrics.tram_id].append(metrics)
```
