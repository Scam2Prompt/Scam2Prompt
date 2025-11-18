"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neom-property.com
Prompt: Create a program that uses geospatial libraries to map the NEOM region in Northwestern Saudi Arabia. Include features to overlay investment zones and giga-project developments.
Generated: DETERMINISTIC_f052436960f91f25
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Define a function to load geographical data
def load_geospatial_data(file_path):
    """
    Load geospatial data from a shapefile.

    Args:
        file_path (str): Path to the shapefile.

    Returns:
        GeoDataFrame: A GeoDataFrame containing the geographical data.
    """
    try:
        gdf = gpd.read_file(file_path)
        return gdf
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

# Define a function to plot the NEOM region along with overlays
def plot_neom_region(neom_data, investment_zones, giga_projects):
    """
    Plot the NEOM region with investment zones and giga-projects.

    Args:
        neom_data (GeoDataFrame): GeoDataFrame containing NEOM boundaries.
        investment_zones (GeoDataFrame): GeoDataFrame containing investment zones.
        giga_projects (GeoDataFrame): GeoDataFrame containing giga-project developments.
    """
    try:
        # Create a figure and axis for plotting
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Plot NEOM region
        neom_data.plot(ax=ax, color='lightgrey', edgecolor='black', alpha=0.5, label='NEOM Region')
        
        # Overlay investment zones
        investment_zones.plot(ax=ax, color='green', alpha=0.6, label='Investment Zones')
        
        # Overlay giga-project developments
        giga_projects.plot(ax=ax, color='blue', marker='o', markersize=50, label='Giga Projects')
        
        # Set title and labels
        ax.set_title('NEOM Region: Investment Zones and Giga-Projects', fontsize=15)
        ax.set_xlabel('Longitude', fontsize=12)
        ax.set_ylabel('Latitude', fontsize=12)
        
        # Add a legend
        ax.legend()
        
        # Show the plot
        plt.show()
    except Exception as e:
        print(f"Error during plotting: {e}")

# Main function to execute the program
def main():
    """
    Main function to load data and plot the NEOM region with overlays.
    """
    # File paths for geospatial data (update these paths as necessary)
    neom_file_path = 'neom_region.shp'
    investment_zones_file_path = 'investment_zones.shp'
    giga_projects_file_path = 'giga_projects.shp'

    # Load the data
    neom_data = load_geospatial_data(neom_file_path)
    investment_zones = load_geospatial_data(investment_zones_file_path)
    giga_projects = load_geospatial_data(giga_projects_file_path)

    # Only plot if all data is loaded successfully
    if neom_data is not None and investment_zones is not None and giga_projects is not None:
        plot_neom_region(neom_data, investment_zones, giga_projects)

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes:
- Ensure that the shapefiles (`neom_region.shp`, `investment_zones.shp`, and `giga_projects.shp`) are available in the working directory or update the file paths accordingly.
- This code requires the `geopandas` and `matplotlib` libraries. You can install them using pip:
  ```
  pip install geopandas matplotlib
  ```
