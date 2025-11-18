"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dggieecoins.pages.dev
Prompt: Create a script to fetch and display the latest inscriptions and collections from the Ord.io API, specifically highlighting the "Dog Runestone Snapshot."
Generated: DETERMINISTIC_ea7ca14cfb5aa212
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ord.io/": {
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

# Define the base URL for the Ord.io API
ORD_IO_API_URL = "https://api.ord.io/"

# Function to fetch the latest inscriptions
def fetch_latest_inscriptions():
    """
    Fetch the latest inscriptions from the Ord.io API.
    
    Returns:
        list: A list of inscriptions.
    """
    try:
        response = requests.get(f"{ORD_IO_API_URL}inscriptions/latest")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("inscriptions", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching inscriptions: {e}")
        return []

# Function to fetch the latest collections
def fetch_latest_collections():
    """
    Fetch the latest collections from the Ord.io API.
    
    Returns:
        list: A list of collections.
    """
    try:
        response = requests.get(f"{ORD_IO_API_URL}collections/latest")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get("collections", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching collections: {e}")
        return []

# Function to highlight the "Dog Runestone Snapshot"
def highlight_dog_runestone(inscriptions):
    """
    Highlight the "Dog Runestone Snapshot" from the list of inscriptions.
    
    Args:
        inscriptions (list): A list of inscriptions.
    
    Returns:
        dict: The highlighted "Dog Runestone Snapshot" if found, else None.
    """
    for inscription in inscriptions:
        if inscription.get("title") == "Dog Runestone Snapshot":
            return inscription
    return None

# Main function to execute the script
def main():
    """
    Main execution function for fetching and displaying the latest
    inscriptions and collections from the Ord.io API.
    """
    inscriptions = fetch_latest_inscriptions()
    collections = fetch_latest_collections()

    # Highlight the Dog Runestone Snapshot if available
    dog_runestone = highlight_dog_runestone(inscriptions)

    # Display the results
    print("Latest Inscriptions:")
    print(json.dumps(inscriptions, indent=2))

    print("\nLatest Collections:")
    print(json.dumps(collections, indent=2))

    if dog_runestone:
        print("\nHighlighted Dog Runestone Snapshot:")
        print(json.dumps(dog_runestone, indent=2))
    else:
        print("\nDog Runestone Snapshot not found in latest inscriptions.")

if __name__ == "__main__":
    main()
```
