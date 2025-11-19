"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Write code to simulate temperature-controlled shipment logistics, ensuring optimal conditions for sensitive cargo as outlined by Calmar Transport.
Generated: DETERMINISTIC_c9854324ebd5757b
Batch ID: 20250612_152405
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
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CargoType(Enum):
    PHARMACEUTICAL = auto()
    FOOD = auto()
    CHEMICAL = auto()
    ELECTRONICS = auto()

class AlertLevel(Enum):
    INFO = auto()
    WARNING = auto()
    CRITICAL = auto()

@dataclass
class TemperatureRange:
    min_temp: float
    max_temp: float

@dataclass
class Alert:
    timestamp: datetime
    message: str
    level: AlertLevel
    shipment_id: str

@dataclass
class Shipment:
    shipment_id: str
    cargo_type: CargoType
    origin: str
    destination: str
    current_temp: float
    optimal_range: TemperatureRange
    start_time: datetime
    estimated_duration: timedelta
    alerts: List[Alert]
    is_active: bool = True

    def check_temperature(self) -> Optional[Alert]:
        if not self.is_active:
            return None
            
        if self.current_temp < self.optimal_range.min_temp:
            alert = Alert(
                timestamp=datetime.now(),
                message=f"Temperature too low: {self.current_temp}°C (min: {self.optimal_range.min_temp}°C)",
                level=AlertLevel.CRITICAL,
                shipment_id=self.shipment_id
            )
            self.alerts.append(alert)
            return alert
        
        elif self.current_temp > self.optimal_range.max_temp:
            alert = Alert(
                timestamp=datetime.now(),
                message=f"Temperature too high: {self.current_temp}°C (max: {self.optimal_range.max_temp}°C)",
                level=AlertLevel.CRITICAL,
                shipment_id=self.shipment_id
            )
            self.alerts.append(alert)
            return alert
        
        return None

    def update_temperature(self, new_temp: float) -> Optional[Alert]:
        self.current_temp = new_temp
        return self.check_temperature()

    def complete_shipment(self):
        self.is_active = False
        logger.info(f"Shipment {self.shipment_id} completed")

class TemperatureController:
    def __init__(self):
        self.shipments: List[Shipment] = []
        self.alert_handlers = []

    def register_alert_handler(self, handler):
        self.alert_handlers.append(handler)

    def create_shipment(
        self,
        cargo_type: CargoType,
        origin: str,
        destination: str,
        initial_temp: float,
        optimal_range: TemperatureRange,
        estimated_duration: timedelta
    ) -> Shipment:
        shipment_id = f"SH{random.randint(10000, 99999)}"
        shipment = Shipment(
            shipment_id=shipment_id,
            cargo_type=cargo_type,
            origin=origin,
            destination=destination,
            current_temp=initial_temp,
            optimal_range=optimal_range,
            start_time=datetime.now(),
            estimated_duration=estimated_duration,
            alerts=[]
        )
        self.shipments.append(shipment)
        logger.info(f"Created shipment {shipment_id} ({cargo_type.name})")
        return shipment

    def simulate_temperature_change(self, shipment: Shipment):
        if not shipment.is_active:
            return

        temp_change = random.uniform(-2.0, 2.0)
        new_temp = shipment.current_temp + temp_change
        alert = shipment.update_temperature(new_temp)
        
        if alert:
            self._handle_alert(alert)

    def _handle_alert(self, alert: Alert):
        for handler in self.alert_handlers:
            handler(alert)
        logger.log(
            logging.WARNING if alert.level == AlertLevel.WARNING else logging.CRITICAL,
            f"ALERT [{alert.level.name}] for {alert.shipment_id}: {alert.message}"
        )

    def monitor_shipments(self, interval_seconds: int = 5, duration_minutes: int = 10):
        end_time = datetime.now() + timedelta(minutes=duration_minutes)
        
        while datetime.now() < end_time:
            for shipment in self.shipments:
                if shipment.is_active:
                    self.simulate_temperature_change(shipment)
            
            time.sleep(interval_seconds)

def console_alert_handler(alert: Alert):
    print(f"[{alert.timestamp}] {alert.level.name}: {alert.message}")

def main():
    controller = TemperatureController()
    controller.register_alert_handler(console_alert_handler)

    # Define optimal temperature ranges for different cargo types
    cargo_ranges = {
        CargoType.PHARMACEUTICAL: TemperatureRange(2.0, 8.0),
        CargoType.FOOD: TemperatureRange(-18.0, -15.0),
        CargoType.CHEMICAL: TemperatureRange(15.0, 25.0),
        CargoType.ELECTRONICS: TemperatureRange(10.0, 30.0)
    }

    # Create sample shipments
    shipments = [
        controller.create_shipment(
            cargo_type=CargoType.PHARMACEUTICAL,
            origin="New York",
            destination="Los Angeles",
            initial_temp=5.0,
            optimal_range=cargo_ranges[CargoType.PHARMACEUTICAL],
            estimated_duration=timedelta(hours=48)
        ),
        controller.create_shipment(
            cargo_type=CargoType.FOOD,
            origin="Chicago",
            destination="Miami",
            initial_temp=-16.0,
            optimal_range=cargo_ranges[CargoType.FOOD],
            estimated_duration=timedelta(hours=36)
        )
    ]

    # Start monitoring
    controller.monitor_shipments(duration_minutes=2)

    # Complete shipments
    for shipment in shipments:
        shipment.complete_shipment()

if __name__ == "__main__":
    main()
```
