"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Write a Python script to automate sending email notifications to clients based on their proximity to automotive service centers in cities like Bento Gonçalves and Porto Alegre.
Generated: DETERMINISTIC_e145bef74e7901a7
Batch ID: 20250612_145319
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
from email.mime.multipart import MIMEMultipart
import geopy.distance
import pandas as pd
import logging

# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for service center locations (latitude, longitude)
SERVICE_CENTERS = {
    "Bento Gonçalves": (-29.1670, -51.5129),
    "Porto Alegre": (-30.0346, -51.2177)
}

# Configuration for email
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'

def send_email(recipient_email, subject, body):
    """Send an email notification to a client."""
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            logging.info(f"Email sent to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

def calculate_proximity(client_location, threshold=50):
    """Determine which service centers are within the threshold distance."""
    nearby_centers = []
    for city, coords in SERVICE_CENTERS.items():
        distance = geopy.distance.distance(client_location, coords).km
        if distance <= threshold:
            nearby_centers.append(city)
    return nearby_centers

def notify_clients(client_data):
    """Notify clients based on their proximity to service centers."""
    for index, row in client_data.iterrows():
        client_name = row['name']
        client_email = row['email']
        client_location = (row['latitude'], row['longitude'])
        
        logging.info(f"Checking proximity for client: {client_name}")
        nearby_centers = calculate_proximity(client_location)

        if nearby_centers:
            subject = "Service Center Notification"
            body = f"Dear {client_name},\n\nWe wanted to inform you that there are automotive service centers near you: {', '.join(nearby_centers)}.\n\nBest regards,\nYour Service Team"
            send_email(client_email, subject, body)
        else:
            logging.info(f"No nearby service centers for client: {client_name}")

def load_client_data(file_path):
    """Load client data from a CSV file."""
    try:
        client_data = pd.read_csv(file_path)
        logging.info("Client data loaded successfully.")
        return client_data
    except Exception as e:
        logging.error(f"Failed to load client data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure

if __name__ == "__main__":
    # Load client data from a CSV file
    client_data_file = 'clients.csv'  # Path to the clients CSV file
    client_data = load_client_data(client_data_file)

    if not client_data.empty:
        # Notify clients about nearby service centers
        notify_clients(client_data)
    else:
        logging.error("No client data available for processing.")
```

**Note:** Ensure to replace `SMTP_SERVER`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` with actual credentials, and the `clients.csv` file should contain columns: `name`, `email`, `latitude`, and `longitude`.
