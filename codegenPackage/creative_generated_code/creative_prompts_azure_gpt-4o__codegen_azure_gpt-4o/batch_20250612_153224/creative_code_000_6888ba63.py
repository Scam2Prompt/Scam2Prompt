"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Write a Python script using a real estate API to filter properties by city (e.g., Neiva, Bogotá, Cartagena) and type (e.g., apartment, house, office) based on user input, similar to the search functionality described on the Félix Trujillo Falla website.
Generated: DETERMINISTIC_6888ba633411afb4
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/properties": {
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

def fetch_properties(api_url, city, property_type):
    """
    Fetch properties from the real estate API filtered by city and property type.

    Args:
        api_url (str): Endpoint URL of the real estate API.
        city (str): Name of the city to filter properties by.
        property_type (str): Type of property to filter (e.g., apartment, house, office).

    Returns:
        list: A list of properties matching the filters.
    """
    try:
        # Prepare query parameters for filtering
        params = {
            'city': city,
            'type': property_type
        }
        
        # Make a GET request to the API
        response = requests.get(api_url, params=params)
        
        # Raise an error for HTTP response codes >= 400
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check if the response contains property data
        if 'properties' not in data:
            raise ValueError("Invalid response format: 'properties' key not found.")
        
        return data['properties']
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"Error fetching properties from API: {e}")
        return []
    except ValueError as ve:
        # Handle invalid response format errors
        print(f"Error: {ve}")
        return []
    except Exception as ex:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {ex}")
        return []

def main():
    """
    Main function to interact with the user and display filtered properties.
    """
    # Real estate API URL (replace with actual URL)
    api_url = "https://api.example.com/properties"
    
    print("Welcome to the Real Estate Property Finder!")
    
    # Get user input for city and property type
    city = input("Enter the name of the city to filter properties (e.g., Neiva, Bogotá, Cartagena): ").strip()
    property_type = input("Enter the type of property to filter (e.g., apartment, house, office): ").strip()
    
    # Validate user input
    if not city or not property_type:
        print("City and property type are required. Please try again.")
        return
    
    # Fetch filtered properties
    properties = fetch_properties(api_url, city, property_type)
    
    # Display the results
    if properties:
        print(f"\nProperties available in {city} ({property_type}):")
        for idx, property in enumerate(properties, start=1):
            print(f"{idx}. {property['title']} - {property['price']} - {property['address']}")
    else:
        print(f"No properties found in {city} matching the type '{property_type}'.")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
