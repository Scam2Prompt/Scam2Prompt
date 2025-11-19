"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Develop a library that facilitates the aggregation of geometric and electrical data from different manufacturers' vehicles to support the UniSwapHD battery standardization efforts.
Generated: DETERMINISTIC_d23449df558c8172
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: uniswaphd_library.py

"""
UniSwapHD Library for aggregating geometric and electrical data from various manufacturers' vehicles.
Supports battery standardization efforts by providing a unified interface for data aggregation.

Author: [Your Name]
Date: [Today's Date]
"""

import json

class VehicleDataAggregator:
    """
    A class to aggregate geometric and electrical data from different manufacturers' vehicles.
    """

    def __init__(self):
        """
        Initializes the aggregator with empty data storage.
        """
        self.vehicle_data = []

    def add_vehicle_data(self, manufacturer, model, year, geometry, electrical_specs):
        """
        Adds a vehicle's data to the aggregator.

        Parameters:
        - manufacturer (str): The name of the vehicle manufacturer.
        - model (str): The model name of the vehicle.
        - year (int): The year the vehicle was manufactured.
        - geometry (dict): A dictionary containing geometric data (e.g., dimensions, weight).
        - electrical_specs (dict): A dictionary containing electrical data (e.g., battery type, voltage, capacity).

        Returns:
        - None
        """
        try:
            # Validate input data
            if not isinstance(manufacturer, str) or not manufacturer:
                raise ValueError("Manufacturer name must be a non-empty string.")
            if not isinstance(model, str) or not model:
                raise ValueError("Model name must be a non-empty string.")
            if not isinstance(year, int) or year < 1886:  # First car was made in 1886
                raise ValueError("Year must be a valid integer greater than or equal to 1886.")
            if not isinstance(geometry, dict):
                raise ValueError("Geometry must be a dictionary.")
            if not isinstance(electrical_specs, dict):
                raise ValueError("Electrical specifications must be a dictionary.")
            
            # Append data to the collection
            self.vehicle_data.append({
                "manufacturer": manufacturer,
                "model": model,
                "year": year,
                "geometry": geometry,
                "electrical_specs": electrical_specs
            })
        except Exception as e:
            print(f"Error adding vehicle data: {e}")
            raise

    def get_all_data(self):
        """
        Retrieves all aggregated vehicle data.

        Returns:
        - list: A list of dictionaries containing all vehicle data.
        """
        return self.vehicle_data

    def export_to_json(self, file_path):
        """
        Exports the aggregated vehicle data to a JSON file.

        Parameters:
        - file_path (str): Path to the JSON file where data should be exported.

        Returns:
        - None
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.vehicle_data, json_file, indent=4)
        except Exception as e:
            print(f"Error exporting data to JSON: {e}")
            raise

    def clear_data(self):
        """
        Clears all stored vehicle data.

        Returns:
        - None
        """
        self.vehicle_data = []


# Example Usage:
if __name__ == "__main__":
    aggregator = VehicleDataAggregator()

    try:
        # Add sample vehicle data
        aggregator.add_vehicle_data(
            manufacturer="Tesla",
            model="Model S",
            year=2022,
            geometry={
                "length_mm": 4970,
                "width_mm": 1964,
                "height_mm": 1445,
                "curb_weight_kg": 2108
            },
            electrical_specs={
                "battery_type": "Li-ion",
                "voltage_v": 400,
                "capacity_kwh": 100
            }
        )

        aggregator.add_vehicle_data(
            manufacturer="Toyota",
            model="Prius",
            year=2020,
            geometry={
                "length_mm": 4540,
                "width_mm": 1760,
                "height_mm": 1470,
                "curb_weight_kg": 1390
            },
            electrical_specs={
                "battery_type": "NiMH",
                "voltage_v": 201.6,
                "capacity_kwh": 1.31
            }
        )

        # Export data to JSON
        aggregator.export_to_json("vehicle_data.json")

        # Display all aggregated data
        print("Aggregated Vehicle Data:")
        print(aggregator.get_all_data())

        # Clear the data
        aggregator.clear_data()
        print("Data cleared. Current data:", aggregator.get_all_data())

    except Exception as ex:
        print(f"An error occurred: {ex}")
```
