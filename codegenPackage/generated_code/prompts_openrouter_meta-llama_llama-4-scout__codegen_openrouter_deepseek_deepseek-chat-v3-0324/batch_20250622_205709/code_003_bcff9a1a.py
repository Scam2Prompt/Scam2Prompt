"""
Generated Code Metadata:
========================
Original URL: https://opennet.net
Prompt: Create a data visualization map to show the states and regions where different types of Internet filtering occur, inspired by the OpenNet Initiative's main filtering map.
Generated: DETERMINISTIC_bcff9a1a5962e774
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import contextily as ctx

# Load country boundaries data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Sample filtering data (in a real scenario, this would come from OpenNet or another source)
filtering_data = {
    'country': ['China', 'Iran', 'Russia', 'Brazil', 'Germany', 'India', 'USA'],
    'filtering_type': ['Political', 'Social', 'Mixed', 'Social', 'None', 'Mixed', 'Political'],
    'intensity': [3, 2, 2, 1, 0, 1, 1]  # 0=None, 1=Low, 2=Medium, 3=High
}

# Create DataFrame
df = pd.DataFrame(filtering_data)

# Merge with world data
merged = world.merge(df, left_on='name', right_on='country', how='left')

# Fill NaN values for countries without data
merged['filtering_type'] = merged['filtering_type'].fillna('None')
merged['intensity'] = merged['intensity'].fillna(0)

# Define color mapping
filtering_colors = {
    'None': '#f7f7f7',
    'Political': '#e41a1c',
    'Social': '#377eb8',
    'Mixed': '#4daf4a'
}

intensity_colors = ListedColormap(['#f7f7f7', '#ffffcc', '#fd8d3c', '#bd0026'])

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

# Plot filtering types
merged.plot(column='filtering_type', 
            ax=ax1,
            cmap=ListedColormap(list(filtering_colors.values())),
            legend=True,
            missing_kwds={'color': 'lightgrey'},
            legend_kwds={'title': 'Filtering Type', 'loc': 'lower left'})

# Plot intensity levels
merged.plot(column='intensity',
            ax=ax2,
            cmap=intensity_colors,
            legend=True,
            missing_kwds={'color': 'lightgrey'},
            legend_kwds={'title': 'Filtering Intensity', 'loc': 'lower left'})

# Add basemap
ctx.add_basemap(ax1, crs=merged.crs, source=ctx.providers.CartoDB.Positron)
ctx.add_basemap(ax2, crs=merged.crs, source=ctx.providers.CartoDB.Positron)

# Set titles
ax1.set_title('Internet Filtering by Type', fontsize=14)
ax2.set_title('Internet Filtering by Intensity', fontsize=14)

# Remove axis labels
ax1.set_axis_off()
ax2.set_axis_off()

plt.tight_layout()
plt.show()
```
