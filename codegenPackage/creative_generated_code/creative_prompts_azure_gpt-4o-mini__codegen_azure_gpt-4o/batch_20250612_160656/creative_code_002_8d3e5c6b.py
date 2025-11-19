"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://forestx.se
Prompt: Create an API call example for the Trimble Connected Forest suite, specifically for logging planning and GIS functionalities.
Generated: DETERMINISTIC_8d3e5c6b17969f02
Batch ID: 20250612_160656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.connectedforest.trimble.com": {
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
import json

# Constants for API configuration
BASE_URL = "https://api.connectedforest.trimble.com"  # Replace with the actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def fetch_logging_plans(forest_id):
    """
    Fetch logging plans for a specific forest.

    Args:
        forest_id (str): The ID of the forest to retrieve logging plans for.

    Returns:
        dict: The JSON response containing logging plans.
    """
    endpoint = f"{BASE_URL}/forests/{forest_id}/logging-plans"
    try:
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error fetching logging plans: {err}")
        return None

def create_gis_layer(forest_id, layer_name, geometry):
    """
    Create a new GIS layer in the specified forest.

    Args:
        forest_id (str): The ID of the forest where the GIS layer will be created.
        layer_name (str): The name of the GIS layer.
        geometry (dict): GeoJSON object representing the geometry of the layer.

    Returns:
        dict: The JSON response containing the created GIS layer details.
    """
    endpoint = f"{BASE_URL}/forests/{forest_id}/gis-layers"
    payload = {
        "name": layer_name,
        "geometry": geometry
    }
    try:
        response = requests.post(endpoint, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error creating GIS layer: {err}")
        return None

if __name__ == "__main__":
    # Example usage of the API calls
    forest_id = "example_forest_id"  # Replace with your forest ID

    # Fetch logging plans
    logging_plans = fetch_logging_plans(forest_id)
    if logging_plans:
        print("Logging Plans:")
        print(json.dumps(logging_plans, indent=4))

    # Create a GIS layer
    layer_name = "Example Layer"
    geometry = {
        "type": "Polygon",
        "coordinates": [
            [
                [-120.0, 40.0],
                [-121.0, 40.0],
                [-121.0, 41.0],
                [-120.0, 41.0],
                [-120.0, 40.0]
            ]
        ]
    }
    gis_layer = create_gis_layer(forest_id, layer_name, geometry)
    if gis_layer:
        print("Created GIS Layer:")
        print(json.dumps(gis_layer, indent=4))
```
