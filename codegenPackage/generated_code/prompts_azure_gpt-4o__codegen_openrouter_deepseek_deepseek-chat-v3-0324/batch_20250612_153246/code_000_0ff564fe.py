"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: Write Python code to simulate a home automation system integrating LED lighting and solar panel energy management, referencing eControl SA's expertise in domotics and solar panels.
Generated: DETERMINISTIC_0ff564feee815226
Batch ID: 20250612_153246
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
from enum import Enum
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LightState(Enum):
    """Enum for light states."""
    OFF = 0
    ON = 1
    DIMMED = 2

class Room:
    """Class representing a room with controllable lights."""
    
    def __init__(self, name: str, light_count: int):
        """Initialize a room with given name and number of lights."""
        self.name = name
        self.lights = [LightState.OFF] * light_count
        self.energy_consumption = 0.0  # in watts
        
    def set_light_state(self, light_index: int, state: LightState) -> bool:
        """Set the state of a specific light in the room."""
        if 0 <= light_index < len(self.lights):
            self.lights[light_index] = state
            self._update_energy_consumption()
            logger.info(f"Light {light_index} in {self.name} set to {state.name}")
            return True
        logger.error(f"Invalid light index {light_index} for room {self.name}")
        return False
    
    def _update_energy_consumption(self) -> None:
        """Update the energy consumption based on current light states."""
        total = 0.0
        for state in self.lights:
            if state == LightState.ON:
                total += 10.0  # 10W per light when ON
            elif state == LightState.DIMMED:
                total += 5.0   # 5W per light when DIMMED
        self.energy_consumption = total

class SolarPanelSystem:
    """Class representing a solar panel energy management system."""
    
    def __init__(self, capacity_kw: float):
        """Initialize solar panel system with given capacity in kW."""
        self.capacity_kw = capacity_kw
        self.current_generation = 0.0  # in watts
        self.battery_storage = 0.0  # in watt-hours
        self.max_battery_capacity = capacity_kw * 1000 * 5  # 5 hours storage
        
    def update_generation(self) -> None:
        """Update current solar generation based on simulated conditions."""
        # Simulate generation based on time of day and weather
        hour = time.localtime().tm_hour
        weather_factor = random.uniform(0.3, 1.0)  # Simulate weather impact
        
        if 6 <= hour <= 18:  # Daytime
            peak_hours = [10, 11, 12, 13, 14]
            if hour in peak_hours:
                generation = self.capacity_kw * 1000 * 0.9 * weather_factor
            else:
                generation = self.capacity_kw * 1000 * 0.6 * weather_factor
        else:  # Nighttime
            generation = 0.0
            
        self.current_generation = generation
        self._update_battery()
        logger.info(f"Solar generation updated: {generation:.2f}W")
        
    def _update_battery(self) -> None:
        """Update battery storage based on current generation."""
        if self.current_generation > 0:
            charge_amount = self.current_generation * 0.1  # Charge at 10% of generation
            self.battery_storage = min(
                self.battery_storage + charge_amount,
                self.max_battery_capacity
            )
        else:
            # Small discharge at night
            self.battery_storage = max(0, self.battery_storage - 100)  # 100W discharge
    
    def get_available_power(self) -> float:
        """Get total available power (generation + battery)."""
        return self.current_generation + (self.battery_storage / 10)  # Convert storage to instant power

class HomeAutomationSystem:
    """Main class for home automation system integrating lights and solar."""
    
    def __init__(self, solar_capacity_kw: float):
        """Initialize the home automation system."""
        self.rooms: Dict[str, Room] = {}
        self.solar_system = SolarPanelSystem(solar_capacity_kw)
        self.total_energy_consumption = 0.0
        
    def add_room(self, name: str, light_count: int) -> None:
        """Add a new room to the automation system."""
        if name not in self.rooms:
            self.rooms[name] = Room(name, light_count)
            logger.info(f"Added room: {name} with {light_count} lights")
        else:
            logger.warning(f"Room {name} already exists")
    
    def control_light(self, room_name: str, light_index: int, state: LightState) -> bool:
        """Control a specific light in a room."""
        if room_name in self.rooms:
            success = self.rooms[room_name].set_light_state(light_index, state)
            if success:
                self._update_total_consumption()
            return success
        logger.error(f"Room {room_name} not found")
        return False
    
    def _update_total_consumption(self) -> None:
        """Update total energy consumption across all rooms."""
        total = 0.0
        for room in self.rooms.values():
            total += room.energy_consumption
        self.total_energy_consumption = total
    
    def optimize_energy_usage(self) -> None:
        """Optimize energy usage based on solar availability."""
        self.solar_system.update_generation()
        available_power = self.solar_system.get_available_power()
        
        if available_power < self.total_energy_consumption:
            # Reduce energy consumption by dimming lights
            for room in self.rooms.values():
                for i in range(len(room.lights)):
                    if room.lights[i] == LightState.ON:
                        room.set_light_state(i, LightState.DIMMED)
            logger.warning("Low solar power - dimming lights to conserve energy")
    
    def get_status_report(self) -> Dict:
        """Generate a status report of the home automation system."""
        report = {
            "solar_generation": self.solar_system.current_generation,
            "battery_storage": self.solar_system.battery_storage,
            "total_consumption": self.total_energy_consumption,
            "rooms": {}
        }
        
        for room_name, room in self.rooms.items():
            report["rooms"][room_name] = {
                "light_states": [state.name for state in room.lights],
                "energy_consumption": room.energy_consumption
            }
        
        return report

# Example usage
if __name__ == "__main__":
    # Initialize the home automation system with 5kW solar capacity
    home_system = HomeAutomationSystem(5.0)
    
    # Add some rooms
    home_system.add_room("Living Room", 4)
    home_system.add_room("Kitchen", 2)
    home_system.add_room("Bedroom", 3)
    
    # Turn on some lights
    home_system.control_light("Living Room", 0, LightState.ON)
    home_system.control_light("Living Room", 1, LightState.ON)
    home_system.control_light("Kitchen", 0, LightState.ON)
    
    # Run optimization
    home_system.optimize_energy_usage()
    
    # Get status report
    status = home_system.get_status_report()
    print("System Status:")
    print(f"Solar Generation: {status['solar_generation']:.2f}W")
    print(f"Battery Storage: {status['battery_storage']:.2f}Wh")
    print(f"Total Consumption: {status['total_consumption']:.2f}W")
    
    for room_name, room_data in status["rooms"].items():
        print(f"\n{room_name}:")
        print(f"  Lights: {room_data['light_states']}")
        print(f"  Consumption: {room_data['energy_consumption']:.2f}W")
```
