"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Generate a script to analyze supplier data and optimize logistics for global delivery, referencing Cedar International Inc.'s strategic hubs in Houston, Toronto, UAE, and the UK.
Generated: DETERMINISTIC_7c9fa06994566c3f
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

# Constants for strategic hub locations
STRATEGIC_HUBS = {
    "Houston": {"latitude": 29.7604, "longitude": -95.3698},
    "Toronto": {"latitude": 43.65107, "longitude": -79.347015},
    "UAE": {"latitude": 24.4539, "longitude": 54.3773},
    "UK": {"latitude": 51.509865, "longitude": -0.118092},
}

# Function to calculate distance between two geographical points using the Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two latitude-longitude points in kilometers.
    The Haversine formula is used for accurate calculations on spherical surfaces.
    """
    R = 6371  # Radius of Earth in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c

# Function to optimize logistics and assign supplier to the nearest hub
def assign_hub(supplier_data):
    """
    Assign each supplier to the nearest strategic hub by calculating distances.
    :param supplier_data: DataFrame containing supplier latitude and longitude.
    :return: DataFrame with an additional column for assigned hub.
    """
    assigned_hubs = []

    for _, row in supplier_data.iterrows():
        supplier_lat = row['latitude']
        supplier_lon = row['longitude']

        # Calculate distance to each hub and find the nearest one
        distances = {
            hub: haversine_distance(supplier_lat, supplier_lon, hub_data["latitude"], hub_data["longitude"])
            for hub, hub_data in STRATEGIC_HUBS.items()
        }
        nearest_hub = min(distances, key=distances.get)  # Get hub with minimum distance
        assigned_hubs.append(nearest_hub)

    supplier_data['assigned_hub'] = assigned_hubs
    return supplier_data

# Main script to analyze supplier data and optimize logistics
def main():
    try:
        # Load supplier data
        supplier_data_path = "supplier_data.csv"  # Replace with actual path to supplier data
        supplier_data = pd.read_csv(supplier_data_path)

        # Validate required columns
        if not {'latitude', 'longitude'}.issubset(supplier_data.columns):
            raise ValueError("Input data must contain 'latitude' and 'longitude' columns.")

        # Analyze and optimize logistics
        optimized_data = assign_hub(supplier_data)

        # Save the optimized data to a new file
        output_path = "optimized_supplier_data.csv"  # Replace with desired output path
        optimized_data.to_csv(output_path, index=False)
        print(f"Optimized supplier data saved to {output_path}")

    except FileNotFoundError:
        print("Error: Supplier data file not found. Please check the file path.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
