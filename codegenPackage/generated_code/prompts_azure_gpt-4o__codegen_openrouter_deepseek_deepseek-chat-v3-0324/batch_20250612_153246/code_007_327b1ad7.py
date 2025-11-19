"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Write code to simulate bulk chiller transport logistics, including handling large shipments and maintaining temperature control, inspired by the solutions on RefrigeratorTransport.com.
Generated: DETERMINISTIC_327b1ad732aa9f28
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta
from enum import Enum
import logging
from typing import List, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TemperatureUnit(Enum):
    CELSIUS = "°C"
    FAHRENHEIT = "°F"

class ChillerStatus(Enum):
    OPERATIONAL = "Operational"
    MAINTENANCE_REQUIRED = "Maintenance Required"
    CRITICAL_FAILURE = "Critical Failure"

class TransportStatus(Enum):
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    DELAYED = "Delayed"
    CANCELLED = "Cancelled"

class ChillerUnit:
    def __init__(
        self,
        unit_id: str,
        capacity_liters: float,
        min_temp: float,
        max_temp: float,
        temp_unit: TemperatureUnit = TemperatureUnit.CELSIUS
    ):
        self.unit_id = unit_id
        self.capacity_liters = capacity_liters
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.temp_unit = temp_unit
        self.current_temp = max_temp
        self.status = ChillerStatus.OPERATIONAL
        self.last_maintenance = datetime.now()
        self.maintenance_interval = timedelta(days=30)

    def update_temperature(self, ambient_temp: float) -> None:
        """Update the chiller temperature based on ambient conditions."""
        if self.status != ChillerStatus.OPERATIONAL:
            return

        temp_change = (ambient_temp - self.current_temp) * 0.05
        self.current_temp += temp_change

        # Ensure temperature stays within bounds
        self.current_temp = max(self.min_temp, min(self.max_temp, self.current_temp))

    def check_maintenance(self) -> None:
        """Check if maintenance is required."""
        time_since_maintenance = datetime.now() - self.last_maintenance
        if time_since_maintenance > self.maintenance_interval:
            if random.random() < 0.3:  # 30% chance of critical failure if overdue
                self.status = ChillerStatus.CRITICAL_FAILURE
                logger.error(f"Chiller {self.unit_id} has critical failure!")
            else:
                self.status = ChillerStatus.MAINTENANCE_REQUIRED
                logger.warning(f"Chiller {self.unit_id} requires maintenance")

    def perform_maintenance(self) -> None:
        """Perform maintenance on the chiller."""
        self.status = ChillerStatus.OPERATIONAL
        self.last_maintenance = datetime.now()
        logger.info(f"Maintenance performed on chiller {self.unit_id}")

    def __str__(self) -> str:
        return (f"Chiller {self.unit_id}: {self.status.value}, "
                f"Temp: {self.current_temp:.1f}{self.temp_unit.value}, "
                f"Capacity: {self.capacity_liters}L")

class Shipment:
    def __init__(
        self,
        shipment_id: str,
        chillers: List[ChillerUnit],
        origin: str,
        destination: str,
        expected_duration_hours: float
    ):
        self.shipment_id = shipment_id
        self.chillers = chillers
        self.origin = origin
        self.destination = destination
        self.expected_duration = timedelta(hours=expected_duration_hours)
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
        self.status = TransportStatus.PENDING
        self.current_location = origin
        self.route_progress = 0.0  # 0 to 1
        self.temperature_log: List[Dict[str, float]] = []

    def start_transport(self) -> None:
        """Start the shipment transport."""
        if self.status != TransportStatus.PENDING:
            raise ValueError("Shipment can only start from PENDING status")
        
        self.start_time = datetime.now()
        self.status = TransportStatus.IN_TRANSIT
        logger.info(f"Shipment {self.shipment_id} started from {self.origin} to {self.destination}")

    def update_transport(self, time_elapsed: timedelta, ambient_temp: float) -> None:
        """Update the shipment progress and chiller status."""
        if self.status != TransportStatus.IN_TRANSIT:
            return

        # Update route progress
        total_time = (datetime.now() - self.start_time).total_seconds()
        expected_seconds = self.expected_duration.total_seconds()
        self.route_progress = min(1.0, total_time / expected_seconds)

        # Random chance of delay
        if random.random() < 0.05:  # 5% chance of delay
            self.status = TransportStatus.DELAYED
            logger.warning(f"Shipment {self.shipment_id} delayed!")
            return

        # Update chiller temperatures
        temp_readings = {}
        for chiller in self.chillers:
            chiller.update_temperature(ambient_temp)
            chiller.check_maintenance()
            temp_readings[chiller.unit_id] = chiller.current_temp

            if chiller.status == ChillerStatus.CRITICAL_FAILURE:
                self.status = TransportStatus.DELAYED
                logger.error(f"Shipment {self.shipment_id} delayed due to chiller {chiller.unit_id} failure")

        self.temperature_log.append({
            "timestamp": datetime.now().isoformat(),
            "temperatures": temp_readings,
            "ambient_temp": ambient_temp
        })

        # Update location based on progress
        if self.route_progress < 0.33:
            self.current_location = f"En route from {self.origin}"
        elif self.route_progress < 0.66:
            self.current_location = "Mid-transit"
        else:
            self.current_location = f"Approaching {self.destination}"

        # Check if shipment is complete
        if self.route_progress >= 1.0:
            self.complete_transport()

    def complete_transport(self) -> None:
        """Mark the shipment as delivered."""
        self.status = TransportStatus.DELIVERED
        self.end_time = datetime.now()
        self.current_location = self.destination
        logger.info(f"Shipment {self.shipment_id} delivered to {self.destination}")

    def get_status_report(self) -> Dict:
        """Generate a status report for the shipment."""
        return {
            "shipment_id": self.shipment_id,
            "status": self.status.value,
            "current_location": self.current_location,
            "progress": f"{self.route_progress * 100:.1f}%",
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "estimated_completion": (
                (self.start_time + self.expected_duration).isoformat()
                if self.start_time else None
            ),
            "chillers": [str(chiller) for chiller in self.chillers]
        }

class TransportSimulator:
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}
        self.ambient_temps: List[Tuple[float, float]] = [
            (5, 15),   # Early morning
            (15, 25),  # Daytime
            (10, 20)   # Evening
        ]

    def create_shipment(
        self,
        origin: str,
        destination: str,
        distance_km: float,
        num_chillers: int = 3
    ) -> Shipment:
        """Create a new shipment with chillers."""
        shipment_id = f"SH{random.randint(1000, 9999)}"
        avg_speed_kmh = random.uniform(60, 80)
        expected_hours = distance_km / avg_speed_kmh

        chillers = []
        for i in range(num_chillers):
            capacity = random.choice([1000, 2000, 3000])
            min_temp = random.choice([-20, -15, -10])
            max_temp = random.choice([0, 2, 5])
            chiller = ChillerUnit(
                unit_id=f"{shipment_id}-CH{i+1}",
                capacity_liters=capacity,
                min_temp=min_temp,
                max_temp=max_temp
            )
            chillers.append(chiller)

        shipment = Shipment(
            shipment_id=shipment_id,
            chillers=chillers,
            origin=origin,
            destination=destination,
            expected_duration_hours=expected_hours
        )
        self.shipments[shipment_id] = shipment
        return shipment

    def simulate_time_progress(self, hours: float = 1.0) -> None:
        """Simulate the passage of time for all shipments."""
        time_elapsed = timedelta(hours=hours)
        current_hour =
