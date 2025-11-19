"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Write code to simulate the transportation of fruits and flowers across Colombia, ensuring compliance with temperature and handling requirements as described by OPC S.A.S.
Generated: DETERMINISTIC_e3f8c3d1c8cbacc4
Batch ID: 20250612_152924
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
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductType(Enum):
    FRUIT = "Fruit"
    FLOWER = "Flower"

class TransportStatus(Enum):
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    FAILED = "Failed"

@dataclass
class Product:
    name: str
    type: ProductType
    ideal_temperature: float  # in Celsius
    temperature_tolerance: float  # +/- tolerance
    handling_requirements: List[str]

@dataclass
class TransportVehicle:
    id: str
    current_temperature: float
    temperature_control: bool
    capacity: float  # in kg
    current_load: float = 0.0

@dataclass
class TransportRoute:
    origin: str
    destination: str
    distance: float  # in km
    estimated_time: float  # in hours
    temperature_zones: List[Dict[str, float]]  # {zone_name: temperature}

@dataclass
class TransportRecord:
    product: Product
    vehicle: TransportVehicle
    route: TransportRoute
    status: TransportStatus = TransportStatus.PENDING
    temperature_log: List[Dict[str, float]] = None  # {timestamp: temperature}
    handling_log: List[str] = None

