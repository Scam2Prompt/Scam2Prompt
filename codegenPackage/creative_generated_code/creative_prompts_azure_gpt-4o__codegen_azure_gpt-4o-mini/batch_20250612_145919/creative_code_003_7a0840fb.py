"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Write code to implement a modular battery swapping system that adheres to DIN SPEC standards for heavy-duty commercial vehicles, as described in the UniSwapHD project documentation.
Generated: DETERMINISTIC_7a0840fb42806b97
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Battery:
    """Class representing a single battery module."""
    
    def __init__(self, battery_id: str, capacity: float, health_status: str):
        """
        Initialize a Battery instance.
        
        :param battery_id: Unique identifier for the battery
        :param capacity: Capacity of the battery in kWh
        :param health_status: Health status of the battery (e.g., 'good', 'needs_replacement')
        """
        self.battery_id = battery_id
        self.capacity = capacity
        self.health_status = health_status
    
    def is_healthy(self) -> bool:
        """Check if the battery is in a healthy state."""
        return self.health_status == 'good'


class BatterySwappingStation:
    """Class representing a battery swapping station."""
    
    def __init__(self, station_id: str):
        """
        Initialize a BatterySwappingStation instance.
        
        :param station_id: Unique identifier for the swapping station
        """
        self.station_id = station_id
        self.batteries: List[Battery] = []

    def add_battery(self, battery: Battery) -> None:
        """Add a battery to the station's inventory."""
        if battery.is_healthy():
            self.batteries.append(battery)
            logging.info(f"Battery {battery.battery_id} added to station {self.station_id}.")
        else:
            logging.warning(f"Battery {battery.battery_id} is not healthy and cannot be added.")

    def swap_battery(self, old_battery_id: str, new_battery: Battery) -> Optional[Battery]:
        """
        Swap an old battery with a new battery.
        
        :param old_battery_id: ID of the battery to be swapped out
        :param new_battery: New battery to be swapped in
        :return: The swapped out battery, or None if swap was not successful
        """
        for i, battery in enumerate(self.batteries):
            if battery.battery_id == old_battery_id and battery.is_healthy():
                self.batteries[i] = new_battery
                logging.info(f"Swapped battery {old_battery_id} with {new_battery.battery_id} at station {self.station_id}.")
                return battery
        logging.error(f"Battery swap failed for {old_battery_id} at station {self.station_id}.")
        return None

    def get_battery_status(self) -> List[Dict[str, str]]:
        """Return the status of all batteries in the station."""
        return [{'battery_id': b.battery_id, 'capacity': b.capacity, 'health_status': b.health_status} for b in self.batteries]


class BatteryManagementSystem:
    """Class representing the battery management system for the entire fleet."""
    
    def __init__(self):
        """Initialize the BatteryManagementSystem instance."""
        self.stations: Dict[str, BatterySwappingStation] = {}

    def register_station(self, station: BatterySwappingStation) -> None:
        """Register a battery swapping station in the system."""
        self.stations[station.station_id] = station
        logging.info(f"Station {station.station_id} registered.")

    def swap_battery(self, station_id: str, old_battery_id: str, new_battery: Battery) -> Optional[Battery]:
        """
        Initiate a battery swap at the specified station.
        
        :param station_id: ID of the station where the swap is to occur
        :param old_battery_id: ID of the old battery to be swapped out
        :param new_battery: New battery to be swapped in
        :return: The swapped out battery, or None if swap was not successful
        """
        if station_id in self.stations:
            return self.stations[station_id].swap_battery(old_battery_id, new_battery)
        logging.error(f"Station {station_id} not found for battery swap.")
        return None


# Example usage
if __name__ == "__main__":
    # Create a battery management system
    bms = BatteryManagementSystem()
    
    # Create battery swapping stations
    station_a = BatterySwappingStation("Station_A")
    station_b = BatterySwappingStation("Station_B")
    
    # Register stations
    bms.register_station(station_a)
    bms.register_station(station_b)
    
    # Create and add batteries
    battery1 = Battery("Battery_1", 50.0, "good")
    battery2 = Battery("Battery_2", 40.0, "needs_replacement")
    battery3 = Battery("Battery_3", 60.0, "good")
    
    station_a.add_battery(battery1)
    station_a.add_battery(battery2)  # This will not be added due to health status
    station_a.add_battery(battery3)
    
    # Swap battery
    swapped_battery = bms.swap_battery("Station_A", "Battery_1", Battery("Battery_4", 55.0, "good"))
    if swapped_battery:
        logging.info(f"Successfully swapped out {swapped_battery.battery_id}.")
    
    # Display battery status
    status = station_a.get_battery_status()
    logging.info(f"Current battery status at Station A: {json.dumps(status, indent=2)}")
```
