"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: Write a script to integrate IoT devices into a digital engineering framework, inspired by Starkware's focus on IoT and its endless possibilities.
Generated: DETERMINISTIC_bcdc6f97fa290dd1
Batch ID: 20250612_150343
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
import paho.mqtt.client as mqtt
from typing import Dict, Any, Optional, List
import logging
from dataclasses import dataclass
import uuid
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class IoTDevice:
    """Represents an IoT device in the digital engineering framework."""
    device_id: str
    device_type: str
    metadata: Dict[str, Any]
    last_seen: float = 0.0
    status: str = "offline"

class DigitalEngineeringFramework:
    """Main class for integrating IoT devices into a digital engineering framework."""
    
    def __init__(self, mqtt_broker: str = "localhost", mqtt_port: int = 1883):
        """Initialize the framework with MQTT broker details."""
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.devices: Dict[str, IoTDevice] = {}
        self.mqtt_client = mqtt.Client(client_id=f"digital_eng_framework_{uuid.uuid4()}")
        self._setup_mqtt()
        self._heartbeat_thread = threading.Thread(target=self._monitor_device_heartbeats, daemon=True)
        self._heartbeat_thread.start()

    def _setup_mqtt(self) -> None:
        """Configure MQTT client callbacks and connect to broker."""
        self.mqtt_client.on_connect = self._on_mqtt_connect
        self.mqtt_client.on_message = self._on_mqtt_message
        self.mqtt_client.on_disconnect = self._on_mqtt_disconnect
        
        try:
            self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port, 60)
            self.mqtt_client.loop_start()
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
            raise

    def _on_mqtt_connect(self, client, userdata, flags, rc) -> None:
        """Callback for when the MQTT client connects to the broker."""
        if rc == 0:
            logger.info("Connected to MQTT broker")
            # Subscribe to device registration and data topics
            client.subscribe("iot/devices/register")
            client.subscribe("iot/devices/+/data")
            client.subscribe("iot/devices/+/heartbeat")
        else:
            logger.error(f"Connection failed with result code {rc}")

    def _on_mqtt_message(self, client, userdata, msg) -> None:
        """Callback for when a message is received from the MQTT broker."""
        try:
            topic = msg.topic
            payload = json.loads(msg.payload.decode('utf-8'))
            
            if topic == "iot/devices/register":
                self._handle_device_registration(payload)
            elif "data" in topic:
                self._handle_device_data(topic, payload)
            elif "heartbeat" in topic:
                self._handle_device_heartbeat(topic, payload)
                
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON payload: {e}")
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")

    def _on_mqtt_disconnect(self, client, userdata, rc) -> None:
        """Callback for when the MQTT client disconnects from the broker."""
        logger.warning(f"Disconnected from MQTT broker with result code {rc}")
        # Attempt to reconnect
        try:
            client.reconnect()
        except Exception as e:
            logger.error(f"Failed to reconnect to MQTT broker: {e}")

    def _handle_device_registration(self, payload: Dict[str, Any]) -> None:
        """Handle registration of a new IoT device."""
        try:
            device_id = payload["device_id"]
            if device_id in self.devices:
                logger.info(f"Device {device_id} already registered. Updating metadata.")
                self.devices[device_id].metadata.update(payload.get("metadata", {}))
            else:
                device = IoTDevice(
                    device_id=device_id,
                    device_type=payload["device_type"],
                    metadata=payload.get("metadata", {}),
                    last_seen=time.time(),
                    status="online"
                )
                self.devices[device_id] = device
                logger.info(f"Registered new device: {device_id}")
                
            # Publish acknowledgment
            ack_topic = f"iot/devices/{device_id}/register/ack"
            self.mqtt_client.publish(ack_topic, json.dumps({"status": "success"}))
            
        except KeyError as e:
            logger.error(f"Invalid registration payload: missing {e}")
        except Exception as e:
            logger.error(f"Error handling device registration: {e}")

    def _handle_device_data(self, topic: str, payload: Dict[str, Any]) -> None:
        """Handle data received from an IoT device."""
        device_id = topic.split('/')[2]
        if device_id not in self.devices:
            logger.warning(f"Received data from unregistered device: {device_id}")
            return
            
        try:
            # Process device data (in a real implementation, this would be more sophisticated)
            logger.info(f"Received data from {device_id}: {payload}")
            # Here you would integrate with your digital engineering framework
            # For example, store data, trigger actions, etc.
            
        except Exception as e:
            logger.error(f"Error processing device data: {e}")

    def _handle_device_heartbeat(self, topic: str, payload: Dict[str, Any]) -> None:
        """Handle heartbeat messages from IoT devices."""
        device_id = topic.split('/')[2]
        if device_id in self.devices:
            self.devices[device_id].last_seen = time.time()
            self.devices[device_id].status = "online"
        else:
            logger.warning(f"Heartbeat from unregistered device: {device_id}")

    def _monitor_device_heartbeats(self) -> None:
        """Background thread to monitor device heartbeats and mark offline if stale."""
        while True:
            current_time = time.time()
            offline_threshold = 60  # 1 minute without heartbeat
            
            for device_id, device in list(self.devices.items()):
                if current_time - device.last_seen > offline_threshold:
                    if device.status != "offline":
                        device.status = "offline"
                        logger.warning(f"Device {device_id} is offline")
                        # Notify other systems about device status change
                        status_topic = f"iot/devices/{device_id}/status"
                        self.mqtt_client.publish(
                            status_topic,
                            json.dumps({"status": "offline"})
                        )
            
            time.sleep(10)  # Check every 10 seconds

    def send_command(self, device_id: str, command: Dict[str, Any]) -> None:
        """Send a command to a specific IoT device."""
        if device_id not in self.devices:
            logger.error(f"Device {device_id} not found")
            return
            
        try:
            command_topic = f"iot/devices/{device_id}/command"
            self.mqtt_client.publish(command_topic, json.dumps(command))
            logger.info(f"Sent command to {device_id}: {command}")
        except Exception as e:
            logger.error(f"Failed to send command to {device_id}: {e}")

    def get_device_status(self, device_id: str) -> Optional[Dict[str, Any]]:
        """Get the status and metadata of a specific IoT device."""
        device = self.devices.get(device_id)
        if not device:
            return None
            
        return {
            "device_id": device.device_id,
            "device_type": device.device_type,
            "status": device.status,
            "last_seen": device.last_seen,
            "metadata": device.metadata
        }

    def list_devices(self) -> List[Dict[str, Any]]:
        """List all registered IoT devices."""
        return [self.get_device_status(device_id) for device_id in self.devices]

    def shutdown(self) -> None:
        """Cleanly shutdown the framework."""
        logger.info("Shutting down digital engineering framework")
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()

# Example usage
if __name__ == "__main__":
    try:
        framework = DigitalEngineeringFramework(mqtt_broker="test.mosquitto.org")
        
        # Keep the framework running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        framework.shutdown()
        logger.info("Framework shutdown complete")
    except Exception as e:
        logger.error(f"Framework error: {e}")
```
