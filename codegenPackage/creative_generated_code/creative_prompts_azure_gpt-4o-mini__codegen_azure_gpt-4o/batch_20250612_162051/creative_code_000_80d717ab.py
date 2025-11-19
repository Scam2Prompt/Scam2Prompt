"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Write a Python script to integrate a GPS tracking system that includes anti-theft features and remote immobilization for vehicles, as described by Donture Systems Ltd.
Generated: DETERMINISTIC_80d717abb22571d2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
import random

class Vehicle:
    """
    Class representing a vehicle with GPS tracking, anti-theft, and remote immobilization features.
    """
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.is_immobilized = False
        self.current_location = (0.0, 0.0)  # Default starting GPS coordinates
        self.is_theft_detected = False

    def update_location(self):
        """
        Simulates GPS location updates.
        """
        while True:
            if not self.is_immobilized:
                # Simulate changing GPS coordinates
                self.current_location = (
                    self.current_location[0] + random.uniform(-0.001, 0.001),
                    self.current_location[1] + random.uniform(-0.001, 0.001)
                )
                print(f"Vehicle {self.vehicle_id} Location Updated: {self.current_location}")
            time.sleep(5)  # Update every 5 seconds

    def immobilize(self):
        """
        Remotely immobilize the vehicle.
        """
        self.is_immobilized = True
        print(f"Vehicle {self.vehicle_id} has been immobilized.")

    def unimmobilize(self):
        """
        Remotely unimmobilize the vehicle.
        """
        self.is_immobilized = False
        print(f"Vehicle {self.vehicle_id} has been unimmobilized.")

    def detect_theft(self):
        """
        Simulates theft detection logic.
        """
        while True:
            # Randomly determine if theft is detected (for simulation purposes)
            self.is_theft_detected = random.choice([True, False])
            if self.is_theft_detected:
                print(f"ALERT! Theft detected for Vehicle {self.vehicle_id}.")
                self.immobilize()
            time.sleep(10)  # Check for theft every 10 seconds


class GPSControlSystem:
    """
    Control system to manage multiple vehicles' GPS tracking and anti-theft features.
    """
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_id):
        """
        Adds a new vehicle to the GPS control system.
        """
        if vehicle_id in self.vehicles:
            print(f"Vehicle {vehicle_id} is already registered.")
            return
        vehicle = Vehicle(vehicle_id)
        self.vehicles[vehicle_id] = vehicle

        # Start location update and theft detection in separate threads
        threading.Thread(target=vehicle.update_location, daemon=True).start()
        threading.Thread(target=vehicle.detect_theft, daemon=True).start()

        print(f"Vehicle {vehicle_id} added to the system.")

    def immobilize_vehicle(self, vehicle_id):
        """
        Remotely immobilizes a vehicle by its ID.
        """
        vehicle = self.vehicles.get(vehicle_id)
        if not vehicle:
            print(f"Vehicle {vehicle_id} not found.")
            return
        vehicle.immobilize()

    def unimmobilize_vehicle(self, vehicle_id):
        """
        Remotely unimmobilizes a vehicle by its ID.
        """
        vehicle = self.vehicles.get(vehicle_id)
        if not vehicle:
            print(f"Vehicle {vehicle_id} not found.")
            return
        vehicle.unimmobilize()

    def get_vehicle_location(self, vehicle_id):
        """
        Retrieves the current location of a vehicle by its ID.
        """
        vehicle = self.vehicles.get(vehicle_id)
        if not vehicle:
            print(f"Vehicle {vehicle_id} not found.")
            return None
        return vehicle.current_location


if __name__ == "__main__":
    # Example usage of the GPSControlSystem
    gps_system = GPSControlSystem()

    # Add vehicles to the system
    gps_system.add_vehicle("V12345")
    gps_system.add_vehicle("V67890")

    time.sleep(15)  # Let the threads update locations and check for theft

    # Immobilize a vehicle
    gps_system.immobilize_vehicle("V12345")

    # Unimmobilize a vehicle
    gps_system.unimmobilize_vehicle("V12345")

    # Fetch vehicle location
    location = gps_system.get_vehicle_location("V67890")
    if location:
        print(f"Current location of Vehicle V67890: {location}")

    # Keep the program running to allow threads to continue
    print("Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting the system.")
```
