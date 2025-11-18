"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resolveprocess.com
Prompt: Write a Python program to calculate and visualize key KPIs for Network Operations Centers (NOCs) using Resolve.io’s Insights platform.
Generated: DETERMINISTIC_56eeaa277280371c
Batch ID: 20250612_151158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.resolve.io/insights": {
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
import datetime

# ------------------------------- Configuration -------------------------------
# Replace with your actual API key and base URL for Resolve.io Insights platform.
API_KEY = "your_api_key_here"
BASE_URL = "https://api.resolve.io/insights"

# ------------------------------- Helper Functions -------------------------------
def fetch_kpi_data(endpoint, params=None):
    """
    Fetch KPI data from Resolve.io Insights API.
    
    Args:
        endpoint (str): API endpoint for the specific KPI.
        params (dict): Optional query parameters for the API request.
    
    Returns:
        dict: Parsed JSON response from the API.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return {}

# ------------------------------- KPI Calculation -------------------------------
def calculate_kpis():
    """
    Calculate key KPIs for the Network Operations Center (NOC).
    
    Returns:
        dict: Dictionary containing calculated KPIs.
    """
    # Fetch data for key metrics
    incidents_data = fetch_kpi_data("incidents")
    response_times_data = fetch_kpi_data("response-times")
    resolution_times_data = fetch_kpi_data("resolution-times")

    # Calculate KPIs
    kpis = {}
    if "incidents" in incidents_data:
        kpis["incident_count"] = len(incidents_data["incidents"])  # Total incident count

    if "response_times" in response_times_data:
        response_times = response_times_data["response_times"]
        kpis["average_response_time"] = sum(response_times) / len(response_times) if response_times else 0

    if "resolution_times" in resolution_times_data:
        resolution_times = resolution_times_data["resolution_times"]
        kpis["average_resolution_time"] = sum(resolution_times) / len(resolution_times) if resolution_times else 0

    return kpis

# ------------------------------- Data Visualization -------------------------------
def visualize_kpis(kpis):
    """
    Visualize the calculated KPIs using matplotlib.

    Args:
        kpis (dict): Dictionary containing calculated KPIs.
    """
    kpi_names = list(kpis.keys())
    kpi_values = list(kpis.values())

    # Create a bar chart for KPIs
    plt.figure(figsize=(10, 6))
    plt.bar(kpi_names, kpi_values, color="skyblue")
    plt.title("NOC KPI Visualization", fontsize=16)
    plt.xlabel("KPI", fontsize=14)
    plt.ylabel("Value", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()  # Adjust layout to prevent label overlap
    plt.show()

# ------------------------------- Main Program -------------------------------
def main():
    """
    Main entry point for the program.
    """
    print("Fetching and calculating KPIs for Network Operations Center...")
    kpis = calculate_kpis()

    if kpis:
        print("KPIs successfully calculated:")
        for kpi, value in kpis.items():
            print(f"{kpi}: {value}")

        print("\nVisualizing KPIs...")
        visualize_kpis(kpis)
    else:
        print("Failed to calculate KPIs. Please check API connectivity and data availability.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
