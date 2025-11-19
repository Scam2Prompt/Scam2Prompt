"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: "Generate code for monitoring and controlling industrial refrigeration systems using pumps with magnetic coupling, including alert systems for temperature fluctuations."
Generated: DETERMINISTIC_dce9a4d0a8aee22e
Batch ID: 20250622_204932
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
        logging.FileHandler('refrigeration_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AlertLevel(Enum):
    INFO = auto()
    WARNING = auto()
    CRITICAL = auto()

@dataclass
class Alert:
    message: str
    level: AlertLevel
    timestamp: float = time.time()

class PumpStatus(Enum):
    RUNNING = auto()
    STOPPED = auto()
    FAULT = auto()

@dataclass
class Pump:
    id: str
    name: str
    status: PumpStatus
    temperature: float
    last_maintenance: float
    magnetic_coupling_health: float  # 0-100%

class RefrigerationSystem:
    def __init__(self, system_id: str, name: str, min_temp: float, max_temp: float):
        self.system_id = system_id
        self.name = name
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.pumps: Dict[str, Pump] = {}
        self.alerts: List[Alert] = []
        self.email_config: Optional[Dict] = None

    def add_pump(self, pump: Pump) -> None:
        """Add a pump to the system."""
        self.pumps[pump.id] = pump

    def remove_pump(self, pump_id: str) -> None:
        """Remove a pump from the system."""
        if pump_id in self.pumps:
            del self.pumps[pump_id]

    def update_pump_temperature(self, pump_id: str, temperature: float) -> None:
        """Update pump temperature and check for alerts."""
        if pump_id not in self.pumps:
            logger.warning(f"Pump {pump_id} not found in system {self.system_id}")
            return

        pump = self.pumps[pump_id]
        pump.temperature = temperature

        # Check temperature thresholds
        if temperature > self.max_temp:
            self._add_alert(
                f"High temperature alert on pump {pump_id}: {temperature}°C (max: {self.max_temp}°C)",
                AlertLevel.CRITICAL
            )
        elif temperature < self.min_temp:
            self._add_alert(
                f"Low temperature alert on pump {pump_id}: {temperature}°C (min: {self.min_temp}°C)",
                AlertLevel.WARNING
            )

        # Check magnetic coupling health
        if pump.magnetic_coupling_health < 30:
            self._add_alert(
                f"Low magnetic coupling health on pump {pump_id}: {pump.magnetic_coupling_health}%",
                AlertLevel.WARNING
            )

    def _add_alert(self, message: str, level: AlertLevel) -> None:
        """Internal method to add an alert and trigger notifications."""
        alert = Alert(message, level)
        self.alerts.append(alert)
        logger.log(
            logging.WARNING if level == AlertLevel.WARNING else logging.ERROR,
            message
        )
        self._send_notification(alert)

    def _send_notification(self, alert: Alert) -> None:
        """Send email notification for critical alerts."""
        if self.email_config is None or alert.level == AlertLevel.INFO:
            return

        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender']
            msg['To'] = ', '.join(self.email_config['recipients'])
            msg['Subject'] = f"{alert.level.name} Alert: {self.name}"

            body = f"""
            System: {self.name} ({self.system_id})
            Time: {time.ctime(alert.timestamp)}
            Alert: {alert.message}
            """
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(
                host=self.email_config['smtp_server'],
                port=self.email_config['smtp_port']
            ) as server:
                if self.email_config.get('use_tls', False):
                    server.starttls()
                if 'username' in self.email_config:
                    server.login(
                        self.email_config['username'],
                        self.email_config['password']
                    )
                server.send_message(msg)
                logger.info(f"Sent alert email for: {alert.message}")

        except Exception as e:
            logger.error(f"Failed to send alert email: {str(e)}")

    def get_status_report(self) -> Dict:
        """Generate a system status report."""
        return {
            'system_id': self.system_id,
            'name': self.name,
            'timestamp': time.time(),
            'pumps': [
                {
                    'id': pump.id,
                    'name': pump.name,
                    'status': pump.status.name,
                    'temperature': pump.temperature,
                    'magnetic_coupling_health': pump.magnetic_coupling_health
                }
                for pump in self.pumps.values()
            ],
            'active_alerts': [
                {
                    'message': alert.message,
                    'level': alert.level.name,
                    'timestamp': alert.timestamp
                }
                for alert in self.alerts[-10:]  # Last 10 alerts
            ]
        }

    def control_pump(self, pump_id: str, action: str) -> bool:
        """Control pump operation (start/stop)."""
        if pump_id not in self.pumps:
            logger.warning(f"Pump {pump_id} not found in system {self.system_id}")
            return False

        pump = self.pumps[pump_id]
        
        if action.lower() == 'start':
            if pump.status == PumpStatus.FAULT:
                logger.warning(f"Cannot start pump {pump_id} - in fault state")
                return False
            pump.status = PumpStatus.RUNNING
            logger.info(f"Started pump {pump_id}")
            return True
        elif action.lower() == 'stop':
            pump.status = PumpStatus.STOPPED
            logger.info(f"Stopped pump {pump_id}")
            return True
        else:
            logger.warning(f"Invalid action '{action}' for pump {pump_id}")
            return False

# Example usage
if __name__ == "__main__":
    # Create a refrigeration system
    system = RefrigerationSystem(
        system_id="RS-001",
        name="Main Refrigeration System",
        min_temp=-20.0,
        max_temp=5.0
    )

    # Configure email alerts
    system.email_config = {
        'sender': 'monitoring@example.com',
        'recipients': ['operator@example.com', 'manager@example.com'],
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'use_tls': True,
        'username': 'user@example.com',
        'password': 'password'
    }

    # Add pumps
    system.add_pump(Pump(
        id="P-001",
        name="Primary Pump",
        status=PumpStatus.RUNNING,
        temperature=2.5,
        last_maintenance=time.time() - 86400 * 30,  # 30 days ago
        magnetic_coupling_health=85.0
    ))

    system.add_pump(Pump(
        id="P-002",
        name="Backup Pump",
        status=PumpStatus.STOPPED,
        temperature=-5.0,
        last_maintenance=time.time() - 86400 * 60,  # 60 days ago
        magnetic_coupling_health=25.0
    ))

    # Simulate temperature updates
    system.update_pump_temperature("P-001", 6.0)  # Should trigger high temp alert
    system.update_pump_temperature("P-002", -25.0)  # Should trigger low temp alert

    # Generate status report
    print(system.get_status_report())

    # Control pumps
    system.control_pump("P-002", "start")
    system.control_pump("P-001", "stop")
```
