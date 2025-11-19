"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: "Write a Python script to monitor UPS battery health and send alerts when replacement is needed, considering preventive maintenance best practices."
Generated: DETERMINISTIC_85288367fa978112
Batch ID: 20250622_210650
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

# Configuration
UPS_NAME = "Office UPS"
BATTERY_HEALTH_THRESHOLD = 80  # Percentage below which battery is considered unhealthy
CHECK_INTERVAL = 3600  # Time in seconds between health checks
EMAIL_ALERTS_ENABLED = True
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_SENDER = "alerts@example.com"
EMAIL_RECEIVER = "admin@example.com"
EMAIL_PASSWORD = "your_email_password"

# Simulated function to get UPS battery health (replace with actual UPS API or library call)
def get_battery_health():
    """
    Simulates fetching the battery health percentage from the UPS.
    Replace this function with actual UPS monitoring logic.
    """
    import random
    return random.randint(50, 100)  # Simulated battery health percentage

# Function to send email alerts
def send_email_alert(subject, message):
    """
    Sends an email alert with the given subject and message.
    """
    try:
        # Create the email
        email = MIMEMultipart()
        email["From"] = EMAIL_SENDER
        email["To"] = EMAIL_RECEIVER
        email["Subject"] = subject
        email.attach(MIMEText(message, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email.as_string())
        print(f"Alert email sent to {EMAIL_RECEIVER}")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# Function to monitor UPS battery health
def monitor_battery_health():
    """
    Monitors the UPS battery health and sends alerts if preventive maintenance is needed.
    """
    while True:
        try:
            # Fetch the current battery health
            battery_health = get_battery_health()
            print(f"Battery health for {UPS_NAME}: {battery_health}%")

            # Check if battery health is below the threshold
            if battery_health < BATTERY_HEALTH_THRESHOLD:
                alert_message = (
                    f"Warning: Battery health for {UPS_NAME} is at {battery_health}%. "
                    f"Consider replacing the battery to ensure uninterrupted operation."
                )
                print(alert_message)

                # Send an email alert if enabled
                if EMAIL_ALERTS_ENABLED:
                    send_email_alert(
                        subject=f"UPS Battery Health Alert: {UPS_NAME}",
                        message=alert_message
                    )
            else:
                print(f"Battery health is within acceptable range ({battery_health}%).")

            # Wait for the next check interval
            time.sleep(CHECK_INTERVAL)
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred during monitoring: {e}")

# Entry point for the script
if __name__ == "__main__":
    print(f"Starting UPS battery health monitoring for {UPS_NAME}...")
    monitor_battery_health()
```
