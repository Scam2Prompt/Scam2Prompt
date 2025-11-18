"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enfock.com
Prompt: Generate code to implement a telemetry system for monitoring vehicle data, referencing the features listed on Enfock's website for fuel station management.
Generated: DETERMINISTIC_fd6cc2f07bc6dc58
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VehicleTelemetry:
    """A class to represent a telemetry system for monitoring vehicle data."""
    
    def __init__(self):
        self.vehicle_data: List[Dict[str, Any]] = []  # List to hold telemetry data for vehicles

    def add_vehicle_data(self, vehicle_id: str, fuel_level: float, speed: float, location: Dict[str, float]) -> None:
        """
        Adds vehicle telemetry data to the system.

        Args:
            vehicle_id (str): Unique identifier for the vehicle.
            fuel_level (float): Current fuel level of the vehicle.
            speed (float): Current speed of the vehicle.
            location (Dict[str, float]): Latitude and longitude of the vehicle's location.
        """
        if fuel_level < 0 or speed < 0:
            logging.error("Fuel level and speed must not be negative.")
            raise ValueError("Fuel level and speed must not be negative.")

        # Create telemetry data entry
        data_entry = {
            "vehicle_id": vehicle_id,
            "fuel_level": fuel_level,
            "speed": speed,
            "location": location
        }
        self.vehicle_data.append(data_entry)
        logging.info(f"Added telemetry data for vehicle {vehicle_id}: {data_entry}")

    def get_vehicle_data(self, vehicle_id: str) -> Dict[str, Any]:
        """
        Retrieves telemetry data for a specified vehicle.

        Args:
            vehicle_id (str): Unique identifier for the vehicle.

        Returns:
            Dict[str, Any]: A dictionary containing vehicle telemetry data.

        Raises:
            ValueError: If the vehicle ID is not found.
        """
        for data in self.vehicle_data:
            if data['vehicle_id'] == vehicle_id:
                logging.info(f"Retrieved telemetry data for vehicle {vehicle_id}.")
                return data
        
        logging.error(f"Vehicle ID {vehicle_id} not found.")
        raise ValueError(f"Vehicle ID {vehicle_id} not found.")

    def export_data_to_json(self, file_path: str) -> None:
        """
        Exports the telemetry data to a JSON file.

        Args:
            file_path (str): Path to the file where data will be exported.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.vehicle_data, json_file, indent=4)
            logging.info(f"Telemetry data exported to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    telemetry_system = VehicleTelemetry()
    
    # Add some vehicle data
    telemetry_system.add_vehicle_data("V123", fuel_level=50.5, speed=60.0, location={"latitude": 34.0522, "longitude": -118.2437})
    telemetry_system.add_vehicle_data("V456", fuel_level=75.0, speed=45.0, location={"latitude": 40.7128, "longitude": -74.0060})

    # Retrieve data for a specific vehicle
    try:
        vehicle_info = telemetry_system.get_vehicle_data("V123")
        print(vehicle_info)
    except ValueError as e:
        logging.error(e)

    # Export data to JSON
    telemetry_system.export_data_to_json("vehicle_telemetry.json")
```
