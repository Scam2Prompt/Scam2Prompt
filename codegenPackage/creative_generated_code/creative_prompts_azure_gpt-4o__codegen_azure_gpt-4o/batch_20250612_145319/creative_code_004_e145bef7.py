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
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import geopy.distance
import csv

# Configuration for the email server
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"          # Replace with your email's app password

# Example service centers and their coordinates
SERVICE_CENTERS = {
    "Bento Gonçalves": {"lat": -29.1662, "lon": -51.5165},
    "Porto Alegre": {"lat": -30.0346, "lon": -51.2177},
}

# Maximum distance (in kilometers) to notify a client
MAX_DISTANCE_KM = 20

def read_client_data(file_path):
    """
    Reads client data from a CSV file. The file should have the following headers: 
    Name,Email,Latitude,Longitude.

    :param file_path: Path to the input CSV file.
    :return: List of dictionaries containing client data.
    """
    clients = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                clients.append({
                    "name": row["Name"],
                    "email": row["Email"],
                    "latitude": float(row["Latitude"]),
                    "longitude": float(row["Longitude"]),
                })
    except Exception as e:
        print(f"Error reading client data: {e}")
    return clients

def calculate_distance(client_coords, center_coords):
    """
    Calculates the distance between two geographical points.

    :param client_coords: Tuple of (latitude, longitude) for the client.
    :param center_coords: Tuple of (latitude, longitude) for the service center.
    :return: Distance in kilometers.
    """
    return geopy.distance.distance(client_coords, center_coords).km

def find_nearby_clients(clients):
    """
    Filters clients based on their proximity to any of the service centers.

    :param clients: List of client dictionaries.
    :return: List of clients that are within the MAX_DISTANCE_KM of any service center.
    """
    nearby_clients = []
    for client in clients:
        client_coords = (client["latitude"], client["longitude"])
        for city, coords in SERVICE_CENTERS.items():
            center_coords = (coords["lat"], coords["lon"])
            distance = calculate_distance(client_coords, center_coords)
            if distance <= MAX_DISTANCE_KM:
                client["city"] = city
                client["distance"] = round(distance, 2)
                nearby_clients.append(client)
                break  # Stop checking other service centers for this client
    return nearby_clients

def send_email(client, city, distance):
    """
    Sends an email notification to the client.

    :param client: The client dictionary containing name and email.
    :param city: The city of the service center.
    :param distance: The distance of the client to the service center.
    """
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            # Secure the connection
            context = ssl.create_default_context()
            server.starttls(context=context)

            # Login to the email account
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            # Construct the email
            message = MIMEMultipart("alternative")
            message["Subject"] = "Nearby Automotive Service Center"
            message["From"] = EMAIL_ADDRESS
            message["To"] = client["email"]

            # Email content
            text = f"""\
            Hi {client['name']},

            We noticed that you are located approximately {distance} km from our service center in {city}.
            Visit us for automotive services and support.

            Best regards,
            Automotive Service Center
            """
            message.attach(MIMEText(text, "plain"))

            # Send the email
            server.sendmail(EMAIL_ADDRESS, client["email"], message.as_string())
            print(f"Email sent to {client['name']} at {client['email']}")
    except Exception as e:
        print(f"Error sending email to {client['email']}: {e}")

def main():
    """
    Main function to orchestrate the process of reading client data, 
    identifying nearby clients, and sending notifications.
    """
    # Path to the CSV file containing client data
    client_file_path = "clients.csv"  # Replace with the actual file path

    # Read client data from the file
    clients = read_client_data(client_file_path)
    if not clients:
        print("No client data available. Exiting.")
        return

    # Find clients near service centers
    nearby_clients = find_nearby_clients(clients)
    if not nearby_clients:
        print("No clients found near service centers. Exiting.")
        return

    # Send email notifications
    for client in nearby_clients:
        send_email(client, city=client["city"], distance=client["distance"])

if __name__ == "__main__":
    main()
```
