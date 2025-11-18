"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Provide code to visualize the geographic distribution of institutional-grade tenants in a property portfolio, similar to the one managed by Rosebud Holdings Property Income REIT in Malta.
Generated: DETERMINISTIC_2a93d5e61681b3e3
Batch ID: 20250612_152827
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/tenants": {
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
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import requests

# Function to fetch geographical data of tenants from a given API endpoint
def fetch_tenant_data(api_url):
    """
    Fetch tenant data from the API.
    
    Parameters:
        api_url (str): The URL of the API endpoint providing tenant data.
    
    Returns:
        DataFrame: A pandas DataFrame containing tenant information.
    
    Raises:
        Exception: If there is an issue fetching the data from the API.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return pd.DataFrame(response.json())  # Convert JSON response to DataFrame
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise

# Function to visualize the geographic distribution of tenants
def visualize_tenant_distribution(tenant_data):
    """
    Visualize the geographic distribution of institutional-grade tenants.
    
    Parameters:
        tenant_data (DataFrame): A DataFrame containing tenant information with 'latitude' and 'longitude' columns.
    """
    # Check if required columns are present
    if 'latitude' not in tenant_data.columns or 'longitude' not in tenant_data.columns:
        raise ValueError("Tenant data must contain 'latitude' and 'longitude' columns.")

    # Convert tenant data to GeoDataFrame
    geometry = [Point(xy) for xy in zip(tenant_data.longitude, tenant_data.latitude)]
    geo_df = gpd.GeoDataFrame(tenant_data, geometry=geometry)

    # Load world map using GeoPandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Plotting the distribution of tenants
    fig, ax = plt.subplots(figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=1)
    geo_df.plot(ax=ax, color='blue', markersize=50, alpha=0.5, label='Institutional Tenants')

    # Customizing the plot
    plt.title('Geographic Distribution of Institutional-Grade Tenants', fontsize=16)
    plt.xlabel('Longitude', fontsize=12)
    plt.ylabel('Latitude', fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()

# Main execution block
if __name__ == "__main__":
    # API endpoint for tenant data (mock URL)
    api_url = "https://api.example.com/tenants"

    # Fetch tenant data
    tenant_data = fetch_tenant_data(api_url)

    # Visualize tenant distribution
    visualize_tenant_distribution(tenant_data)
```
