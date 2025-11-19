"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Develop an algorithm to optimize transportation routes for a logistics park with centralized geographic advantages, similar to PLM's Costa Rica location.
Generated: DETERMINISTIC_126842420b3d90de
Batch ID: 20250612_152710
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
import math

class LogisticsParkRouteOptimizer:
    """
    A class to optimize transportation routes for a logistics park with centralized geographic advantages.
    Uses Dijkstra's algorithm for shortest path calculations and considers various constraints.
    """

    def __init__(self, location_data):
        """
        Initialize the route optimizer with location data.
        
        Args:
            location_data (dict): A dictionary containing:
                - 'central_location': Coordinates of the central logistics park (lat, lon)
                - 'nodes': List of destination nodes with their coordinates
                - 'road_network': Graph representation of road connections between nodes
                - 'constraints': Dictionary of constraints (e.g., max_distance, vehicle_capacity)
        """
        self.central_location = location_data['central_location']
        self.nodes = location_data['nodes']
        self.road_network = location_data['road_network']
        self.constraints = location_data.get('constraints', {})
        self.validate_input_data()

    def validate_input_data(self):
        """Validate the input data structure and types."""
        if not isinstance(self.central_location, (tuple, list)) or len(self.central_location) != 2:
            raise ValueError("Central location must be a tuple/list of (lat, lon)")
        if not isinstance(self.nodes, list):
            raise ValueError("Nodes must be a list of destinations")
        if not isinstance(self.road_network, dict):
            raise ValueError("Road network must be a dictionary graph representation")

    def haversine_distance(self, coord1, coord2):
        """
        Calculate the great-circle distance between two points on the Earth.
        
        Args:
            coord1 (tuple): (lat, lon) of first point
            coord2 (tuple): (lat, lon) of second point
            
        Returns:
            float: Distance in kilometers
        """
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Earth radius in km
        return c * r

    def optimize_routes(self):
        """
        Optimize transportation routes from the central location to all nodes.
        
        Returns:
            dict: Optimized routes with distances and paths
        """
        optimized_routes = {}
        
        for node in self.nodes:
            node_id = node['id']
            node_coords = (node['lat'], node['lon'])
            
            try:
                # Calculate distance from central location to node
                distance = self.haversine_distance(self.central_location, node_coords)
                
                # Find shortest path using Dijkstra's algorithm
                path, path_distance = self.find_shortest_path(node_id)
                
                # Apply constraints if any
                if self.constraints.get('max_distance') and path_distance > self.constraints['max_distance']:
                    raise ValueError(f"Route to {node_id} exceeds maximum allowed distance")
                
                optimized_routes[node_id] = {
                    'direct_distance': distance,
                    'road_distance': path_distance,
                    'path': path
                }
                
            except Exception as e:
                print(f"Error optimizing route for node {node_id}: {str(e)}")
                optimized_routes[node_id] = {
                    'error': str(e)
                }
        
        return optimized_routes

    def find_shortest_path(self, destination_id):
        """
        Find the shortest path from central location to destination using Dijkstra's algorithm.
        
        Args:
            destination_id: ID of the destination node
            
        Returns:
            tuple: (path as list of node IDs, total distance)
        """
        # Initialize distances with infinity
        distances = {node: float('inf') for node in self.road_network}
        previous_nodes = {node: None for node in self.road_network}
        
        # The central location is the starting point (distance 0)
        central_node = self.find_closest_node(self.central_location)
        distances[central_node] = 0
        
        # Priority queue for Dijkstra's algorithm
        priority_queue = [(0, central_node)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # Stop if we've reached the destination
            if current_node == destination_id:
                break
                
            # Skip if we've found a better path already
            if current_distance > distances[current_node]:
                continue
                
            # Explore neighbors
            for neighbor, edge_data in self.road_network[current_node].items():
                distance = current_distance + edge_data['distance']
                
                # Found a shorter path to the neighbor
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Reconstruct path
        path = []
        current_node = destination_id
        
        if previous_nodes[current_node] is None and current_node != central_node:
            raise ValueError(f"No path exists to node {destination_id}")
            
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
            
        path.reverse()
        
        return path, distances[destination_id]

    def find_closest_node(self, coords):
        """
        Find the closest node in the road network to given coordinates.
        
        Args:
            coords (tuple): (lat, lon) coordinates
            
        Returns:
            str: ID of the closest node
        """
        closest_node = None
        min_distance = float('inf')
        
        for node_id in self.road_network:
            node_data = next((n for n in self.nodes if n['id'] == node_id), None)
            if node_data:
                node_coords = (node_data['lat'], node_data['lon'])
                distance = self.haversine_distance(coords, node_coords)
                if distance < min_distance:
                    min_distance = distance
                    closest_node = node_id
        
        if closest_node is None:
            raise ValueError("No nodes found in road network")
            
        return closest_node

# Example usage
if __name__ == "__main__":
    # Sample data structure
    location_data = {
        'central_location': (9.9281, -84.0907),  # Approximate San José, Costa Rica
        'nodes': [
            {'id': 'A', 'lat': 9.9345, 'lon': -84.0920},
            {'id': 'B', 'lat': 9.9250, 'lon': -84.0850},
            {'id': 'C', 'lat': 9.9300, 'lon': -84.1000}
        ],
        'road_network': {
            'A': {'B': {'distance': 1.5}, 'C': {'distance': 2.0}},
            'B': {'A': {'distance': 1.5}, 'C': {'distance': 1.8}},
            'C': {'A': {'distance': 2.0}, 'B': {'distance': 1.8}}
        },
        'constraints': {
            'max_distance': 10.0  # Maximum allowed route distance in km
        }
    }
    
    optimizer = LogisticsParkRouteOptimizer(location_data)
    optimized_routes = optimizer.optimize_routes()
    print(optimized_routes)
```
