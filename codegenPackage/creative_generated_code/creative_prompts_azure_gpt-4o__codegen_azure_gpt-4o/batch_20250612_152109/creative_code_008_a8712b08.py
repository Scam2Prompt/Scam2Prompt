"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opennet.net
Prompt: Write a script to fetch and visualize ONI's regional overviews data, focusing on Internet filtering trends in the Middle East & North Africa.
Generated: DETERMINISTIC_a8712b089b1fab42
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://open-net-initiative-api-url.example.com/regions/middle-east-north-africa": {
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
import matplotlib.pyplot as plt
import json

def fetch_oni_data():
    """
    Fetch ONI data from the regional overviews API for Middle East & North Africa.
    Returns the filtered data focusing on Internet filtering trends.
    """
    try:
        # URL for ONI's regional overviews API
        url = "https://open-net-initiative-api-url.example.com/regions/middle-east-north-africa"
        
        # Make an HTTP GET request to fetch the data
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        
        # Parse JSON response
        data = response.json()
        
        # Extract Internet filtering trends from the data
        filtering_trends = []
        for country_data in data.get("countries", []):
            country_name = country_data.get("name", "Unknown Country")
            filtering_trend = country_data.get("internet_filtering_trend", "No Data")
            filtering_trends.append((country_name, filtering_trend))
        
        return filtering_trends
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
        return []

def visualize_filtering_trends(filtering_trends):
    """
    Visualize Internet filtering trends in the Middle East & North Africa.
    Args:
        filtering_trends (list): List of tuples containing country names and filtering trends.
    """
    try:
        # Unpack country names and their filtering trends
        countries = [item[0] for item in filtering_trends]
        trends = [item[1] for item in filtering_trends]
        
        # Create a bar plot
        plt.figure(figsize=(12, 6))
        plt.bar(countries, trends, color='skyblue')
        plt.title("Internet Filtering Trends in Middle East & North Africa", fontsize=16)
        plt.xlabel("Country", fontsize=14)
        plt.ylabel("Filtering Trend", fontsize=14)
        plt.xticks(rotation=45, ha="right", fontsize=12)
        plt.tight_layout()
        
        # Show the plot
        plt.show()
    
    except Exception as e:
        print(f"Error visualizing data: {e}")

def main():
    """
    Main function to fetch and visualize ONI's regional overviews data.
    """
    print("Fetching Internet filtering trends for Middle East & North Africa...")
    filtering_trends = fetch_oni_data()
    
    if filtering_trends:
        print("Data fetched successfully. Visualizing trends...")
        visualize_filtering_trends(filtering_trends)
    else:
        print("No data available to visualize.")

if __name__ == "__main__":
    main()
```
