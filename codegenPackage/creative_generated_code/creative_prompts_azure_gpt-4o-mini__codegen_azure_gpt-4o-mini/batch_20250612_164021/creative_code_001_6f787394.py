"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pharmanet.org.pl
Prompt: Write a code snippet that analyzes the geographical distribution of pharmacies in Poland, focusing on the "aptek białe plamy" issue highlighted by PharmaNET.
Generated: DETERMINISTIC_6f7873941bed655f
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Define the path to the pharmacy data and geographical boundaries
pharmacy_data_path = 'pharmacies_poland.csv'
poland_geo_data_path = 'poland_boundaries.geojson'

def load_data(pharmacy_data_path, poland_geo_data_path):
    """
    Load pharmacy data and Polish geographical boundaries.

    :param pharmacy_data_path: Path to the CSV file containing pharmacy data.
    :param poland_geo_data_path: Path to the GeoJSON file containing Polish boundaries.
    :return: Tuple of DataFrames for pharmacies and GeoDataFrame for Poland.
    """
    try:
        pharmacies = pd.read_csv(pharmacy_data_path)
        poland_boundaries = gpd.read_file(poland_geo_data_path)
        return pharmacies, poland_boundaries
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")

def analyze_pharmacies(pharmacies):
    """
    Analyze pharmacy distribution and identify 'aptek białe plamy' (white spots).

    :param pharmacies: DataFrame containing pharmacy locations.
    :return: DataFrame with analysis results.
    """
    # Group by postal code to count pharmacies
    pharmacy_counts = pharmacies.groupby('postal_code').size().reset_index(name='count')

    # Identify postal codes with fewer than a threshold number of pharmacies
    threshold = 3  # Define a threshold for 'białe plamy' identification
    aptek_biale_plamy = pharmacy_counts[pharmacy_counts['count'] < threshold]

    return aptek_biale_plamy

def visualize_distribution(poland_boundaries, pharmacies, aptek_biale_plamy):
    """
    Visualize the distribution of pharmacies and highlight 'aptek białe plamy'.

    :param poland_boundaries: GeoDataFrame containing Polish boundaries.
    :param pharmacies: DataFrame containing pharmacy locations.
    :param aptek_biale_plamy: DataFrame with identified postal codes of 'białe plamy'.
    """
    # Convert pharmacy locations to a GeoDataFrame
    gdf_pharmacies = gpd.GeoDataFrame(
        pharmacies, 
        geometry=gpd.points_from_xy(pharmacies.longitude, pharmacies.latitude),
        crs="EPSG:4326"
    )

    # Plot the boundaries of Poland
    fig, ax = plt.subplots(figsize=(10, 10))
    poland_boundaries.plot(ax=ax, color='lightgrey')

    # Plot pharmacies
    gdf_pharmacies.plot(ax=ax, color='blue', markersize=5, label='Pharmacies')

    # Highlight 'białe plamy'
    missing_pharmacy_locations = gdf_pharmacies[gdf_pharmacies['postal_code'].isin(aptek_biale_plamy['postal_code'])]
    missing_pharmacy_locations.plot(ax=ax, color='red', markersize=30, label='Aptek Białe Plamy')

    # Add legend and titles
    plt.title('Geographical Distribution of Pharmacies in Poland')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    """
    Main function to execute the pharmacy analysis and visualization.
    """
    try:
        # Load data
        pharmacies, poland_boundaries = load_data(pharmacy_data_path, poland_geo_data_path)
        
        # Analyze pharmacies
        aptek_biale_plamy = analyze_pharmacies(pharmacies)
        
        # Visualize results
        visualize_distribution(poland_boundaries, pharmacies, aptek_biale_plamy)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
