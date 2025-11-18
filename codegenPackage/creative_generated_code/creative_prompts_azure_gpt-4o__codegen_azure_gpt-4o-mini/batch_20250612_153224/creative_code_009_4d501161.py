"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Develop a script to track and visualize the distribution network growth for a marketing campaign targeting agricultural businesses, using geographic data and mapping libraries like Folium or GeoPandas.
Generated: DETERMINISTIC_4d501161db8cfaff
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import geopy.exc
from geopy.geocoders import Nominatim

# Function to geocode addresses using Nominatim
def geocode_address(address):
    """
    Geocode an address using Nominatim.
    
    Parameters:
        address (str): The address to geocode.
    
    Returns:
        tuple: (latitude, longitude) if successful, else (None, None).
    """
    geolocator = Nominatim(user_agent="agriculture_campaign_tracker")
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            print(f"Could not geocode address: {address}")
            return (None, None)
    except geopy.exc.GeocoderTimedOut:
        print(f"Geocoding timed out for address: {address}")
        return (None, None)

# Function to visualize the distribution network
def create_map(locations):
    """
    Create a Folium map with clustered markers for the given locations.
    
    Parameters:
        locations (list): A list of tuples with (latitude, longitude, name).
    
    Returns:
        folium.Map: A Folium map object with markers.
    """
    # Initialize the map centered on the average location
    if not locations:
        raise ValueError("No locations provided to create the map.")

    # Calculate the average latitude and longitude for centering
    avg_lat = sum(lat for lat, _, _ in locations) / len(locations)
    avg_lon = sum(lon for _, lon, _ in locations) / len(locations)
    
    campaign_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=6)
    
    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(campaign_map)
    
    for lat, lon, name in locations:
        folium.Marker(
            location=[lat, lon],
            popup=name,
            icon=folium.Icon(color='blue')
        ).add_to(marker_cluster)
    
    return campaign_map

# Example usage with a list of addresses targeting agricultural businesses
addresses = [
    "123 Farm St, Agriculture City, Country",
    "456 Crop Ave, Farmington, Country",
    "789 Grain Blvd, Harvest Town, Country"
]

# Geocode addresses and build location list
locations = []
for address in addresses:
    lat, lon = geocode_address(address)
    if lat is not None and lon is not None:
        locations.append((lat, lon, address))

# Create and save the map
try:
    distribution_map = create_map(locations)
    distribution_map.save("distribution_network_growth.html")
    print("Map created successfully: distribution_network_growth.html")
except ValueError as ve:
    print(f"Error while creating map: {ve}")
```
