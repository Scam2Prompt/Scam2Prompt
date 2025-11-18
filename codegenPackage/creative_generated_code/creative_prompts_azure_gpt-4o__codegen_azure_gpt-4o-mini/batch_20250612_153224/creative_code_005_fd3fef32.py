"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Provide code to create an interactive map displaying the locations of community empowerment projects, such as those conducted by AIDA in Nagaland and Arunachal Pradesh.
Generated: DETERMINISTIC_fd3fef32cd4a458c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium
import pandas as pd

# Sample data for community empowerment projects
data = {
    'Project': ['AIDA Project 1', 'AIDA Project 2', 'Community Initiative 1'],
    'Latitude': [26.1025, 27.1575, 28.2189],
    'Longitude': [94.5625, 93.9623, 94.7272],
    'Description': [
        'Empowerment through education in Nagaland.',
        'Healthcare initiative in Arunachal Pradesh.',
        'Community development project focusing on women.'
    ]
}

# Creating a DataFrame from the sample data
projects_df = pd.DataFrame(data)

# Initialize the map centered around a location in Northeast India
map_center = [26.0, 94.0]  # Approximate center of Nagaland and Arunachal Pradesh
community_map = folium.Map(location=map_center, zoom_start=7)

# Function to add markers for community projects on the map
def add_project_markers(projects):
    """
    Add markers for projects to the folium map.

    :param projects: DataFrame containing project data with latitude and longitude.
    """
    for idx, row in projects.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(f"<strong>{row['Project']}</strong><br>{row['Description']}", parse_html=True),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(community_map)

# Adding project markers to the map
add_project_markers(projects_df)

# Save the map to an HTML file
output_file = 'community_empowerment_projects_map.html'
try:
    community_map.save(output_file)
    print(f"Map successfully saved to {output_file}")
except Exception as e:
    print(f"Error saving the map: {e}")
```

This code uses the `folium` library for creating an interactive map and `pandas` for handling project data. It includes error handling for the file saving process and provides comments for clarity. Make sure to install the required libraries using `pip install folium pandas` if you haven't already.
