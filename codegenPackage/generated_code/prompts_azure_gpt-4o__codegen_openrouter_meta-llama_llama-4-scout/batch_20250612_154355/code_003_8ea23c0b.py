"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Create a Python program to display available advertising locations on a map, similar to WOW MEDIA's "ver ubicaciones" feature.
Generated: DETERMINISTIC_8ea23c0b203e2b92
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import folium
import pandas as pd
from typing import List, Dict

class AdvertisingLocation:
    def __init__(self, id: int, name: str, latitude: float, longitude: float):
        """
        Initialize an AdvertisingLocation object.

        Args:
        id (int): Unique identifier for the location.
        name (str): Name of the location.
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        """
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class AdvertisingLocationMapper:
    def __init__(self, locations: List[AdvertisingLocation]):
        """
        Initialize an AdvertisingLocationMapper object.

        Args:
        locations (List[AdvertisingLocation]): List of AdvertisingLocation objects.
        """
        self.locations = locations

    def display_locations_on_map(self, map_center: tuple = (0, 0), zoom_start: int = 10) -> folium.Map:
        """
        Display advertising locations on a map.

        Args:
        map_center (tuple, optional): Center of the map. Defaults to (0, 0).
        zoom_start (int, optional): Initial zoom level of the map. Defaults to 10.

        Returns:
        folium.Map: A Folium map with markers at the advertising locations.
        """
        # Create a Folium map
        m = folium.Map(location=map_center, zoom_start=zoom_start)

        # Add markers for each location
        for location in self.locations:
            folium.Marker(
                [location.latitude, location.longitude],
                popup=f"{location.name} (ID: {location.id})",
                icon=folium.Icon(color='blue')
            ).add_to(m)

        return m

def load_locations_from_csv(file_path: str) -> List[AdvertisingLocation]:
    """
    Load advertising locations from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    List[AdvertisingLocation]: List of AdvertisingLocation objects.

    Raises:
    FileNotFoundError: If the file does not exist.
    pd.errors.EmptyDataError: If the file is empty.
    pd.errors.ParserError: If the file is not in the correct format.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)

        # Ensure required columns exist
        required_columns = ['id', 'name', 'latitude', 'longitude']
        if not all(column in data.columns for column in required_columns):
            raise ValueError("The CSV file is missing required columns.")

        # Create AdvertisingLocation objects
        locations = [
            AdvertisingLocation(row['id'], row['name'], row['latitude'], row['longitude'])
            for index, row in data.iterrows()
        ]

        return locations

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return []
    except pd.errors.ParserError:
        print(f"Error parsing file: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    # Load locations from CSV file
    locations = load_locations_from_csv('locations.csv')

    # Create a mapper and display locations on a map
    if locations:
        mapper = AdvertisingLocationMapper(locations)
        map = mapper.display_locations_on_map((37.7749, -122.4194), 12)
        map.save('advertising_locations.html')

if __name__ == "__main__":
    main()
```
