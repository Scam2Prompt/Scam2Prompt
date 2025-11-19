"""
Generated Code Metadata:
========================
Original URL: https://www.flyvirtualfrontier.net
Prompt: How can I implement a custom ACARS system similar to WILDCARS for flight tracking in a virtual airline setting?
Generated: DETERMINISTIC_264f2736604c2b79
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import threading
import json
import time
from datetime import datetime

# Configuration for the ACARS system
SERVER_HOST = '127.0.0.1'  # Server IP address
SERVER_PORT = 5555         # Server port
BUFFER_SIZE = 1024         # Buffer size for receiving data
LOG_FILE = 'acars_log.json'  # File to store flight logs

# Flight data structure
class FlightData:
    def __init__(self, flight_number, aircraft, departure, destination, position, altitude, speed, timestamp):
        self.flight_number = flight_number
        self.aircraft = aircraft
        self.departure = departure
        self.destination = destination
        self.position = position
        self.altitude = altitude
        self.speed = speed
        self.timestamp = timestamp

    def to_dict(self):
        """Convert flight data to a dictionary for JSON serialization."""
        return {
            "flight_number": self.flight_number,
            "aircraft": self.aircraft,
            "departure": self.departure,
            "destination": self.destination,
            "position": self.position,
            "altitude": self.altitude,
            "speed": self.speed,
            "timestamp": self.timestamp
        }

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"[INFO] Connection established with {address}")
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if not data:
                break

            # Parse the received data
            try:
                flight_data = json.loads(data)
                flight = FlightData(
                    flight_number=flight_data.get("flight_number"),
                    aircraft=flight_data.get("aircraft"),
                    departure=flight_data.get("departure"),
                    destination=flight_data.get("destination"),
                    position=flight_data.get("position"),
                    altitude=flight_data.get("altitude"),
                    speed=flight_data.get("speed"),
                    timestamp=datetime.now().isoformat()
                )

                # Log the flight data to a file
                log_flight_data(flight)
                print(f"[INFO] Flight data logged: {flight.flight_number}")
            except json.JSONDecodeError:
                print("[ERROR] Failed to decode JSON data")
                client_socket.send("Invalid data format".encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] Error handling client {address}: {e}")
    finally:
        print(f"[INFO] Connection closed with {address}")
        client_socket.close()

# Function to log flight data to a file
def log_flight_data(flight):
    try:
        with open(LOG_FILE, 'a') as log_file:
            log_file.write(json.dumps(flight.to_dict()) + '\n')
    except Exception as e:
        print(f"[ERROR] Failed to log flight data: {e}")

# Function to start the ACARS server
def start_server():
    print("[INFO] Starting ACARS server...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)  # Listen for up to 5 connections
    print(f"[INFO] Server listening on {SERVER_HOST}:{SERVER_PORT}")

    try:
        while True:
            # Accept incoming client connections
            client_socket, client_address = server_socket.accept()
            # Handle the client connection in a separate thread
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("[INFO] Shutting down server...")
    except Exception as e:
        print(f"[ERROR] Server error: {e}")
    finally:
        server_socket.close()

# Entry point for the script
if __name__ == "__main__":
    start_server()
```
