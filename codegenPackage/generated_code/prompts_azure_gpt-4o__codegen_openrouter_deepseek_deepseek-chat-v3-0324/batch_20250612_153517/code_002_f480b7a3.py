"""
Generated Code Metadata:
========================
Original URL: https://tidhholding.com
Prompt: Generate code to visualize the impact of reclaimed desert land projects, similar to TIDH Holding's "Desert to Green Oasis" initiative, using geospatial libraries like GeoPandas or Folium.
Generated: DETERMINISTIC_f480b7a3a576427e
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from shapely.geometry import Point, Polygon
from datetime import datetime

# Configuration
DATA_DIR = "data"
OUTPUT_DIR = "output"
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Sample data generation function
def generate_sample_data(num_projects=10):
    """Generate sample geospatial data for desert reclamation projects."""
    np.random.seed(42)
    
    # Sample project locations around desert regions
    base_locations = {
        'Sahara': (20, 10),
        'Arabian': (24, 45),
        'Gobi': (42.5, 105),
        'Kalahari': (-23, 20),
        'Atacama': (-24, -69)
    }
    
    projects = []
    for i in range(num_projects):
        region = np.random.choice(list(base_locations.keys()))
        base_lat, base_lon = base_locations[region]
        
        lat = base_lat + np.random.uniform(-5, 5)
        lon = base_lon + np.random.uniform(-5, 5)
        
        start_date = datetime(2010 + np.random.randint(0, 10), 1, 1)
        end_date = start_date.replace(year=start_date.year + np.random.randint(1, 5))
        
        projects.append({
            'project_id': f"PRJ-{1000 + i}",
            'name': f"{region} Reclamation {i+1}",
            'region': region,
            'start_date': start_date,
            'end_date': end_date,
            'area_reclaimed_ha': np.random.uniform(100, 5000),
            'water_saved_ml': np.random.uniform(1000, 50000),
            'co2_reduced_kt': np.random.uniform(1, 100),
            'geometry': Point(lon, lat)
        })
    
    return gpd.GeoDataFrame(projects, crs="EPSG:4326")

# Visualization functions
def create_folium_map(gdf):
    """Create an interactive Folium map with project locations and details."""
    center = [gdf.geometry.y.mean(), gdf.geometry.x.mean()]
    m = folium.Map(location=center, zoom_start=3, tiles='cartodbpositron')
    
    marker_cluster = MarkerCluster().add_to(m)
    
    for _, row in gdf.iterrows():
        popup_html = f"""
        <b>Project:</b> {row['name']}<br>
        <b>Region:</b> {row['region']}<br>
        <b>Area Reclaimed:</b> {row['area_reclaimed_ha']:,.0f} ha<br>
        <b>Water Saved:</b> {row['water_saved_ml']:,.0f} ML<br>
        <b>CO₂ Reduced:</b> {row['co2_reduced_kt']:,.1f} kt<br>
        <b>Duration:</b> {row['start_date'].year}-{row['end_date'].year}
        """
        
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color='green', icon='tree')
        ).add_to(marker_cluster)
    
    # Add desert boundaries layer (sample)
    folium.GeoJson(
        data=gdf.dissolve(by='region').geometry,
        style_function=lambda x: {'fillColor': '#f5e79e', 'color': '#f5e79e', 'weight': 1, 'fillOpacity': 0.3},
        name='Desert Regions'
    ).add_to(m)
    
    folium.LayerControl().add_to(m)
    
    return m

def create_impact_plots(gdf):
    """Create matplotlib plots showing impact metrics."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Area reclaimed by region
    gdf.groupby('region')['area_reclaimed_ha'].sum().sort_values().plot(
        kind='barh', ax=axes[0, 0], color='green', alpha=0.7
    )
    axes[0, 0].set_title('Total Area Reclaimed by Region (ha)')
    axes[0, 0].set_xlabel('Hectares')
    
    # Water saved over time
    yearly_water = gdf.groupby(gdf['start_date'].dt.year)['water_saved_ml'].sum()
    yearly_water.plot(
        kind='line', ax=axes[0, 1], marker='o', color='blue', linestyle='--'
    )
    axes[0, 1].set_title('Water Saved Over Time (ML)')
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Megaliters')
    
    # CO2 reduced by project size
    gdf.plot.scatter(
        x='area_reclaimed_ha', y='co2_reduced_kt', ax=axes[1, 0], 
        c='green', s=100, alpha=0.6
    )
    axes[1, 0].set_title('CO₂ Reduction vs Reclaimed Area')
    axes[1, 0].set_xlabel('Area Reclaimed (ha)')
    axes[1, 0].set_ylabel('CO₂ Reduced (kt)')
    
    # Project duration distribution
    gdf['duration_years'] = (gdf['end_date'] - gdf['start_date']).dt.days / 365
    gdf['duration_years'].plot(
        kind='hist', ax=axes[1, 1], bins=10, color='orange', alpha=0.7
    )
    axes[1, 1].set_title('Project Duration Distribution')
    axes[1, 1].set_xlabel('Years')
    
    plt.tight_layout()
    return fig

# Main execution
if __name__ == "__main__":
    try:
        print("Generating sample data...")
        projects_gdf = generate_sample_data(25)
        
        print("Creating visualizations...")
        # Save GeoJSON
        projects_gdf.to_file(os.path.join(DATA_DIR, "projects.geojson"), driver='GeoJSON')
        
        # Create and save Folium map
        folium_map = create_folium_map(projects_gdf)
        folium_map.save(os.path.join(OUTPUT_DIR, "desert_reclamation_map.html"))
        
        # Create and save impact plots
        impact_fig = create_impact_plots(projects_gdf)
        impact_fig.savefig(os.path.join(OUTPUT_DIR, "impact_metrics.png"), dpi=150)
        
        print(f"Visualizations saved to {OUTPUT_DIR} directory.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
