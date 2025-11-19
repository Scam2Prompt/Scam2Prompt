"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Generate code for calculating delivery schedules and optimizing routes for a fleet of chiller vans equipped with GPS tracking, as mentioned on RefrigeratorTransport.com.
Generated: DETERMINISTIC_4996284f3b02e248
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
import math
from collections import defaultdict
import json

# Constants
EARTH_RADIUS_KM = 6371.0
MAX_VAN_CAPACITY = 1000  # kg
AVERAGE_SPEED = 50  # km/h
WORKING_HOURS_PER_DAY = 8  # hours
MAX_DELIVERY_TIME_HOURS = 24  # Max allowed delivery time in hours

class Location:
    """Represents a geographical location with latitude and longitude."""
    
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon
    
    def distance_to(self, other: 'Location') -> float:
        """Calculate Haversine distance between two locations in kilometers."""
        lat1, lon1 = math.radians(self.lat), math.radians(self.lon)
        lat2, lon2 = math.radians(other.lat), math.radians(other.lon)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return EARTH_RADIUS_KM * c

class DeliveryPoint:
    """Represents a delivery point with location, time window, and demand."""
    
    def __init__(self, id: str, location: Location, demand: float, 
                 time_window_start: datetime, time_window_end: datetime):
        self.id = id
        self.location = location
        self.demand = demand
        self.time_window_start = time_window_start
        self.time_window_end = time_window_end
    
    def __repr__(self):
        return f"DeliveryPoint(id={self.id}, demand={self.demand})"

class ChillerVan:
    """Represents a chiller van with current location and capacity."""
    
    def __init__(self, id: str, current_location: Location, capacity: float = MAX_VAN_CAPACITY):
        self.id = id
        self.current_location = current_location
        self.capacity = capacity
        self.current_load = 0.0
        self.route = []
        self.schedule = []
    
    def can_serve(self, delivery_point: DeliveryPoint) -> bool:
        """Check if van can serve the delivery point considering capacity."""
        return self.current_load + delivery_point.demand <= self.capacity
    
    def add_to_route(self, delivery_point: DeliveryPoint):
        """Add delivery point to van's route."""
        if not self.can_serve(delivery_point):
            raise ValueError("Cannot add delivery point - exceeds capacity")
        
        self.route.append(delivery_point)
        self.current_load += delivery_point.demand
    
    def clear_route(self):
        """Clear the current route and reset load."""
        self.route = []
        self.current_load = 0.0
    
    def __repr__(self):
        return f"ChillerVan(id={self.id}, load={self.current_load}/{self.capacity})"

