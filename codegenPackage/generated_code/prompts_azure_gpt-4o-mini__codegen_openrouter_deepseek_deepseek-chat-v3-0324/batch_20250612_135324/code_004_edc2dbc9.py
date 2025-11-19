"""
Generated Code Metadata:
========================
Original URL: https://starkware.in
Prompt: Illustrate how to implement IoT solutions in a business context, drawing from Starkware's exploration of digital engineering and IoT technologies.
Generated: DETERMINISTIC_edc2dbc9837e5f47
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
IoT Business Solution Implementation

This script demonstrates a simplified IoT solution for a business context,
inspired by Starkware's digital engineering and IoT technologies.
It includes device simulation, data collection, processing, and analytics.

Key Components:
- IoT Device Simulation
- Data Collection Service
- Data Processing Pipeline
- Analytics Dashboard
- Alerting System
"""

import random
import time
import json
from datetime import datetime
from typing import Dict, List, Optional
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class IoTDevice(ABC):
    """Abstract base class for IoT devices."""
    
    def __init__(self, device_id: str, device_type: str):
        self.device_id = device_id
        self.device_type = device_type
        self.status = "offline"
        self.last_reading_time = None
    
    @abstractmethod
    def collect_data(self) -> Dict:
        """Collect data from the device."""
        pass
    
    def connect(self) -> bool:
        """Simulate device connection."""
        self.status = "online"
        logger.info(f"Device {self.device_id} connected")
        return True
    
    def disconnect(self) -> bool:
        """Simulate device disconnection."""
        self.status = "offline"
        logger.info(f"Device {self.device_id} disconnected")
        return True


class TemperatureSensor(IoTDevice):
    """Concrete implementation of a temperature sensor device."""
    
    def __init__(self, device_id: str):
        super().__init__(device_id, "temperature_sensor")
        self.min_temp = -20
        self.max_temp = 50
    
    def collect_data(self) -> Dict:
        """Collect temperature data with timestamp."""
        if self.status != "online":
            raise ConnectionError("Device is offline")
        
        temp = round(random.uniform(self.min_temp, self.max_temp), 2)
        self.last_reading_time = datetime.utcnow().isoformat()
        
        return {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "temperature": temp,
            "timestamp": self.last_reading_time,
            "unit": "Celsius"
        }


class DataCollector:
    """Service to collect data from multiple IoT devices."""
    
    def __init__(self):
        self.devices: Dict[str, IoTDevice] = {}
    
    def register_device(self, device: IoTDevice) -> bool:
        """Register a new IoT device."""
        if device.device_id in self.devices:
            logger.warning(f"Device {device.device_id} already registered")
            return False
        
        self.devices[device.device_id] = device
        logger.info(f"Registered device {device.device_id}")
        return True
    
    def collect_all_data(self) -> List[Dict]:
        """Collect data from all registered devices."""
        data = []
        for device_id, device in self.devices.items():
            try:
                if device.connect():
                    device_data = device.collect_data()
                    data.append(device_data)
                    device.disconnect()
            except Exception as e:
                logger.error(f"Error collecting data from {device_id}: {str(e)}")
        
        return data


