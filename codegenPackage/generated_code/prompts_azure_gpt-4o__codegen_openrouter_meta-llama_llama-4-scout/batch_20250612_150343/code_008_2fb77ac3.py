"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Recommend technologies or frameworks for developing a scalable and managed GPS tracking system for consignment-based tracking, as mentioned on Starknet IT Solutions' website.
Generated: DETERMINISTIC_2fb77ac309af5f8c
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gps_tracking_system.py

import logging
from typing import Dict, List
import os
import time
from datetime import datetime
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Define a class for GPS Device
class GPSDevice:
    def __init__(self, device_id: str, location: Dict):
        """
        Initialize a GPS device.

        Args:
        - device_id (str): Unique identifier for the device.
        - location (Dict): Initial location of the device.
        """
        self.device_id = device_id
        self.location = location
        self.last_updated = datetime.now()

    def update_location(self, new_location: Dict):
        """
        Update the location of the device.

        Args:
        - new_location (Dict): New location of the device.
        """
        self.location = new_location
        self.last_updated = datetime.now()

# In-memory storage for GPS devices (replace with a database in production)
gps_devices: Dict[str, GPSDevice] = {}

# Define a function to handle device location updates
def handle_location_update(device_id: str, location: Dict):
    """
    Handle location updates for a GPS device.

    Args:
    - device_id (str): Unique identifier for the device.
    - location (Dict): New location of the device.
    """
    if device_id in gps_devices:
        gps_devices[device_id].update_location(location)
    else:
        gps_devices[device_id] = GPSDevice(device_id, location)

# Define a route for device location updates
@app.route('/update_location', methods=['POST'])
def update_location():
    try:
        data = request.json
        device_id = data['device_id']
        location = data['location']
        handle_location_update(device_id, location)
        return jsonify({'message': 'Location updated successfully'}), 200
    except Exception as e:
        logging.error(f'Error updating location: {str(e)}')
        return jsonify({'message': 'Failed to update location'}), 500

# Define a route for retrieving device locations
@app.route('/get_location', methods=['GET'])
def get_location():
    try:
        device_id = request.args.get('device_id')
        if device_id in gps_devices:
            location = gps_devices[device_id].location
            return jsonify({'location': location}), 200
        else:
            return jsonify({'message': 'Device not found'}), 404
    except Exception as e:
        logging.error(f'Error getting location: {str(e)}')
        return jsonify({'message': 'Failed to retrieve location'}), 500

# Define a function to send notifications (e.g., via email or SMS)
def send_notification(device_id: str, location: Dict):
    """
    Send notifications for a GPS device location update.

    Args:
    - device_id (str): Unique identifier for the device.
    - location (Dict): New location of the device.
    """
    # Implement notification logic here (e.g., using a library like smtplib or twilio)
    pass

# Define a function to periodically check for device location updates
def check_for_updates():
    """
    Periodically check for device location updates and send notifications.
    """
    while True:
        for device_id, device in gps_devices.items():
            # Check if the device location has changed significantly
            # Implement logic here (e.g., using geopy or a similar library)
            pass
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    # Start the Flask development server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    # Start the background task for periodic updates
    import threading
    threading.Thread(target=check_for_updates).start()
```

```sql
-- gps_tracking_schema.sql

CREATE TABLE gps_devices (
    device_id VARCHAR(255) PRIMARY KEY,
    location JSONB NOT NULL,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE device_locations (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(255) NOT NULL,
    location JSONB NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES gps_devices(device_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_device_id ON device_locations(device_id);
CREATE INDEX idx_updated_at ON device_locations(updated_at);
```

```dockerfile
# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "gps_tracking_system.py"]
```

```yml
# docker-compose.yml

version: '3'
services:
  gps-tracking:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - postgres
    environment:
      - DATABASE_HOST=postgres
      - DATABASE_USER=myuser
      - DATABASE_PASSWORD=mypassword
      - DATABASE_NAME=mydb

  postgres:
    image: postgres:13
    environment:
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypassword
      - POSTGRES_DB=mydb
    volumes:
      - pg-data:/var/lib/postgresql/data

volumes:
  pg-data:
```

```python
# requirements.txt

flask
psycopg2-binary
geopy
smtplib
twilio
```
