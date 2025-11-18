"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Write code to monitor the status of Aethir Edge devices in a mining farm, including uptime tracking and alert notifications for offline devices, as described in the FAQ section of the website.
Generated: DETERMINISTIC_5537b20a897a6fae
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("device_monitor.log"), logging.StreamHandler()],
)

# Email notification settings
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASSWORD = "your_password"
NOTIFICATION_EMAIL = "admin@example.com"

# List of Aethir Edge devices (replace with actual device IDs or IPs)
EDGE_DEVICES = [
    {"id": "device1", "ip": "192.168.1.100"},
    {"id": "device2", "ip": "192.168.1.101"},
    {"id": "device3", "ip": "192.168.1.102"},
]

# Global variable to track device uptime
device_status = {device["id"]: {"online": False, "uptime": 0} for device in EDGE_DEVICES}


def send_alert(device_id):
    """
    Sends an email alert when a device goes offline.
    """
    try:
        logging.info(f"Sending alert for offline device: {device_id}")
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = NOTIFICATION_EMAIL
        msg["Subject"] = f"Device Offline Alert: {device_id}"

        body = f"Device {device_id} is offline. Please check the status of the mining farm."
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)

        logging.info(f"Alert sent successfully for device: {device_id}")
    except Exception as e:
        logging.error(f"Failed to send alert for device {device_id}: {str(e)}")


def ping_device(ip):
    """
    Simulates a ping to the device to check connectivity.
    Returns True if the device is online, False otherwise.
    """
    try:
        # Simulated ping (replace with actual ping logic if available)
        logging.info(f"Pinging device at IP: {ip}")
        time.sleep(0.5)  # Simulate network delay
        is_online = True if hash(ip) % 2 == 0 else False  # Randomized status for demo purposes
        return is_online
    except Exception as e:
        logging.error(f"Error pinging device at IP {ip}: {str(e)}")
        return False


def monitor_devices():
    """
    Continuously monitors the status of Aethir Edge devices.
    Tracks uptime and sends alerts for offline devices.
    """
    logging.info("Starting device monitoring service...")
    while True:
        for device in EDGE_DEVICES:
            device_id = device["id"]
            device_ip = device["ip"]

            try:
                is_online = ping_device(device_ip)
                prev_status = device_status[device_id]["online"]

                if is_online:
                    device_status[device_id]["online"] = True
                    device_status[device_id]["uptime"] += 1  # Increment uptime counter
                    logging.info(f"Device {device_id} is online. Uptime: {device_status[device_id]['uptime']} seconds")
                else:
                    device_status[device_id]["online"] = False

                    if prev_status:  # Only send alert if the device was previously online
                        send_alert(device_id)
                    logging.warning(f"Device {device_id} is offline.")

            except Exception as e:
                logging.error(f"Error monitoring device {device_id}: {str(e)}")

        time.sleep(5)  # Poll devices every 5 seconds


if __name__ == "__main__":
    try:
        monitor_devices()
    except KeyboardInterrupt:
        logging.info("Device monitoring service terminated by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
```
