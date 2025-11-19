"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: Generate an example of how to visualize onchain activities in Phi Land using different content formats supported by Phi Protocol.
Generated: DETERMINISTIC_0ac238276d6f0492
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.philandprotocol.com": {
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
import matplotlib.pyplot as plt

# Constants for API endpoints and keys (adjust as needed)
PHI_API_BASE_URL = "https://api.philandprotocol.com"
ONCHAIN_ACTIVITIES_ENDPOINT = "/onchain-activities"
API_KEY = "your_api_key_here"  # Replace with a valid API key

def fetch_onchain_activities(address):
    """
    Fetches onchain activities for a given address using the Phi Protocol API.
    
    :param address: Ethereum address to fetch onchain activities for
    :return: JSON response containing onchain activities or None if an error occurs
    """
    url = f"{PHI_API_BASE_URL}{ONCHAIN_ACTIVITIES_ENDPOINT}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"address": address}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching onchain activities: {e}")
        return None

def visualize_onchain_activities(data):
    """
    Visualizes onchain activities using a bar chart.
    
    :param data: JSON data containing onchain activities
    """
    if not data or "activities" not in data:
        print("No valid data provided for visualization.")
        return

    # Extract activity types and their counts
    activities = data["activities"]
    activity_types = [activity["type"] for activity in activities]
    activity_counts = [activity["count"] for activity in activities]

    # Plot data using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(activity_types, activity_counts, color='skyblue')
    plt.title("Onchain Activities in Phi Land", fontsize=16)
    plt.xlabel("Activity Type", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to handle user input, fetch data, and visualize it.
    """
    # Prompt for an Ethereum address
    address = input("Enter the Ethereum address to fetch onchain activities: ").strip()

    if not address:
        print("Invalid address entered.")
        return
    
    # Fetch onchain activities
    print("Fetching onchain activities...")
    data = fetch_onchain_activities(address)
    
    if data:
        print("Data fetched successfully.")
        # Visualize the activities
        visualize_onchain_activities(data)
    else:
        print("Failed to fetch data. Please check the address and try again.")

if __name__ == "__main__":
    main()
```
