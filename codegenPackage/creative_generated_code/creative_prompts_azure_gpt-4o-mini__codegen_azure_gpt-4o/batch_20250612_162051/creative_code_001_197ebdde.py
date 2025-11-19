"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Write a Python function that retrieves and displays information about the various horse riding tours offered by Chile Horse Riding, including details on the Rari Discovery Ride and Moonshine Ride.
Generated: DETERMINISTIC_197ebdde3405b3f2
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/chile-horse-riding/tours": {
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

def get_horse_riding_tours():
    """
    Retrieves and displays information about horse riding tours offered by Chile Horse Riding.

    The function fetches the data from a simulated API endpoint or data source and displays details
    including the Rari Discovery Ride and Moonshine Ride.

    Returns:
        None
    """
    # Simulated API endpoint (replace with the real one if available)
    api_url = "https://api.example.com/chile-horse-riding/tours"

    try:
        # Send a GET request to the API endpoint
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the JSON response
        tours = response.json()

        # Check if tours data exists in the response
        if not tours or 'tours' not in tours:
            print("No horse riding tours found.")
            return

        # Display information about the tours
        print("Horse Riding Tours Offered by Chile Horse Riding:")
        for tour in tours['tours']:
            print(f"\nTour Name: {tour.get('name', 'Unknown')}")
            print(f"Description: {tour.get('description', 'No description available.')}")
            print(f"Duration: {tour.get('duration', 'Unknown')}")
            print(f"Price: {tour.get('price', 'Unknown')}")

    except requests.RequestException as e:
        # Handle connection errors or HTTP errors
        print(f"Error retrieving horse riding tours: {e}")

if __name__ == "__main__":
    get_horse_riding_tours()
```

Note: Replace the `api_url` with the actual URL of the API providing the horse riding tours' data when available. Simulated data source handling assumes JSON structure like:
```json
{
  "tours": [
    {
      "name": "Rari Discovery Ride",
      "description": "Explore the natural beauty of Rari on horseback.",
      "duration": "3 hours",
      "price": "$50"
    },
    {
      "name": "Moonshine Ride",
      "description": "Experience a magical night ride under the moonlight.",
      "duration": "2 hours",
      "price": "$40"
    }
  ]
}
```
