"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rheinmetall-zulieferer.com
Prompt: Provide Python code to visualize the geographical distribution of Rheinmetall suppliers using the Folium library, based on their addresses listed on the webpage.
Generated: DETERMINISTIC_19683abaa48afd5d
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium
import pandas as pd
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Function to geocode addresses to latitude and longitude
def geocode_address(address):
    geolocator = Nominatim(user_agent="rheinmetall_supplier_locator")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return geocode_address(address)  # Retry on timeout

# Function to create a Folium map and add supplier markers
def create_supplier_map(supplier_data):
    # Create a base map
    supplier_map = folium.Map(location=[51.1657, 10.4515], zoom_start=5)  # Centered on Germany

    # Add markers for each supplier
    for index, row in supplier_data.iterrows():
        latitude, longitude = geocode_address(row['Address'])
        if latitude and longitude:
            folium.Marker(
                location=[latitude, longitude],
                popup=f"{row['Supplier Name']}: {row['Address']}",
                icon=folium.Icon(color='blue')
            ).add_to(supplier_map)
        else:
            print(f"Geocoding failed for address: {row['Address']}")

    return supplier_map

# Main function to fetch supplier data and visualize it
def main():
    # Example supplier data format
    # In practice, you would fetch this data from a webpage or an API
    supplier_data = {
        'Supplier Name': ['Supplier A', 'Supplier B', 'Supplier C'],
        'Address': ['Address A, Germany', 'Address B, Germany', 'Address C, Germany']
    }

    # Convert supplier data to DataFrame
    supplier_df = pd.DataFrame(supplier_data)

    # Create a map with supplier locations
    supplier_map = create_supplier_map(supplier_df)

    # Save map to an HTML file
    supplier_map.save('rheinmetall_suppliers_map.html')
    print("Map saved to rheinmetall_suppliers_map.html")

if __name__ == "__main__":
    main()
```
