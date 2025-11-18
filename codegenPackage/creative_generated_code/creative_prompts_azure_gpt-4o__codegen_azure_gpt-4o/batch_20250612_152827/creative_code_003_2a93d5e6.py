"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Provide code to visualize the geographic distribution of institutional-grade tenants in a property portfolio, similar to the one managed by Rosebud Holdings Property Income REIT in Malta.
Generated: DETERMINISTIC_2a93d5e61681b3e3
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Data preparation
# Replace this DataFrame with actual tenant data from a database or CSV file
# Ensure the DataFrame contains columns for tenant name, latitude, longitude, and other relevant details
data = {
    "Tenant Name": ["Tenant A", "Tenant B", "Tenant C", "Tenant D"],
    "Latitude": [35.8991, 35.8941, 36.0421, 35.8890],
    "Longitude": [14.5146, 14.5015, 14.5178, 14.5184],
    "Property Name": ["Property 1", "Property 2", "Property 3", "Property 4"],
    "Rental Value": [12000, 15000, 10000, 18000],
}
df = pd.DataFrame(data)

# Create a base map centered in Malta
malta_coordinates = [35.8991, 14.5146]  # Approximate geographic center of Malta
map = folium.Map(location=malta_coordinates, zoom_start=12)

# MarkerCluster to group nearby markers
marker_cluster = MarkerCluster().add_to(map)

# Add markers for each tenant
for index, row in df.iterrows():
    # Create a popup with tenant details
    popup_content = (
        f"<b>Tenant Name:</b> {row['Tenant Name']}<br>"
        f"<b>Property Name:</b> {row['Property Name']}<br>"
        f"<b>Rental Value:</b> €{row['Rental Value']:,}"
    )
    popup = folium.Popup(popup_content, max_width=250)

    # Add marker to the cluster
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=popup,
        tooltip=row["Tenant Name"],  # Tooltip for quick identification
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(marker_cluster)

# Save the map to an HTML file
map.save("institutional_tenants_map.html")

# Code is complete. Open 'institutional_tenants_map.html' in a browser to view the map.
```
