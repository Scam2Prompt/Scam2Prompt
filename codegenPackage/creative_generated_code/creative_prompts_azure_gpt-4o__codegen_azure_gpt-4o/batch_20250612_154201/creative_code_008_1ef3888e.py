"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enfock.com
Prompt: Generate code to implement a centralized control system for managing multiple fuel station brands, including features for restaurant and convenience store integration, as described by Enfock.
Generated: DETERMINISTIC_1ef3888e2cf7f2bb
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FuelStationControlSystem:
    """
    A centralized control system for managing multiple fuel station brands,
    including restaurant and convenience store integration.
    """

    def __init__(self):
        """
        Initialize the control system with empty station records.
        """
        self.fuel_stations = {}

    def add_station(self, station_id, brand, has_restaurant=False, has_store=False):
        """
        Add a new fuel station to the system.

        :param station_id: Unique identifier for the fuel station.
        :param brand: Brand name of the fuel station.
        :param has_restaurant: Boolean indicating if the station has a restaurant.
        :param has_store: Boolean indicating if the station has a convenience store.
        :raises ValueError: If the station_id already exists.
        """
        if station_id in self.fuel_stations:
            logging.error(f"Station ID '{station_id}' already exists.")
            raise ValueError("Station ID already exists.")
        
        self.fuel_stations[station_id] = {
            "brand": brand,
            "has_restaurant": has_restaurant,
            "has_store": has_store
        }
        logging.info(f"Station '{station_id}' added successfully.")

    def update_station(self, station_id, brand=None, has_restaurant=None, has_store=None):
        """
        Update details of an existing fuel station.

        :param station_id: Unique identifier for the fuel station.
        :param brand: New brand name (optional).
        :param has_restaurant: New restaurant status (optional).
        :param has_store: New store status (optional).
        :raises KeyError: If the station_id does not exist.
        """
        if station_id not in self.fuel_stations:
            logging.error(f"Station ID '{station_id}' not found.")
            raise KeyError("Station ID not found.")
        
        if brand is not None:
            self.fuel_stations[station_id]["brand"] = brand
        if has_restaurant is not None:
            self.fuel_stations[station_id]["has_restaurant"] = has_restaurant
        if has_store is not None:
            self.fuel_stations[station_id]["has_store"] = has_store
        
        logging.info(f"Station '{station_id}' updated successfully.")

    def remove_station(self, station_id):
        """
        Remove a fuel station from the system.

        :param station_id: Unique identifier for the fuel station.
        :raises KeyError: If the station_id does not exist.
        """
        if station_id not in self.fuel_stations:
            logging.error(f"Station ID '{station_id}' not found.")
            raise KeyError("Station ID not found.")
        
        del self.fuel_stations[station_id]
        logging.info(f"Station '{station_id}' removed successfully.")

    def get_station_details(self, station_id):
        """
        Retrieve details of a specific fuel station.

        :param station_id: Unique identifier for the fuel station.
        :return: Dictionary containing station details.
        :raises KeyError: If the station_id does not exist.
        """
        if station_id not in self.fuel_stations:
            logging.error(f"Station ID '{station_id}' not found.")
            raise KeyError("Station ID not found.")
        
        return self.fuel_stations[station_id]

    def list_stations(self):
        """
        List all fuel stations managed by the system.

        :return: Dictionary containing all stations and their details.
        """
        return self.fuel_stations


# Example Usage (For demonstration purposes only, remove in production)
if __name__ == "__main__":
    # Instantiate the control system
    system = FuelStationControlSystem()

    try:
        # Add some fuel stations
        system.add_station("001", "BrandA", has_restaurant=True, has_store=True)
        system.add_station("002", "BrandB", has_restaurant=False, has_store=True)

        # Update a station
        system.update_station("001", brand="BrandA+", has_restaurant=False)

        # Retrieve station details
        station_details = system.get_station_details("001")
        logging.info(f"Details of station '001': {station_details}")

        # List all stations
        all_stations = system.list_stations()
        logging.info(f"All stations: {all_stations}")

        # Remove a station
        system.remove_station("002")

    except (ValueError, KeyError) as e:
        logging.error(f"Error occurred: {e}")
```
