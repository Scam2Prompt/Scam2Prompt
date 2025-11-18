"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasnavi.pages.dev
Prompt: Develop a script to send maintenance alerts for insurance, inspection, and road tax expiration based on vehicle data stored in Atlas Navi's NFT car garage.
Generated: DETERMINISTIC_d40da443cb07fece
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Constants
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_USERNAME = "your-email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your-password"  # Replace with your email password
ALERT_DAYS_BEFORE = 7  # Number of days before expiration to send alert

# Vehicle data for demonstration purposes. Replace with real NFT data source.
vehicle_data = [
    {
        "owner": "john.doe@example.com",
        "vehicle_model": "Tesla Model 3",
        "insurance_expiration": "2023-12-01",
        "inspection_expiration": "2023-11-25",
        "road_tax_expiration": "2023-12-10"
    },
    {
        "owner": "jane.smith@example.com",
        "vehicle_model": "Ford Mustang",
        "insurance_expiration": "2023-11-29",
        "inspection_expiration": "2023-12-05",
        "road_tax_expiration": "2024-01-15"
    }
]

def send_email(recipient, subject, message):
    """
    Sends an email using SMTP.

    Args:
        recipient (str): Email address of the recipient.
        subject (str): Subject of the email.
        message (str): Body of the email.

    Raises:
        Exception: If there's an error sending the email.
    """
    try:
        # Create the email
        email_msg = MIMEText(message)
        email_msg["From"] = EMAIL_USERNAME
        email_msg["To"] = recipient
        email_msg["Subject"] = subject

        # Set up the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(email_msg)
            print(f"Alert email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

def check_expirations(vehicle_data):
    """
    Checks for upcoming expirations and sends alerts.

    Args:
        vehicle_data (list): List of vehicle dictionaries containing expiration data.
    """
    today = datetime.now()

    for vehicle in vehicle_data:
        alerts = []
        owner_email = vehicle["owner"]
        vehicle_model = vehicle["vehicle_model"]

        # Check insurance expiration
        insurance_date = datetime.strptime(vehicle["insurance_expiration"], "%Y-%m-%d")
        if insurance_date - today <= timedelta(days=ALERT_DAYS_BEFORE):
            alerts.append(f"Insurance expiration date: {insurance_date.strftime('%Y-%m-%d')}")

        # Check inspection expiration
        inspection_date = datetime.strptime(vehicle["inspection_expiration"], "%Y-%m-%d")
        if inspection_date - today <= timedelta(days=ALERT_DAYS_BEFORE):
            alerts.append(f"Inspection expiration date: {inspection_date.strftime('%Y-%m-%d')}")

        # Check road tax expiration
        road_tax_date = datetime.strptime(vehicle["road_tax_expiration"], "%Y-%m-%d")
        if road_tax_date - today <= timedelta(days=ALERT_DAYS_BEFORE):
            alerts.append(f"Road tax expiration date: {road_tax_date.strftime('%Y-%m-%d')}")

        # Send email alert if there are any expirations
        if alerts:
            alert_message = f"Dear {owner_email},\n\nYour vehicle '{vehicle_model}' has upcoming expirations:\n\n" + "\n".join(alerts) + "\n\nPlease ensure timely renewals to avoid any issues.\n\nBest regards,\nAtlas Navi"
            send_email(owner_email, f"Maintenance Alert for {vehicle_model}", alert_message)

if __name__ == "__main__":
    # Entry point to the script
    print("Checking vehicle data for upcoming expirations...")
    check_expirations(vehicle_data)
    print("Maintenance alert script completed.")
```
