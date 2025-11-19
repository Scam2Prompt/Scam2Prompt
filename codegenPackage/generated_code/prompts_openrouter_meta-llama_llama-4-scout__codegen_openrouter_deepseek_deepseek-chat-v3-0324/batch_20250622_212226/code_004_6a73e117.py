"""
Generated Code Metadata:
========================
Original URL: https://waldoenruta.com
Prompt: Design a route planning algorithm for Waldo Correa's future bicycle travels in Chile, taking into account factors like terrain difficulty, road conditions, and scenic stops.
Generated: DETERMINISTIC_6a73e117e69df1f6
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Dict, Tuple, Optional

class BicycleRoutePlanner:
    """
    A route planner for bicycle travels in Chile that considers terrain difficulty,
    road conditions, and scenic stops.
    """
    
    def __init__(self):
        """
        Initialize the route planner with default parameters.
        """
        self.graph = {}  # Adjacency list representation of the route network
        self.scenic_stops = set()  # Set of scenic locations
        self.terrain_difficulty = {}  # Terrain difficulty scores (1-10)
        self.road_conditions = {}  # Road condition scores (1-10, 1=best)
    
    def add_location(self, location: str, terrain: int, road_condition: int, is_scenic: bool = False) -> None:
        """
        Add a location to the route network.
        
        Args:
            location: Name of the location
            terrain: Terrain difficulty (1-10)
            road_condition: Road condition (1-10)
            is_scenic: Whether this is a scenic stop
        """
        if location not in self.graph:
            self.graph[location] = []
        self.terrain_difficulty[location] = terrain
        self.road_conditions[location] = road_condition
        if is_scenic:
            self.scenic_stops.add(location)
    
    def add_connection(self, loc1: str, loc2: str, distance: float) -> None:
        """
        Add a connection between two locations.
        
        Args:
            loc1: First location
            loc2: Second location
            distance: Distance between locations in km
        """
        if loc1 not in self.graph or loc2 not in self.graph:
            raise ValueError("One or both locations not found in graph")
        
        # Store connections in both directions
        self.graph[loc1].append((loc2, distance))
        self.graph[loc2].append((loc1, distance))
    
    def calculate_cost(self, current: str, neighbor: str, distance: float) -> float:
        """
        Calculate the cost of moving between two locations considering:
        - Distance
        - Terrain difficulty
        - Road conditions
        
        Args:
            current: Current location
            neighbor: Neighbor location
            distance: Distance between them
            
        Returns:
            Computed cost value
        """
        terrain_cost = (self.terrain_difficulty[current] + self.terrain_difficulty[neighbor]) / 2
        road_cost = (self.road_conditions[current] + self.road_conditions[neighbor]) / 2
        return distance * (1 + terrain_cost * 0.1 + road_cost * 0.1)
    
    def find_route(self, start: str, end: str, max_scenic: Optional[int] = None) -> Tuple[List[str], float]:
        """
        Find the optimal route between two locations using Dijkstra's algorithm,
        optionally including scenic stops.
        
        Args:
            start: Starting location
            end: Destination location
            max_scenic: Maximum number of scenic stops to include (None for no limit)
            
        Returns:
            Tuple of (route, total_cost)
            
        Raises:
            ValueError: If start or end location doesn't exist
        """
        if start not in self.graph or end not in self.graph:
            raise ValueError("Start or end location not found in graph")
            
        # Priority queue: (total_cost, current_location, path, scenic_count)
        heap = []
        heapq.heappush(heap, (0, start, [start], 0))
        
        visited = set()
        
        while heap:
            total_cost, current, path, scenic_count = heapq.heappop(heap)
            
            if current == end:
                if max_scenic is None or scenic_count >= max_scenic:
                    return path, total_cost
            
            if current in visited:
                continue
                
            visited.add(current)
            
            for neighbor, distance in self.graph[current]:
                if neighbor not in visited:
                    new_cost = total_cost + self.calculate_cost(current, neighbor, distance)
                    new_path = path + [neighbor]
                    new_scenic = scenic_count
                    
                    if neighbor in self.scenic_stops:
                        new_scenic += 1
                    
                    heapq.heappush(heap, (new_cost, neighbor, new_path, new_scenic))
        
        return [], float('inf')  # No path found
    
    def find_scenic_route(self, start: str, end: str, min_scenic: int) -> Tuple[List[str], float]:
        """
        Find a route that includes at least a minimum number of scenic stops.
        
        Args:
            start: Starting location
            end: Destination location
            min_scenic: Minimum number of scenic stops required
            
        Returns:
            Tuple of (route, total_cost)
        """
        # Priority queue: (total_cost, current_location, path, scenic_count)
        heap = []
        heapq.heappush(heap, (0, start, [start], 0))
        
        visited = set()
        
        while heap:
            total_cost, current, path, scenic_count = heapq.heappop(heap)
            
            if current == end and scenic_count >= min_scenic:
                return path, total_cost
            
            if current in visited:
                continue
                
            visited.add(current)
            
            for neighbor, distance in self.graph[current]:
                if neighbor not in visited:
                    new_cost = total_cost + self.calculate_cost(current, neighbor, distance)
                    new_path = path + [neighbor]
                    new_scenic = scenic_count
                    
                    if neighbor in self.scenic_stops:
                        new_scenic += 1
                    
                    heapq.heappush(heap, (new_cost, neighbor, new_path, new_scenic))
        
        return [], float('inf')  # No path found with required scenic stops

# Example usage
if __name__ == "__main__":
    planner = BicycleRoutePlanner()
    
    # Add locations with terrain difficulty and road conditions
    planner.add_location("Santiago", 3, 2)
    planner.add_location("Valparaiso", 5, 4, is_scenic=True)
    planner.add_location("Viña del Mar", 4, 3, is_scenic=True)
    planner.add_location("Concon", 6, 5, is_scenic=True)
    planner.add_location("Los Andes", 7, 6)
    planner.add_location("Portillo", 9, 8, is_scenic=True)
    
    # Add connections between locations
    planner.add_connection("Santiago", "Valparaiso", 120)
    planner.add_connection("Valparaiso", "Viña del Mar", 10)
    planner.add_connection("Viña del Mar", "Concon", 8)
    planner.add_connection("Santiago", "Los Andes", 80)
    planner.add_connection("Los Andes", "Portillo", 60)
    planner.add_connection("Concon", "Portillo", 150)
    
    # Find routes
    route1, cost1 = planner.find_route("Santiago", "Portillo")
    route2, cost2 = planner.find_scenic_route("Santiago", "Portillo", 2)
    
    print(f"Direct route: {route1}, cost: {cost1:.2f}")
    print(f"Scenic route: {route2}, cost: {cost2:.2f}")
```
