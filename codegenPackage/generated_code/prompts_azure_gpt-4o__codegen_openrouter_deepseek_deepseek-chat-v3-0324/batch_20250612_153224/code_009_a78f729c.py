"""
Generated Code Metadata:
========================
Original URL: https://instrumentacionum.com
Prompt: Write code to automate data collection from temperature sensors and pressure transmitters in an industrial setting, inspired by Instrumentación UM's product range.
Generated: DETERMINISTIC_a78f729caa5474f7
Batch ID: 20250612_153224
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
import logging
from dataclasses import dataclass
from typing import List, Optional
import json
from datetime import datetime
import requests
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sensor_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class SensorConfig:
    """Configuration for a single sensor"""
    sensor_id: str
    sensor_type: str  # 'temperature' or 'pressure'
    min_value: float
    max_value: float
    unit: str
    poll_interval: int  # in seconds
    api_endpoint: Optional[str] = None

class SensorMonitor:
    def __init__(self, config_file: str):
        """Initialize sensor monitor with configuration"""
        self.sensors = self._load_config(config_file)
        self.running = False
        
    def _load_config(self, config_file: str) -> List[SensorConfig]:
        """Load sensor configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                config_data = json.load(f)
                return [SensorConfig(**sensor) for sensor in config_data['sensors']]
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading config: {e}")
            raise

    def _read_sensor(self, sensor: SensorConfig) -> float:
        """Simulate reading from a physical sensor"""
        # In a real implementation, this would interface with actual hardware
        if sensor.sensor_type == 'temperature':
            value = random.uniform(sensor.min_value, sensor.max_value)
        elif sensor.sensor_type == 'pressure':
            value = random.uniform(sensor.min_value, sensor.max_value)
        else:
            raise ValueError(f"Unknown sensor type: {sensor.sensor_type}")
        
        logger.debug(f"Read {sensor.sensor_type} from {sensor.sensor_id}: {value} {sensor.unit}")
        return round(value, 2)

    def _send_data(self, sensor: SensorConfig, value: float) -> bool:
        """Send sensor data to API endpoint if configured"""
        if not sensor.api_endpoint:
            return False
            
        timestamp = datetime.utcnow().isoformat()
        payload = {
            'sensor_id': sensor.sensor_id,
            'value': value,
            'unit': sensor.unit,
            'timestamp': timestamp
        }
        
        try:
            response = requests.post(
                sensor.api_endpoint,
                json=payload,
                timeout=5
            )
            response.raise_for_status()
            logger.debug(f"Data sent successfully for {sensor.sensor_id}")
            return True
        except RequestException as e:
            logger.error(f"Failed to send data for {sensor.sensor_id}: {e}")
            return False

    def _monitor_sensor(self, sensor: SensorConfig):
        """Monitor a single sensor in a loop"""
        while self.running:
            try:
                value = self._read_sensor(sensor)
                self._send_data(sensor, value)
                
                # Log the reading
                logger.info(
                    f"Sensor {sensor.sensor_id} ({sensor.sensor_type}): "
                    f"{value} {sensor.unit}"
                )
                
            except Exception as e:
                logger.error(f"Error monitoring sensor {sensor.sensor_id}: {e}")
            
            time.sleep(sensor.poll_interval)

    def start(self):
        """Start monitoring all sensors"""
        self.running = True
        logger.info("Starting sensor monitoring system")
        
        import threading
        threads = []
        for sensor in self.sensors:
            thread = threading.Thread(
                target=self._monitor_sensor,
                args=(sensor,),
                daemon=True
            )
            thread.start()
            threads.append(thread)
            logger.info(f"Started monitoring for sensor {sensor.sensor_id}")
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        """Stop monitoring all sensors"""
        self.running = False
        logger.info("Stopping sensor monitoring system")

if __name__ == "__main__":
    try:
        monitor = SensorMonitor('sensor_config.json')
        monitor.start()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
```
