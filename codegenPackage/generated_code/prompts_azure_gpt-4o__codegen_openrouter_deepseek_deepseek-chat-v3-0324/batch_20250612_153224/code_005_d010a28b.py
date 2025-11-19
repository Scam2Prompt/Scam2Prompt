"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Develop code to automate electric fence monitoring and alert systems for residential security, referencing the installation services provided by Donture Systems Ltd.
Generated: DETERMINISTIC_d010a28b54cfc184
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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO  # Assuming Raspberry Pi for hardware interface

# Configuration
CONFIG = {
    "email": {
        "sender": "security@donturesystems.com",
        "password": "secure_password",
        "recipient": "homeowner@example.com",
        "smtp_server": "smtp.donturesystems.com",
        "smtp_port": 587
    },
    "fence": {
        "sensor_pin": 17,  # GPIO pin connected to fence sensor
        "check_interval": 30,  # seconds between checks
        "voltage_threshold": 5000  # minimum voltage in millivolts
    },
    "alert": {
        "max_retries": 3,
        "cooldown": 300  # seconds between alerts for same issue
    }
}

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONFIG["fence"]["sensor_pin"], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class FenceMonitor:
    def __init__(self):
        self.last_alert_time = 0
        self.alert_retries = 0

    def read_fence_status(self):
        """Read the current fence voltage status."""
        try:
            # Simulating voltage reading - replace with actual hardware interface
            voltage = GPIO.input(CONFIG["fence"]["sensor_pin"]) * 5000
            return voltage >= CONFIG["fence"]["voltage_threshold"], voltage
        except Exception as e:
            print(f"Error reading fence status: {e}")
            return False, 0

    def send_alert(self, subject, message):
        """Send email alert about fence status."""
        current_time = time.time()
        if (current_time - self.last_alert_time) < CONFIG["alert"]["cooldown"]:
            return False

        try:
            msg = MIMEMultipart()
            msg["From"] = CONFIG["email"]["sender"]
            msg["To"] = CONFIG["email"]["recipient"]
            msg["Subject"] = f"Donture Fence Alert: {subject}"

            body = f"""
            Donture Electric Fence Monitoring System Alert:
            
            {message}
            
            Time: {time.strftime('%Y-%m-%d %H:%M:%S')}
            
            Please check your fence system or contact Donture Systems Ltd
            for immediate assistance.
            """
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(
                CONFIG["email"]["smtp_server"],
                CONFIG["email"]["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    CONFIG["email"]["sender"],
                    CONFIG["email"]["password"]
                )
                server.send_message(msg)

            self.last_alert_time = current_time
            self.alert_retries = 0
            return True

        except Exception as e:
            print(f"Error sending alert: {e}")
            self.alert_retries += 1
            if self.alert_retries >= CONFIG["alert"]["max_retries"]:
                print("Max retries reached for alert")
                self.alert_retries = 0
            return False

    def monitor_loop(self):
        """Main monitoring loop."""
        print("Donture Electric Fence Monitoring System started")
        while True:
            try:
                is_active, voltage = self.read_fence_status()
                
                if not is_active:
                    self.send_alert(
                        "Low Voltage Detected",
                        f"Fence voltage dropped to {voltage}mV (below threshold of {CONFIG['fence']['voltage_threshold']}mV)"
                    )
                else:
                    print(f"Fence status OK - Voltage: {voltage}mV")

            except Exception as e:
                print(f"Monitoring error: {e}")

            time.sleep(CONFIG["fence"]["check_interval"])

    def cleanup(self):
        """Clean up resources."""
        GPIO.cleanup()

if __name__ == "__main__":
    monitor = FenceMonitor()
    try:
        monitor.monitor_loop()
    except KeyboardInterrupt:
        print("\nStopping monitoring...")
    finally:
        monitor.cleanup()
```
