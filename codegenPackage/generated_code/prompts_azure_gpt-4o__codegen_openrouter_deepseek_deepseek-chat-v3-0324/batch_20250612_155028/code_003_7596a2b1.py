"""
Generated Code Metadata:
========================
Original URL: https://stelllar.org
Prompt: Create a program to optimize freight management across multiple carriers and schedules, inspired by Stelllar Logistics' coordinated shipping approach.
Generated: DETERMINISTIC_7596a2b12187d28a
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass(order=True)
class Shipment:
    """Represents a shipment with its properties."""
    id: str
    origin: str
    destination: str
    weight: float  # in kg
    volume: float  # in cubic meters
    earliest_pickup: datetime
    latest_delivery: datetime
    priority: int = field(default=1, compare=False)  # 1-5 scale (1 highest)

@dataclass
class Carrier:
    """Represents a carrier with their capabilities."""
    id: str
    name: str
    supported_routes: List[str]  # List of route codes (e.g., "NYC-LAX")
    max_weight: float  # in kg
    max_volume: float  # in cubic meters
    cost_per_kg: float
    cost_per_volume: float
    transit_times: Dict[str, int]  # Route code to days
    reliability: float  # 0-1 scale

@dataclass
class Route:
    """Represents a shipping route between two locations."""
    code: str  # e.g., "NYC-LAX"
    origin: str
    destination: str
    distance: float  # in km
    available_carriers: List[str]  # List of carrier IDs

class FreightOptimizer:
    """Optimizes freight management across multiple carriers and schedules."""
    
    def __init__(self):
        self.carriers: Dict[str, Carrier] = {}
        self.routes: Dict[str, Route] = {}
        self.shipments: Dict[str, Shipment] = {}
        
    def add_carrier(self, carrier: Carrier) -> None:
        """Add a carrier to the system."""
        if carrier.id in self.carriers:
            logger.warning(f"Carrier {carrier.id} already exists. Overwriting.")
        self.carriers[carrier.id] = carrier
        logger.info(f"Added carrier: {carrier.name} ({carrier.id})")
        
    def add_route(self, route: Route) -> None:
        """Add a route to the system."""
        if route.code in self.routes:
            logger.warning(f"Route {route.code} already exists. Overwriting.")
        self.routes[route.code] = route
        logger.info(f"Added route: {route.origin} -> {route.destination} ({route.code})")
        
    def add_shipment(self, shipment: Shipment) -> None:
        """Add a shipment to be optimized."""
        if shipment.id in self.shipments:
            logger.warning(f"Shipment {shipment.id} already exists. Overwriting.")
        self.shipments[shipment.id] = shipment
        logger.info(f"Added shipment: {shipment.id} ({shipment.origin} -> {shipment.destination})")
        
    def find_route(self, origin: str, destination: str) -> Optional[Route]:
        """Find a route between origin and destination."""
        route_code = f"{origin}-{destination}"
        return self.routes.get(route_code)
    
    def get_compatible_carriers(self, shipment: Shipment) -> List[Carrier]:
        """Get carriers that can handle the shipment based on route, weight, and volume."""
        route = self.find_route(shipment.origin, shipment.destination)
        if not route:
            return []
            
        compatible = []
        for carrier_id in route.available_carriers:
            carrier = self.carriers.get(carrier_id)
            if (carrier and 
                shipment.weight <= carrier.max_weight and 
                shipment.volume <= carrier.max_volume and
                route.code in carrier.supported_routes):
                compatible.append(carrier)
                
        return compatible
    
    def calculate_cost(self, carrier: Carrier, shipment: Shipment) -> float:
        """Calculate the cost of shipping with a given carrier."""
        route_code = f"{shipment.origin}-{shipment.destination}"
        weight_cost = shipment.weight * carrier.cost_per_kg
        volume_cost = shipment.volume * carrier.cost_per_volume
        return weight_cost + volume_cost
    
    def calculate_delivery_date(self, carrier: Carrier, shipment: Shipment) -> datetime:
        """Calculate the estimated delivery date."""
        route_code = f"{shipment.origin}-{shipment.destination}"
        transit_days = carrier.transit_times.get(route_code, 0)
        return shipment.earliest_pickup + timedelta(days=transit_days)
    
    def optimize_shipment(self, shipment_id: str) -> Dict:
        """Find the optimal carrier for a shipment based on cost, reliability, and delivery time."""
        shipment = self.shipments.get(shipment_id)
        if not shipment:
            logger.error(f"Shipment {shipment_id} not found.")
            return {}
            
        compatible_carriers = self.get_compatible_carriers(shipment)
        if not compatible_carriers:
            logger.error(f"No compatible carriers found for shipment {shipment_id}.")
            return {}
            
        options = []
        for carrier in compatible_carriers:
            cost = self.calculate_cost(carrier, shipment)
            delivery_date = self.calculate_delivery_date(carrier, shipment)
            reliability_score = carrier.reliability * 100
            
            # Check if delivery meets the deadline
            meets_deadline = delivery_date <= shipment.latest_delivery
            
            # Score based on cost, reliability, and delivery time
            score = (0.5 * (1 / cost) + 0.3 * reliability_score + 
                    0.2 * (1 if meets_deadline else 0.5))
            
            options.append({
                'carrier_id': carrier.id,
                'carrier_name': carrier.name,
                'cost': cost,
                'estimated_delivery': delivery_date,
                'reliability': reliability_score,
                'meets_deadline': meets_deadline,
                'score': score
            })
        
        # Sort by score (descending) and cost (ascending)
        options.sort(key=lambda x: (-x['score'], x['cost']))
        
        if options:
            best_option = options[0]
            logger.info(f"Best option for shipment {shipment_id}: {best_option['carrier_name']}")
            return best_option
        else:
            logger.error(f"No valid options found for shipment {shipment_id}.")
            return {}
    
    def optimize_all_shipments(self) -> Dict[str, Dict]:
        """Optimize all shipments in the system."""
        results = {}
        for shipment_id in self.shipments:
            results[shipment_id] = self.optimize_shipment(shipment_id)
        return results
    
    def save_to_json(self, filename: str) -> None:
        """Save the current state to a JSON file."""
        data = {
            'carriers': [vars(carrier) for carrier in self.carriers.values()],
            'routes': [vars(route) for route in self.routes.values()],
            'shipments': [vars(shipment) for shipment in self.shipments.values()]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, default=str, indent=2)
            logger.info(f"Data saved to {filename}")
        except Exception as e:
            logger.error(f"Failed to save data: {e}")
    
    def load_from_json(self, filename: str) -> None:
        """Load data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.carriers = {}
            for carrier_data in data.get('carriers', []):
                # Convert string dates back to datetime objects
                carrier = Carrier(**carrier_data)
                self.add_carrier(carrier)
                
            self.routes = {}
            for route_data in data.get('routes', []):
                route = Route(**route_data)
                self.add_route(route)
                
            self.shipments = {}
            for shipment_data in data.get('shipments', []):
                # Convert string dates back to datetime objects
                shipment_data['earliest_pickup'] = datetime.fromisoformat(shipment_data['earliest_pickup'])
                shipment_data['latest_delivery'] = datetime.fromisoformat(shipment_data['latest_delivery'])
                shipment = Shipment(**shipment_data)
                self.add_shipment(shipment)
                
            logger.info(f"Data loaded from {filename}")
        except Exception as e:
            logger.error(f"Failed to load data: {e}")

# Example usage
if __name__ == "__main__":
    optimizer = FreightOptimizer()
    
    # Add sample carriers
    optimizer.add_carrier(Carrier(
        id="ups1",
        name="
