"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Create a Python program to display available advertising locations on a map, similar to WOW MEDIA's "ver ubicaciones" feature.
Generated: DETERMINISTIC_8ea23c0b203e2b92
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_advertising_locations(file_path):
    """
    Load advertising locations from a JSON file.
    :param file_path: Path to the JSON file containing location data.
    :return: List of advertising location dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info("Advertising locations loaded successfully.")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        return []

def create_map(locations, map_file):
    """
    Create an interactive map with advertising locations.
    :param locations: List of dictionaries containing location data (latitude, longitude, description).
    :param map_file: Name of the output HTML file for the map.
    """
    try:
        # Create a map centered at the average latitude and longitude of all locations
        if not locations:
            logging.warning("No locations provided. An empty map will be created.")
            center_lat, center_lon = 0, 0  # Default center for an empty map
        else:
            center_lat = sum(loc['latitude'] for loc in locations) / len(locations)
            center_lon = sum(loc['longitude'] for loc in locations) / len(locations)

        advertising_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

        # Add markers for each advertising location
        for location in locations:
            try:
                folium.Marker(
                    location=[location['latitude'], location['longitude']],
                    popup=folium.Popup(location.get('description', 'No description available')),
                    tooltip=location.get('name', 'Advertising Location')
                ).add_to(advertising_map)
            except (KeyError, ValueError) as e:
                logging.error(f"Error adding marker for location: {location}. Details: {e}")

        # Save the map to an HTML file
        advertising_map.save(map_file)
        logging.info(f"Map saved successfully to {map_file}")
    except Exception as e:
        logging.error(f"An error occurred while creating the map: {e}")

if __name__ == "__main__":
    # File path to the JSON containing advertising locations
    input_file = "advertising_locations.json"
    # File name for the generated HTML map
    output_map_file = "advertising_map.html"

    # Load advertising locations
    advertising_locations = load_advertising_locations(input_file)

    # Create and save the map
    create_map(advertising_locations, output_map_file)

    logging.info("Program completed.")
```

### Notes:
1. To run this program, you need to have a JSON file (`advertising_locations.json`) with the structure:
   ```json
   [
       {
           "name": "Location 1",
           "latitude": 34.052235,
           "longitude": -118.243683,
           "description": "Prime advertising spot in downtown LA."
       },
       {
           "name": "Location 2",
           "latitude": 36.778259,
           "longitude": -119.417931,
           "description": "Great location near Fresno."
       }
   ]
   ```
2. Install `folium` if not already installed: `pip install folium`.
3. The program will generate an HTML file (`advertising_map.html`) that you can open in a web browser to view the map.
