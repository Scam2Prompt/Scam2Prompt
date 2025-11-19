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
import uuid
import time
import logging
from typing import Dict, List

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Trailer:
    """
    Represents a trailer with advanced tracking capabilities.
    """
    def __init__(self, trailer_id: str, location: str):
        """
        Initialize a trailer object.

        :param trailer_id: Unique identifier for the trailer.
        :param location: Current location of the trailer.
        """
        self.trailer_id = trailer_id
        self.location = location
        self.last_updated = time.time()

    def update_location(self, new_location: str):
        """
        Update the trailer's location.

        :param new_location: The new location of the trailer.
        """
        self.location = new_location
        self.last_updated = time.time()
        logging.info(f"Trailer {self.trailer_id} location updated to {self.location}.")

    def get_status(self) -> Dict[str, str]:
        """
        Get the current status of the trailer.

        :return: A dictionary containing the trailer's ID, location, and last updated timestamp.
        """
        return {
            "trailer_id": self.trailer_id,
            "location": self.location,
            "last_updated": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.last_updated))
        }


class TrailerTrackingSystem:
    """
    A system for tracking trailers in real-time.
    """
    def __init__(self):
        """
        Initialize the tracking system.
        """
        self.trailers: Dict[str, Trailer] = {}

    def add_trailer(self, location: str) -> str:
        """
        Add a new trailer to the system.

        :param location: Initial location of the trailer.
        :return: The unique ID of the newly added trailer.
        """
        trailer_id = str(uuid.uuid4())  # Generate a unique ID for the trailer
        self.trailers[trailer_id] = Trailer(trailer_id, location)
        logging.info(f"Trailer {trailer_id} added at location {location}.")
        return trailer_id

    def update_trailer_location(self, trailer_id: str, new_location: str):
        """
        Update the location of a specific trailer.

        :param trailer_id: The unique ID of the trailer.
        :param new_location: The new location of the trailer.
        :raises KeyError: If the trailer ID does not exist in the system.
        """
        if trailer_id not in self.trailers:
            logging.error(f"Trailer {trailer_id} not found.")
            raise KeyError(f"Trailer {trailer_id} does not exist.")
        self.trailers[trailer_id].update_location(new_location)

    def get_trailer_status(self, trailer_id: str) -> Dict[str, str]:
        """
        Get the status of a specific trailer.

        :param trailer_id: The unique ID of the trailer.
        :return: A dictionary containing the trailer's status.
        :raises KeyError: If the trailer ID does not exist in the system.
        """
        if trailer_id not in self.trailers:
            logging.error(f"Trailer {trailer_id} not found.")
            raise KeyError(f"Trailer {trailer_id} does not exist.")
        return self.trailers[trailer_id].get_status()

    def get_all_trailers_status(self) -> List[Dict[str, str]]:
        """
        Get the status of all trailers in the system.

        :return: A list of dictionaries containing the status of all trailers.
        """
        return [trailer.get_status() for trailer in self.trailers.values()]


# Example usage (this would typically be in a separate file or script):
if __name__ == "__main__":
    try:
        # Initialize the tracking system
        tracking_system = TrailerTrackingSystem()

        # Add a new trailer
        trailer_id = tracking_system.add_trailer("Calmar Depot")

        # Update the trailer's location
        tracking_system.update_trailer_location(trailer_id, "Highway 401")

        # Get the trailer's status
        status = tracking_system.get_trailer_status(trailer_id)
        print("Trailer Status:", status)

        # Get the status of all trailers
        all_status = tracking_system.get_all_trailers_status()
        print("All Trailers Status:", all_status)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
