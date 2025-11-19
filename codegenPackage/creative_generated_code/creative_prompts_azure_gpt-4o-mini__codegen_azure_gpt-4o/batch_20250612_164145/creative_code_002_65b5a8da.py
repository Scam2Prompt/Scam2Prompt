"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.flyvirtualfrontier.net
Prompt: What are the key features to consider when developing a virtual airline platform that supports multiple flight simulator versions like Microsoft Flight Simulator and XPlane?
Generated: DETERMINISTIC_65b5a8da0dd2af26
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of a foundational Python implementation for a virtual airline platform. The code focuses on modularity, scalability, and clean practices while addressing the user request:

```python
import json
import os
from typing import List, Dict

# Define supported simulator versions
SUPPORTED_SIMULATORS = ["Microsoft Flight Simulator", "XPlane"]

class SimulatorNotSupportedError(Exception):
    """Custom exception for unsupported flight simulators."""
    pass

class VirtualAirlinePlatform:
    """
    A class representing the virtual airline platform.
    Supports multiple flight simulator versions.
    """

    def __init__(self):
        """
        Initialize the platform with an empty list of pilots and flights.
        """
        self.pilots = []
        self.flights = []

    def add_pilot(self, name: str, simulator: str) -> None:
        """
        Add a new pilot to the platform.
        
        :param name: Name of the pilot.
        :param simulator: Flight simulator the pilot uses.
        :raises SimulatorNotSupportedError: If the simulator is not supported.
        """
        if simulator not in SUPPORTED_SIMULATORS:
            raise SimulatorNotSupportedError(f"Simulator '{simulator}' is not supported.")
        
        pilot = {
            "name": name,
            "simulator": simulator
        }
        self.pilots.append(pilot)
        print(f"Pilot '{name}' added successfully using '{simulator}'.")

    def add_flight(self, pilot_name: str, flight_data: Dict[str, str]) -> None:
        """
        Add a flight record to the platform.
        
        :param pilot_name: Name of the pilot associated with the flight.
        :param flight_data: Dictionary containing flight details (e.g., origin, destination).
        :raises ValueError: If the pilot does not exist.
        """
        # Validate pilot
        pilot = next((p for p in self.pilots if p["name"] == pilot_name), None)
        if not pilot:
            raise ValueError(f"Pilot '{pilot_name}' not found.")
        
        # Add flight data
        flight_record = {
            "pilot_name": pilot_name,
            **flight_data
        }
        self.flights.append(flight_record)
        print(f"Flight added successfully for pilot '{pilot_name}'.")

    def list_pilots(self) -> List[Dict[str, str]]:
        """
        List all pilots registered on the platform.
        
        :return: List of dictionaries containing pilot information.
        """
        return self.pilots

    def list_flights(self) -> List[Dict[str, str]]:
        """
        List all flights recorded on the platform.
        
        :return: List of dictionaries containing flight information.
        """
        return self.flights

    def save_to_file(self, file_path: str) -> None:
        """
        Save platform data (pilots and flights) to a file.
        
        :param file_path: Path to the output file.
        :raises IOError: If the file cannot be written.
        """
        try:
            data = {
                "pilots": self.pilots,
                "flights": self.flights
            }
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Platform data saved successfully to '{file_path}'.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Load platform data (pilots and flights) from a file.
        
        :param file_path: Path to the input file.
        :raises IOError: If the file cannot be read.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")
        
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.pilots = data.get("pilots", [])
                self.flights = data.get("flights", [])
            print(f"Platform data loaded successfully from '{file_path}'.")
        except IOError as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    platform = VirtualAirlinePlatform()

    # Add pilots
    try:
        platform.add_pilot("John Doe", "Microsoft Flight Simulator")
        platform.add_pilot("Jane Smith", "XPlane")
    except SimulatorNotSupportedError as e:
        print(e)

    # Add flights
    try:
        platform.add_flight("John Doe", {"origin": "JFK", "destination": "LAX"})
        platform.add_flight("Jane Smith", {"origin": "SEA", "destination": "SFO"})
    except ValueError as e:
        print(e)

    # List pilots and flights
    print("Registered Pilots:")
    print(platform.list_pilots())

    print("Recorded Flights:")
    print(platform.list_flights())

    # Save and load data
    platform.save_to_file("platform_data.json")
    platform.load_from_file("platform_data.json")
```

This example provides a basic framework for pilot and flight management, handles simulator compatibility, and includes file persistence features. It can be extended further for additional features, such as real-time flight tracking.
