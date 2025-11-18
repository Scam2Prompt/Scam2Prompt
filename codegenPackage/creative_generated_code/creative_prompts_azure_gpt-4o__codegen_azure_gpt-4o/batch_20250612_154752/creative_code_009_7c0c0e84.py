"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gettapeads.com
Prompt: Create a program to monitor and visualize viewer statistics from Streamtape, including geographic data and adblock usage, using their API.
Generated: DETERMINISTIC_7c0c0e8430aae0aa
Batch ID: 20250612_154752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.streamtape.com": {
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

# Constants for the Streamtape API
API_BASE_URL = "https://api.streamtape.com"
API_KEY = "your_api_key"  # Replace with your API key
API_SECRET = "your_api_secret"  # Replace with your API secret

# Function to fetch viewer statistics from Streamtape API
def fetch_viewer_statistics(api_key, api_secret):
    """
    Fetch viewer statistics from the Streamtape API.

    :param api_key: API key for authentication
    :param api_secret: API secret for authentication
    :return: Dictionary containing statistics data or None in case of failure
    """
    try:
        # Construct API endpoint URL
        url = f"{API_BASE_URL}/stat/viewers?key={api_key}&secret={api_secret}"
        
        # Send GET request
        response = requests.get(url)
        
        # Check for successful response
        if response.status_code == 200:
            return response.json()['result']
        else:
            print(f"Error: Failed to fetch statistics. HTTP Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Handle network errors
        print(f"Error: Network error occurred while fetching statistics. Details: {str(e)}")
        return None

# Function to visualize viewer statistics
def visualize_statistics(data):
    """
    Visualize viewer statistics using matplotlib.

    :param data: Dictionary containing statistics data
    """
    try:
        # Extract geographic data and adblock usage
        countries = data['countries']
        adblock_count = data['adblock']

        # Prepare data for visualization
        country_names = list(countries.keys())
        country_counts = list(countries.values())

        # Create bar chart for geographic data
        plt.figure(figsize=(12, 6))
        plt.bar(country_names, country_counts, color='skyblue')
        plt.title("Viewer Statistics by Country")
        plt.xlabel("Country")
        plt.ylabel("Viewer Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Display adblock usage statistics
        print("\nAdblock Usage Statistics:")
        print(f"Adblock enabled viewers: {adblock_count['enabled']}")
        print(f"Adblock disabled viewers: {adblock_count['disabled']}")
    except KeyError as e:
        print(f"Error: Missing data key in statistics. Details: {str(e)}")
    except Exception as e:
        print(f"Error: An unexpected error occurred during visualization. Details: {str(e)}")

if __name__ == "__main__":
    # Fetch statistics from Streamtape API
    statistics_data = fetch_viewer_statistics(API_KEY, API_SECRET)

    # Check if statistics were successfully fetched
    if statistics_data:
        # Visualize the fetched statistics
        visualize_statistics(statistics_data)
    else:
        print("Failed to retrieve viewer statistics.")
```

**Note**: Replace `your_api_key` and `your_api_secret` with actual credentials from the Streamtape API. Also, ensure the required libraries (`requests` and `matplotlib`) are installed in your Python environment (`pip install requests matplotlib`).
