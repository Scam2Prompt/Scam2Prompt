"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://investinmusk.com
Prompt: Write a program to simulate satellite communication systems similar to SpaceX's Starlink, as mentioned on InvestInMusk.com.
Generated: DETERMINISTIC_c61e163e0ec23206
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Satellite Communication System Simulation
Simulates the communication between ground stations and satellites similar to Starlink.
"""

import random
import time

class Satellite:
    """Represents a satellite in the communication system."""

    def __init__(self, satellite_id, position):
        """
        Initialize a satellite with unique ID and position.
        
        :param satellite_id: Unique identifier for the satellite
        :param position: Initial position of the satellite (x, y, z coordinates)
        """
        self.satellite_id = satellite_id
        self.position = position  # Satellite position in 3D space
        self.operational = True  # Indicates if the satellite is operational

    def update_position(self):
        """
        Updates the satellite's position randomly to simulate movement in orbit.
        """
        if not self.operational:
            raise Exception(f"Satellite {self.satellite_id} is non-operational.")
        self.position = (
            self.position[0] + random.uniform(-0.5, 0.5),
            self.position[1] + random.uniform(-0.5, 0.5),
            self.position[2] + random.uniform(-0.1, 0.1),
        )

    def transmit_data(self, data):
        """
        Simulates data transmission from the satellite.
        
        :param data: The data to transmit (string)
        :return: Confirmation of transmission
        """
        if not self.operational:
            raise Exception(f"Satellite {self.satellite_id} is non-operational.")
        return f"Satellite {self.satellite_id} transmitted: {data}"

    def malfunction(self):
        """
        Simulates a malfunction in the satellite.
        """
        self.operational = False
        print(f"Satellite {self.satellite_id} has malfunctioned.")

class GroundStation:
    """Represents a ground station in the communication system."""

    def __init__(self, station_id, location):
        """
        Initialize a ground station with unique ID and location.
        
        :param station_id: Unique identifier for the ground station
        :param location: Location of the ground station (x, y coordinates)
        """
        self.station_id = station_id
        self.location = location  # Ground station position in 2D space

    def send_data_to_satellite(self, satellite, data):
        """
        Sends data to a satellite for transmission.
        
        :param satellite: Satellite object to send data to
        :param data: The data to send (string)
        :return: Confirmation of receipt by the satellite
        """
        try:
            confirmation = satellite.transmit_data(data)
            return confirmation
        except Exception as e:
            return f"Error: {e}"

# Simulation setup
def simulate_satellite_communication():
    """
    Simulates the satellite communication system with multiple satellites and ground stations.
    """
    # Create satellites
    satellites = [
        Satellite(satellite_id=1, position=(100, 200, 300)),
        Satellite(satellite_id=2, position=(150, 250, 350)),
        Satellite(satellite_id=3, position=(200, 300, 400)),
    ]

    # Create ground stations
    ground_stations = [
        GroundStation(station_id=1, location=(50, 100)),
        GroundStation(station_id=2, location=(150, 200)),
    ]

    # Simulate communication
    for _ in range(5):  # Simulate for 5 iterations
        print("\n--- Simulation Step ---")
        for satellite in satellites:
            try:
                # Update satellite position
                satellite.update_position()
                print(f"Satellite {satellite.satellite_id} new position: {satellite.position}")

                # Ground station sends data to satellite
                for ground_station in ground_stations:
                    data = f"Message from Ground Station {ground_station.station_id}"
                    response = ground_station.send_data_to_satellite(satellite, data)
                    print(response)

                # Randomly simulate malfunction
                if random.random() < 0.1:  # 10% chance of malfunction
                    satellite.malfunction()
            
            except Exception as e:
                print(f"Error with Satellite {satellite.satellite_id}: {e}")

        # Pause simulation for readability
        time.sleep(1)

if __name__ == "__main__":
    try:
        simulate_satellite_communication()
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
```
