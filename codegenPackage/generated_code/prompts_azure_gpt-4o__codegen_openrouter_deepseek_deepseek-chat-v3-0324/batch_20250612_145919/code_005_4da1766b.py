"""
Generated Code Metadata:
========================
Original URL: https://uniswaphd.de
Prompt: Create a simulation model in Python to test the practical performance of a standardized battery swapping system for heavy-duty trucks, including compatibility with multiple manufacturers, as discussed in the UniSwapHD project.
Generated: DETERMINISTIC_4da1766b71b17627
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import simpy
import random
import numpy as np
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class BatteryStatus(Enum):
    """Enum representing battery status."""
    FULL = auto()
    CHARGING = auto()
    DEPLETED = auto()

class TruckStatus(Enum):
    """Enum representing truck status."""
    IN_TRANSIT = auto()
    WAITING_FOR_SWAP = auto()
    SWAPPING = auto()
    CHARGING = auto()

@dataclass
class Battery:
    """Class representing a battery."""
    id: str
    capacity: float  # kWh
    current_charge: float  # kWh
    manufacturer: str
    status: BatteryStatus
    charge_rate: float  # kW

@dataclass
class Truck:
    """Class representing a truck."""
    id: str
    battery: Battery
    consumption_rate: float  # kWh/km
    status: TruckStatus
    manufacturer: str

class BatterySwapStation:
    """Class representing a battery swap station."""
    def __init__(self, env: simpy.Environment, num_swapping_bays: int, num_charging_slots: int):
        self.env = env
        self.swapping_bays = simpy.Resource(env, num_swapping_bays)
        self.charging_slots = simpy.Resource(env, num_charging_slots)
        self.available_batteries: Dict[str, List[Battery]] = defaultdict(list)
        self.charging_batteries: Dict[str, List[Battery]] = defaultdict(list)
        self.swap_log = []
        self.charging_log = []

    def add_battery(self, battery: Battery) -> None:
        """Add a battery to the station's inventory."""
        if battery.status == BatteryStatus.FULL:
            self.available_batteries[battery.manufacturer].append(battery)
        elif battery.status == BatteryStatus.DEPLETED:
            self.charging_batteries[battery.manufacturer].append(battery)

    def request_swap(self, truck: Truck) -> Optional[Battery]:
        """Request a battery swap for a truck."""
        manufacturer = truck.manufacturer
        if manufacturer in self.available_batteries and self.available_batteries[manufacturer]:
            return self.available_batteries[manufacturer].pop()
        return None

    def start_charging(self, battery: Battery) -> None:
        """Start charging a depleted battery."""
        self.charging_batteries[battery.manufacturer].append(battery)
        battery.status = BatteryStatus.CHARGING

    def complete_charging(self, battery: Battery) -> None:
        """Complete charging a battery and make it available."""
        if battery in self.charging_batteries[battery.manufacturer]:
            self.charging_batteries[battery.manufacturer].remove(battery)
        battery.status = BatteryStatus.FULL
        battery.current_charge = battery.capacity
        self.available_batteries[battery.manufacturer].append(battery)

def truck_process(env: simpy.Environment, truck: Truck, station: BatterySwapStation, route_length: float):
    """Simulate a truck's operation including battery swapping."""
    while True:
        # Truck is in transit
        truck.status = TruckStatus.IN_TRANSIT
        travel_time = route_length / 80  # Assuming 80 km/h average speed
        battery_drain = route_length * truck.consumption_rate
        
        if truck.battery.current_charge < battery_drain:
            # Not enough charge for the route, must swap
            yield env.timeout(travel_time * (truck.battery.current_charge / battery_drain))
            truck.battery.current_charge = 0
            truck.battery.status = BatteryStatus.DEPLETED
        else:
            # Complete the route
            yield env.timeout(travel_time)
            truck.battery.current_charge -= battery_drain
        
        # Arrive at station for swap
        truck.status = TruckStatus.WAITING_FOR_SWAP
        arrival_time = env.now
        
        with station.swapping_bays.request() as request:
            yield request
            truck.status = TruckStatus.SWAPPING
            swap_start = env.now
            wait_time = swap_start - arrival_time
            
            # Perform battery swap
            new_battery = station.request_swap(truck)
            if new_battery:
                # Log the swap
                station.swap_log.append({
                    'time': env.now,
                    'truck_id': truck.id,
                    'old_battery': truck.battery.id,
                    'new_battery': new_battery.id,
                    'wait_time': wait_time
                })
                
                # Return old battery to station for charging
                old_battery = truck.battery
                station.add_battery(old_battery)
                
                # Assign new battery to truck
                truck.battery = new_battery
                
                # Simulate swap time (5 minutes)
                yield env.timeout(5 / 60)
            else:
                # No battery available, must wait (simplified)
                yield env.timeout(30 / 60)  # Wait 30 minutes
            
            truck.status = TruckStatus.IN_TRANSIT

