"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Generate code to visualize the distribution of visapwr's visa application centres across 90 countries, using geolocation data.
Generated: DETERMINISTIC_791c8298916f0564
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def load_and_preprocess_data(file_path):
    """
    Load and preprocess the visa application centers data.
    """
    try:
        df = pd.read_csv(file_path)
        
        # Basic data validation
        required_columns = ['country', 'latitude', 'longitude', 'center_name']
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        # Drop rows with missing geolocation data
        df = df.dropna(subset=['latitude', 'longitude'])
        
        # Convert to proper numeric types
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
        df = df.dropna(subset=['latitude', 'longitude'])
        
        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def create_geo_dataframe(df):
    """
    Convert DataFrame to GeoDataFrame with Point geometry.
    """
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    return gdf

def plot_world_distribution(gdf):
    """
    Plot the global distribution of visa centers using a world map.
    """
    try:
        # Get world map data
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        
        # Plot the world map
        fig, ax = plt.subplots(figsize=(15, 10))
        world.plot(ax=ax, color='lightgray', edgecolor='black')
        
        # Plot the visa centers
        gdf.plot(ax=ax, marker='o', color='red', markersize=5, alpha=0.7)
        
        plt.title('Global Distribution of Visa Application Centers')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting world distribution: {str(e)}")

def create_interactive_map(df):
    """
    Create an interactive Folium map with marker clusters.
    """
    try:
        # Create base map
        m = folium.Map(location=[20, 0], zoom_start=2, tiles='cartodbpositron')
        
        # Add marker clusters
        marker_cluster = MarkerCluster().add_to(m)
        
        # Add markers for each visa center
        for idx, row in df.iterrows():
            popup_text = f"""
            <b>Country:</b> {row['country']}<br>
            <b>Center:</b> {row['center_name']}<br>
            <b>Location:</b> {row['latitude']:.4f}, {row['longitude']:.4f}
            """
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=folium.Popup(popup_text, max_width=250),
                icon=folium.Icon(color='blue', icon='home')
            ).add_to(marker_cluster)
        
        # Add layer control
        folium.LayerControl().add_to(m)
        
        return m
    except Exception as e:
        print(f"Error creating interactive map: {str(e)}")
        return None

def main():
    # File path to the visa centers data
    data_file = 'visa_centers.csv'  # Replace with your actual file path
    
    # Load and preprocess data
    df = load_and_preprocess_data(data_file)
    if df is None:
        return
    
    print(f"Loaded data for {len(df)} visa centers across {df['country'].nunique()} countries")
    
    # Create GeoDataFrame
    gdf = create_geo_dataframe(df)
    
    # Visualizations
    print("\nGenerating visualizations...")
    
    # Static world map plot
    plot_world_distribution(gdf)
    
    # Interactive Folium map
    interactive_map = create_interactive_map(df)
    if interactive_map:
        interactive_map.save('visa_centers_map.html')
        print("Interactive map saved as 'visa_centers_map.html'")

if __name__ == "__main__":
    main()
```