class DataProcessor:
    """Process and analyze IoT data."""
    
    def __init__(self):
        self.alert_thresholds = {
            "temperature_sensor": {
                "min": 0,
                "max": 30
            }
        }
    
    def process_data(self, raw_data: List[Dict]) -> Dict:
        """Process raw IoT data and generate insights."""
        processed = {
            "devices": len(raw_data),
            "readings": raw_data,
            "alerts": [],
            "stats": {}
        }
        
        # Calculate statistics
        temp_readings = [
            d["temperature"] for d in raw_data 
            if d["device_type"] == "temperature_sensor"
        ]
        
        if temp_readings:
            processed["stats"]["temperature"] = {
                "average": round(sum(temp_readings) / len(temp_readings), 2),
                "min": min(temp_readings),
                "max": max(temp_readings)
            }
        
        # Check for alerts
        for reading in raw_data:
            device_type = reading["device_type"]
            if device_type in self.alert_thresholds:
                thresholds = self.alert_thresholds[device_type]
                if "temperature" in reading:
                    temp = reading["temperature"]
                    if temp < thresholds["min"]:
                        processed["alerts"].append({
                            "device_id": reading["device_id"],
                            "type": "LOW_TEMPERATURE",
                            "value": temp,
                            "threshold": thresholds["min"],
                            "timestamp": reading["timestamp"]
                        })
                    elif temp > thresholds["max"]:
                        processed["alerts"].append({
                            "device_id": reading["device_id"],
                            "type": "HIGH_TEMPERATURE",
                            "value": temp,
                            "threshold": thresholds["max"],
                            "timestamp": reading["timestamp"]
                        })
        
        return processed


class Dashboard:
    """Visual representation of IoT data and analytics."""
    
    @staticmethod
    def display(data: Dict) -> None:
        """Display processed data in a human-readable format."""
        print("\n=== IoT DASHBOARD ===")
        print(f"Devices Online: {data['devices']}")
        
        if "temperature" in data["stats"]:
            stats = data["stats"]["temperature"]
            print(f"\nTemperature Statistics:")
            print(f"  Average: {stats['average']}°C")
            print(f"  Minimum: {stats['min']}°C")
            print(f"  Maximum: {stats['max']}°C")
        
        if data["alerts"]:
            print("\n=== ALERTS ===")
            for alert in data["alerts"]:
                print(
                    f"{alert['timestamp']} - {alert['device_id']}: "
                    f"{alert['type']} ({alert['value']} vs threshold {alert['threshold']})"
                )


class AlertSystem:
    """System for handling and notifying about alerts."""
    
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, callback) -> None:
        """Subscribe to receive alert notifications."""
        self.subscribers.append(callback)
    
    def notify(self, alerts: List[Dict]) -> None:
        """Notify all subscribers about new alerts."""
        for alert in alerts:
            for callback in self.subscribers:
                try:
                    callback(alert)
                except Exception as e:
                    logger.error(f"Error in alert notification: {str(e)}")


def email_alert_handler(alert: Dict) -> None:
    """Example alert handler that simulates sending email alerts."""
    subject = f"IoT Alert: {alert['type']}"
    body = (
        f"Device: {alert['device_id']}\n"
        f"Value: {alert['value']}\n"
        f"Threshold: {alert['threshold']}\n"
        f"Time: {alert['timestamp']}"
    )
    logger.info(f"Email Alert Sent:\nSubject: {subject}\nBody: {body}")


def main():
    """Main execution of the IoT solution."""
    try:
        # Initialize components
        collector = DataCollector()
        processor = DataProcessor()
        dashboard = Dashboard()
        alert_system = AlertSystem()
        
        # Subscribe alert handlers
        alert_system.subscribe(email_alert_handler)
        
        # Register devices
        devices = [
            TemperatureSensor("temp_sensor_1"),
            TemperatureSensor("temp_sensor_2"),
            TemperatureSensor("temp_sensor_3")
        ]
        
        for device in devices:
            collector.register_device(device)
        
        # Main loop
        while True:
            try:
                # Collect data
                raw_data = collector.collect_all_data()
                
                if not raw_data:
                    logger.warning("No data collected from devices")
                    time.sleep(5)
                    continue
                
                # Process data
                processed_data = processor.process_data(raw_data)
                
                # Display dashboard
                dashboard.display(processed_data)
                
                # Handle alerts
                if processed_data["alerts"]:
                    alert_system.notify(processed_data["alerts"])
                
                # Wait before next collection
                time.sleep(10)
                
            except KeyboardInterrupt:
                logger.info("Shutting down IoT system...")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {str(e)}")
                time.sleep(5)
    
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
```
