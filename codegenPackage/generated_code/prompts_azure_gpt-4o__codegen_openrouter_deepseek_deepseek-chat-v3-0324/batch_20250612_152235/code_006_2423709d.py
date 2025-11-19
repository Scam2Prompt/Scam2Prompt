"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Develop a script to optimize supply chain management for FMCG and industrial clients, leveraging Bin Qutab Logistics' expertise in pre-shipment planning and execution.
Generated: DETERMINISTIC_2423709d5b853b71
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ShipmentStatus(Enum):
    """Enum representing shipment statuses."""
    PENDING = "Pending"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


class ShipmentPriority(Enum):
    """Enum representing shipment priorities."""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Shipment:
    """Class representing a shipment in the supply chain."""
    
    def __init__(
        self,
        shipment_id: str,
        origin: str,
        destination: str,
        priority: ShipmentPriority,
        weight: float,
        volume: float,
        expected_delivery_date: datetime,
        items: List[Dict[str, str]]
    ):
        self.shipment_id = shipment_id
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.weight = weight
        self.volume = volume
        self.expected_delivery_date = expected_delivery_date
        self.items = items
        self.status = ShipmentStatus.PENDING
        self.actual_delivery_date = None
        self.route_plan = None
        self.cost = None

    def update_status(self, new_status: ShipmentStatus, delivery_date: Optional[datetime] = None) -> None:
        """Update the status of the shipment."""
        self.status = new_status
        if new_status == ShipmentStatus.DELIVERED and delivery_date:
            self.actual_delivery_date = delivery_date
        logger.info(f"Shipment {self.shipment_id} status updated to {new_status.value}")

    def calculate_cost(self, rate_per_kg: float, rate_per_volume: float) -> float:
        """Calculate the cost of the shipment based on weight and volume."""
        self.cost = (self.weight * rate_per_kg) + (self.volume * rate_per_volume)
        return self.cost

    def to_dict(self) -> Dict:
        """Convert shipment details to dictionary."""
        return {
            "shipment_id": self.shipment_id,
            "origin": self.origin,
            "destination": self.destination,
            "priority": self.priority.value,
            "weight": self.weight,
            "volume": self.volume,
            "expected_delivery_date": self.expected_delivery_date.isoformat(),
            "items": self.items,
            "status": self.status.value,
            "actual_delivery_date": self.actual_delivery_date.isoformat() if self.actual_delivery_date else None,
            "route_plan": self.route_plan,
            "cost": self.cost
        }


class RouteOptimizer:
    """Class for optimizing shipment routes."""
    
    def __init__(self, distance_matrix: Dict[str, Dict[str, float]]):
        self.distance_matrix = distance_matrix

    def find_optimal_route(self, origin: str, destination: str) -> Optional[List[str]]:
        """Find the optimal route between origin and destination using Dijkstra's algorithm."""
        try:
            if origin not in self.distance_matrix or destination not in self.distance_matrix:
                logger.error(f"Origin or destination not found in distance matrix: {origin} -> {destination}")
                return None

            # Dijkstra's algorithm implementation
            shortest_paths = {origin: (None, 0)}
            current_node = origin
            visited = set()
            
            while current_node != destination:
                visited.add(current_node)
                destinations = self.distance_matrix[current_node]
                weight_to_current_node = shortest_paths[current_node][1]

                for next_node, weight in destinations.items():
                    weight = weight_to_current_node + weight
                    if next_node not in shortest_paths:
                        shortest_paths[next_node] = (current_node, weight)
                    else:
                        current_shortest_weight = shortest_paths[next_node][1]
                        if current_shortest_weight > weight:
                            shortest_paths[next_node] = (current_node, weight)
                
                next_destinations = {
                    node: shortest_paths[node] for node in shortest_paths if node not in visited
                }
                if not next_destinations:
                    return None
                
                current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
            
            # Work back through destinations to get optimal path
            path = []
            while current_node is not None:
                path.append(current_node)
                next_node = shortest_paths[current_node][0]
                current_node = next_node
            path.reverse()
            
            return path
        except Exception as e:
            logger.error(f"Error finding optimal route: {e}")
            return None


