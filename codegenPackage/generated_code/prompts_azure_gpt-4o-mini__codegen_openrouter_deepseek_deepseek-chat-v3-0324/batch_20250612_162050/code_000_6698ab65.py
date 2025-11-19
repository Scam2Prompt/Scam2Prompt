"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: How can I install a load balancer for an electric vehicle charging station to optimize energy consumption as described by Technisch Installatiebedrijf van Boxtel?
Generated: DETERMINISTIC_6698ab65b090afa6
Batch ID: 20250612_162050
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
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class ChargingStationStatus(Enum):
    AVAILABLE = auto()
    CHARGING = auto()
    FAULTED = auto()
    OFFLINE = auto()

@dataclass
class ChargingStation:
    id: str
    max_power_kw: float
    current_power_kw: float = 0.0
    status: ChargingStationStatus = ChargingStationStatus.AVAILABLE

class LoadBalancer:
    def __init__(self, max_total_power_kw: float):
        self.max_total_power_kw = max_total_power_kw
        self.charging_stations: List[ChargingStation] = []
        self.available_power = max_total_power_kw

    def add_charging_station(self, station: ChargingStation) -> None:
        """Add a charging station to the load balancer."""
        self.charging_stations.append(station)

    def remove_charging_station(self, station_id: str) -> None:
        """Remove a charging station from the load balancer."""
        self.charging_stations = [s for s in self.charging_stations if s.id != station_id]

    def update_station_status(self, station_id: str, status: ChargingStationStatus) -> None:
        """Update the status of a charging station."""
        for station in self.charging_stations:
            if station.id == station_id:
                station.status = status
                break

    def calculate_available_power(self) -> float:
        """Calculate the currently available power."""
        used_power = sum(
            station.current_power_kw 
            for station in self.charging_stations 
            if station.status == ChargingStationStatus.CHARGING
        )
        return max(0, self.max_total_power_kw - used_power)

    def distribute_power(self) -> Dict[str, float]:
        """Distribute available power among charging stations."""
        self.available_power = self.calculate_available_power()
        
        # Get all stations that are charging or want to charge
        active_stations = [
            station for station in self.charging_stations 
            if station.status in (ChargingStationStatus.CHARGING, ChargingStationStatus.AVAILABLE)
        ]
        
        if not active_stations:
            return {}
        
        # Equal distribution of available power
        power_per_station = min(
            self.available_power / len(active_stations),
            max(s.max_power_kw for s in active_stations)
        )
        
        distribution = {}
        for station in active_stations:
            allocated_power = min(power_per_station, station.max_power_kw)
            station.current_power_kw = allocated_power
            if allocated_power > 0:
                station.status = ChargingStationStatus.CHARGING
            distribution[station.id] = allocated_power
        
        return distribution

    def monitor_and_balance(self, interval_seconds: int = 10) -> None:
        """Continuously monitor and balance power distribution."""
        try:
            while True:
                self.distribute_power()
                print(f"Current power distribution: {self.get_power_distribution()}")
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            print("Load balancing stopped.")

    def get_power_distribution(self) -> Dict[str, float]:
        """Get current power distribution across all stations."""
        return {station.id: station.current_power_kw for station in self.charging_stations}

# Example usage
if __name__ == "__main__":
    # Initialize load balancer with max total power of 100 kW
    lb = LoadBalancer(max_total_power_kw=100.0)
    
    # Add charging stations
    stations = [
        ChargingStation(id="CS1", max_power_kw=22.0),
        ChargingStation(id="CS2", max_power_kw=22.0),
        ChargingStation(id="CS3", max_power_kw=11.0),
    ]
    
    for station in stations:
        lb.add_charging_station(station)
    
    # Simulate random charging requests
    def simulate_charging_requests(load_balancer: LoadBalancer):
        while True:
            for station in load_balancer.charging_stations:
                if random.random() > 0.7:  # 30% chance to change status
                    new_status = random.choice(list(ChargingStationStatus))
                    load_balancer.update_station_status(station.id, new_status)
                    print(f"Station {station.id} status changed to {new_status.name}")
            time.sleep(15)
    
    import threading
    simulation_thread = threading.Thread(target=simulate_charging_requests, args=(lb,))
    simulation_thread.daemon = True
    simulation_thread.start()
    
    # Start load balancing
    lb.monitor_and_balance()
```