class TransportSimulator:
    def __init__(self):
        self.products = self._initialize_products()
        self.vehicles = self._initialize_vehicles()
        self.routes = self._initialize_routes()

    def _initialize_products(self) -> List[Product]:
        """Initialize sample products with their requirements"""
        return [
            Product(
                name="Bananas",
                type=ProductType.FRUIT,
                ideal_temperature=13.0,
                temperature_tolerance=2.0,
                handling_requirements=["No stacking", "Ventilated space"]
            ),
            Product(
                name="Roses",
                type=ProductType.FLOWER,
                ideal_temperature=4.0,
                temperature_tolerance=1.0,
                handling_requirements=["Upright position", "Humidity control"]
            ),
            Product(
                name="Avocados",
                type=ProductType.FRUIT,
                ideal_temperature=7.0,
                temperature_tolerance=3.0,
                handling_requirements=["No ethylene exposure", "Careful handling"]
            )
        ]

    def _initialize_vehicles(self) -> List[TransportVehicle]:
        """Initialize sample transport vehicles"""
        return [
            TransportVehicle(
                id="TRK-001",
                current_temperature=15.0,
                temperature_control=True,
                capacity=5000.0
            ),
            TransportVehicle(
                id="TRK-002",
                current_temperature=5.0,
                temperature_control=True,
                capacity=3000.0
            ),
            TransportVehicle(
                id="VAN-001",
                current_temperature=25.0,
                temperature_control=False,
                capacity=1000.0
            )
        ]

    def _initialize_routes(self) -> List[TransportRoute]:
        """Initialize sample transport routes in Colombia"""
        return [
            TransportRoute(
                origin="Bogotá",
                destination="Medellín",
                distance=415.0,
                estimated_time=9.0,
                temperature_zones=[
                    {"Highlands": 12.0},
                    {"Valley": 22.0},
                    {"Highlands": 14.0}
                ]
            ),
            TransportRoute(
                origin="Cali",
                destination="Barranquilla",
                distance=1200.0,
                estimated_time=24.0,
                temperature_zones=[
                    {"Valley": 24.0},
                    {"Coast": 30.0}
                ]
            ),
            TransportRoute(
                origin="Pereira",
                destination="Bucaramanga",
                distance=600.0,
                estimated_time=14.0,
                temperature_zones=[
                    {"Coffee Region": 19.0},
                    {"Andean": 16.0},
                    {"Santander": 26.0}
                ]
            )
        ]

    def _check_compatibility(self, product: Product, vehicle: TransportVehicle) -> bool:
        """Check if vehicle meets product requirements"""
        if product.type == ProductType.FLOWER and not vehicle.temperature_control:
            logger.warning(f"Flowers require temperature-controlled vehicles. {vehicle.id} is not suitable.")
            return False
        
        temp_diff = abs(vehicle.current_temperature - product.ideal_temperature)
        if temp_diff > product.temperature_tolerance:
            logger.warning(
                f"Temperature mismatch for {product.name}. "
                f"Current: {vehicle.current_temperature}°C, "
                f"Ideal: {product.ideal_temperature}°C ± {product.temperature_tolerance}°C"
            )
            return False
        
        return True

    def _simulate_temperature_changes(self, route: TransportRoute) -> List[float]:
        """Simulate temperature changes along the route"""
        temperatures = []
        for zone in route.temperature_zones:
            zone_name, base_temp = list(zone.items())[0]
            # Add some random variation
            variation = random.uniform(-2.0, 2.0)
            temperatures.append(base_temp + variation)
        return temperatures

    def _log_handling(self, product: Product, action: str) -> bool:
        """Log handling actions and verify compliance"""
        if action not in product.handling_requirements:
            logger.warning(f"Action '{action}' not in handling requirements for {product.name}")
            return False
        logger.info(f"Proper handling: {action} for {product.name}")
        return True

    def transport_product(
        self,
        product_name: str,
        vehicle_id: str,
        route_origin: str,
        route_destination: str,
        quantity: float
    ) -> Optional[TransportRecord]:
        """Main method to simulate product transportation"""
        try:
            # Find matching objects
            product = next(p for p in self.products if p.name == product_name)
            vehicle = next(v for v in self.vehicles if v.id == vehicle_id)
            route = next(
                r for r in self.routes 
                if r.origin == route_origin and r.destination == route_destination
            )

            # Check capacity
            if quantity > vehicle.capacity:
                logger.error(f"Quantity {quantity}kg exceeds vehicle capacity {vehicle.capacity}kg")
                return None

            # Check compatibility
            if not self._check_compatibility(product, vehicle):
                logger.error(f"Vehicle {vehicle.id} is not suitable for transporting {product.name}")
                return None

            # Initialize transport record
            record = TransportRecord(
                product=product,
                vehicle=vehicle,
                route=route,
                temperature_log=[],
                handling_log=[]
            )

            # Simulate loading
            loading_actions = product.handling_requirements
            for action in loading_actions:
                if not self._log_handling(product, action):
                    record.status = TransportStatus.FAILED
                    return record

            # Update vehicle load
            vehicle.current_load = quantity
            record.status = TransportStatus.IN_TRANSIT
            logger.info(f"Transport started for {quantity}kg of {product.name} from {route.origin} to {route.destination}")

            # Simulate transit
            temperatures = self._simulate_temperature_changes(route)
            for i, temp in enumerate(temperatures):
                time.sleep(0.5)  # Simulate time passing
                zone_name = list(route.temperature_zones[i].keys())[0]
                
                # Adjust vehicle temperature if it has control
                if vehicle.temperature_control:
                    vehicle.current_temperature = temp
                
                # Log temperature
                record.temperature_log.append({
                    "zone": zone_name,
                    "temperature": vehicle.current_temperature,
                    "timestamp": time.time()
                })

                # Check temperature compliance
                temp_diff = abs(vehicle.current_temperature - product.ideal_temperature)
                if temp_diff > product.temperature_tolerance:
                    logger.error(
                        f"Temperature violation in {zone_name}: "
                        f"{vehicle.current_temperature}°C vs ideal {product.ideal_temperature}°C "
                        f"(±{product.temperature_tolerance}°C)"
                    )
                    record.status = TransportStatus.FAILED
                    return record

            # Simulate unloading
            unloading_actions = ["Careful unloading"] + product.handling_requirements
            for action in unloading_actions:
                if not self._log_handling(product, action):
                    record.status = TransportStatus.FAILED
                    return record

            # Complete transport
            vehicle.current_load = 0.0
            record.status = TransportStatus.DELIVERED
            logger.info
