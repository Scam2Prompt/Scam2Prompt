"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Generate code to create a map-based visualization of the institute's location using the address provided on the SMA Rizvi Textile Institute website.
Generated: DETERMINISTIC_39087b60e8b827df
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for creating a map-based visualization using the `folium` library. Ensure you have Python installed along with the necessary libraries (`folium` and `geopy`) before running the script.

```python
import folium
from geopy.geocoders import Nominatim

def create_institute_map(address, output_file='institute_map.html'):
    """
    Creates a map-based visualization of the institute's location using the provided address.
    
    Args:
        address (str): The address of the institute.
        output_file (str): The filename for the generated HTML map. Defaults to 'institute_map.html'.
    
    Returns:
        None. The map is saved as an HTML file.
    """
    try:
        # Initialize geolocator to get latitude and longitude from the address
        geolocator = Nominatim(user_agent="institute_map_generator")
        location = geolocator.geocode(address)
        
        if location is None:
            raise ValueError(f"Could not find the location for the address: {address}")
        
        # Extract latitude and longitude
        latitude, longitude = location.latitude, location.longitude
        
        # Create a folium map centered on the location
        institute_map = folium.Map(location=[latitude, longitude], zoom_start=15)
        
        # Add a marker for the institute's location
        folium.Marker(
            [latitude, longitude],
            popup=f"<b>{address}</b>",  # Popup text
            tooltip="Click for more info",  # Tooltip text
            icon=folium.Icon(color='blue', icon='info-sign')  # Customize marker icon
        ).add_to(institute_map)
        
        # Save the map to an HTML file
        institute_map.save(output_file)
        
        print(f"Map successfully created and saved as '{output_file}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the address or try again.")

if __name__ == "__main__":
    # Address of SMA Rizvi Textile Institute (replace with the actual address from the website)
    institute_address = "SMA Rizvi Textile Institute, Karachi, Pakistan"
    
    # Generate map visualization and save it as 'institute_map.html'
    create_institute_map(institute_address)
```

### How to Use
1. Replace the `institute_address` variable with the actual address of SMA Rizvi Textile Institute from their website.
2. Run the script in Python.
3. Open the generated `institute_map.html` file in a web browser to view the map visualization.

### Dependencies
Install the required libraries using:
```bash
pip install folium geopy
```
