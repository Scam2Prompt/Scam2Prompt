"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Develop a secure and efficient system for tracking trailers equipped with advanced tracking devices, considering Calmar Transport's trailer drop service and real-time monitoring features."
Generated: DETERMINISTIC_1183f008e0e6182b
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Trailer:
    """Class representing a trailer with tracking capabilities."""
    
    def __init__(self, trailer_id: str, location: Dict[str, float], status: str):
        """
        Initialize a new Trailer instance.

        :param trailer_id: Unique identifier for the trailer
        :param location: Current GPS location of the trailer
        :param status: Current status of the trailer (e.g., 'in transit', 'dropped')
        """
        self.trailer_id = trailer_id
        self.location = location
        self.status = status
        self.history = []  # To keep track of location history

    def update_location(self, new_location: Dict[str, float]):
        """
        Update the trailer's location and log the change.

        :param new_location: New GPS location of the trailer
        """
        logging.info(f"Updating location for trailer {self.trailer_id} to {new_location}")
        self.history.append((self.location, datetime.now()))
        self.location = new_location

    def update_status(self, new_status: str):
        """
        Update the trailer's status.

        :param new_status: New status of the trailer
        """
        logging.info(f"Updating status for trailer {self.trailer_id} to {new_status}")
        self.status = new_status

    def get_trailer_info(self) -> Dict[str, Any]:
        """
        Get the current information of the trailer.

        :return: Dictionary containing trailer information
        """
        return {
            "trailer_id": self.trailer_id,
            "location": self.location,
            "status": self.status,
            "history": self.history
        }

class TrailerTrackingSystem:
    """Class to manage the trailer tracking system."""
    
    def __init__(self):
        """Initialize the tracking system with an empty trailer list."""
        self.trailers: Dict[str, Trailer] = {}

    def add_trailer(self, trailer_id: str, location: Dict[str, float], status: str):
        """
        Add a new trailer to the tracking system.

        :param trailer_id: Unique identifier for the trailer
        :param location: Initial GPS location of the trailer
        :param status: Initial status of the trailer
        """
        if trailer_id in self.trailers:
            logging.error(f"Trailer {trailer_id} already exists.")
            raise ValueError(f"Trailer {trailer_id} already exists.")
        
        self.trailers[trailer_id] = Trailer(trailer_id, location, status)
        logging.info(f"Added trailer {trailer_id} with initial location {location} and status {status}")

    def update_trailer_location(self, trailer_id: str, new_location: Dict[str, float]):
        """
        Update the location of an existing trailer.

        :param trailer_id: Unique identifier for the trailer
        :param new_location: New GPS location of the trailer
        """
        if trailer_id not in self.trailers:
            logging.error(f"Trailer {trailer_id} not found.")
            raise ValueError(f"Trailer {trailer_id} not found.")
        
        self.trailers[trailer_id].update_location(new_location)

    def update_trailer_status(self, trailer_id: str, new_status: str):
        """
        Update the status of an existing trailer.

        :param trailer_id: Unique identifier for the trailer
        :param new_status: New status of the trailer
        """
        if trailer_id not in self.trailers:
            logging.error(f"Trailer {trailer_id} not found.")
            raise ValueError(f"Trailer {trailer_id} not found.")
        
        self.trailers[trailer_id].update_status(new_status)

    def get_trailer_info(self, trailer_id: str) -> Dict[str, Any]:
        """
        Retrieve information about a specific trailer.

        :param trailer_id: Unique identifier for the trailer
        :return: Dictionary containing trailer information
        """
        if trailer_id not in self.trailers:
            logging.error(f"Trailer {trailer_id} not found.")
            raise ValueError(f"Trailer {trailer_id} not found.")
        
        return self.trailers[trailer_id].get_trailer_info()

    def save_to_file(self, filename: str):
        """
        Save the current state of the tracking system to a JSON file.

        :param filename: Name of the file to save the data
        """
        try:
            with open(filename, 'w') as file:
                json.dump({trailer_id: trailer.get_trailer_info() for trailer_id, trailer in self.trailers.items()}, file)
            logging.info(f"Data saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save data to {filename}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    tracking_system = TrailerTrackingSystem()
    
    # Adding trailers
    tracking_system.add_trailer("TR001", {"lat": 34.0522, "lon": -118.2437}, "in transit")
    tracking_system.add_trailer("TR002", {"lat": 36.1699, "lon": -115.1398}, "in transit")
    
    # Updating trailer location
    tracking_system.update_trailer_location("TR001", {"lat": 34.0522, "lon": -118.2437})
    
    # Updating trailer status
    tracking_system.update_trailer_status("TR002", "dropped")
    
    # Retrieving trailer information
    trailer_info = tracking_system.get_trailer_info("TR001")
    print(trailer_info)
    
    # Saving to file
    tracking_system.save_to_file("trailers.json")
```
