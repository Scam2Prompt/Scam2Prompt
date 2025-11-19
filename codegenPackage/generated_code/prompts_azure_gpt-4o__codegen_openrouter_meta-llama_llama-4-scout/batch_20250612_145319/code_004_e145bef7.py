"""
Generated Code Metadata:
========================
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Write a Python script to automate sending email notifications to clients based on their proximity to automotive service centers in cities like Bento Gonçalves and Porto Alegre.
Generated: DETERMINISTIC_e145bef74e7901a7
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import googlemaps
from typing import Dict, List

# Define constants
SERVICE_CENTER_LOCATIONS: Dict[str, Dict[str, float]] = {
    "Bento Gonçalves": {"lat": -29.1719, "lng": -55.2336},
    "Porto Alegre": {"lat": -30.0339, "lng": -51.2304}
}

CLIENT_LOCATIONS: Dict[str, Dict[str, float]] = {
    # Example client locations
    "Client1": {"lat": -29.1718, "lng": -55.2337},
    "Client2": {"lat": -30.0340, "lng": -51.2305}
}

# Google Maps API Key
GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FROM_EMAIL = "your-email@gmail.com"
PASSWORD = "your-password"

def calculate_distance(client_location: Dict[str, float], service_center_location: Dict[str, float]) -> float:
    """
    Calculate distance between two points using Google Maps API.
    
    Args:
    client_location (Dict[str, float]): Client location.
    service_center_location (Dict[str, float]): Service center location.
    
    Returns:
    float: Distance in kilometers.
    """
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    distance_result = gmaps.distance_matrix(origins=[(client_location["lat"], client_location["lng"])], 
                                           destinations=[(service_center_location["lat"], service_center_location["lng"])], 
                                           mode="driving", units="metric")
    try:
        distance = distance_result["rows"][0]["elements"][0]["distance"]["value"] / 1000  # Convert meters to kilometers
        return distance
    except Exception as e:
        print(f"Error calculating distance: {e}")
        return float("inf")  # Return infinity on error

def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Send email using SMTP server.
    
    Args:
    to_email (str): Recipient email.
    subject (str): Email subject.
    body (str): Email body.
    """
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, to_email, text)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def main() -> None:
    # Define notification threshold in kilometers
    notification_threshold = 10.0
    
    for client, client_location in CLIENT_LOCATIONS.items():
        for city, service_center_location in SERVICE_CENTER_LOCATIONS.items():
            distance = calculate_distance(client_location, service_center_location)
            if distance <= notification_threshold:
                subject = f"Service Center Notification: {city}"
                body = f"Dear {client}, our service center in {city} is within {distance:.2f} km of your location."
                send_email(client + "@example.com", subject, body)  # Replace with actual client email

if __name__ == "__main__":
    main()
```
