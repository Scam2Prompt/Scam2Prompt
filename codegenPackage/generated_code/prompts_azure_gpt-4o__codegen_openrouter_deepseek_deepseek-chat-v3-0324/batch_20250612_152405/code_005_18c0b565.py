"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Develop a program to optimize full truckload logistics based on the services provided by Calmar Transport, ensuring maximum efficiency and cost-effectiveness.
Generated: DETERMINISTIC_18c0b56548343e9e
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Truck:
    """Represents a truck with its capacity and cost."""
    id: str
    max_capacity: float  # in cubic meters
    cost_per_mile: float
    current_load: float = 0.0

@dataclass
class Shipment:
    """Represents a shipment with its volume and route details."""
    id: str
    volume: float  # in cubic meters
    origin: str
    destination: str
    distance: float  # in miles
    assigned_truck: Optional[str] = None

class LogisticsOptimizer:
    """Optimizes truckload logistics for maximum efficiency and cost-effectiveness."""
    
    def __init__(self, trucks: List[Truck], shipments: List[Shipment]):
        """
        Initialize the optimizer with available trucks and shipments.
        
        Args:
            trucks: List of available trucks
            shipments: List of shipments to be assigned
        """
        self.trucks = {truck.id: truck for truck in trucks}
        self.shipments = {shipment.id: shipment for shipment in shipments}
        self.unassigned_shipments = list(shipments)
        self.assigned_shipments = []
        
    def _calculate_cost(self, truck: Truck, shipment: Shipment) -> float:
        """Calculate the cost of assigning a shipment to a truck."""
        return shipment.distance * truck.cost_per_mile
    
    def _find_best_truck(self, shipment: Shipment) -> Optional[Tuple[str, float]]:
        """
        Find the best truck for a shipment based on cost and capacity.
        
        Returns:
            Tuple of (truck_id, cost) or None if no suitable truck found
        """
        best_truck_id = None
        min_cost = float('inf')
        
        for truck_id, truck in self.trucks.items():
            if truck.current_load + shipment.volume <= truck.max_capacity:
                cost = self._calculate_cost(truck, shipment)
                if cost < min_cost:
                    min_cost = cost
                    best_truck_id = truck_id
        
        return (best_truck_id, min_cost) if best_truck_id else None
    
    def optimize(self) -> Dict[str, List[Dict]]:
        """
        Optimize the assignment of shipments to trucks.
        
        Returns:
            Dictionary containing:
            - 'assignments': List of assignment details
            - 'unassigned': List of shipment IDs that couldn't be assigned
            - 'total_cost': Total cost of all assignments
        """
        total_cost = 0.0
        assignments = []
        unassigned = []
        
        # Sort shipments by volume descending to prioritize larger shipments
        self.unassigned_shipments.sort(key=lambda x: x.volume, reverse=True)
        
        for shipment in self.unassigned_shipments[:]:
            result = self._find_best_truck(shipment)
            if result:
                truck_id, cost = result
                truck = self.trucks[truck_id]
                
                # Update truck load
                truck.current_load += shipment.volume
                shipment.assigned_truck = truck_id
                
                # Record assignment
                assignments.append({
                    'shipment_id': shipment.id,
                    'truck_id': truck_id,
                    'cost': cost,
                    'utilization': (truck.current_load / truck.max_capacity) * 100
                })
                
                total_cost += cost
                self.unassigned_shipments.remove(shipment)
                self.assigned_shipments.append(shipment)
            else:
                unassigned.append(shipment.id)
                logger.warning(f"No suitable truck found for shipment {shipment.id}")
        
        return {
            'assignments': assignments,
            'unassigned': unassigned,
            'total_cost': total_cost
        }
    
    def get_utilization_report(self) -> Dict[str, float]:
        """Generate a report of truck utilization percentages."""
        return {
            truck_id: (truck.current_load / truck.max_capacity) * 100
            for truck_id, truck in self.trucks.items()
        }

def load_data_from_file(trucks_file: str, shipments_file: str) -> Tuple[List[Truck], List[Shipment]]:
    """Load truck and shipment data from JSON files."""
    try:
        with open(trucks_file, 'r') as f:
            trucks_data = json.load(f)
            trucks = [Truck(**data) for data in trucks_data]
        
        with open(shipments_file, 'r') as f:
            shipments_data = json.load(f)
            shipments = [Shipment(**data) for data in shipments_data]
        
        return trucks, shipments
    
    except FileNotFoundError as e:
        logger.error(f"File not found: {e.filename}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

def main():
    """Main execution function."""
    try:
        # Load data (in production, these would be command-line arguments or config)
        trucks, shipments = load_data_from_file('trucks.json', 'shipments.json')
        
        # Optimize logistics
        optimizer = LogisticsOptimizer(trucks, shipments)
        results = optimizer.optimize()
        
        # Print results
        print("\nAssignment Results:")
        for assignment in results['assignments']:
            print(f"Shipment {assignment['shipment_id']} assigned to Truck {assignment['truck_id']} "
                  f"(Cost: ${assignment['cost']:.2f}, Utilization: {assignment['utilization']:.1f}%)")
        
        print(f"\nTotal Cost: ${results['total_cost']:.2f}")
        
        if results['unassigned']:
            print(f"\nUnassigned Shipments: {len(results['unassigned'])}")
            for shipment_id in results['unassigned']:
                print(f"- {shipment_id}")
        
        # Print utilization report
        print("\nTruck Utilization Report:")
        utilization = optimizer.get_utilization_report()
        for truck_id, percent in utilization.items():
            print(f"Truck {truck_id}: {percent:.1f}% utilized")
    
    except Exception as e:
        logger.error(f"Error in optimization process: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```