def charging_process(env: simpy.Environment, station: BatterySwapStation):
    """Simulate battery charging at the station."""
    while True:
        for manufacturer, batteries in station.charging_batteries.items():
            for battery in batteries[:]:  # Create a copy for iteration
                if battery.status == BatteryStatus.DEPLETED:
                    with station.charging_slots.request() as request:
                        yield request
                        battery.status = BatteryStatus.CHARGING
                        charge_time = (battery.capacity - battery.current_charge) / battery.charge_rate
                        
                        # Log charging start
                        station.charging_log.append({
                            'time': env.now,
                            'battery_id': battery.id,
                            'action': 'start_charging',
                            'manufacturer': manufacturer
                        })
                        
                        yield env.timeout(charge_time)
                        station.complete_charging(battery)
                        
                        # Log charging completion
                        station.charging_log.append({
                            'time': env.now,
                            'battery_id': battery.id,
                            'action': 'complete_charging',
                            'manufacturer': manufacturer
                        })
        yield env.timeout(1)  # Check every hour

def simulate(
    num_trucks: int,
    num_swapping_bays: int,
    num_charging_slots: int,
    simulation_duration: float,
    manufacturers: List[str],
    battery_capacity: float,
    charge_rate: float
) -> Tuple[BatterySwapStation, List[Dict]]:
    """Run the simulation."""
    env = simpy.Environment()
    station = BatterySwapStation(env, num_swapping_bays, num_charging_slots)
    
    # Initialize batteries
    for i in range(num_trucks * 2):  # 2 batteries per truck
        manufacturer = random.choice(manufacturers)
        battery = Battery(
            id=f"battery_{i}",
            capacity=battery_capacity,
            current_charge=battery_capacity,
            manufacturer=manufacturer,
            status=BatteryStatus.FULL,
            charge_rate=charge_rate
        )
        station.add_battery(battery)
    
    # Initialize trucks
    trucks = []
    for i in range(num_trucks):
        manufacturer = random.choice(manufacturers)
        battery = station.available_batteries[manufacturer].pop()
        truck = Truck(
            id=f"truck_{i}",
            battery=battery,
            consumption_rate=1.5 + random.random() * 0.5,  # 1.5-2.0 kWh/km
            status=TruckStatus.IN_TRANSIT,
            manufacturer=manufacturer
        )
        trucks.append(truck)
        env.process(truck_process(env, truck, station, route_length=400))  # 400 km route
    
    # Start charging process
    env.process(charging_process(env, station))
    
    # Run simulation
    env.run(until=simulation_duration)
    
    return station, trucks

def analyze_results(station: BatterySwapStation, trucks: List[Truck]) -> Dict:
    """Analyze simulation results."""
    total_swaps = len(station.swap_log)
    total_charging_cycles = len([x for x in station.charging_log if x['action'] == 'complete_charging'])
    
    if total_swaps > 0:
        avg_wait_time = sum(swap['wait_time'] for swap in station.swap_log) / total_swaps
    else:
        avg_wait_time = 0
    
    battery_utilization = {}
    for manufacturer, batteries in station.available_batteries.items():
        battery_utilization[manufacturer] = len(batteries) / (len(batteries) + len(station.charging_batteries.get(manufacturer, [])))
    
    return {
        'total_swaps': total_swaps,
        'total_charging_cycles': total_charging_cycles,
        'avg_wait_time': avg_wait_time,
        'battery_util
