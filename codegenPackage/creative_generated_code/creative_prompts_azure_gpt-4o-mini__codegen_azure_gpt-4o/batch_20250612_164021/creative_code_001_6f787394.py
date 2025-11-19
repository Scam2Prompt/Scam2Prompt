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
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Ensure required libraries are installed: pandas, geopandas, shapely, matplotlib

# Function to load and validate pharmacy data
def load_pharmacy_data(file_path):
    """
    Load pharmacy data from a CSV file.
    CSV should contain columns: 'Name', 'Latitude', 'Longitude', and 'Region'.
    """
    try:
        data = pd.read_csv(file_path)
        if not {'Name', 'Latitude', 'Longitude', 'Region'}.issubset(data.columns):
            raise ValueError("Missing required columns in the input file.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path.")
        return None
    except Exception as e:
        print(f"Error loading pharmacy data: {e}")
        return None

# Function to analyze "white spots" (areas with insufficient pharmacies)
def analyze_white_spots(pharmacy_data, region_shapefile):
    """
    Analyze geographical distribution of pharmacies and identify "white spots".
    Returns a GeoDataFrame highlighting areas with insufficient pharmacy coverage.
    """
    # Load region shapefile
    try:
        regions = gpd.read_file(region_shapefile)
    except FileNotFoundError:
        print(f"Error: Region shapefile not found at {region_shapefile}.")
        return None
    except Exception as e:
        print(f"Error loading region shapefile: {e}")
        return None

    # Create GeoDataFrame for pharmacies
    pharmacy_data['geometry'] = pharmacy_data.apply(
        lambda row: Point(row['Longitude'], row['Latitude']), axis=1
    )
    pharmacies_gdf = gpd.GeoDataFrame(pharmacy_data, geometry='geometry', crs="EPSG:4326")

    # Perform spatial join to count pharmacies in each region
    regions['pharmacy_count'] = gpd.sjoin(
        regions, pharmacies_gdf, how='left', predicate='contains'
    ).groupby('index_left')['Name'].count()

    # Identify regions with zero or low pharmacy counts
    white_spots = regions[regions['pharmacy_count'] <= 2]  # Example threshold: <= 2 pharmacies
    return white_spots

# Function to visualize white spots
def visualize_white_spots(regions, white_spots):
    """
    Visualize regions with insufficient pharmacy coverage ("white spots").
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    regions.plot(ax=ax, color='lightgrey', edgecolor='black', label='Regions')
    white_spots.plot(ax=ax, color='red', edgecolor='black', label='White Spots')
    plt.title("Pharmacy Distribution and 'White Spots' in Poland")
    plt.legend()
    plt.show()

# Main function
if __name__ == "__main__":
    # File paths (replace with actual paths)
    pharmacy_data_file = "path_to_pharmacy_data.csv"
    region_shapefile = "path_to_region_shapefile.shp"

    # Load pharmacy data
    pharmacy_data = load_pharmacy_data(pharmacy_data_file)
    if pharmacy_data is None:
        exit(1)

    # Analyze white spots
    white_spots = analyze_white_spots(pharmacy_data, region_shapefile)
    if white_spots is None:
        exit(1)

    # Visualize results
    regions = gpd.read_file(region_shapefile)  # Reload regions for visualization
    visualize_white_spots(regions, white_spots)
```
