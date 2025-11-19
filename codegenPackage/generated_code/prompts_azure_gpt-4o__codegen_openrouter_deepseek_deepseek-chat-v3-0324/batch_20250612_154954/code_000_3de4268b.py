"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Write Python code to design a system for controlling a paddy dryer unit, incorporating components like heat exchangers, blowers, and elevators as described on Mechano Solutions' website.
Generated: DETERMINISTIC_3de4268b55916435
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from enum import Enum
import logging
from typing import Optional, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ComponentStatus(Enum):
    """Enum for component status."""
    OFF = 0
    ON = 1
    ERROR = 2


class PaddyDryerController:
    """Main controller class for the paddy dryer unit."""
    
    def __init__(self):
        """Initialize the paddy dryer controller with default values."""
        self.components = {
            'heat_exchanger': {
                'status': ComponentStatus.OFF,
                'temperature': 0.0,
                'max_temperature': 80.0  # in Celsius
            },
            'blower': {
                'status': ComponentStatus.OFF,
                'speed': 0,  # 0-100%
                'max_speed': 100
            },
            'elevator': {
                'status': ComponentStatus.OFF,
                'speed': 0,  # 0-100%
                'max_speed': 100
            }
        }
        self.safety_thresholds = {
            'max_temperature': 85.0,
            'min_temperature': 10.0,
            'max_humidity': 80.0
        }
        self.sensors = {
            'temperature': 25.0,
            'humidity': 50.0
        }
        self.is_running = False
        self.drying_programs = {
            'standard': {'temp': 60.0, 'blower_speed': 70, 'duration': 3600},
            'gentle': {'temp': 50.0, 'blower_speed': 50, 'duration': 5400},
            'rapid': {'temp': 70.0, 'blower_speed': 90, 'duration': 1800}
        }

    def start_drying(self, program: str = 'standard') -> bool:
        """Start the drying process with the specified program."""
        if not self.is_running:
            if program not in self.drying_programs:
                logger.error(f"Invalid drying program: {program}")
                return False
            
            try:
                program_settings = self.drying_programs[program]
                self._set_heat_exchanger(program_settings['temp'])
                self._set_blower(program_settings['blower_speed'])
                self._set_elevator(50)  # Default elevator speed
                
                self.is_running = True
                logger.info(f"Started drying with program: {program}")
                return True
            except Exception as e:
                logger.error(f"Error starting drying process: {e}")
                self.emergency_stop()
                return False
        else:
            logger.warning("Drying process is already running")
            return False

    def stop_drying(self) -> None:
        """Stop the drying process gracefully."""
        if self.is_running:
            try:
                self._set_heat_exchanger(0)
                self._set_blower(0)
                self._set_elevator(0)
                self.is_running = False
                logger.info("Drying process stopped")
            except Exception as e:
                logger.error(f"Error stopping drying process: {e}")
                self.emergency_stop()

    def emergency_stop(self) -> None:
        """Immediately stop all components due to emergency."""
        try:
            for component in self.components:
                self.components[component]['status'] = ComponentStatus.OFF
                if 'speed' in self.components[component]:
                    self.components[component]['speed'] = 0
                if 'temperature' in self.components[component]:
                    self.components[component]['temperature'] = 0
            
            self.is_running = False
            logger.warning("EMERGENCY STOP ACTIVATED - All components turned off")
        except Exception as e:
            logger.critical(f"Emergency stop failed: {e}")

    def _set_heat_exchanger(self, temperature: float) -> None:
        """Set the heat exchanger temperature."""
        if temperature < 0 or temperature > self.components['heat_exchanger']['max_temperature']:
            raise ValueError(f"Temperature {temperature}°C is out of range")
        
        self.components['heat_exchanger']['temperature'] = temperature
        self.components['heat_exchanger']['status'] = (
            ComponentStatus.ON if temperature > 0 else ComponentStatus.OFF
        )
        logger.info(f"Heat exchanger set to {temperature}°C")

    def _set_blower(self, speed: int) -> None:
        """Set the blower speed."""
        if speed < 0 or speed > self.components['blower']['max_speed']:
            raise ValueError(f"Blower speed {speed}% is out of range")
        
        self.components['blower']['speed'] = speed
        self.components['blower']['status'] = (
            ComponentStatus.ON if speed > 0 else ComponentStatus.OFF
        )
        logger.info(f"Blower speed set to {speed}%")

    def _set_elevator(self, speed: int) -> None:
        """Set the elevator speed."""
        if speed < 0 or speed > self.components['elevator']['max_speed']:
            raise ValueError(f"Elevator speed {speed}% is out of range")
        
        self.components['elevator']['speed'] = speed
        self.components['elevator']['status'] = (
            ComponentStatus.ON if speed > 0 else ComponentStatus.OFF
        )
        logger.info(f"Elevator speed set to {speed}%")

    def update_sensors(self, temperature: float, humidity: float) -> None:
        """Update sensor readings and check safety thresholds."""
        try:
            self.sensors['temperature'] = temperature
            self.sensors['humidity'] = humidity
            
            # Check safety thresholds
            if (temperature > self.safety_thresholds['max_temperature'] or 
                temperature < self.safety_thresholds['min_temperature'] or 
                humidity > self.safety_thresholds['max_humidity']):
                logger.warning("Safety thresholds exceeded - triggering emergency stop")
                self.emergency_stop()
        except Exception as e:
            logger.error(f"Error updating sensors: {e}")

    def get_status(self) -> Dict:
        """Return the current status of the system."""
        return {
            'is_running': self.is_running,
            'components': self.components,
            'sensors': self.sensors
        }

    def run_drying_cycle(self, program: str = 'standard') -> None:
        """Run a complete drying cycle with the specified program."""
        if not self.start_drying(program):
            return
        
        try:
            program_settings = self.drying_programs[program]
            start_time = time.time()
            end_time = start_time + program_settings['duration']
            
            logger.info(f"Running drying cycle for {program_settings['duration']} seconds")
            
            while time.time() < end_time and self.is_running:
                # Simulate sensor updates (in real system, this would come from actual sensors)
                self.update_sensors(
                    temperature=self.components['heat_exchanger']['temperature'] - 5,
                    humidity=60 - (time.time() - start_time) / program_settings['duration'] * 30
                )
                time.sleep(1)  # Simulate time passing
            
            self.stop_drying()
            logger.info("Drying cycle completed successfully")
        except Exception as e:
            logger.error(f"Error during drying cycle: {e}")
            self.emergency_stop()


# Example usage
if __name__ == "__main__":
    dryer = PaddyDryerController()
    dryer.run_drying_cycle('standard')
```
