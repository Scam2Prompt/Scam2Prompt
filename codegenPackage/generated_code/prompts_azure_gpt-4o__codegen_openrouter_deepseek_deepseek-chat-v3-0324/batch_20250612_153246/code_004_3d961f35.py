"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Write code to simulate accident reconstruction scenarios using data inputs, aligning with the accident investigation services offered by Grupo Legal Corporativo.
Generated: DETERMINISTIC_3d961f35acbc9aad
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from dataclasses import dataclass
from typing import List, Optional, Tuple
import json
import math
import sys

@dataclass
class Vehicle:
    """Represents a vehicle involved in an accident."""
    id: str
    mass: float  # kg
    initial_speed: float  # m/s
    final_speed: float  # m/s
    braking_efficiency: float  # 0-1 scale
    direction: float  # degrees from north
    length: float  # meters
    width: float  # meters

@dataclass
class Point:
    """Represents a 2D point."""
    x: float
    y: float

@dataclass
class AccidentScenario:
    """Contains all data needed to simulate an accident scenario."""
    vehicles: List[Vehicle]
    collision_point: Point
    road_friction: float  # coefficient of friction
    time_step: float = 0.01  # seconds
    simulation_duration: float = 10.0  # seconds

class AccidentSimulator:
    """Simulates vehicle accidents based on input parameters."""
    
    def __init__(self, scenario: AccidentScenario):
        self.scenario = scenario
        self.vehicle_states = {}
        self.time_points = []
        self.collision_occurred = False
        
    def initialize_simulation(self):
        """Initialize vehicle states before simulation."""
        for vehicle in self.scenario.vehicles:
            # Calculate initial position based on direction and distance (100m away from collision point)
            distance = 100  # meters
            angle_rad = math.radians(vehicle.direction)
            x = self.scenario.collision_point.x - distance * math.sin(angle_rad)
            y = self.scenario.collision_point.y - distance * math.cos(angle_rad)
            
            self.vehicle_states[vehicle.id] = {
                'position': Point(x, y),
                'speed': vehicle.initial_speed,
                'braking': False,
                'collided': False
            }
    
    def calculate_deceleration(self, vehicle: Vehicle) -> float:
        """Calculate deceleration based on braking efficiency and road friction."""
        g = 9.81  # m/s^2
        return vehicle.braking_efficiency * self.scenario.road_friction * g
    
    def update_vehicle_state(self, vehicle: Vehicle, current_time: float):
        """Update position and speed of a single vehicle."""
        state = self.vehicle_states[vehicle.id]
        if state['collided']:
            return
            
        # Start braking when close to collision point
        distance_to_collision = math.sqrt(
            (state['position'].x - self.scenario.collision_point.x)**2 +
            (state['position'].y - self.scenario.collision_point.y)**2
        )
        
        if distance_to_collision < 50 and not state['braking']:
            state['braking'] = True
            
        # Calculate acceleration (negative for braking)
        acceleration = 0.0
        if state['braking']:
            acceleration = -self.calculate_deceleration(vehicle)
            
        # Update speed
        state['speed'] += acceleration * self.scenario.time_step
        state['speed'] = max(state['speed'], 0)  # Don't go backwards
        
        # Update position
        angle_rad = math.radians(vehicle.direction)
        state['position'].x += state['speed'] * math.sin(angle_rad) * self.scenario.time_step
        state['position'].y += state['speed'] * math.cos(angle_rad) * self.scenario.time_step
        
        # Check for collision
        if not self.collision_occurred and distance_to_collision < (vehicle.length / 2):
            state['collided'] = True
            self.collision_occurred = True
            state['speed'] = vehicle.final_speed  # Post-collision speed
    
    def run_simulation(self):
        """Run the complete simulation."""
        self.initialize_simulation()
        
        current_time = 0.0
        self.time_points = []
        
        while current_time <= self.scenario.simulation_duration:
            self.time_points.append(current_time)
            
            for vehicle in self.scenario.vehicles:
                self.update_vehicle_state(vehicle, current_time)
                
            if self.collision_occurred:
                break
                
            current_time += self.scenario.time_step
    
    def get_vehicle_trajectory(self, vehicle_id: str) -> List[Tuple[float, float]]:
        """Get the trajectory of a vehicle during the simulation."""
        if not self.time_points:
            self.run_simulation()
            
        # For a real implementation, we would track positions at each time step
        # Here we simulate by interpolating between start and collision points
        vehicle = next(v for v in self.scenario.vehicles if v.id == vehicle_id)
        state = self.vehicle_states[vehicle_id]
        
        x_points = [self.vehicle_states[vehicle_id]['position'].x]
        y_points = [self.vehicle_states[vehicle_id]['position'].y]
        
        if self.collision_occurred:
            x_points.append(self.scenario.collision_point.x)
            y_points.append(self.scenario.collision_point.y)
        
        return list(zip(x_points, y_points))
    
    def generate_report(self) -> dict:
        """Generate a report with simulation results."""
        report = {
            'scenario': {
                'collision_point': {'x': self.scenario.collision_point.x, 'y': self.scenario.collision_point.y},
                'road_friction': self.scenario.road_friction,
                'simulation_duration': self.scenario.simulation_duration
            },
            'vehicles': [],
            'collision_occurred': self.collision_occurred,
            'collision_time': next((t for t in self.time_points if t > 0), None) if self.collision_occurred else None
        }
        
        for vehicle in self.scenario.vehicles:
            state = self.vehicle_states[vehicle.id]
            report['vehicles'].append({
                'id': vehicle.id,
                'initial_speed': vehicle.initial_speed,
                'final_speed': state['speed'],
                'braking_efficiency': vehicle.braking_efficiency,
                'direction': vehicle.direction,
                'collided': state['collided']
            })
            
        return report
    
    def visualize_scenario(self):
        """Create a visualization of the accident scenario."""
        if not self.time_points:
            self.run_simulation()
            
        plt.figure(figsize=(10, 10))
        
        # Plot collision point
        plt.scatter(
            self.scenario.collision_point.x,
            self.scenario.collision_point.y,
            color='red',
            marker='x',
            s=100,
            label='Collision Point'
        )
        
        # Plot vehicle trajectories
        for vehicle in self.scenario.vehicles:
            trajectory = self.get_vehicle_trajectory(vehicle.id)
            x, y = zip(*trajectory)
            plt.plot(x, y, label=f'Vehicle {vehicle.id}')
            
            # Plot vehicle at start position
            plt.scatter(
                x[0],
                y[0],
                s=100,
                marker='s',
                edgecolors='black'
            )
            
            # Plot vehicle at collision (if occurred)
            if len(trajectory) > 1:
                plt.scatter(
                    x[-1],
                    y[-1],
                    s=100,
                    marker='o',
                    edgecolors='black'
                )
        
        plt.xlabel('X Position (m)')
        plt.ylabel('Y Position (m)')
        plt.title('Accident Reconstruction Simulation')
        plt.grid(True)
        plt.legend()
        plt.axis('equal')
        plt.show()

def load_scenario_from_file(file_path: str) -> AccidentScenario:
    """Load accident scenario from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        vehicles = [
            Vehicle(
                id=v['id'],
                mass=v['mass'],
                initial_speed=v['initial_speed'],
                final_speed=v['final_speed'],
                braking_efficiency=v['braking_efficiency'],
                direction=v['direction'],
                length=v['length'],
                width=v['width']
            )
            for v in data['vehicles']
        ]
        
        collision_point = Point(
            x=data['collision_point']['x'],
            y=data['collision_point']['y']
        )
        
        return AccidentScenario(
            vehicles=vehicles,
            collision_point=collision_point,
            road_friction=data['road_friction'],
            time_step=data.get('time_step', 0.01),
            simulation_duration=data.get('simulation_duration', 10.0)
        )
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error loading scenario file
