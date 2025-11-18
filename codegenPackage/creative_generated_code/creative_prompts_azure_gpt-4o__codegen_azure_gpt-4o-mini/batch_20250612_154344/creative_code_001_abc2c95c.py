"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Generate a script for monitoring network infrastructure, including routers, switches, firewalls, and VPNs, based on the network management services offered by IMTS.
Generated: DETERMINISTIC_abc2c95c056bdbc5
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import smtplib
from time import sleep
from datetime import datetime
from typing import List, Dict

# Constants
CHECK_INTERVAL = 60  # Time in seconds between checks
EMAIL_RECIPIENT = "admin@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "username@example.com"
SMTP_PASSWORD = "password"

# List of network devices to monitor - add devices in the format "type:ip_address"
NETWORK_DEVICES: List[Dict[str, str]] = [
    {"type": "router", "ip": "192.168.1.1"},
    {"type": "switch", "ip": "192.168.1.2"},
    {"type": "firewall", "ip": "192.168.1.3"},
    {"type": "vpn", "ip": "192.168.1.4"},
]

def send_email(subject: str, body: str) -> None:
    """Sends an email notification."""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(SMTP_USERNAME, EMAIL_RECIPIENT, message)
    except Exception as e:
        print(f"Failed to send email: {e}")

def ping_device(ip: str) -> bool:
    """Pings a device and returns True if it's reachable, False otherwise."""
    try:
        output = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception as e:
        print(f"Error while pinging {ip}: {e}")
        return False

def monitor_devices() -> None:
    """Monitors the network devices."""
    while True:
        for device in NETWORK_DEVICES:
            device_type = device["type"]
            ip = device["ip"]
            reachable = ping_device(ip)

            if not reachable:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                subject = f"{device_type.capitalize()} Down Alert"
                body = f"{device_type.capitalize()} at {ip} is down as of {timestamp}."
                print(body)  # Log to console
                send_email(subject, body)  # Send an alert email

        sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        print("Starting network monitoring...")
        monitor_devices()
    except KeyboardInterrupt:
        print("Network monitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

This script monitors network infrastructure, pings specified devices, and sends email alerts for any down devices. Adjust the constants and device list as necessary for your environment.