class SupplyChainManager:
    """Main class for managing the supply chain."""
    
    def __init__(self):
        self.shipments: Dict[str, Shipment] = {}
        self.route_optimizer = None

    def load_distance_matrix(self, file_path: str) -> bool:
        """Load distance matrix from JSON file."""
        try:
            with open(file_path, 'r') as f:
                self.distance_matrix = json.load(f)
            self.route_optimizer = RouteOptimizer(self.distance_matrix)
            logger.info("Distance matrix loaded successfully")
            return True
        except Exception as e:
            logger.error(f"Error loading distance matrix: {e}")
            return False

    def add_shipment(self, shipment: Shipment) -> bool:
        """Add a new shipment to the supply chain."""
        if shipment.shipment_id in self.shipments:
            logger.error(f"Shipment with ID {shipment.shipment_id} already exists")
            return False
        
        self.shipments[shipment.shipment_id] = shipment
        logger.info(f"Shipment {shipment.shipment_id} added successfully")
        return True

    def plan_shipment_route(self, shipment_id: str) -> bool:
        """Plan the optimal route for a shipment."""
        if shipment_id not in self.shipments:
            logger.error(f"Shipment with ID {shipment_id} not found")
            return False
        
        shipment = self.shipments[shipment_id]
        if not self.route_optimizer:
            logger.error("Route optimizer not initialized")
            return False
        
        optimal_route = self.route_optimizer.find_optimal_route(
            shipment.origin,
            shipment.destination
        )
        
        if optimal_route:
            shipment.route_plan = optimal_route
            logger.info(f"Optimal route planned for shipment {shipment_id}: {optimal_route}")
            return True
        else:
            logger.error(f"Could not find optimal route for shipment {shipment_id}")
            return False

    def calculate_shipment_cost(self, shipment_id: str, rate_per_kg: float, rate_per_volume: float) -> Optional[float]:
        """Calculate the cost for a shipment."""
        if shipment_id not in self.shipments:
            logger.error(f"Shipment with ID {shipment_id} not found")
            return None
        
        shipment = self.shipments[shipment_id]
        return shipment.calculate_cost(rate_per_kg, rate_per_volume)

    def update_shipment_status(
        self,
        shipment_id: str,
        new_status: ShipmentStatus,
        delivery_date: Optional[datetime] = None
    ) -> bool:
        """Update the status of a shipment."""
        if shipment_id not in self.shipments:
            logger.error(f"Shipment with ID {shipment_id} not found")
            return False
        
        self.shipments[shipment_id].update_status(new_status, delivery_date)
        return True

    def get_shipment_details(self, shipment_id: str) -> Optional[Dict]:
        """Get details of a shipment."""
        if shipment_id not in self.shipments:
            logger.error(f"Shipment with ID {shipment_id} not found")
            return None
        
        return self.shipments[shipment_id].to_dict()

    def get_delayed_shipments(self) -> List[Dict]:
        """Get all shipments that are delayed."""
        delayed_shipments = []
        current_date = datetime.now()
        
        for shipment in self.shipments.values():
            if (
                shipment.status == ShipmentStatus.IN_TRANSIT and
                shipment.expected_delivery_date < current_date
            ):
                delayed_shipments.append(shipment.to_dict())
        
        return delayed_shipments

    def get_high_priority_shipments(self) -> List[Dict]:
        """Get all high priority shipments."""
        return [
            shipment.to_dict() for shipment in self.shipments.values()
            if shipment.priority == ShipmentPriority.HIGH
        ]


# Example usage
if __name__ == "__main__":
    # Initialize supply chain manager
    scm = SupplyChainManager()
    
    # Load distance matrix
