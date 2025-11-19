"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: Create a simulation script for testing a real-time health monitoring system using IoT devices, based on the features highlighted by Hooshmand Teb.
Generated: DETERMINISTIC_40286bef8e9ef6b9
Batch ID: 20250612_153225
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
from datetime import datetime
import paho.mqtt.client as mqtt
from typing import Dict, Any, Optional

# Configuration for MQTT Broker
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC_PUBLISH = "health_monitoring/data"
MQTT_TOPIC_SUBSCRIBE = "health_monitoring/alerts"

# Simulated IoT Device Configuration
DEVICE_ID = "health_monitor_001"
PATIENT_ID = "patient_123"
SAMPLE_RATE = 5  # seconds between readings

# Health thresholds for alerts
HEART_RATE_THRESHOLDS = {"min": 60, "max": 100}
BLOOD_PRESSURE_THRESHOLDS = {"systolic_min": 90, "systolic_max": 140, "diastolic_min": 60, "diastolic_max": 90}
TEMPERATURE_THRESHOLDS = {"min": 36.1, "max": 37.2}
OXYGEN_THRESHOLDS = {"min": 95, "max": 100}

class HealthMonitorSimulator:
    """
    Simulates an IoT health monitoring device that collects and publishes health metrics.
    Also subscribes to alerts from the monitoring system.
    """
    
    def __init__(self):
        self.client = mqtt.Client(client_id=DEVICE_ID)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        
    def on_connect(self, client, userdata, flags, rc):
        """Callback when connected to MQTT broker."""
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        else:
            print(f"Failed to connect, return code {rc}")
    
    def on_message(self, client, userdata, msg):
        """Callback when a message is received on a subscribed topic."""
        try:
            payload = json.loads(msg.payload.decode())
            print(f"Received alert: {payload}")
        except Exception as e:
            print(f"Error processing message: {e}")
    
    def on_disconnect(self, client, userdata, rc):
        """Callback when disconnected from MQTT broker."""
        print(f"Disconnected from MQTT Broker with code: {rc}")
        if rc != 0:
            print("Reconnecting...")
            self.reconnect()
    
    def reconnect(self):
        """Attempt to reconnect to the MQTT broker."""
        max_retries = 5
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                self.client.reconnect()
                print("Reconnected successfully!")
                return
            except Exception as e:
                print(f"Reconnection failed: {e}")
                retry_count += 1
                time.sleep(5)
        
        print("Max retries reached. Could not reconnect.")
    
    def generate_health_data(self) -> Dict[str, Any]:
        """Generate simulated health data with random values within realistic ranges."""
        timestamp = datetime.now().isoformat()
        
        heart_rate = random.randint(50, 120)
        systolic_bp = random.randint(80, 160)
        diastolic_bp = random.randint(50, 100)
        temperature = round(random.uniform(35.5, 38.5), 1)
        oxygen_level = random.randint(90, 100)
        
        # Simulate occasional abnormal readings
        if random.random() < 0.1:  # 10% chance of abnormal reading
            heart_rate = random.choice([random.randint(30, 59), random.randint(101, 150)])
        
        return {
            "device_id": DEVICE_ID,
            "patient_id": PATIENT_ID,
            "timestamp": timestamp,
            "heart_rate": heart_rate,
            "blood_pressure": {
                "systolic": systolic_bp,
                "diastolic": diastolic_bp
            },
            "temperature": temperature,
            "oxygen_level": oxygen_level
        }
    
    def check_health_alerts(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Check if any health metrics are outside normal thresholds."""
        alerts = []
        
        if not HEART_RATE_THRESHOLDS["min"] <= data["heart_rate"] <= HEART_RATE_THRESHOLDS["max"]:
            alerts.append({
                "metric": "heart_rate",
                "value": data["heart_rate"],
                "threshold": HEART_RATE_THRESHOLDS
            })
        
        bp = data["blood_pressure"]
        if not (BLOOD_PRESSURE_THRESHOLDS["systolic_min"] <= bp["systolic"] <= BLOOD_PRESSURE_THRESHOLDS["systolic_max"] and
                BLOOD_PRESSURE_THRESHOLDS["diastolic_min"] <= bp["diastolic"] <= BLOOD_PRESSURE_THRESHOLDS["diastolic_max"]):
            alerts.append({
                "metric": "blood_pressure",
                "value": bp,
                "threshold": BLOOD_PRESSURE_THRESHOLDS
            })
        
        if not TEMPERATURE_THRESHOLDS["min"] <= data["temperature"] <= TEMPERATURE_THRESHOLDS["max"]:
            alerts.append({
                "metric": "temperature",
                "value": data["temperature"],
                "threshold": TEMPERATURE_THRESHOLDS
            })
        
        if not OXYGEN_THRESHOLDS["min"] <= data["oxygen_level"] <= OXYGEN_THRESHOLDS["max"]:
            alerts.append({
                "metric": "oxygen_level",
                "value": data["oxygen_level"],
                "threshold": OXYGEN_THRESHOLDS
            })
        
        if alerts:
            return {
                "patient_id": PATIENT_ID,
                "device_id": DEVICE_ID,
                "timestamp": data["timestamp"],
                "alerts": alerts
            }
        return None
    
    def publish_data(self, data: Dict[str, Any]):
        """Publish health data to MQTT topic."""
        try:
            payload = json.dumps(data)
            result = self.client.publish(MQTT_TOPIC_PUBLISH, payload)
            
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Published data: {data['timestamp']}")
            else:
                print(f"Failed to publish message: {result.rc}")
        except Exception as e:
            print(f"Error publishing data: {e}")
    
    def run(self):
        """Main loop to generate and publish health data."""
        try:
            self.client.connect(MQTT_BROKER, MQTT_PORT)
            self.client.loop_start()
            
            while True:
                data = self.generate_health_data()
                self.publish_data(data)
                
                alert = self.check_health_alerts(data)
                if alert:
                    self.publish_data(alert)
                
                time.sleep(SAMPLE_RATE)
                
        except KeyboardInterrupt:
            print("Simulation stopped by user")
        except Exception as e:
            print(f"Error in simulation: {e}")
        finally:
            self.client.loop_stop()
            self.client.disconnect()

if __name__ == "__main__":
    simulator = HealthMonitorSimulator()
    simulator.run()
```
