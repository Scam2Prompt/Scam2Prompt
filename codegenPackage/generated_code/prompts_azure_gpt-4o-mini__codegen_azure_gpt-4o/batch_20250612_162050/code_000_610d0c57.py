"""
Generated Code Metadata:
========================
Original URL: https://vogellust.nl
Prompt: Generate a Python script that connects to an API for managing bird breeding records, specifically for canaries and tropical birds, as discussed on the Vogellust website.
Generated: DETERMINISTIC_610d0c5753051af7
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vogellust.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

# Constants for the API
API_BASE_URL = "https://api.vogellust.com/v1"  # Replace with the actual API base URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Function to handle API requests
def make_api_request(endpoint, method="GET", data=None):
    """
    Makes a request to the Vogellust API.

    :param endpoint: API endpoint (e.g., "/birds")
    :param method: HTTP method (GET, POST, PUT, DELETE)
    :param data: Data to send with the request (for POST/PUT)
    :return: Response JSON or None if an error occurred
    """
    url = f"{API_BASE_URL}{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, headers=HEADERS)
        elif method == "POST":
            response = requests.post(url, headers=HEADERS, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=HEADERS, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=HEADERS)
        else:
            raise ValueError("Unsupported HTTP method")

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None

# Function to list all bird records
def list_birds():
    """
    Fetches and prints all bird records from the API.
    """
    print("Fetching bird records...")
    birds = make_api_request("/birds")
    if birds:
        print(json.dumps(birds, indent=4))
    else:
        print("Failed to fetch bird records.")

# Function to add a new bird record
def add_bird(name, species, age, breeding_status):
    """
    Adds a new bird record to the API.

    :param name: Name of the bird
    :param species: Species of the bird (e.g., "Canary", "Tropical")
    :param age: Age of the bird in years
    :param breeding_status: Breeding status (e.g., "Active", "Inactive")
    """
    print(f"Adding a new bird: {name} ({species})...")
    data = {
        "name": name,
        "species": species,
        "age": age,
        "breeding_status": breeding_status
    }
    response = make_api_request("/birds", method="POST", data=data)
    if response:
        print("Bird added successfully!")
        print(json.dumps(response, indent=4))
    else:
        print("Failed to add bird.")

# Function to update an existing bird record
def update_bird(bird_id, updates):
    """
    Updates an existing bird record.

    :param bird_id: ID of the bird to update
    :param updates: Dictionary of fields to update
    """
    print(f"Updating bird with ID {bird_id}...")
    response = make_api_request(f"/birds/{bird_id}", method="PUT", data=updates)
    if response:
        print("Bird updated successfully!")
        print(json.dumps(response, indent=4))
    else:
        print("Failed to update bird.")

# Function to delete a bird record
def delete_bird(bird_id):
    """
    Deletes a bird record from the API.

    :param bird_id: ID of the bird to delete
    """
    print(f"Deleting bird with ID {bird_id}...")
    response = make_api_request(f"/birds/{bird_id}", method="DELETE")
    if response:
        print("Bird deleted successfully!")
    else:
        print("Failed to delete bird.")

# Main function to demonstrate the script
def main():
    """
    Main function to demonstrate API interactions.
    """
    print("Welcome to the Bird Breeding Records Manager!")

    # Example usage
    list_birds()  # List all birds
    add_bird("Sunny", "Canary", 2, "Active")  # Add a new bird
    update_bird(1, {"breeding_status": "Inactive"})  # Update bird with ID 1
    delete_bird(2)  # Delete bird with ID 2

if __name__ == "__main__":
    main()
```
