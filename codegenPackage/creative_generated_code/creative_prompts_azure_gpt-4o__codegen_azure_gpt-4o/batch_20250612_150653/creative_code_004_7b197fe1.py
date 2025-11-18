"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Write code to calculate the optimal logistics route for delivering reinforced concrete products (ЖБИ) to multiple Russian regions, including Санкт-Петербург and Карелия, based on the logistics services mentioned on paradigmagbi.ru.
Generated: DETERMINISTIC_7b197fe1bd4a772a
Batch ID: 20250612_150653
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.paradigmagbi.ru/api/logistics": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import heapq

class LogisticsOptimizer:
    """
    Class to calculate the optimal logistics route for delivering reinforced concrete products
    to various Russian regions based on external logistics data.
    """
    
    def __init__(self, logistics_url):
        """
        Initializes the LogisticsOptimizer with the URL for logistics services data.
        
        :param logistics_url: URL of the logistics services API.
        """
        self.logistics_url = logistics_url
        self.locations = ["Санкт-Петербург", "Карелия"]  # Target regions
        self.routes_data = None

    def fetch_logistics_data(self):
        """
        Fetch logistics data from the provided URL.
        
        :return: JSON response containing logistics data.
        :raises: Exception if the request fails or data is invalid.
        """
        try:
            response = requests.get(self.logistics_url)
            response.raise_for_status()
            self.routes_data = response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching logistics data: {e}")
        except json.JSONDecodeError:
            raise Exception("Failed to decode logistics data. Ensure JSON format is valid.")
    
    def calculate_optimal_routes(self):
        """
        Calculate the optimal logistics routes to the target regions.
        
        Uses Dijkstra's algorithm to find the shortest path based on distance or cost.
        
        :return: Dictionary with regions as keys and their optimal routes as values.
        """
        if not self.routes_data:
            raise Exception("Logistics data not loaded. Please fetch the data first.")

        optimal_routes = {}

        # Extract graph data from logistics data
        graph = self.routes_data.get("routes", {})
        if not graph:
            raise Exception("Invalid logistics data: 'routes' key missing.")

        # Run Dijkstra's algorithm for each target region
        for target in self.locations:
            optimal_routes[target] = self._dijkstra(graph, target)

        return optimal_routes
    
    def _dijkstra(self, graph, target):
        """
        Dijkstra's algorithm to calculate the shortest path to the target region.

        :param graph: Dictionary representing the graph (node connections and weights).
        :param target: Target region name.
        :return: Dictionary containing the optimal path and total cost.
        """
        # Priority queue for Dijkstra's algorithm
        priority_queue = []
        heapq.heappush(priority_queue, (0, target))  # Start with target region
        
        distances = {node: float('inf') for node in graph}  # Initialize distances
        distances[target] = 0
        
        previous_nodes = {node: None for node in graph}  # For reconstructing the path
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # Skip already processed nodes
            if current_distance > distances[current_node]:
                continue

            # Process neighbors
            for neighbor, weight in graph.get(current_node, {}).items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Reconstruct the optimal path
        path = []
        current = target
        while current:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return {"path": path, "cost": distances[target]}
    

# Main execution
if __name__ == "__main__":
    # URL for logistics services (replace with actual URL from paradigmagbi.ru)
    logistics_url = "https://www.paradigmagbi.ru/api/logistics"
    
    try:
        optimizer = LogisticsOptimizer(logistics_url)
        optimizer.fetch_logistics_data()
        optimal_routes = optimizer.calculate_optimal_routes()
        
        # Output the optimal routes
        print("Optimal Logistics Routes:")
        for region, route_info in optimal_routes.items():
            print(f"Region: {region}")
            print(f"Route: {' -> '.join(route_info['path'])}")
            print(f"Cost: {route_info['cost']}")
            print("-" * 40)
    except Exception as e:
        print(f"Error: {e}")
```