class RouteOptimizer:
    """Optimizes delivery routes for a fleet of chiller vans."""
    
    def __init__(self, vans: List[ChillerVan], delivery_points: List[DeliveryPoint]):
        self.vans = vans
        self.delivery_points = delivery_points
        self.distance_matrix = self._build_distance_matrix()
    
    def _build_distance_matrix(self) -> Dict[str, Dict[str, float]]:
        """Build a distance matrix between all locations."""
        all_locations = [van.current_location for van in self.vans] + \
                       [dp.location for dp in self.delivery_points]
        all_ids = [f"van_{van.id}" for van in self.vans] + \
                  [dp.id for dp in self.delivery_points]
        
        matrix = defaultdict(dict)
        for i, loc1 in enumerate(all_locations):
            for j, loc2 in enumerate(all_locations):
                if i != j:
                    matrix[all_ids[i]][all_ids[j]] = loc1.distance_to(loc2)
        return matrix
    
    def _calculate_time(self, distance_km: float) -> timedelta:
        """Calculate travel time based on distance."""
        hours = distance_km / AVERAGE_SPEED
        return timedelta(hours=hours)
    
    def _calculate_route_time(self, route: List[DeliveryPoint], start_location: Location) -> timedelta:
        """Calculate total time for a route."""
        total_time = timedelta()
        current_location = start_location
        
        for dp in route:
            distance = self.distance_matrix.get(f"van_{current_location.id}", {}).get(dp.id, 0)
            if distance == 0:
                distance = current_location.distance_to(dp.location)
            total_time += self._calculate_time(distance)
            current_location = dp.location
        
        return total_time
    
    def _check_time_window(self, route: List[DeliveryPoint], start_time: datetime, 
                          start_location: Location) -> bool:
        """Check if route satisfies all time windows."""
        current_time = start_time
        current_location = start_location
        
        for dp in route:
            distance = self.distance_matrix.get(f"van_{current_location.id}", {}).get(dp.id, 0)
            if distance == 0:
                distance = current_location.distance_to(dp.location)
            
            travel_time = self._calculate_time(distance)
            arrival_time = current_time + travel_time
            
            if arrival_time > dp.time_window_end:
                return False
            
            # Ensure we don't arrive too early
            if arrival_time < dp.time_window_start:
                arrival_time = dp.time_window_start
            
            current_time = arrival_time
            current_location = dp.location
        
        return True
    
    def _nearest_neighbor(self, van: ChillerVan, remaining_points: List[DeliveryPoint]) -> List[DeliveryPoint]:
        """Generate a route using nearest neighbor heuristic."""
        route = []
        current_location = van.current_location
        remaining_points = remaining_points.copy()
        
        while remaining_points and van.current_load < van.capacity:
            # Find nearest point that can be served within time window
            nearest = None
            min_distance = float('inf')
            
            for dp in remaining_points:
                if not van.can_serve(dp):
                    continue
                
                distance = self.distance_matrix.get(f"van_{current_location.id}", {}).get(dp.id, 0)
                if distance == 0:
                    distance = current_location.distance_to(dp.location)
                
                if distance < min_distance:
                    min_distance = distance
                    nearest = dp
            
            if nearest is None:
                break
            
            # Check if adding this point would violate time constraints
            temp_route = route + [nearest]
            if self._check_time_window(temp_route, datetime.now(), van.current_location):
                route.append(nearest)
                van.add_to_route(nearest)
                remaining_points.remove(nearest)
                current_location = nearest.location
            else:
                break
        
        return route
    
    def optimize_routes(self) -> Dict[str, List[Dict]]:
        """Optimize routes for all vans using a greedy algorithm."""
        remaining_points = self.delivery_points.copy()
        optimized_routes = {}
        
        for van in self.vans:
            van.clear_route()
            route = self._nearest_neighbor(van, remaining_points)
            
            if not route:
                optimized_routes[van.id] = []
                continue
            
            # Calculate schedule with estimated times
            schedule = []
            current_time = datetime.now()
            current_location = van.current_location
            
            for dp in route:
                distance = self.distance_matrix.get(f"van_{current_location.id}", {}).get(dp.id, 0)
                if distance == 0:
                    distance = current_location.distance_to(dp.location)
                
                travel_time = self._calculate_time(distance)
                arrival_time = current_time + travel_time
                
                # Adjust for time window if arriving too early
                if arrival_time < dp.time_window_start:
                    arrival_time = dp.time_window_start
                
                schedule.append({
                    'delivery_point_id': dp.id,
                    'arrival_time': arrival_time.isoformat(),
                    'departure_time': (arrival_time + timedelta(minutes=30)).isoformat(),  # 30 min for delivery
                    'location': {'lat': dp.location.lat, 'lon': dp.location.lon}
                })
                
                current_time = arrival_time + timedelta(minutes=30)
                current_location = dp.location
            
            optimized_routes[van.id] = schedule
            remaining_points = [dp for dp in remaining_points if dp not in route]
        
        return optimized_routes

class GPSDataProcessor:
    """Processes real-time GPS data from chiller vans."""
    
    @staticmethod
    def parse_gps_data(gps_data: Dict) -> Tuple[float, float, datetime]:
        """Parse raw GPS data into location and timestamp."""
        try:
            lat = float(gps_data
