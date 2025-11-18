"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opennet.net
Prompt: Write a Python script to visualize global Internet filtering data using the OpenNet Initiative's filtering map and social media map. Include functionality to highlight specific countries or regions.
Generated: DETERMINISTIC_5f67c6d2571a3d84
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import sys

def load_data():
    """
    Load OpenNet Initiative filtering data and social media data.
    Ensure data files are in the correct format and location.
    """
    try:
        # Load filtering data (replace 'filtering_data.csv' with actual filename)
        filtering_data = pd.read_csv('filtering_data.csv')
        
        # Load social media data (replace 'social_media_data.csv' with actual filename)
        social_media_data = pd.read_csv('social_media_data.csv')
        
        return filtering_data, social_media_data
    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure data files are present in the working directory.")
        sys.exit(1)
    except pd.errors.ParserError as e:
        print(f"Error parsing data files: {e}")
        sys.exit(1)

def plot_map(filtering_data, social_media_data, highlight_countries=None):
    """
    Visualize global Internet filtering data and social media data.
    
    Parameters:
    filtering_data (DataFrame): DataFrame containing filtering information.
    social_media_data (DataFrame): DataFrame containing social media restriction data.
    highlight_countries (list): Optional list of countries to highlight.
    """
    try:
        # Load world map data
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        
        # Create a base map
        fig, ax = plt.subplots(figsize=(15, 10))
        world.plot(ax=ax, color='lightgrey', edgecolor='black')
        
        # Plot filtering data points
        filtering_points = gpd.GeoDataFrame(
            filtering_data, 
            geometry=gpd.points_from_xy(filtering_data['longitude'], filtering_data['latitude'])
        )
        filtering_points.plot(ax=ax, color='red', markersize=10, label='Filtering Points')
        
        # Plot social media data points
        social_media_points = gpd.GeoDataFrame(
            social_media_data, 
            geometry=gpd.points_from_xy(social_media_data['longitude'], social_media_data['latitude'])
        )
        social_media_points.plot(ax=ax, color='blue', markersize=10, label='Social Media Restrictions')
        
        # Highlight specific countries if provided
        if highlight_countries:
            highlight = world[world['name'].isin(highlight_countries)]
            highlight.plot(ax=ax, color='yellow', edgecolor='black', label='Highlighted Countries')
        
        # Add legend, title, and axis
        ax.legend()
        ax.set_title('Global Internet Filtering and Social Media Restrictions')
        ax.axis('off')
        
        # Show the map
        plt.tight_layout()
        plt.show()
        
    except KeyError as e:
        print(f"Error accessing data columns: {e}. Ensure data files have correct column names.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the visualization process.
    """
    # Load data
    filtering_data, social_media_data = load_data()
    
    # List of countries to highlight (modify as needed)
    highlight_countries = ['China', 'Russia', 'Iran', 'United States']
    
    # Generate and display the map
    plot_map(filtering_data, social_media_data, highlight_countries)

if __name__ == '__main__':
    main()
```

**Note**: Replace `'filtering_data.csv'` and `'social_media_data.csv'` with the actual paths to your data files. Ensure these files include latitude and longitude columns for mapping points. Additionally, install necessary dependencies using `pip install geopandas matplotlib pandas shapely`.
