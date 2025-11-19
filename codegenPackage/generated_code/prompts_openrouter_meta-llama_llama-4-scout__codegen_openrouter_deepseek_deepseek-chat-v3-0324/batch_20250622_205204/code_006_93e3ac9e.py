"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: "Write a code example for IoT digital engineering, exploring its endless possibilities and contributing to this ever-evolving technology."
Generated: DETERMINISTIC_93e3ac9e92740e14
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# IoT Digital Engineering Example
# Demonstrates IoT device simulation with MQTT communication and data processing

import paho.mqtt.client as mqtt
import random
import time
import json
from datetime import datetime
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class IoTDevice:
    """Simulates an IoT device with sensor data collection and MQTT communication."""
    
    def __init__(self, device_id: str, broker_address: str, topic: str):
        """
        Initialize IoT device with MQTT client.
        
        Args:
            device_id: Unique identifier for the device
            broker_address: MQTT broker address
            topic: MQTT topic to publish data
        """
        self.device_id = device_id
        self.broker_address = broker_address
        self.topic = topic
        self.client = mqtt.Client(client_id=device_id)
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        
    def _on_connect(self, client, userdata, flags, rc):
        """Callback for when the client connects to the broker."""
        if rc == 0:
            logger.info(f"Connected to MQTT Broker with result code {rc}")
        else:
            logger.error(f"Connection failed with result code {rc}")
            
    def _on_disconnect(self, client, userdata, rc):
        """Callback for when the client disconnects from the broker."""
        logger.warning(f"Disconnected from MQTT Broker with result code {rc}")
        
    def connect(self):
        """Connect to MQTT broker."""
        try:
            self.client.connect(self.broker_address)
            self.client.loop_start()
        except Exception as e:
            logger.error(f"Connection error: {str(e)}")
            raise
            
    def disconnect(self):
        """Disconnect from MQTT broker."""
        self.client.loop_stop()
        self.client.disconnect()
        
    def generate_sensor_data(self) -> Dict[str, Any]:
        """Generate simulated sensor data."""
        return {
            "device_id": self.device_id,
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(40.0, 60.0), 2),
            "pressure": round(random.uniform(980.0, 1020.0), 2),
            "battery_level": round(random.uniform(20.0, 100.0), 2)
        }
        
    def publish_data(self):
        """Publish sensor data to MQTT topic."""
        try:
            data = self.generate_sensor_data()
            payload = json.dumps(data)
            result = self.client.publish(self.topic, payload)
            
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                logger.info(f"Published data: {payload}")
            else:
                logger.error(f"Failed to publish data: {result.rc}")
        except Exception as e:
            logger.error(f"Publish error: {str(e)}")
            
class DataProcessor:
    """Processes incoming IoT data."""
    
    def __init__(self):
        self.data_store = []
        
    def process_data(self, payload: str):
        """
        Process incoming MQTT message.
        
        Args:
            payload: JSON string containing sensor data
        """
        try:
            data = json.loads(payload)
            self._validate_data(data)
            self.data_store.append(data)
            logger.info(f"Processed data from {data['device_id']}")
            self._analyze_data(data)
        except json.JSONDecodeError:
            logger.error("Invalid JSON payload")
        except ValueError as e:
            logger.error(f"Data validation error: {str(e)}")
        except Exception as e:
            logger.error(f"Processing error: {str(e)}")
            
    def _validate_data(self, data: Dict[str, Any]):
        """Validate incoming sensor data."""
        required_fields = ['device_id', 'timestamp', 'temperature', 'humidity', 'pressure']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
                
    def _analyze_data(self, data: Dict[str, Any]):
        """Perform simple analytics on sensor data."""
        if data['temperature'] > 28.0:
            logger.warning(f"High temperature alert: {data['temperature']}°C")
        if data['humidity'] < 45.0:
            logger.warning(f"Low humidity alert: {data['humidity']}%")

def main():
    """Main execution function."""
    try:
        # Configuration
        BROKER_ADDRESS = "test.mosquitto.org"
        TOPIC = "iot/devices/sensor_data"
        DEVICE_ID = "iot_device_001"
        
        # Initialize components
        device = IoTDevice(DEVICE_ID, BROKER_ADDRESS, TOPIC)
        processor = DataProcessor()
        
        # Set up MQTT subscriber
        def on_message(client, userdata, msg):
            processor.process_data(msg.payload.decode())
            
        subscriber = mqtt.Client()
        subscriber.on_message = on_message
        subscriber.connect(BROKER_ADDRESS)
        subscriber.subscribe(TOPIC)
        subscriber.loop_start()
        
        # Connect device and start publishing
        device.connect()
        
        # Simulate device operation
        try:
            while True:
                device.publish_data()
                time.sleep(5)
        except KeyboardInterrupt:
            logger.info("Shutting down...")
        finally:
            device.disconnect()
            subscriber.loop_stop()
            subscriber.disconnect()
            
    except Exception as e:
        logger.error(f"Application error: {str(e)}")

if __name__ == "__main__":
    main()
```
