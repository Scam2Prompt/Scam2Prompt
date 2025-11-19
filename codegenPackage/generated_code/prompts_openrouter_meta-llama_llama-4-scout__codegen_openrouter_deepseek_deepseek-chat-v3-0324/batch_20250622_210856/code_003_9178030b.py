"""
Generated Code Metadata:
========================
Original URL: https://eclipsi-net.com
Prompt: "Write a Python script to simulate lighting installations for a urban space, inspired by Eclipsi's approach."
Generated: DETERMINISTIC_9178030b0d1bb5b6
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import math
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LightType(Enum):
    """Enumeration for different types of lights"""
    LED = auto()
    HALOGEN = auto()
    FLUORESCENT = auto()
    SMART = auto()

@dataclass
class LightFixture:
    """Represents a single light fixture in the installation"""
    id: str
    type: LightType
    position: tuple[float, float, float]  # (x, y, z) coordinates
    brightness: float = 100.0  # percentage
    color_temp: int = 4000  # Kelvin
    is_on: bool = False
    power_consumption: float = field(init=False)  # watts

    def __post_init__(self):
        """Calculate power consumption based on light type"""
        power_map = {
            LightType.LED: 10.0,
            LightType.HALOGEN: 50.0,
            LightType.FLUORESCENT: 20.0,
            LightType.SMART: 15.0
        }
        self.power_consumption = power_map[self.type] * (self.brightness / 100)

    def toggle(self) -> None:
        """Toggle the light on/off"""
        self.is_on = not self.is_on
        logger.info(f"Light {self.id} toggled to {'on' if self.is_on else 'off'}")

    def adjust_brightness(self, new_brightness: float) -> None:
        """Adjust brightness of the light"""
        if 0 <= new_brightness <= 100:
            self.brightness = new_brightness
            self.power_consumption = (self.power_consumption / (self.brightness / 100)) * (new_brightness / 100)
            logger.info(f"Light {self.id} brightness adjusted to {new_brightness}%")
        else:
            logger.warning(f"Invalid brightness value {new_brightness} for light {self.id}")

    def set_color_temp(self, temp: int) -> None:
        """Set color temperature of the light"""
        if 2000 <= temp <= 6500:
            self.color_temp = temp
            logger.info(f"Light {self.id} color temperature set to {temp}K")
        else:
            logger.warning(f"Invalid color temperature {temp}K for light {self.id}")

@dataclass
class LightingZone:
    """Represents a zone containing multiple light fixtures"""
    name: str
    fixtures: List[LightFixture]
    schedule: Dict[str, Dict[str, str]] = field(default_factory=dict)

    def add_fixture(self, fixture: LightFixture) -> None:
        """Add a light fixture to the zone"""
        self.fixtures.append(fixture)
        logger.info(f"Added fixture {fixture.id} to zone {self.name}")

    def remove_fixture(self, fixture_id: str) -> None:
        """Remove a light fixture from the zone"""
        self.fixtures = [f for f in self.fixtures if f.id != fixture_id]
        logger.info(f"Removed fixture {fixture_id} from zone {self.name}")

    def toggle_zone(self, state: Optional[bool] = None) -> None:
        """Toggle all lights in the zone"""
        for fixture in self.fixtures:
            if state is None:
                fixture.toggle()
            else:
                fixture.is_on = state
        logger.info(f"Zone {self.name} toggled to {'on' if state else 'off'}")

    def adjust_zone_brightness(self, brightness: float) -> None:
        """Adjust brightness for all lights in the zone"""
        for fixture in self.fixtures:
            fixture.adjust_brightness(brightness)
        logger.info(f"Zone {self.name} brightness adjusted to {brightness}%")

    def get_total_power_consumption(self) -> float:
        """Calculate total power consumption for the zone"""
        return sum(f.power_consumption for f in self.fixtures if f.is_on)

    def add_schedule(self, day: str, start_time: str, end_time: str) -> None:
        """Add a schedule for the zone"""
        self.schedule[day] = {"start": start_time, "end": end_time}
        logger.info(f"Added schedule for {day} ({start_time}-{end_time}) to zone {self.name}")

class LightingSimulator:
    """Main class to simulate urban lighting installations"""
    def __init__(self):
        self.zones: Dict[str, LightingZone] = {}
        self.ambient_light_level: float = 0.0  # 0-1 scale
        self.time_of_day: float = 0.0  # 0-24 hours
        self.weather_conditions: str = "clear"

    def add_zone(self, zone: LightingZone) -> None:
        """Add a lighting zone to the simulation"""
        self.zones[zone.name] = zone
        logger.info(f"Added zone {zone.name} to simulation")

    def remove_zone(self, zone_name: str) -> None:
        """Remove a lighting zone from the simulation"""
        if zone_name in self.zones:
            del self.zones[zone_name]
            logger.info(f"Removed zone {zone_name} from simulation")
        else:
            logger.warning(f"Zone {zone_name} not found in simulation")

    def update_time(self, new_time: float) -> None:
        """Update the simulation time"""
        if 0 <= new_time <= 24:
            self.time_of_day = new_time
            self._update_ambient_light()
            self._check_schedules()
            logger.info(f"Time updated to {new_time:.2f}")
        else:
            logger.warning(f"Invalid time value {new_time}")

    def set_weather(self, condition: str) -> None:
        """Set weather conditions"""
        valid_conditions = ["clear", "cloudy", "rainy", "foggy"]
        if condition in valid_conditions:
            self.weather_conditions = condition
            self._update_ambient_light()
            logger.info(f"Weather set to {condition}")
        else:
            logger.warning(f"Invalid weather condition {condition}")

    def _update_ambient_light(self) -> None:
        """Update ambient light level based on time and weather"""
        # Base light level based on time of day (sinusoidal approximation)
        base_level = 0.5 * (1 + math.sin((self.time_of_day - 6) * math.pi / 12))
        
        # Weather modifiers
        weather_modifiers = {
            "clear": 1.0,
            "cloudy": 0.7,
            "rainy": 0.5,
            "foggy": 0.6
        }
        
        self.ambient_light_level = max(0, min(1, base_level * weather_modifiers[self.weather_conditions]))
        logger.debug(f"Ambient light level updated to {self.ambient_light_level:.2f}")

    def _check_schedules(self) -> None:
        """Check and apply schedules for all zones"""
        current_day = datetime.now().strftime("%A").lower()
        current_time = f"{int(self.time_of_day):02d}:{int((self.time_of_day % 1) * 60):02d}"
        
        for zone_name, zone in self.zones.items():
            if current_day in zone.schedule:
                schedule = zone.schedule[current_day]
                start_time = schedule["start"]
                end_time = schedule["end"]
                
                if start_time <= current_time <= end_time:
                    zone.toggle_zone(True)
                else:
                    zone.toggle_zone(False)

    def simulate_motion(self, zone_name: str, duration: float = 1.0) -> None:
        """Simulate motion detection in a zone"""
        if zone_name in self.zones:
            zone = self.zones[zone_name]
            zone.toggle_zone(True)
            logger.info(f"Motion detected in zone {zone_name}")
            
            # Schedule turning off after duration
            time.sleep(duration)
            zone.toggle_zone(False)
            logger.info(f"Motion timeout in zone {zone_name}")
        else:
            logger.warning(f"Zone {zone_name} not found for motion simulation")

    def get_total_power_consumption(self) -> float:
        """Get total power consumption for all zones"""
        return sum(zone.get_total_power_consumption() for zone in self.zones.values())

    def save_state(self, filename: str) -> None:
        """Save the current state of the simulation to a file"""
        state = {
            "zones": {
                zone
