"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Write a Python function that retrieves and displays car listings from a JSON API, focusing on attributes like brand, model, and fuel type, as seen on Helfen Motors.
Generated: DETERMINISTIC_cc8cea4118bd3d95
Batch ID: 20250612_163835
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/car-listings": {
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

def fetch_car_listings(api_url):
    """
    Fetches and displays car listings from the given JSON API URL.

    Args:
        api_url (str): The URL of the JSON API providing car listings.

    Returns:
        None: Prints the car listings to the console.
    """
    try:
        # Make the HTTP GET request to fetch the JSON data
        response = requests.get(api_url)
        
        # Raise an exception if the response status code is not OK (200)
        response.raise_for_status()
        
        # Parse the JSON response
        car_listings = response.json()
        
        # Ensure the response contains a list of car listings
        if not isinstance(car_listings, list):
            print("Error: Unexpected data format in API response.")
            return
        
        # Display the car listings
        print("Car Listings from Helfen Motors:")
        print("-------------------------------")
        for car in car_listings:
            # Safely retrieve car attributes, defaulting to 'Unknown' if missing
            brand = car.get("brand", "Unknown")
            model = car.get("model", "Unknown")
            fuel_type = car.get("fuel_type", "Unknown")
            
            # Print car details in a readable format
            print(f"Brand: {brand}, Model: {model}, Fuel Type: {fuel_type}")
        
    except requests.exceptions.RequestException as e:
        # Handle any request errors
        print(f"Error: Failed to fetch car listings. Details: {e}")
    except ValueError:
        # Handle JSON decoding errors
        print("Error: Failed to decode JSON data from API response.")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"Error: An unexpected error occurred. Details: {e}")

# Example usage:
# Replace 'https://api.example.com/car-listings' with the actual API URL
# fetch_car_listings('https://api.example.com/car-listings')
```
