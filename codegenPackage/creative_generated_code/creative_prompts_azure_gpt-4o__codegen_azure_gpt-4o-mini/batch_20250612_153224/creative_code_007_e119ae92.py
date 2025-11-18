"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westbengalrealestates.com
Prompt: Suggest a Python library for geocoding the locations of projects like "Realmark Amora" and "Sugam Serenity Kamalgazi" from https://westbengalrealestates.com and provide an example script to map these locations.
Generated: DETERMINISTIC_e119ae9268d4bb48
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opencagedata.com/geocode/v1/json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import folium

# Define a function to fetch geocoding information
def geocode_location(location_name):
    """
    Geocode a location using the OpenCage Geocoding API.
    
    Args:
        location_name (str): The name of the location to geocode.

    Returns:
        tuple: A tuple containing the latitude and longitude of the location.
        
    Raises:
        Exception: Raises an exception if the API request fails or returns no results.
    """
    API_KEY = 'YOUR_OPENCAGE_API_KEY'  # Replace with your OpenCage API key
    base_url = 'https://api.opencagedata.com/geocode/v1/json'
    
    params = {
        'q': location_name,
        'key': API_KEY,
        'limit': 1  # Limit to one result
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        if data['results']:
            # Extract latitude and longitude from the response
            lat = data['results'][0]['geometry']['lat']
            lng = data['results'][0]['geometry']['lng']
            return (lat, lng)
        else:
            raise Exception(f'No results found for location: {location_name}')
    
    except requests.exceptions.RequestException as e:
        raise Exception(f'Error during API request: {e}')

# Define a function to create a map with markers for the locations
def create_map(locations):
    """
    Create a map with markers for the given locations.
    
    Args:
        locations (dict): A dictionary with location names as keys and (lat, lng) tuples as values.
    """
    # Initialize a map centered around the average location
    avg_lat = sum(lat for lat, _ in locations.values()) / len(locations)
    avg_lng = sum(lng for _, lng in locations.values()) / len(locations)
    project_map = folium.Map(location=[avg_lat, avg_lng], zoom_start=12)

    # Add markers for each location
    for location_name, (lat, lng) in locations.items():
        folium.Marker(location=[lat, lng], popup=location_name).add_to(project_map)

    # Save the map to an HTML file
    project_map.save('projects_map.html')

def main():
    # List of project names to geocode
    project_names = ["Realmark Amora", "Sugam Serenity Kamalgazi"]
    
    # Dictionary to hold geocoded locations
    locations = {}
    
    for project in project_names:
        try:
            lat, lng = geocode_location(project)
            locations[project] = (lat, lng)
        except Exception as e:
            print(f'Failed to geocode {project}: {e}')

    if locations:
        create_map(locations)
        print("Map created successfully. Open 'projects_map.html' to view it.")
    else:
        print("No valid locations to map.")

if __name__ == '__main__':
    main()
```

> Note: Please remember to replace `'YOUR_OPENCAGE_API_KEY'` with a valid OpenCage API key to run the script successfully.
