"""
Generated Code Metadata:
========================
Original URL: https://pumpx.me
Prompt: Develop a program to integrate PumpX's RollX Series equipment into an IoT-enabled construction site, allowing remote monitoring and control.
Generated: DETERMINISTIC_174d08eefd090387
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
import requests
from typing import Dict, Optional, List
import logging
from dataclasses import dataclass
import paho.mqtt.client as mqtt
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EquipmentStatus(Enum):
    """Enum representing possible equipment states."""
    ONLINE = "online"
    OFFLINE = "offline"
    ACTIVE = "active"
    IDLE = "idle"
    MAINTENANCE = "maintenance"
    ERROR = "error"

@dataclass
class EquipmentData:
    """Data class representing equipment metrics."""
    equipment_id: str
    status: EquipmentStatus
    pressure: float
    flow_rate: float
    temperature: float
    vibration: float
    timestamp: float = time.time()

class PumpXRollXIntegration:
    """Main class for PumpX RollX Series IoT integration."""
    
    def __init__(
        self,
        api_base_url: str,
        mqtt_broker: str,
        mqtt_port: int = 1883,
        mqtt_username: Optional[str] = None,
        mqtt_password: Optional[str] = None
    ):
        """Initialize the integration service.
        
        Args:
            api_base_url: Base URL for the PumpX API
            mqtt_broker: MQTT broker address
            mqtt_port: MQTT broker port
            mqtt_username: Optional MQTT username
            mqtt_password: Optional MQTT password
        """
        self.api_base_url = api_base_url
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        
        # Initialize MQTT client
        self.mqtt_client = mqtt.Client(client_id="pumpx_rollx_integration")
        if self.mqtt_username and self.mqtt_password:
            self.mqtt_client.username_pw_set(self.mqtt_username, self.mqtt_password)
        
        # Set up MQTT callbacks
        self.mqtt_client.on_connect = self._on_mqtt_connect
        self.mqtt_client.on_message = self._on_mqtt_message
        self.mqtt_client.on_disconnect = self._on_mqtt_disconnect
        
        # Equipment data cache
        self.equipment_cache: Dict[str, EquipmentData] = {}
        
    def _on_mqtt_connect(self, client, userdata, flags, rc):
        """Callback for MQTT connection events."""
        if rc == 0:
            logger.info("Successfully connected to MQTT broker")
            # Subscribe to control topics
            client.subscribe("pumpx/rollx/control/#")
        else:
            logger.error(f"Failed to connect to MQTT broker with result code {rc}")
    
    def _on_mqtt_message(self, client, userdata, msg):
        """Callback for MQTT message events."""
        try:
            topic = msg.topic
            payload = json.loads(msg.payload.decode())
            logger.info(f"Received message on topic {topic}: {payload}")
            
            if topic.startswith("pumpx/rollx/control/"):
                equipment_id = topic.split("/")[-1]
                self._handle_control_message(equipment_id, payload)
                
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")
    
    def _on_mqtt_disconnect(self, client, userdata, rc):
        """Callback for MQTT disconnection events."""
        if rc != 0:
            logger.warning(f"Unexpected MQTT disconnection (rc={rc}). Attempting to reconnect...")
            self._reconnect_mqtt()
    
    def _reconnect_mqtt(self):
        """Attempt to reconnect to MQTT broker."""
        max_retries = 5
        retry_delay = 5  # seconds
        
        for attempt in range(max_retries):
            try:
                self.mqtt_client.reconnect()
                logger.info("Successfully reconnected to MQTT broker")
                return
            except Exception as e:
                logger.warning(f"Reconnection attempt {attempt + 1} failed: {e}")
                time.sleep(retry_delay)
        
        logger.error("Failed to reconnect to MQTT broker after multiple attempts")
    
    def _handle_control_message(self, equipment_id: str, payload: Dict):
        """Process control messages for equipment."""
        try:
            action = payload.get("action")
            params = payload.get("parameters", {})
            
            if action == "start":
                self._start_equipment(equipment_id, params)
            elif action == "stop":
                self._stop_equipment(equipment_id)
            elif action == "configure":
                self._configure_equipment(equipment_id, params)
            else:
                logger.warning(f"Unknown action received: {action}")
                
        except Exception as e:
            logger.error(f"Error handling control message: {e}")
    
    def _start_equipment(self, equipment_id: str, params: Dict):
        """Start the specified equipment."""
        logger.info(f"Starting equipment {equipment_id} with params: {params}")
        # In a real implementation, this would send a command to the actual equipment
        self._update_equipment_status(equipment_id, EquipmentStatus.ACTIVE)
    
    def _stop_equipment(self, equipment_id: str):
        """Stop the specified equipment."""
        logger.info(f"Stopping equipment {equipment_id}")
        # In a real implementation, this would send a command to the actual equipment
        self._update_equipment_status(equipment_id, EquipmentStatus.IDLE)
    
    def _configure_equipment(self, equipment_id: str, params: Dict):
        """Configure the specified equipment."""
        logger.info(f"Configuring equipment {equipment_id} with params: {params}")
        # In a real implementation, this would send configuration to the actual equipment
    
    def _update_equipment_status(self, equipment_id: str, status: EquipmentStatus):
        """Update the status of equipment in cache."""
        if equipment_id in self.equipment_cache:
            self.equipment_cache[equipment_id].status = status
            self.equipment_cache[equipment_id].timestamp = time.time()
        else:
            logger.warning(f"Equipment {equipment_id} not found in cache")
    
    def connect(self):
        """Connect to both MQTT broker and API services."""
        try:
            # Connect to MQTT
            self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port)
            self.mqtt_client.loop_start()
            
            # Verify API connectivity
            response = requests.get(f"{self.api_base_url}/health", timeout=5)
            if response.status_code != 200:
                raise ConnectionError("Failed to connect to PumpX API")
            
            logger.info("Successfully connected to all services")
            return True
            
        except Exception as e:
            logger.error(f"Connection error: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from all services."""
        try:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
            logger.info("Successfully disconnected from all services")
        except Exception as e:
            logger.error(f"Error during disconnection: {e}")
    
    def publish_equipment_data(self, equipment_data: EquipmentData):
        """Publish equipment data to MQTT broker and API."""
        try:
            # Update cache
            self.equipment_cache[equipment_data.equipment_id] = equipment_data
            
            # Publish to MQTT
            topic = f"pumpx/rollx/telemetry/{equipment_data.equipment_id}"
            payload = {
                "status": equipment_data.status.value,
                "pressure": equipment_data.pressure,
                "flow_rate": equipment_data.flow_rate,
                "temperature": equipment_data.temperature,
                "vibration": equipment_data.vibration,
                "timestamp": equipment_data.timestamp
            }
            self.mqtt_client.publish(topic, json.dumps(payload))
            
            # Send to API
            api_url = f"{self.api_base_url}/equipment/{equipment_data.equipment_id}/telemetry"
            response = requests.post(api_url, json=payload, timeout=5)
            if response.status_code != 200:
                logger.warning(f"Failed to send telemetry to API for equipment {equipment_data.equipment_id}")
            
            logger.debug(f"Published data for equipment {equipment_data.equipment_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error publishing equipment data: {e}")
            return False
    
    def get_equipment_status(self, equipment_id: str) -> Optional
