"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sassmgmt.com
Prompt: Write a Python script that integrates with an API to manage actor profiles and commercial extras for a talent agency.
Generated: DETERMINISTIC_64958f713757845c
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.talentagency.com/v1": {
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

# Constants for API integration
API_BASE_URL = "https://api.talentagency.com/v1"  # Replace with the actual API base URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def fetch_actor_profiles():
    """
    Fetch all actor profiles from the API.
    Returns:
        list: A list of actor profiles, or an empty list if the request fails.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/actors", headers=HEADERS)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Assuming the API returns a JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching actor profiles: {e}")
        return []

def add_actor_profile(actor_data):
    """
    Add a new actor profile via the API.
    Args:
        actor_data (dict): A dictionary containing actor profile details.
    Returns:
        dict: The response from the API, or a dictionary with an error message.
    """
    try:
        response = requests.post(f"{API_BASE_URL}/actors", headers=HEADERS, json=actor_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error adding actor profile: {e}")
        return {"error": str(e)}

def update_actor_profile(actor_id, updated_data):
    """
    Update an existing actor profile via the API.
    Args:
        actor_id (str): The ID of the actor profile to update.
        updated_data (dict): A dictionary containing updated profile details.
    Returns:
        dict: The response from the API, or a dictionary with an error message.
    """
    try:
        response = requests.put(f"{API_BASE_URL}/actors/{actor_id}", headers=HEADERS, json=updated_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating actor profile: {e}")
        return {"error": str(e)}

def delete_actor_profile(actor_id):
    """
    Delete an actor profile via the API.
    Args:
        actor_id (str): The ID of the actor profile to delete.
    Returns:
        dict: The response from the API, or a dictionary with an error message.
    """
    try:
        response = requests.delete(f"{API_BASE_URL}/actors/{actor_id}", headers=HEADERS)
        response.raise_for_status()
        return {"message": "Actor profile deleted successfully."}
    except requests.exceptions.RequestException as e:
        print(f"Error deleting actor profile: {e}")
        return {"error": str(e)}

def fetch_commercial_extras():
    """
    Fetch all commercial extras from the API.
    Returns:
        list: A list of commercial extras, or an empty list if the request fails.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/commercial_extras", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching commercial extras: {e}")
        return []

def add_commercial_extra(extra_data):
    """
    Add a new commercial extra via the API.
    Args:
        extra_data (dict): A dictionary containing commercial extra details.
    Returns:
        dict: The response from the API, or a dictionary with an error message.
    """
    try:
        response = requests.post(f"{API_BASE_URL}/commercial_extras", headers=HEADERS, json=extra_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error adding commercial extra: {e}")
        return {"error": str(e)}

def main():
    """
    Main function to demonstrate API integration.
    """
    # Example operations
    print("Fetching actor profiles...")
    actors = fetch_actor_profiles()
    print(json.dumps(actors, indent=2))

    print("\nAdding a new actor profile...")
    new_actor = {
        "name": "John Doe",
        "age": 35,
        "experience": "5 years",
        "skills": ["acting", "singing", "dancing"]
    }
    add_response = add_actor_profile(new_actor)
    print(json.dumps(add_response, indent=2))

    print("\nFetching commercial extras...")
    extras = fetch_commercial_extras()
    print(json.dumps(extras, indent=2))

if __name__ == "__main__":
    main()
```
