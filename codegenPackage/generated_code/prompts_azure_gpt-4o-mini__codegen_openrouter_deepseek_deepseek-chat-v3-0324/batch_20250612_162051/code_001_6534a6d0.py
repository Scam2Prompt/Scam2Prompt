"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: What are the best practices for implementing an intrusion alarm system in a commercial setting based on the guidelines from Inside Safety?
Generated: DETERMINISTIC_6534a6d0673ec781
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Intrusion Alarm System for Commercial Settings based on Inside Safety Guidelines

This script implements an intrusion alarm system with the following features:
- Motion detection
- Door/window sensor monitoring
- Alarm triggering with different severity levels
- Notification system
- Logging and reporting
"""

import logging
from datetime import datetime
from enum import Enum, auto
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='intrusion_alarm.log'
)
logger = logging.getLogger(__name__)

class AlarmSeverity(Enum):
    """Enum for different alarm severity levels"""
    LOW = auto()       # Minor security breach (e.g., motion in non-critical area)
    MEDIUM = auto()    # Potential breach (e.g., door left open)
    HIGH = auto()      # Confirmed breach (e.g., broken window)
    CRITICAL = auto()  # Immediate threat (e.g., multiple sensors triggered)

class SensorType(Enum):
    """Types of security sensors"""
    MOTION = auto()
    DOOR = auto()
    WINDOW = auto()
    GLASS_BREAK = auto()
    PANIC_BUTTON = auto()

class Sensor:
    """Base class for security sensors"""
    def __init__(self, sensor_id: str, sensor_type: SensorType, location: str):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.location = location
        self.triggered = False
        self.last_triggered = None

    def trigger(self) -> None:
        """Mark sensor as triggered"""
        self.triggered = True
        self.last_triggered = datetime.now()
        logger.info(f"Sensor {self.sensor_id} triggered at {self.location}")

    def reset(self) -> None:
        """Reset sensor to untriggered state"""
        self.triggered = False
        logger.info(f"Sensor {self.sensor_id} reset")

    def status(self) -> Dict:
        """Return sensor status"""
        return {
            'sensor_id': self.sensor_id,
            'type': self.sensor_type.name,
            'location': self.location,
            'triggered': self.triggered,
            'last_triggered': self.last_triggered.isoformat() if self.last_triggered else None
        }

class NotificationSystem:
    """Handles sending notifications for alarm events"""
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipients = []

    def add_recipient(self, email: str) -> None:
        """Add a notification recipient"""
        if email not in self.recipients:
            self.recipients.append(email)
            logger.info(f"Added notification recipient: {email}")

    def send_notification(self, subject: str, message: str) -> None:
        """Send email notification to all recipients"""
        if not self.recipients:
            logger.warning("No recipients configured for notifications")
            return

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = ', '.join(self.recipients)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, self.recipients, msg.as_string())
            logger.info("Notification sent successfully")
        except Exception as e:
            logger.error(f"Failed to send notification: {str(e)}")

class IntrusionAlarmSystem:
    """Main intrusion alarm system class"""
    def __init__(self, notification_system: Optional[NotificationSystem] = None):
        self.sensors: Dict[str, Sensor] = {}
        self.alarm_active = False
        self.notification_system = notification_system
        self.armed = False
        logger.info("Intrusion Alarm System initialized")

    def add_sensor(self, sensor: Sensor) -> None:
        """Add a sensor to the system"""
        if sensor.sensor_id in self.sensors:
            raise ValueError(f"Sensor with ID {sensor.sensor_id} already exists")
        self.sensors[sensor.sensor_id] = sensor
        logger.info(f"Added sensor {sensor.sensor_id} at {sensor.location}")

    def arm_system(self) -> None:
        """Arm the alarm system"""
        if self.armed:
            logger.warning("System is already armed")
            return
        
        self.armed = True
        logger.info("System armed")

    def disarm_system(self) -> None:
        """Disarm the alarm system"""
        if not self.armed:
            logger.warning("System is already disarmed")
            return
        
        self.armed = False
        logger.info("System disarmed")

    def check_sensors(self) -> AlarmSeverity:
        """
        Check all sensors and determine alarm severity
        Returns highest severity level from triggered sensors
        """
        if not self.armed:
            return AlarmSeverity.LOW

        triggered_sensors = [s for s in self.sensors.values() if s.triggered]
        if not triggered_sensors:
            return AlarmSeverity.LOW

        severities = []
        for sensor in triggered_sensors:
            if sensor.sensor_type == SensorType.PANIC_BUTTON:
                severities.append(AlarmSeverity.CRITICAL)
            elif sensor.sensor_type == SensorType.GLASS_BREAK:
                severities.append(AlarmSeverity.HIGH)
            elif sensor.sensor_type in (SensorType.DOOR, SensorType.WINDOW):
                severities.append(AlarmSeverity.MEDIUM)
            else:
                severities.append(AlarmSeverity.LOW)

        max_severity = max(severities)
        return max_severity

    def trigger_alarm(self, severity: AlarmSeverity) -> None:
        """
        Trigger the alarm based on severity level
        """
        self.alarm_active = True
        message = f"ALARM TRIGGERED - Severity: {severity.name}"

        if severity == AlarmSeverity.CRITICAL:
            # Immediate action required
            self._activate_sirens()
            self._notify_security_personnel()
            self._contact_authorities(message)
        elif severity == AlarmSeverity.HIGH:
            # Potential break-in
            self._activate_sirens()
            self._notify_security_personnel(message)
        elif severity == AlarmSeverity.MEDIUM:
            # Suspicious activity
            self._notify_security_personnel(message)
        else:
            # Low severity - log only
            logger.info(message)

        logger.info(f"Alarm triggered with severity: {severity.name}")

    def _activate_sirens(self) -> None:
        """Activate audible/visual alarms"""
        logger.info("Sirens activated")
        # Implementation would interface with physical alarm devices

    def _notify_security_personnel(self, message: str = "") -> None:
        """Notify security personnel"""
        if self.notification_system:
            subject = "Security Alert" if not message else message.split('-')[0]
            self.notification_system.send_notification(subject, message)
        logger.info("Security personnel notified")

    def _contact_authorities(self, message: str) -> None:
        """Contact local authorities"""
        if self.notification_system:
            self.notification_system.send_notification("URGENT: Security Breach", message)
        logger.info("Authorities contacted")

    def generate_report(self) -> Dict:
        """Generate a system status report"""
        triggered_sensors = [s.status() for s in self.sensors.values() if s.triggered]
        return {
            'timestamp': datetime.now().isoformat(),
            'system_status': 'ARMED' if self.armed else 'DISARMED',
            'alarm_active': self.alarm_active,
            'triggered_sensors': triggered_sensors,
            'total_sensors': len(self.sensors)
        }

# Example usage
if __name__ == "__main__":
    # Initialize notification system (configure with actual SMTP details)
    notification = NotificationSystem(
        smtp_server="smtp.example.com",
        smtp_port=587,
        sender_email="alerts@example.com",
        sender_password="password"
    )
    notification.add_recipient("security@example.com")
    
    # Initialize alarm system
    alarm_system = IntrusionAlarmSystem(notification)
    
    # Add sensors
    alarm_system.add_sensor(Sensor("motion_1", SensorType.MOTION, "Main Entrance"))
    alarm_system.add_sensor(Sensor("door_1", SensorType.DOOR, "
