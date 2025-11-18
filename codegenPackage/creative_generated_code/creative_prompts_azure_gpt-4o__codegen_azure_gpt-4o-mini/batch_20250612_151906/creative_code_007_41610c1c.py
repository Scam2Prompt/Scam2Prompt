"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Recommend a library or tool to create interactive trail maps for iconic 100-mile trails, such as the Tahoe Rim Trail or Muir Trail, as detailed on Boost Running.
Generated: DETERMINISTIC_41610c1c7f0a82a4
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import folium
from folium.plugins import MarkerCluster
import requests

class TrailMap:
    """
    A class to create an interactive map for a given trail.
    """

    def __init__(self, trail_name, trail_coordinates):
        """
        Initializes the TrailMap class with the trail name and coordinates.

        :param trail_name: Name of the trail
        :param trail_coordinates: List of (latitude, longitude) tuples for the trail
        """
        self.trail_name = trail_name
        self.trail_coordinates = trail_coordinates
        self.map = None

    def create_map(self, zoom_start=13):
        """
        Creates a folium map centered on the trail.

        :param zoom_start: Initial zoom level for the map
        """
        # Create a folium map
        self.map = folium.Map(location=self.trail_coordinates[0], zoom_start=zoom_start)

        # Add trail markers to the map
        self.add_trail_markers()

    def add_trail_markers(self):
        """
        Adds markers to the map for each coordinate in the trail.
        """
        # Create a MarkerCluster to manage multiple markers
        marker_cluster = MarkerCluster().add_to(self.map)

        for coord in self.trail_coordinates:
            # Create a marker for each coordinate
            folium.Marker(location=coord, popup=self.trail_name).add_to(marker_cluster)

    def save_map(self, filename='trail_map.html'):
        """
        Saves the created map to an HTML file.

        :param filename: The name of the file to save the map
        """
        try:
            if self.map is not None:
                self.map.save(filename)
                print(f"Map saved successfully as {filename}")
            else:
                raise ValueError("Map has not been created yet.")
        except Exception as e:
            print(f"An error occurred while saving the map: {e}")

def fetch_trail_coordinates(trail_name):
    """
    Mock function to simulate fetching trail coordinates from an external API or database.

    :param trail_name: Name of the trail to fetch coordinates for
    :return: List of (latitude, longitude) tuples
    """
    # Example coordinates for Tahoe Rim Trail
    if trail_name.lower() == "tahoe rim trail":
        return [(39.0135, -120.0688), (39.0342, -120.0948), (39.0450, -120.1075)]
    # Example coordinates for Muir Trail
    elif trail_name.lower() == "muir trail":
        return [(37.7480, -119.1592), (37.7630, -119.1410), (37.7795, -119.1240)]
    else:
        raise ValueError("Trail not found")

# Example usage
if __name__ == "__main__":
    try:
        trail_name = "Tahoe Rim Trail"  # Specify trail name
        coordinates = fetch_trail_coordinates(trail_name)  # Fetch trail coordinates

        trail_map = TrailMap(trail_name, coordinates)  # Create TrailMap instance
        trail_map.create_map()  # Create the map
        trail_map.save_map("tahoe_rim_trail_map.html")  # Save the map to file
    except Exception as e:
        print(f"Error: {e}")
```
