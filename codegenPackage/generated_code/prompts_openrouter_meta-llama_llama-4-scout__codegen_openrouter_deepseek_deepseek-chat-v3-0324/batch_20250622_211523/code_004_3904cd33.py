"""
Generated Code Metadata:
========================
Original URL: https://blackpanttthers.com
Prompt: "Create a scenario-based automation script for a smart home, adjusting lighting, temperature, and entertainment systems based on occupants' daily routines and preferences."
Generated: DETERMINISTIC_3904cd33858afcb6
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import json
from enum import Enum
from typing import Dict, Optional, List
import logging
from datetime import datetime, time as dt_time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DeviceType(Enum):
    LIGHT = "light"
    THERMOSTAT = "thermostat"
    ENTERTAINMENT = "entertainment"

class DeviceState:
    def __init__(self, device_type: DeviceType, device_id: str, state: Dict):
        self.device_type = device_type
        self.device_id = device_id
        self.state = state

    def __str__(self):
        return f"{self.device_type.value}_{self.device_id}: {self.state}"

class SmartHomeController:
    def __init__(self):
        self.devices: Dict[str, DeviceState] = {}
        self.routines: Dict[str, Dict] = {}
        self.load_config()

    def load_config(self):
        """Load device configurations and routines from file"""
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                self.routines = config.get('routines', {})
                
                # Initialize device states
                for device in config.get('devices', []):
                    device_type = DeviceType(device['type'])
                    device_id = device['id']
                    self.devices[device_id] = DeviceState(
                        device_type, device_id, device.get('state', {})
                    )
        except FileNotFoundError:
            logger.error("Config file not found")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON in config file")
            raise
        except Exception as e:
            logger.error(f"Error loading config: {str(e)}")
            raise

    def update_device_state(self, device_id: str, new_state: Dict) -> bool:
        """Update the state of a device"""
        if device_id not in self.devices:
            logger.error(f"Device {device_id} not found")
            return False
        
        device = self.devices[device_id]
        device.state.update(new_state)
        logger.info(f"Updated {device_id}: {new_state}")
        return True

    def get_current_routine(self) -> Optional[Dict]:
        """Get the current routine based on time of day"""
        now = datetime.now().time()
        
        for routine_name, routine in self.routines.items():
            start_time = dt_time.fromisoformat(routine['start_time'])
            end_time = dt_time.fromisoformat(routine['end_time'])
            
            if start_time <= now <= end_time:
                return routine
        return None

    def execute_routine(self, routine: Dict) -> bool:
        """Execute a routine by adjusting devices"""
        try:
            for device_id, settings in routine.get('devices', {}).items():
                if device_id in self.devices:
                    self.update_device_state(device_id, settings)
                else:
                    logger.warning(f"Device {device_id} in routine not found")
            
            logger.info(f"Executed routine: {routine.get('name', 'unknown')}")
            return True
        except Exception as e:
            logger.error(f"Error executing routine: {str(e)}")
            return False

    def run(self):
        """Main loop to monitor and adjust devices based on routines"""
        logger.info("Smart Home Controller started")
        
        try:
            while True:
                current_routine = self.get_current_routine()
                if current_routine:
                    self.execute_routine(current_routine)
                
                # Check every minute
                time.sleep(60)
        except KeyboardInterrupt:
            logger.info("Shutting down Smart Home Controller")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    try:
        controller = SmartHomeController()
        controller.run()
    except Exception as e:
        logger.error(f"Failed to start controller: {str(e)}")
```

Example `config.json`:
```json
{
  "devices": [
    {
      "id": "living_room_light",
      "type": "light",
      "state": {
        "power": "off",
        "brightness": 0,
        "color": "white"
      }
    },
    {
      "id": "living_room_thermostat",
      "type": "thermostat",
      "state": {
        "power": "off",
        "temperature": 20,
        "mode": "cool"
      }
    },
    {
      "id": "living_room_tv",
      "type": "entertainment",
      "state": {
        "power": "off",
        "volume": 50,
        "source": "hdmi1"
      }
    }
  ],
  "routines": {
    "morning": {
      "name": "Morning Routine",
      "start_time": "06:00:00",
      "end_time": "08:00:00",
      "devices": {
        "living_room_light": {
          "power": "on",
          "brightness": 80
        },
        "living_room_thermostat": {
          "power": "on",
          "temperature": 22
        }
      }
    },
    "evening": {
      "name": "Evening Routine",
      "start_time": "18:00:00",
      "end_time": "22:00:00",
      "devices": {
        "living_room_light": {
          "power": "on",
          "brightness": 50,
          "color": "warm"
        },
        "living_room_thermostat": {
          "power": "on",
          "temperature": 20
        },
        "living_room_tv": {
          "power": "on",
          "volume": 40
        }
      }
    },
    "night": {
      "name": "Night Routine",
      "start_time": "22:00:00",
      "end_time": "06:00:00",
      "devices": {
        "living_room_light": {
          "power": "off"
        },
        "living_room_thermostat": {
          "power": "on",
          "temperature": 18
        },
        "living_room_tv": {
          "power": "off"
        }
      }
    }
  }
}
```
