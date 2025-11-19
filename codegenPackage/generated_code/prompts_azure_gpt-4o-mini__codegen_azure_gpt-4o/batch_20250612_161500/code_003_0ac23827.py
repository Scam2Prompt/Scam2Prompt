"""
Generated Code Metadata:
========================
Original URL: https://phi-f1z.pages.dev
Prompt: Generate an example of how to visualize onchain activities in Phi Land using different content formats supported by Phi Protocol.
Generated: DETERMINISTIC_0ac238276d6f0492
Batch ID: 20250612_161500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.phi.land/v1": {
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
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PHI_API_BASE_URL = "https://api.phi.land/v1"  # Example API endpoint for Phi Protocol
ADDRESS = "0xYourWalletAddressHere"  # Replace with the wallet address you want to query
SUPPORTED_FORMATS = ["image", "text", "video"]  # Example content formats supported by Phi Protocol

def fetch_onchain_activities(address):
    """
    Fetch onchain activities for a given wallet address from Phi Protocol.
    :param address: Wallet address to query
    :return: List of onchain activities
    """
    try:
        response = requests.get(f"{PHI_API_BASE_URL}/activities/{address}")
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching onchain activities: {e}")
        return []

def visualize_activities(activities):
    """
    Visualize onchain activities using different content formats.
    :param activities: List of onchain activities
    """
    # Filter activities by supported formats
    filtered_activities = [activity for activity in activities if activity['format'] in SUPPORTED_FORMATS]

    # Prepare data for visualization
    formats_count = {fmt: 0 for fmt in SUPPORTED_FORMATS}
    timestamps = []

    for activity in filtered_activities:
        formats_count[activity['format']] += 1
        timestamps.append(datetime.fromisoformat(activity['timestamp']))

    # Plot the distribution of content formats
    plt.figure(figsize=(10, 5))
    plt.bar(formats_count.keys(), formats_count.values(), color='skyblue')
    plt.title("Distribution of Onchain Activities by Content Format")
    plt.xlabel("Content Format")
    plt.ylabel("Count")
    plt.show()

    # Plot activity timeline
    plt.figure(figsize=(10, 5))
    plt.hist(timestamps, bins=20, color='lightgreen', edgecolor='black')
    plt.title("Onchain Activity Timeline")
    plt.xlabel("Time")
    plt.ylabel("Number of Activities")
    plt.show()

def main():
    """
    Main function to fetch and visualize onchain activities.
    """
    print("Fetching onchain activities...")
    activities = fetch_onchain_activities(ADDRESS)

    if not activities:
        print("No activities found or an error occurred.")
        return

    print(f"Fetched {len(activities)} activities. Visualizing...")
    visualize_activities(activities)

if __name__ == "__main__":
    main()
```
