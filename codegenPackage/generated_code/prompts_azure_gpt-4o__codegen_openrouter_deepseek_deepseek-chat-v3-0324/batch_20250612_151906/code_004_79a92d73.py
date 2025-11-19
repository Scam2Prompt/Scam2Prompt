"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Suggest a Python library for mapping and visualizing running routes, such as the Albuquerque trails mentioned on Boost Running, including features like elevation and scenic views.
Generated: DETERMINISTIC_79a92d7300eaacfc
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import folium
import gpxpy
import gpxpy.gpx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from branca.colormap import LinearColormap
from geopy.distance import geodesic

class RunningRouteVisualizer:
    """
    A class to visualize running routes with elevation and scenic views using GPX data.
    """
    
    def __init__(self, gpx_file_path):
        """
        Initialize the visualizer with a GPX file.
        
        Args:
            gpx_file_path (str): Path to the GPX file containing the route data.
        """
        self.gpx_file_path = gpx_file_path
        self.gpx_data = self._parse_gpx_file()
        self.route_points = self._extract_route_points()
        
    def _parse_gpx_file(self):
        """
        Parse the GPX file and return the GPX data.
        
        Returns:
            gpxpy.gpx.GPX: Parsed GPX data.
            
        Raises:
            FileNotFoundError: If the GPX file is not found.
            gpxpy.gpx.GPXException: If the GPX file is invalid.
        """
        try:
            with open(self.gpx_file_path, 'r') as gpx_file:
                return gpxpy.parse(gpx_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"GPX file not found: {self.gpx_file_path}")
        except gpxpy.gpx.GPXException as e:
            raise gpxpy.gpx.GPXException(f"Invalid GPX file: {e}")
    
    def _extract_route_points(self):
        """
        Extract route points (latitude, longitude, elevation) from GPX data.
        
        Returns:
            list: List of tuples containing (latitude, longitude, elevation).
        """
        points = []
        for track in self.gpx_data.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append((point.latitude, point.longitude, point.elevation))
        return points
    
    def create_interactive_map(self, scenic_points=None):
        """
        Create an interactive Folium map with the running route and elevation data.
        
        Args:
            scenic_points (list, optional): List of scenic points as (lat, lon, description).
            
        Returns:
            folium.Map: Interactive map with the running route.
        """
        if not self.route_points:
            raise ValueError("No route points available to create map.")
            
        # Calculate center of the route
        lats = [p[0] for p in self.route_points]
        lons = [p[1] for p in self.route_points]
        center_lat = sum(lats) / len(lats)
        center_lon = sum(lons) / len(lons)
        
        # Create base map
        route_map = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=13,
            tiles='OpenStreetMap'
        )
        
        # Add route line
        folium.PolyLine(
            locations=[(p[0], p[1]) for p in self.route_points],
            color='blue',
            weight=5,
            opacity=0.7
        ).add_to(route_map)
        
        # Add elevation markers with color gradient
        elevations = [p[2] for p in self.route_points]
        min_elev = min(elevations)
        max_elev = max(elevations)
        colormap = LinearColormap(
            ['green', 'yellow', 'red'],
            vmin=min_elev,
            vmax=max_elev
        )
        
        for i, point in enumerate(self.route_points):
            if i % 10 == 0:  # Add marker every 10 points for performance
                folium.CircleMarker(
                    location=(point[0], point[1]),
                    radius=3,
                    color=colormap(point[2]),
                    fill=True,
                    fill_color=colormap(point[2]),
                    popup=f"Elevation: {point[2]:.1f}m"
                ).add_to(route_map)
        
        # Add scenic points if provided
        if scenic_points:
            for point in scenic_points:
                folium.Marker(
                    location=(point[0], point[1]),
                    icon=folium.Icon(color='green', icon='camera', prefix='fa'),
                    popup=point[2]
                ).add_to(route_map)
        
        # Add elevation color scale
        colormap.caption = 'Elevation (meters)'
        colormap.add_to(route_map)
        
        return route_map
    
    def plot_elevation_profile(self):
        """
        Plot the elevation profile of the running route using Matplotlib.
        
        Returns:
            matplotlib.figure.Figure: Figure object containing the elevation plot.
        """
        if not self.route_points:
            raise ValueError("No route points available to plot elevation.")
            
        elevations = [p[2] for p in self.route_points]
        distances = self._calculate_cumulative_distances()
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(distances, elevations, color='blue', linewidth=2)
        ax.fill_between(distances, elevations, min(elevations), color='blue', alpha=0.1)
        
        ax.set_title('Running Route Elevation Profile')
        ax.set_xlabel('Distance (km)')
        ax.set_ylabel('Elevation (m)')
        ax.grid(True)
        
        return fig
    
    def _calculate_cumulative_distances(self):
        """
        Calculate cumulative distances between route points.
        
        Returns:
            list: Cumulative distances in kilometers.
        """
        distances = [0.0]
        for i in range(1, len(self.route_points)):
            prev_point = (self.route_points[i-1][0], self.route_points[i-1][1])
            curr_point = (self.route_points[i][0], self.route_points[i][1])
            distances.append(distances[-1] + geodesic(prev_point, curr_point).kilometers)
        return distances

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with a GPX file
        visualizer = RunningRouteVisualizer('running_route.gpx')
        
        # Define some scenic points (optional)
        scenic_points = [
            (35.1107, -106.6100, "Scenic Viewpoint 1"),
            (35.1200, -106.6200, "Scenic Viewpoint 2")
        ]
        
        # Create and display interactive map
        route_map = visualizer.create_interactive_map(scenic_points=scenic_points)
        route_map.save('running_route_map.html')
        
        # Create and display elevation profile
        elevation_fig = visualizer.plot_elevation_profile()
        elevation_fig.savefig('elevation_profile.png')
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")
```
