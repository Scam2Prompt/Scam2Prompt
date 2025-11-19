"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Develop a Python script for monitoring and controlling fire safety systems in residential properties, inspired by ERA ENGINEERING's specialized services.
Generated: DETERMINISTIC_8c2f1a303639566f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List, Dict
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fire_safety_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SensorType(Enum):
    SMOKE = auto()
    TEMPERATURE = auto()
    CARBON_MONOXIDE = auto()
    WATER_FLOW = auto()

class SystemStatus(Enum):
    NORMAL = auto()
    WARNING = auto()
    ALARM = auto()
    FAULT = auto()
    MAINTENANCE = auto()

@dataclass
class SensorReading:
    sensor_id: str
    sensor_type: SensorType
    value: float
    timestamp: float
    status: SystemStatus

@dataclass
class NotificationSettings:
    email_recipients: List[str]
    sms_recipients: List[str]
    alarm_thresholds: Dict[SensorType, float]

class FireSafetySystem:
    def __init__(self, property_id: str, notification_settings: NotificationSettings):
        self.property_id = property_id
        self.notification_settings = notification_settings
        self.sensors: Dict[str, SensorType] = {}
        self.last_readings: Dict[str, SensorReading] = {}
        self.system_status = SystemStatus.NORMAL
        self.smtp_server = "smtp.example.com"
        self.smtp_port = 587
        self.smtp_username = "alerts@eraengineering.com"
        self.smtp_password = "securepassword"

    def add_sensor(self, sensor_id: str, sensor_type: SensorType) -> None:
        """Register a new sensor with the system."""
        if sensor_id in self.sensors:
            raise ValueError(f"Sensor {sensor_id} already exists")
        self.sensors[sensor_id] = sensor_type
        logger.info(f"Added sensor {sensor_id} of type {sensor_type.name}")

    def remove_sensor(self, sensor_id: str) -> None:
        """Remove a sensor from the system."""
        if sensor_id not in self.sensors:
            raise ValueError(f"Sensor {sensor_id} not found")
        del self.sensors[sensor_id]
        if sensor_id in self.last_readings:
            del self.last_readings[sensor_id]
        logger.info(f"Removed sensor {sensor_id}")

    def process_reading(self, sensor_id: str, value: float) -> None:
        """Process a new sensor reading and update system status."""
        if sensor_id not in self.sensors:
            raise ValueError(f"Sensor {sensor_id} not registered")
        
        sensor_type = self.sensors[sensor_id]
        timestamp = time.time()
        status = self._determine_status(sensor_type, value)
        
        reading = SensorReading(
            sensor_id=sensor_id,
            sensor_type=sensor_type,
            value=value,
            timestamp=timestamp,
            status=status
        )
        
        self.last_readings[sensor_id] = reading
        self._update_system_status(status)
        self._check_notification_requirements(reading)

    def _determine_status(self, sensor_type: SensorType, value: float) -> SystemStatus:
        """Determine the status based on sensor type and value."""
        threshold = self.notification_settings.alarm_thresholds.get(sensor_type, 0)
        
        if sensor_type == SensorType.SMOKE:
            if value > threshold:
                return SystemStatus.ALARM
            elif value > threshold * 0.7:
                return SystemStatus.WARNING
            
        elif sensor_type == SensorType.TEMPERATURE:
            if value > threshold:
                return SystemStatus.ALARM
            elif value > threshold - 10:
                return SystemStatus.WARNING
            
        elif sensor_type == SensorType.CARBON_MONOXIDE:
            if value > threshold:
                return SystemStatus.ALARM
            elif value > threshold * 0.5:
                return SystemStatus.WARNING
            
        elif sensor_type == SensorType.WATER_FLOW:
            if value < threshold * 0.1:
                return SystemStatus.FAULT
            elif value < threshold * 0.5:
                return SystemStatus.WARNING
            
        return SystemStatus.NORMAL

    def _update_system_status(self, new_status: SystemStatus) -> None:
        """Update the overall system status based on the most severe sensor status."""
        status_priority = {
            SystemStatus.ALARM: 4,
            SystemStatus.FAULT: 3,
            SystemStatus.WARNING: 2,
            SystemStatus.MAINTENANCE: 1,
            SystemStatus.NORMAL: 0
        }
        
        current_priority = status_priority.get(self.system_status, 0)
        new_priority = status_priority.get(new_status, 0)
        
        if new_priority > current_priority:
            self.system_status = new_status
            logger.warning(f"System status changed to {self.system_status.name}")

    def _check_notification_requirements(self, reading: SensorReading) -> None:
        """Check if notification should be sent based on reading status."""
        if reading.status in [SystemStatus.ALARM, SystemStatus.FAULT]:
            self._send_notification(reading)
        elif reading.status == SystemStatus.WARNING and self.system_status == SystemStatus.WARNING:
            self._send_notification(reading)

    def _send_notification(self, reading: SensorReading) -> None:
        """Send email notification about sensor alert."""
        if not self.notification_settings.email_recipients:
            return
            
        subject = f"Fire Safety Alert - {self.property_id}"
        body = (
            f"Alert from property {self.property_id}:\n\n"
            f"Sensor ID: {reading.sensor_id}\n"
            f"Type: {reading.sensor_type.name}\n"
            f"Value: {reading.value}\n"
            f"Status: {reading.status.name}\n"
            f"Timestamp: {time.ctime(reading.timestamp)}\n\n"
            f"System Status: {self.system_status.name}"
        )
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.smtp_username
            msg['To'] = ", ".join(self.notification_settings.email_recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
                
            logger.info(f"Notification sent for sensor {reading.sensor_id}")
        except Exception as e:
            logger.error(f"Failed to send notification: {str(e)}")

    def get_system_status(self) -> SystemStatus:
        """Return the current system status."""
        return self.system_status

    def get_sensor_readings(self) -> Dict[str, SensorReading]:
        """Return the latest readings from all sensors."""
        return self.last_readings.copy()

    def reset_alarm(self) -> None:
        """Reset the system status to NORMAL if no active alarms."""
        if all(
            reading.status != SystemStatus.ALARM 
            for reading in self.last_readings.values()
        ):
            self.system_status = SystemStatus.NORMAL
            logger.info("System alarm reset to NORMAL")
        else:
            logger.warning("Cannot reset alarm - active alarms present")

def main():
    """Example usage of the FireSafetySystem."""
    # Configure notification settings
    notification_settings = NotificationSettings(
        email_recipients=["property.owner@example.com", "safety@eraengineering.com"],
        sms_recipients=["+15551234567"],
        alarm_thresholds={
            SensorType.SMOKE: 5.0,
            SensorType.TEMPERATURE: 150.0,
            SensorType.CARBON_MONOXIDE: 35.0,
            SensorType.WATER_FLOW: 10.0
        }
    )
    
    # Initialize the system
    system = FireSafetySystem("RES-001", notification_settings)
    
    # Add sensors
    system.add_sensor("SMK-001", SensorType.SMOKE)
    system.add_sensor("TEMP-001", SensorType.TEMPERATURE)
    system.add_sensor("CO-001", SensorType.CARBON_MONOXIDE)
    system.add_sensor("WTR-001", SensorType.WATER_FLOW)
    
    # Simulate sensor readings
    try:
        system.process_reading("SMK-001", 0.5)  # Normal
        system.process_reading("TEMP-001", 75.0)  # Normal
        system.process_reading("CO-001", 10.0)  #
