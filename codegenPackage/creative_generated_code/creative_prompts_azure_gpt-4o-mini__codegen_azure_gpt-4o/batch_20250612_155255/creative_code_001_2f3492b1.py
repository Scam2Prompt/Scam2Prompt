"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styleandmakeupeffect.co.za
Prompt: Write a Python script that integrates with a beauty service API to display personal styling packages like those at Style & Makeup Effect.
Generated: DETERMINISTIC_2f3492b124d644a8
Batch ID: 20250612_155255
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.beautyservices.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.beautyservices.com/v1`": {
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

# Constants for the API
API_BASE_URL = "https://api.beautyservices.com/v1"  # Replace with the actual API base URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

def fetch_styling_packages():
    """
    Fetch personal styling packages from the Beauty Service API.
    
    Returns:
        list: A list of styling packages if successful, or None if an error occurs.
    """
    endpoint = f"{API_BASE_URL}/styling-packages"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(endpoint, headers=headers)
        
        # Check for successful response
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Failed to fetch styling packages. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    
    except requests.exceptions.RequestException as e:
        # Handle potential connection or network errors
        print(f"Error: An exception occurred while fetching styling packages: {e}")
        return None

def display_packages(packages):
    """
    Display the styling packages in a user-friendly format.
    
    Args:
        packages (list): A list of styling packages fetched from the API.
    """
    if not packages:
        print("No styling packages available.")
        return
    
    print("Available Styling Packages:\n")
    for package in packages:
        # Ensure the package has the expected fields
        name = package.get("name", "Unknown Package")
        description = package.get("description", "No description available.")
        price = package.get("price", "Price not specified.")
        
        print(f"Package Name: {name}")
        print(f"Description: {description}")
        print(f"Price: ${price}")
        print("-" * 40)

def main():
    """
    Main function to fetch and display personal styling packages.
    """
    print("Fetching styling packages...")
    packages = fetch_styling_packages()
    
    if packages:
        display_packages(packages)
    else:
        print("Unable to retrieve styling packages. Please try again later.")

if __name__ == "__main__":
    # Entry point for the script
    main()
```

### Notes:
- Replace `https://api.beautyservices.com/v1` with the actual base URL of the Beauty Service API.
- Replace `your_api_key_here` with a valid API key for authentication.
- Ensure the API endpoint `/styling-packages` exists and returns the expected data structure.
