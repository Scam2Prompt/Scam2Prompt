"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.edilciottoli.com
Prompt: Write a Python script that connects to an API providing data on construction materials, specifically focusing on selecting defect-free stones and pebbles.
Generated: DETERMINISTIC_1b2e657930a3a71f
Batch ID: 20250612_163308
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.construction-materials.com/v1/materials": {
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

# Constants
API_URL = "https://api.construction-materials.com/v1/materials"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key

def fetch_materials(api_url, api_key):
    """
    Fetches materials from the API.
    
    Args:
        api_url (str): The endpoint URL of the API.
        api_key (str): The API key for authentication.
        
    Returns:
        list: A list of materials if the request succeeds.
        
    Raises:
        RuntimeError: If the API request fails or returns an error.
    """
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(api_url, headers=headers)

        # Check if the response is successful
        response.raise_for_status()
        return response.json()  # Return parsed JSON data
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch materials: {e}")

def filter_defect_free(materials):
    """
    Filters defect-free stones and pebbles from the material list.
    
    Args:
        materials (list): A list of materials with properties.
        
    Returns:
        list: A list of defect-free stones and pebbles.
    """
    defect_free_items = []
    for material in materials:
        # Check the material type and defect status
        if (
            material.get("type") in ["stone", "pebble"] 
            and material.get("defective") is False
        ):
            defect_free_items.append(material)
    return defect_free_items

def main():
    """
    Main function to fetch materials and filter defect-free stones and pebbles.
    """
    try:
        # Fetch all construction materials from the API
        materials = fetch_materials(API_URL, API_KEY)
        print(f"Fetched {len(materials)} materials from the API.")

        # Filter defect-free stones and pebbles
        defect_free_items = filter_defect_free(materials)
        print(f"Found {len(defect_free_items)} defect-free stones and pebbles.")

        # Output defect-free items
        for item in defect_free_items:
            print(f"Name: {item.get('name')}, Type: {item.get('type')}")
    except RuntimeError as e:
        # Log an error message
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
