"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Develop a logistics optimization algorithm for ENL Consortium's haulage system, considering truck fleet types (flatbeds, low loaders) and routes for local and up-country cargo transportation.
Generated: DETERMINISTIC_a27917c0d78a89ef
Batch ID: 20250612_151232
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
from enum import Enum

class TruckType(Enum):
    FLATBED = "flatbed"
    LOW_LOADER = "low_loader"

class RouteType(Enum):
    LOCAL = "local"
    UPCOUNTRY = "upcountry"

class Truck:
    def __init__(self, truck_id: str, truck_type: TruckType, capacity: float, cost_per_km: float, available: bool = True):
        self.truck_id = truck_id
        self.truck_type = truck_type
        self.capacity = capacity
        self.cost_per_km = cost_per_km
        self.available = available

    def __repr__(self):
        return f"Truck(id={self.truck_id}, type={self.truck_type}, capacity={self.capacity}, cost={self.cost_per_km}, available={self.available})"

class Cargo:
    def __init__(self, cargo_id: str, weight: float, destination: str, route_type: RouteType, requires_low_loader: bool = False):
        self.cargo_id = cargo_id
        self.weight = weight
        self.destination = destination
        self.route_type = route_type
        self.requires_low_loader = requires_low_loader

    def __repr__(self):
        return f"Cargo(id={self.cargo_id}, weight={self.weight}, dest={self.destination}, route={self.route_type}, low_loader={self.requires_low_loader})"

class Route:
    def __init__(self, origin: str, destination: str, distance: float, route_type: RouteType):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.route_type = route_type

    def __repr__(self):
        return f"Route({self.origin}->{self.destination}, distance={self.distance}km, type={self.route_type})"

class LogisticsOptimizer:
    def __init__(self):
        self.trucks: List[Truck] = []
        self.cargos: List[Cargo] = []
        self.routes: Dict[Tuple[str, str], Route] = {}
        self.distance_matrix: Dict[Tuple[str, str], float] = {}

    def add_truck(self, truck: Truck) -> None:
        """Add a truck to the fleet"""
        self.trucks.append(truck)

    def add_cargo(self, cargo: Cargo) -> None:
        """Add cargo to be transported"""
        self.cargos.append(cargo)

    def add_route(self, route: Route) -> None:
        """Add a transportation route"""
        key = (route.origin, route.destination)
        self.routes[key] = route
        self.distance_matrix[key] = route.distance

    def get_route_distance(self, origin: str, destination: str) -> Optional[float]:
        """Get distance between two locations"""
        return self.distance_matrix.get((origin, destination))

    def find_optimal_assignment(self) -> Dict[str, List[Tuple[str, float]]]:
        """
        Find optimal truck-cargo assignments using a priority queue approach
        Returns dict of {truck_id: [(cargo_id, cost)]}
        """
        if not self.trucks or not self.cargos:
            return {}

        # Filter available trucks
        available_trucks = [t for t in self.trucks if t.available]
        if not available_trucks:
            raise ValueError("No available trucks in the fleet")

        # Sort cargos by weight descending
        sorted_cargos = sorted(self.cargos, key=lambda x: x.weight, reverse=True)
        
        # Sort trucks by capacity descending
        sorted_trucks = sorted(available_trucks, key=lambda x: x.capacity, reverse=True)

        assignments = {}
        remaining_capacity = {t.truck_id: t.capacity for t in sorted_trucks}
        truck_costs = {t.truck_id: [] for t in sorted_trucks}

        for cargo in sorted_cargos:
            best_truck = None
            min_cost = float('inf')
            best_route = None

            # Find suitable trucks
            suitable_trucks = []
            for truck in sorted_trucks:
                if (truck.truck_type == TruckType.LOW_LOADER or not cargo.requires_low_loader) and remaining_capacity[truck.truck_id] >= cargo.weight:
                    suitable_trucks.append(truck)

            if not suitable_trucks:
                continue  # Skip cargo if no suitable truck found

            # Find best truck and route
            for truck in suitable_trucks:
                route_distance = self.get_route_distance("depot", cargo.destination)
                if route_distance is None:
                    continue

                cost = route_distance * truck.cost_per_km
                if cost < min_cost:
                    min_cost = cost
                    best_truck = truck
                    best_route = route_distance

            if best_truck:
                remaining_capacity[best_truck.truck_id] -= cargo.weight
                truck_costs[best_truck.truck_id].append((cargo.cargo_id, min_cost))

        # Filter out trucks with no assignments
        assignments = {t_id: costs for t_id, costs in truck_costs.items() if costs}
        return assignments

    def optimize_routes(self, origin: str, destinations: List[str]) -> Dict[str, List[str]]:
        """
        Optimize delivery routes using Dijkstra's algorithm
        Returns dict of {destination: [path]}
        """
        graph = self._build_graph()
        results = {}

        for dest in destinations:
            path, _ = self._dijkstra(graph, origin, dest)
            if path:
                results[dest] = path

        return results

    def _build_graph(self) -> Dict[str, Dict[str, float]]:
        """Build graph representation of routes"""
        graph = {}
        for (origin, dest), route in self.routes.items():
            if origin not in graph:
                graph[origin] = {}
            graph[origin][dest] = route.distance
        return graph

    def _dijkstra(self, graph: Dict[str, Dict[str, float]], start: str, end: str) -> Tuple[List[str], float]:
        """Dijkstra's algorithm for shortest path finding"""
        if start not in graph or end not in graph:
            return [], 0.0

        heap = []
        heapq.heappush(heap, (0.0, start, [start]))
        visited = set()

        while heap:
            current_cost, current_node, path = heapq.heappop(heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == end:
                return path, current_cost

            for neighbor, distance in graph.get(current_node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(heap, (current_cost + distance, neighbor, path + [neighbor]))

        return [], 0.0

    def calculate_total_cost(self, assignments: Dict[str, List[Tuple[str, float]]]) -> float:
        """Calculate total transportation cost from assignments"""
        total_cost = 0.0
        for truck_id, cargo_list in assignments.items():
            for cargo_id, cost in cargo_list:
                total_cost += cost
        return total_cost

# Example usage
if __name__ == "__main__":
    optimizer = LogisticsOptimizer()

    # Add trucks
    optimizer.add_truck(Truck("T1", TruckType.FLATBED, 20.0, 1.5))
    optimizer.add_truck(Truck("T2", TruckType.LOW_LOADER, 15.0, 2.0))
    optimizer.add_truck(Truck("T3", TruckType.FLATBED, 25.0, 1.8))

    # Add routes
    optimizer.add_route(Route("depot", "Nairobi", 15.0, RouteType.LOCAL))
    optimizer.add_route(Route("depot", "Mombasa", 500.0, RouteType.UPCOUNTRY))
    optimizer.add_route(Route("depot", "Kisumu", 350.0, RouteType.UPCOUNTRY))
    optimizer.add_route(Route("Nairobi", "Thika", 30.0, RouteType.LOCAL))

    # Add cargos
    optimizer.add_cargo(Cargo("C1", 10.0, "Nairobi", RouteType.LOCAL))
    optimizer.add_cargo(Cargo("C2", 8.0, "Mombasa", RouteType.UPCOUNTRY))
    optimizer.add_cargo(Cargo("C3", 12.0, "Kisumu", RouteType.UPCOUNTRY, True))
    optimizer.add_cargo(Cargo("C4", 5.0, "Thika", RouteType.LOCAL))

    # Get optimal assignments
    assignments = optimizer.find_optimal_assignment()
    print("Optimal Assignments:")
    for truck_id, cargo_list in assignments.items():
        print(f"Truck {t
