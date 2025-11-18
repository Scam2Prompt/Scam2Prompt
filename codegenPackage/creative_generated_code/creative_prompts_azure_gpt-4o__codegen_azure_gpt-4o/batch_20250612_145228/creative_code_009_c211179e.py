"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Write a script to visualize the geographic distribution of SGFC Finance's community outreach initiatives using mapping libraries like Folium or Plotly.
Generated: DETERMINISTIC_c211179eac1d6965
Batch ID: 20250612_145228
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

# Sample dataset representing SGFC Finance's outreach initiatives
# Replace this with your actual dataset, e.g., from a database or CSV file
data = {
    'Initiative': ['Financial Literacy Workshop', 'Small Business Support', 'Community Bank Partnership', 'Startup Incubator'],
    'Latitude': [40.7128, 34.0522, 41.8781, 37.7749],
    'Longitude': [-74.0060, -118.2437, -87.6298, -122.4194],
    'Description': [
        'Educating communities on financial best practices.',
        'Providing grants and mentoring for small businesses.',
        'Creating partnerships with local community banks.',
        'Supporting entrepreneurs with resources and funding.'
    ]
}

# Convert the sample data into a DataFrame
df = pd.DataFrame(data)

# Create a base map centered on the United States
# The center and zoom level can be adjusted based on your dataset
base_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Use MarkerCluster to group locations for better visualization
marker_cluster = MarkerCluster().add_to(base_map)

# Add markers for each outreach initiative
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(
            f"<strong>{row['Initiative']}</strong><br>{row['Description']}",
            max_width=300,
        ),
        tooltip=row['Initiative']
    ).add_to(marker_cluster)

# Save the map to an HTML file
output_file = 'sgfc_community_outreach_map.html'
base_map.save(output_file)

print(f"Map has been saved successfully to {output_file}. Open it in a browser to view.")
```
