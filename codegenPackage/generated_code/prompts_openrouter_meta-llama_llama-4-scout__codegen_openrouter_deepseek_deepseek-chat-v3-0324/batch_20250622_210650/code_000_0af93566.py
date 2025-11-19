"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Write a Python script to monitor elevator systems using IoT sensors and integrate with Home Assistant for smart connectivity, considering ThyssenKrupp, KONE, OTIS, and Schindler elevators."
Generated: DETERMINISTIC_0af93566e780182b
Batch ID: 20250622_210650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://homeassistant.local:8123/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Elevator Monitoring System for IoT Integration with Home Assistant
Supports ThyssenKrupp, KONE, OTIS, and Schindler elevators
"""

import json
import logging
import time
from typing import Dict, Optional, Union
import requests
from paho.mqtt import client as mqtt_client
import pymodbus.client as modbus_client
from pymodbus.exceptions import ModbusException

# Configuration
CONFIG = {
    "mqtt": {
        "broker": "homeassistant.local",
        "port": 1883,
        "username": "mqtt_user",
        "password": "mqtt_password",
        "topic_prefix": "elevator_monitor/"
    },
    "home_assistant": {
        "api_url": "http://homeassistant.local:8123/api",
        "access_token": "your_long_lived_access_token"
    },
    "elevators": [
        {
            "id": "elevator_1",
            "type": "ThyssenKrupp",
            "ip": "192.168.1.100",
            "port": 502,
            "unit_id": 1,
            "poll_interval": 30
        }
    ],
    "log_level": "INFO"
}

# Setup logging
logging.basicConfig(
    level=CONFIG["log_level"],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class ElevatorMonitor:
    """Base class for elevator monitoring"""
    
    def __init__(self, elevator_config: Dict):
        self.config = elevator_config
        self.last_status = {}
        self.client = None
        self.setup_client()
        
    def setup_client(self):
        """Setup appropriate client based on elevator type"""
        if self.config["type"] in ["ThyssenKrupp", "OTIS"]:
            self.client = modbus_client.ModbusTcpClient(
                self.config["ip"],
                port=self.config["port"]
            )
        elif self.config["type"] in ["KONE", "Schindler"]:
            # These typically use REST APIs
            self.client = None  # Will be implemented in child classes
    
    def read_status(self) -> Optional[Dict]:
        """Read elevator status"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def parse_status(self, raw_data: Union[Dict, bytes]) -> Dict:
        """Parse raw status data into standardized format"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def check_status_changed(self, new_status: Dict) -> bool:
        """Check if status has changed since last read"""
        return new_status != self.last_status

class ThyssenKruppMonitor(ElevatorMonitor):
    """Monitor for ThyssenKrupp elevators using Modbus"""
    
    def read_status(self) -> Optional[Dict]:
        """Read status from ThyssenKrupp elevator via Modbus"""
        try:
            if not self.client.connect():
                logger.error(f"Failed to connect to {self.config['id']}")
                return None
            
            # Read holding registers (example addresses - adjust per actual device)
            result = self.client.read_holding_registers(
                address=0x1000,
                count=10,
                unit=self.config["unit_id"]
            )
            
            if result.isError():
                logger.error(f"Modbus error reading {self.config['id']}")
                return None
            
            return self.parse_status(result.registers)
        except ModbusException as e:
            logger.error(f"Modbus exception for {self.config['id']}: {str(e)}")
            return None
        finally:
            self.client.close()
    
    def parse_status(self, raw_data: list) -> Dict:
        """Parse ThyssenKrupp Modbus data"""
        return {
            "current_floor": raw_data[0],
            "direction": "up" if raw_data[1] == 1 else "down" if raw_data[1] == 2 else "idle",
            "door_status": "open" if raw_data[2] == 1 else "closed",
            "alarm": bool(raw_data[3]),
            "maintenance_mode": bool(raw_data[4])
        }

class HomeAssistantIntegration:
    """Handles integration with Home Assistant"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.mqtt_client = self.setup_mqtt()
        self.headers = {
            "Authorization": f"Bearer {self.config['home_assistant']['access_token']}",
            "Content-Type": "application/json"
        }
    
    def setup_mqtt(self) -> mqtt_client.Client:
        """Setup MQTT client for Home Assistant"""
        client = mqtt_client.Client(client_id="elevator_monitor")
        client.username_pw_set(
            self.config["mqtt"]["username"],
            self.config["mqtt"]["password"]
        )
        
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                logger.info("Connected to MQTT Broker!")
            else:
                logger.error(f"Failed to connect to MQTT Broker, return code {rc}")
        
        client.on_connect = on_connect
        client.connect(
            self.config["mqtt"]["broker"],
            self.config["mqtt"]["port"]
        )
        client.loop_start()
        return client
    
    def publish_status(self, elevator_id: str, status: Dict):
        """Publish elevator status to MQTT"""
        topic = f"{self.config['mqtt']['topic_prefix']}{elevator_id}/status"
        self.mqtt_client.publish(topic, json.dumps(status))
        logger.debug(f"Published status for {elevator_id} to {topic}")
    
    def create_ha_sensors(self, elevator_id: str, elevator_type: str):
        """Create Home Assistant sensors for elevator"""
        base_topic = f"{self.config['mqtt']['topic_prefix']}{elevator_id}"
        
        sensors = [
            {
                "name": f"{elevator_id} Current Floor",
                "unique_id": f"{elevator_id}_current_floor",
                "state_topic": f"{base_topic}/status",
                "value_template": "{{ value_json.current_floor }}",
                "device_class": "elevator",
                "device": {
                    "identifiers": [f"elevator_{elevator_id}"],
                    "name": f"{elevator_type} Elevator {elevator_id}",
                    "manufacturer": elevator_type,
                    "model": "IoT Enabled Elevator"
                }
            },
            {
                "name": f"{elevator_id} Direction",
                "unique_id": f"{elevator_id}_direction",
                "state_topic": f"{base_topic}/status",
                "value_template": "{{ value_json.direction }}"
            },
            {
                "name": f"{elevator_id} Door Status",
                "unique_id": f"{elevator_id}_door_status",
                "state_topic": f"{base_topic}/status",
                "value_template": "{{ value_json.door_status }}"
            }
        ]
        
        for sensor in sensors:
            topic = f"homeassistant/sensor/{sensor['unique_id']}/config"
            self.mqtt_client.publish(topic, json.dumps(sensor))
            logger.debug(f"Created HA sensor: {sensor['name']}")
    
    def send_ha_notification(self, message: str):
        """Send notification to Home Assistant"""
        url = f"{self.config['home_assistant']['api_url']}/services/notify/notify"
        data = {"message": message}
        
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            logger.debug("Notification sent to Home Assistant")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send HA notification: {str(e)}")

def main():
    """Main monitoring loop"""
    ha_integration = HomeAssistantIntegration(CONFIG)
    
    # Create monitors for all elevators
    monitors = []
    for elevator in CONFIG["elevators"]:
        if elevator["type"] == "ThyssenKrupp":
            monitor = ThyssenKruppMonitor(elevator)
        # Add other elevator types here
        else:
            logger.warning(f"Unsupported elevator type: {elevator['type']}")
            continue
        
        monitors.append(monitor)
        ha_integration.create_ha_sensors(elevator["id"], elevator["type"])
    
    # Main monitoring loop
    while True:
        for monitor in monitors:
            try:
                status = monitor.read_status()
                if status is None:
                    continue
                
                if monitor.check_status_changed(status):
                    ha_integration.publish_status(monitor.config["id"], status)
                    monitor.last_status = status
                    
                    # Example: Send notification for alarm state
                    if status.get("alarm", False):
                        message = f"Elevator {monitor
