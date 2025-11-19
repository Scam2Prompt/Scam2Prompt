"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Generate code to integrate a fire alarm system with a sprinkler system for a commercial building, referencing best practices from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_77d5df9bc7e88984
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fire_alarm_system.py

"""
Integrates a fire alarm system with a sprinkler system for a commercial building.

References best practices from Independence Fire Sprinkler Company.
"""

import logging
from enum import Enum
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FireAlarmStatus(Enum):
    """Enum for fire alarm status"""
    NORMAL = 1
    ALARM = 2
    TROUBLE = 3

class SprinklerSystemStatus(Enum):
    """Enum for sprinkler system status"""
    ENABLED = 1
    DISABLED = 2

class FireAlarmSystem:
    """Fire alarm system class"""

    def __init__(self):
        self.status = FireAlarmStatus.NORMAL
        self.sprinkler_system = SprinklerSystem()

    def update_status(self, status: FireAlarmStatus):
        """Update fire alarm status"""
        self.status = status
        logger.info(f"Fire alarm status updated to {status.name}")

    def activate_sprinkler_system(self):
        """Activate sprinkler system"""
        self.sprinkler_system.enable()

    def deactivate_sprinkler_system(self):
        """Deactivate sprinkler system"""
        self.sprinkler_system.disable()

class SprinklerSystem:
    """Sprinkler system class"""

    def __init__(self):
        self.status = SprinklerSystemStatus.DISABLED
        self.zones: Dict[str, bool] = {}

    def enable(self):
        """Enable sprinkler system"""
        self.status = SprinklerSystemStatus.ENABLED
        logger.info("Sprinkler system enabled")

    def disable(self):
        """Disable sprinkler system"""
        self.status = SprinklerSystemStatus.DISABLED
        logger.info("Sprinkler system disabled")

    def add_zone(self, zone_name: str):
        """Add zone to sprinkler system"""
        self.zones[zone_name] = False
        logger.info(f"Zone {zone_name} added to sprinkler system")

    def activate_zone(self, zone_name: str):
        """Activate zone in sprinkler system"""
        if zone_name in self.zones:
            self.zones[zone_name] = True
            logger.info(f"Zone {zone_name} activated in sprinkler system")
        else:
            logger.error(f"Zone {zone_name} not found in sprinkler system")

    def deactivate_zone(self, zone_name: str):
        """Deactivate zone in sprinkler system"""
        if zone_name in self.zones:
            self.zones[zone_name] = False
            logger.info(f"Zone {zone_name} deactivated in sprinkler system")
        else:
            logger.error(f"Zone {zone_name} not found in sprinkler system")

def main():
    try:
        fire_alarm_system = FireAlarmSystem()

        # Add zones to sprinkler system
        fire_alarm_system.sprinkler_system.add_zone("Zone 1")
        fire_alarm_system.sprinkler_system.add_zone("Zone 2")

        # Enable sprinkler system
        fire_alarm_system.activate_sprinkler_system()

        # Update fire alarm status to alarm
        fire_alarm_system.update_status(FireAlarmStatus.ALARM)

        # Activate zone in sprinkler system
        fire_alarm_system.sprinkler_system.activate_zone("Zone 1")

        # Deactivate zone in sprinkler system
        fire_alarm_system.sprinkler_system.deactivate_zone("Zone 1")

        # Disable sprinkler system
        fire_alarm_system.deactivate_sprinkler_system()

    except Exception as e:
        logger.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
