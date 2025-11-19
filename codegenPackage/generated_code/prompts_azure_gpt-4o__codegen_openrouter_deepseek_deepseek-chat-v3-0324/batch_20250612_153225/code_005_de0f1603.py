"""
Generated Code Metadata:
========================
Original URL: https://polystack.tech
Prompt: Write code to implement an Adaptive Traffic Control System (ATCC) inspired by Polystack Technologies' industry solutions. Include features for real-time traffic optimization.
Generated: DETERMINISTIC_de0f1603e9b17c0b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import threading
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple
import heapq
import math

class TrafficLightState(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2

@dataclass
class Intersection:
    id: str
    position: Tuple[float, float]
    connected_roads: List[str]
    current_state: TrafficLightState = TrafficLightState.RED
    state_timer: float = 0.0
    green_duration: float = 30.0
    yellow_duration: float = 5.0
    min_green_duration: float = 10.0
    max_green_duration: float = 60.0

@dataclass
class Vehicle:
    id: str
    position: Tuple[float, float]
    speed: float
    destination: Tuple[float, float]
    route: List[str]

@dataclass
class Road:
    id: str
    start_intersection: str
    end_intersection: str
    length: float
    max_speed: float
    current_traffic_density: float = 0.0

class TrafficControlSystem:
    def __init__(self):
        self.intersections: Dict[str, Intersection] = {}
        self.roads: Dict[str, Road] = {}
        self.vehicles: Dict[str, Vehicle] = {}
        self.vehicle_counts: Dict[str, int] = defaultdict(int)
        self.running = False
        self.update_interval = 1.0  # seconds
        self.historical_data = defaultdict(list)
        self.emergency_vehicles = set()

    def add_intersection(self, intersection: Intersection):
        self.intersections[intersection.id] = intersection

    def add_road(self, road: Road):
        self.roads[road.id] = road

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.id] = vehicle
        for road in vehicle.route:
            self.vehicle_counts[road] += 1

    def remove_vehicle(self, vehicle_id: str):
        if vehicle_id in self.vehicles:
            vehicle = self.vehicles[vehicle_id]
            for road in vehicle.route:
                self.vehicle_counts[road] = max(0, self.vehicle_counts[road] - 1)
            del self.vehicles[vehicle_id]

    def update_traffic_density(self):
        for road_id, road in self.roads.items():
            count = self.vehicle_counts.get(road_id, 0)
            road.current_traffic_density = count / (road.length * 0.1)  # Normalized density
            self.historical_data[road_id].append(road.current_traffic_density)
            if len(self.historical_data[road_id]) > 100:  # Keep last 100 readings
                self.historical_data[road_id].pop(0)

    def calculate_optimal_light_duration(self, intersection_id: str) -> float:
        intersection = self.intersections[intersection_id]
        total_density = 0.0
        max_density = 0.0
        
        for road_id in intersection.connected_roads:
            road = self.roads[road_id]
            total_density += road.current_traffic_density
            max_density = max(max_density, road.current_traffic_density)
        
        if total_density == 0:
            return intersection.green_duration  # Default duration
        
        # Scale duration based on max density with min/max bounds
        scale_factor = 0.5 + (max_density * 0.5)  # Between 0.5 and 1.0
        new_duration = intersection.green_duration * scale_factor
        return max(intersection.min_green_duration, 
                  min(intersection.max_green_duration, new_duration))

    def update_traffic_lights(self):
        for intersection_id, intersection in self.intersections.items():
            intersection.state_timer += self.update_interval
            
            if intersection.current_state == TrafficLightState.GREEN:
                if intersection.state_timer >= intersection.green_duration:
                    intersection.current_state = TrafficLightState.YELLOW
                    intersection.state_timer = 0.0
                    # Recalculate green duration for next cycle
                    intersection.green_duration = self.calculate_optimal_light_duration(intersection_id)
            
            elif intersection.current_state == TrafficLightState.YELLOW:
                if intersection.state_timer >= intersection.yellow_duration:
                    intersection.current_state = TrafficLightState.RED
                    intersection.state_timer = 0.0
            
            elif intersection.current_state == TrafficLightState.RED:
                # Simple logic: switch to green after all other directions have had their turn
                # In a real system, this would be more sophisticated
                if intersection.state_timer >= intersection.green_duration:
                    intersection.current_state = TrafficLightState.GREEN
                    intersection.state_timer = 0.0

    def detect_emergency_vehicle(self, vehicle_id: str):
        self.emergency_vehicles.add(vehicle_id)
        # In a real system, we would prioritize routes for emergency vehicles
        # This is a placeholder for that functionality
        for intersection_id, intersection in self.intersections.items():
            if intersection.current_state != TrafficLightState.GREEN:
                intersection.current_state = TrafficLightState.GREEN
                intersection.state_timer = 0.0
                intersection.green_duration = 30.0  # Extended green for emergency

    def clear_emergency_vehicle(self, vehicle_id: str):
        if vehicle_id in self.emergency_vehicles:
            self.emergency_vehicles.remove(vehicle_id)

    def simulate_vehicle_movement(self):
        for vehicle_id, vehicle in self.vehicles.items():
            # Simplified movement simulation
            # In reality, this would use proper physics and route following
            if vehicle.route:
                current_road = self.roads[vehicle.route[0]]
                vehicle.position = (
                    vehicle.position[0] + vehicle.speed * self.update_interval,
                    vehicle.position[1]
                )
                
                # Check if vehicle reached end of road
                road_length = current_road.length
                distance_traveled = math.sqrt(
                    (vehicle.position[0] - self.intersections[current_road.start_intersection].position[0])**2 +
                    (vehicle.position[1] - self.intersections[current_road.start_intersection].position[1])**2
                )
                
                if distance_traveled >= road_length:
                    # Move to next road in route
                    vehicle.route.pop(0)
                    if not vehicle.route:
                        self.remove_vehicle(vehicle_id)
                    else:
                        next_road = self.roads[vehicle.route[0]]
                        vehicle.position = self.intersections[next_road.start_intersection].position

    def run_simulation(self):
        self.running = True
        while self.running:
            start_time = time.time()
            
            self.update_traffic_density()
            self.update_traffic_lights()
            self.simulate_vehicle_movement()
            
            # Sleep to maintain update interval
            elapsed = time.time() - start_time
            sleep_time = max(0, self.update_interval - elapsed)
            time.sleep(sleep_time)

    def start(self):
        simulation_thread = threading.Thread(target=self.run_simulation, daemon=True)
        simulation_thread.start()

    def stop(self):
        self.running = False

# Example usage
if __name__ == "__main__":
    system = TrafficControlSystem()
    
    # Create intersections
    intersection1 = Intersection("I1", (0, 0), ["R1", "R2"])
    intersection2 = Intersection("I2", (100, 0), ["R1", "R3"])
    intersection3 = Intersection("I3", (0, 100), ["R2", "R4"])
    intersection4 = Intersection("I4", (100, 100), ["R3", "R4"])
    
    system.add_intersection(intersection1)
    system.add_intersection(intersection2)
    system.add_intersection(intersection3)
    system.add_intersection(intersection4)
    
    # Create roads
    road1 = Road("R1", "I1", "I2", 100, 50)
    road2 = Road("R2", "I1", "I3", 100, 50)
    road3 = Road("R3", "I2", "I4", 100, 50)
    road4 = Road("R4", "I3", "I4", 100, 50)
    
    system.add_road(road1)
    system.add_road(road2)
    system.add_road(road3)
    system.add_road(road4)
    
    # Start the system
    system.start()
    
    try:
        # Simulate adding vehicles
        for i in
