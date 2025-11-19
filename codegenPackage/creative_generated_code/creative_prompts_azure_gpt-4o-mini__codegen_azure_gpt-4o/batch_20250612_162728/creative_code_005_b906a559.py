"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseamft.shop
Prompt: Describe a scenario where Open Sea Pro's metocean forecast data significantly reduced operational downtime for a construction site at sea.
Generated: DETERMINISTIC_b906a559a8b76aa8
Batch ID: 20250612_162728
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.openseapro.com/metocean/forecast": {
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
"""
Scenario:
A construction company is building an offshore wind farm. Using Open Sea Pro's metocean forecast API, 
they access accurate and timely data on waves, wind, and currents. This allows them to plan operations 
during favorable weather windows, reducing downtime caused by adverse conditions and optimizing resource usage.
"""

import requests
from datetime import datetime, timedelta

# Define constants for the Open Sea Pro API
API_URL = "https://api.openseapro.com/metocean/forecast"
API_KEY = "your_api_key_here"  # Replace with your Open Sea Pro API key
LOCATION = {"latitude": 54.0, "longitude": -1.2}  # Coordinates of the construction site
FORECAST_HOURS = 48  # Number of hours to fetch forecast data

def fetch_metocean_data(api_url, api_key, location, forecast_hours):
    """
    Fetch metocean forecast data from the Open Sea Pro API.

    Parameters:
        api_url (str): The base URL for the API.
        api_key (str): The API key for authentication.
        location (dict): Dictionary containing latitude and longitude.
        forecast_hours (int): Number of hours to fetch forecast data.

    Returns:
        dict: Parsed JSON response from the API containing metocean forecast data.
    """
    try:
        # Prepare request parameters
        params = {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "hours": forecast_hours,
            "apiKey": api_key
        }

        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)

        # Parse the JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # Log any error encountered during the API request
        print(f"Error fetching metocean data: {e}")
        return None

def analyze_forecast(data):
    """
    Analyze the forecast data to determine favorable weather windows for operations.

    Parameters:
        data (dict): Metocean forecast data.

    Returns:
        list: List of time windows deemed favorable for operations.
    """
    try:
        favorable_windows = []
        if not data or "forecast" not in data:
            print("Invalid or empty forecast data.")
            return favorable_windows

        # Loop through forecast entries
        for entry in data["forecast"]:
            time = entry["time"]
            wave_height = entry["waveHeight"]  # Wave height in meters
            wind_speed = entry["windSpeed"]  # Wind speed in m/s

            # Define favorable conditions
            if wave_height < 1.5 and wind_speed < 10:  # Example thresholds
                favorable_windows.append(time)

        return favorable_windows

    except KeyError as e:
        # Log a KeyError if data structure is not as expected
        print(f"Error analyzing forecast data: Missing key {e}")
        return []

def main():
    """
    Main function to fetch and analyze metocean forecast data, and display favorable weather windows.
    """
    print("Fetching metocean forecast data...")
    forecast_data = fetch_metocean_data(API_URL, API_KEY, LOCATION, FORECAST_HOURS)

    if forecast_data:
        print("Analyzing forecast data...")
        favorable_windows = analyze_forecast(forecast_data)

        if favorable_windows:
            print("Favorable weather windows:")
            for window in favorable_windows:
                print(f"- {window}")
        else:
            print("No favorable weather windows found within the forecast period.")
    else:
        print("Failed to fetch forecast data.")

if __name__ == "__main__":
    main()
```
