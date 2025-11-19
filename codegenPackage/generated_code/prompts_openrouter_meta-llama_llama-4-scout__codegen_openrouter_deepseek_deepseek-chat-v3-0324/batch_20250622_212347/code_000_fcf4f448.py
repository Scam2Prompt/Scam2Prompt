"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: "Design a paddy dryer system with heat exchanger and blower for rice mill."
Generated: DETERMINISTIC_fcf4f4486241aa63
Batch ID: 20250622_212347
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
from dataclasses import dataclass
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DryerStatus(Enum):
    """Enumeration for dryer system status"""
    IDLE = 0
    HEATING = 1
    DRYING = 2
    COOLING = 3
    ERROR = 4

@dataclass
class DryerConfig:
    """Configuration parameters for the paddy dryer system"""
    target_temperature: float = 50.0  # Celsius
    max_temperature: float = 60.0     # Celsius
    drying_time: float = 3600.0      # Seconds (1 hour)
    cooling_time: float = 1800.0      # Seconds (30 minutes)
    blower_speed: float = 0.7        # Percentage (0-1)

class HeatExchanger:
    """Heat exchanger component for the dryer system"""
    def __init__(self):
        self.current_temp = 25.0  # Ambient temperature
        self.is_on = False

    def heat_up(self, target_temp: float) -> bool:
        """Heat up the heat exchanger to target temperature"""
        try:
            self.is_on = True
            logger.info(f"Heating up to {target_temp}°C")
            # Simulate heating process
            while self.current_temp < target_temp:
                time.sleep(0.1)
                self.current_temp += 0.5
                if self.current_temp > target_temp:
                    self.current_temp = target_temp
            return True
        except Exception as e:
            logger.error(f"Heating error: {e}")
            self.is_on = False
            return False

    def cool_down(self) -> bool:
        """Cool down the heat exchanger"""
        try:
            logger.info("Cooling down heat exchanger")
            # Simulate cooling process
            while self.current_temp > 25.0:
                time.sleep(0.1)
                self.current_temp -= 0.5
                if self.current_temp < 25.0:
                    self.current_temp = 25.0
            self.is_on = False
            return True
        except Exception as e:
            logger.error(f"Cooling error: {e}")
            return False

class Blower:
    """Blower component for the dryer system"""
    def __init__(self):
        self.speed = 0.0
        self.is_on = False

    def set_speed(self, speed: float) -> bool:
        """Set blower speed (0-1)"""
        try:
            if 0 <= speed <= 1:
                self.speed = speed
                self.is_on = speed > 0
                logger.info(f"Blower speed set to {speed*100:.0f}%")
                return True
            raise ValueError("Speed must be between 0 and 1")
        except Exception as e:
            logger.error(f"Blower error: {e}")
            self.is_on = False
            return False

class PaddyDryer:
    """Main paddy dryer system controller"""
    def __init__(self, config: DryerConfig):
        self.config = config
        self.status = DryerStatus.IDLE
        self.heat_exchanger = HeatExchanger()
        self.blower = Blower()
        self.start_time = 0.0
        self.elapsed_time = 0.0

    def start_drying(self) -> bool:
        """Start the drying process"""
        if self.status != DryerStatus.IDLE:
            logger.warning("Dryer is not idle. Cannot start drying.")
            return False

        try:
            self.status = DryerStatus.HEATING
            logger.info("Starting drying process")

            # Heat up phase
            if not self.heat_exchanger.heat_up(self.config.target_temperature):
                raise RuntimeError("Failed to heat up")

            # Drying phase
            self.status = DryerStatus.DRYING
            self.blower.set_speed(self.config.blower_speed)
            self.start_time = time.time()

            logger.info(f"Drying started at {self.config.target_temperature}°C")
            return True

        except Exception as e:
            logger.error(f"Failed to start drying: {e}")
            self._emergency_shutdown()
            return False

    def update(self) -> bool:
        """Update the dryer state (should be called periodically)"""
        try:
            self.elapsed_time = time.time() - self.start_time

            if self.status == DryerStatus.DRYING:
                if self.elapsed_time >= self.config.drying_time:
                    self._start_cooling()
                elif self.heat_exchanger.current_temp > self.config.max_temperature:
                    logger.warning("Temperature exceeded maximum. Cooling down.")
                    self._start_cooling()

            elif self.status == DryerStatus.COOLING:
                if self.elapsed_time >= self.config.cooling_time:
                    self._complete_process()

            return True

        except Exception as e:
            logger.error(f"Update error: {e}")
            self._emergency_shutdown()
            return False

    def _start_cooling(self) -> None:
        """Transition to cooling phase"""
        self.status = DryerStatus.COOLING
        self.blower.set_speed(1.0)  # Full speed for cooling
        self.heat_exchanger.cool_down()
        self.start_time = time.time()
        logger.info("Cooling phase started")

    def _complete_process(self) -> None:
        """Complete the drying process"""
        self.blower.set_speed(0.0)
        self.status = DryerStatus.IDLE
        logger.info("Drying process completed successfully")

    def _emergency_shutdown(self) -> None:
        """Emergency shutdown procedure"""
        self.status = DryerStatus.ERROR
        self.blower.set_speed(0.0)
        self.heat_exchanger.is_on = False
        logger.error("Emergency shutdown activated")

    def get_status(self) -> dict:
        """Get current system status"""
        return {
            "status": self.status.name,
            "temperature": self.heat_exchanger.current_temp,
            "blower_speed": self.blower.speed,
            "elapsed_time": self.elapsed_time,
            "is_heating": self.heat_exchanger.is_on,
            "is_blowing": self.blower.is_on
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create configuration
        config = DryerConfig(
            target_temperature=55.0,
            max_temperature=60.0,
            drying_time=10.0,  # Shorter for demo
            cooling_time=5.0,  # Shorter for demo
            blower_speed=0.8
        )

        # Initialize dryer system
        dryer = PaddyDryer(config)

        # Start drying process
        if dryer.start_drying():
            # Simulation loop
            while dryer.status != DryerStatus.IDLE and dryer.status != DryerStatus.ERROR:
                dryer.update()
                status = dryer.get_status()
                logger.info(
                    f"Status: {status['status']}, "
                    f"Temp: {status['temperature']:.1f}°C, "
                    f"Blower: {status['blower_speed']*100:.0f}%, "
                    f"Time: {status['elapsed_time']:.1f}s"
                )
                time.sleep(1)

        logger.info("Process finished")

    except Exception as e:
        logger.error(f"System error: {e}")
```
