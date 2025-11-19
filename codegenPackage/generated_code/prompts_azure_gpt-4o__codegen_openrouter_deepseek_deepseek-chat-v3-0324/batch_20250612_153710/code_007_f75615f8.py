"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-gt.com
Prompt: Write code to simulate the logistics and storage optimization of SymBiotic's integrated farming systems, reducing transport times and strengthening regional value chains.
Generated: DETERMINISTIC_f75615f8deec7f2b
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import random
import math

class Farm:
    """Represents a farm in the SymBiotic network."""
    
    def __init__(self, id: int, location: Tuple[float, float], production_capacity: Dict[str, float], storage_capacity: Dict[str, float]):
        """
        Initialize a farm.
        
        Args:
            id: Unique identifier for the farm
            location: (latitude, longitude) coordinates
            production_capacity: Dictionary mapping product types to production capacity (units/day)
            storage_capacity: Dictionary mapping product types to storage capacity (units)
        """
        self.id = id
        self.location = location
        self.production_capacity = production_capacity
        self.storage_capacity = storage_capacity
        self.current_storage = defaultdict(float)
        self.demand = defaultdict(float)
        
    def produce(self, product: str, amount: float) -> bool:
        """Produce a given amount of product if capacity allows."""
        if product not in self.production_capacity:
            return False
        if amount > self.production_capacity[product]:
            return False
        if self.current_storage[product] + amount > self.storage_capacity[product]:
            return False
        self.current_storage[product] += amount
        return True
    
    def consume(self, product: str, amount: float) -> bool:
        """Consume a given amount of product if available."""
        if product not in self.current_storage:
            return False
        if self.current_storage[product] < amount:
            return False
        self.current_storage[product] -= amount
        return True
    
    def set_demand(self, product: str, amount: float) -> None:
        """Set the demand for a product at this farm."""
        self.demand[product] = amount

class TransportationNetwork:
    """Manages the transportation routes between farms."""
    
    def __init__(self):
        """Initialize the transportation network."""
        self.graph = defaultdict(dict)
        
    def add_route(self, farm1: int, farm2: int, distance: float, speed: float) -> None:
        """
        Add a bidirectional route between two farms.
        
        Args:
            farm1: ID of first farm
            farm2: ID of second farm
            distance: Distance between farms in km
            speed: Average transport speed in km/h
        """
        travel_time = distance / speed  # hours
        self.graph[farm1][farm2] = travel_time
        self.graph[farm2][farm1] = travel_time
        
    def shortest_path(self, start: int, end: int) -> Optional[Tuple[float, List[int]]]:
        """
        Find the shortest path between two farms using Dijkstra's algorithm.
        
        Args:
            start: Starting farm ID
            end: Destination farm ID
            
        Returns:
            Tuple of (total_time, path) or None if no path exists
        """
        if start not in self.graph or end not in self.graph:
            return None
            
        heap = []
        heapq.heappush(heap, (0.0, start, []))
        visited = set()
        
        while heap:
            current_time, current_farm, path = heapq.heappop(heap)
            
            if current_farm in visited:
                continue
                
            visited.add(current_farm)
            new_path = path + [current_farm]
            
            if current_farm == end:
                return (current_time, new_path)
                
            for neighbor, time in self.graph[current_farm].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (current_time + time, neighbor, new_path))
                    
        return None

class SymBioticSystem:
    """Main class for the SymBiotic integrated farming system simulation."""
    
    def __init__(self):
        """Initialize the SymBiotic system."""
        self.farms = {}
        self.transport_network = TransportationNetwork()
        self.products = set()
        
    def add_farm(self, farm: Farm) -> None:
        """Add a farm to the system."""
        self.farms[farm.id] = farm
        for product in farm.production_capacity:
            self.products.add(product)
            
    def optimize_transport(self, product: str) -> Dict[int, Dict[int, float]]:
        """
        Optimize transport for a specific product across all farms.
        
        Args:
            product: The product to optimize transport for
            
        Returns:
            Dictionary mapping source farm IDs to dictionaries of destination farm IDs and optimal amounts
        """
        if product not in self.products:
            return {}
            
        # Step 1: Identify surplus and deficit farms
        surplus_farms = []
        deficit_farms = []
        
        for farm_id, farm in self.farms.items():
            available = farm.current_storage.get(product, 0)
            demand = farm.demand.get(product, 0)
            
            if available > demand:
                surplus_farms.append((farm_id, available - demand))
            elif demand > available:
                deficit_farms.append((farm_id, demand - available))
                
        # Step 2: Match surplus to deficit using transportation network
        transport_plan = defaultdict(dict)
        
        for surplus_id, surplus_amount in surplus_farms:
            for deficit_id, deficit_amount in deficit_farms:
                if deficit_amount <= 0:
                    continue
                    
                path_info = self.transport_network.shortest_path(surplus_id, deficit_id)
                if not path_info:
                    continue
                    
                transport_time, path = path_info
                transfer_amount = min(surplus_amount, deficit_amount)
                
                if transfer_amount > 0:
                    transport_plan[surplus_id][deficit_id] = transfer_amount
                    surplus_amount -= transfer_amount
                    deficit_amount -= transfer_amount
                    
                    if surplus_amount <= 0:
                        break
                        
        return transport_plan
    
    def execute_transport(self, transport_plan: Dict[int, Dict[int, float]], product: str) -> None:
        """
        Execute a transport plan by moving products between farms.
        
        Args:
            transport_plan: The transport plan from optimize_transport
            product: The product being transported
        """
        for source_id, destinations in transport_plan.items():
            source_farm = self.farms[source_id]
            for dest_id, amount in destinations.items():
                dest_farm = self.farms[dest_id]
                
                if source_farm.consume(product, amount):
                    dest_farm.current_storage[product] += amount
    
    def simulate_day(self) -> None:
        """Simulate one day of production, consumption, and transport."""
        # Step 1: Each farm produces according to its capacity
        for farm in self.farms.values():
            for product, capacity in farm.production_capacity.items():
                farm.produce(product, capacity)
                
        # Step 2: Optimize and execute transport for each product
        for product in self.products:
            transport_plan = self.optimize_transport(product)
            self.execute_transport(transport_plan, product)
            
        # Step 3: Each farm consumes according to its demand
        for farm in self.farms.values():
            for product, demand in farm.demand.items():
                farm.consume(product, demand)

def haversine_distance(loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
    """
    Calculate the great-circle distance between two points on the Earth.
    
    Args:
        loc1: (lat1, lon1) in degrees
        loc2: (lat2, lon2) in degrees
        
    Returns:
        Distance in kilometers
    """
    lat1, lon1 = math.radians(loc1[0]), math.radians(loc1[1])
    lat2, lon2 = math.radians(loc2[0]), math.radians(loc2[1])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return 6371 * c  # Earth radius in km

def create_sample_system() -> SymBioticSystem:
    """Create a sample SymBiotic system for demonstration."""
    system = SymBioticSystem()
    
    # Create farms with random locations in a 100km x 100km area
    locations = [
        (45.0 + random.uniform(-0.5, 0.5), 9.0 + random.uniform(-0.5, 0.5)) for _ in range(5)
    ]
    
    # Add farms with different production and storage capacities
    products = ["wheat", "corn", "milk", "eggs"]
    
    for i, loc in enumerate(locations):
        production = {product: random.uniform(10, 100) for product in random.sample(products, 2)}
        storage = {product: cap * random.uniform(1.5, 3) for product, cap in production.items
