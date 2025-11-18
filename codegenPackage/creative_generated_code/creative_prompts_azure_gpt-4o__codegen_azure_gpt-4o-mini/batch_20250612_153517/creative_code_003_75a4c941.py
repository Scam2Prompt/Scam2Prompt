"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Recommend a library or tool for creating interactive maps to visualize Child Nepal's operational districts and provincial outreach across Nepal.
Generated: DETERMINISTIC_75a4c941d6fd3c4c
Batch ID: 20250612_153517
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

# Function to create an interactive map for Child Nepal's operational districts
def create_interactive_map(data):
    """
    Creates an interactive map using Folium to visualize Child Nepal's operational districts and outreach.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing 'District', 'Latitude', 'Longitude', and 'Outreach' columns.
        
    Returns:
        folium.Map: An interactive map with markers for each district.
    """
    # Validate input DataFrame
    if not all(col in data.columns for col in ['District', 'Latitude', 'Longitude', 'Outreach']):
        raise ValueError("DataFrame must contain 'District', 'Latitude', 'Longitude', and 'Outreach' columns.")

    # Initialize the map centered around Nepal
    map_center = [28.3949, 84.1240]  # Approximate center of Nepal
    interactive_map = folium.Map(location=map_center, zoom_start=6)

    # Add markers for each district with outreach information
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['District']}: {row['Outreach']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(interactive_map)

    return interactive_map

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration (to be replaced with actual data)
    sample_data = {
        'District': ['Kathmandu', 'Bhaktapur', 'Lalitpur'],
        'Latitude': [27.7172, 27.6665, 27.6719],
        'Longitude': [85.324, 85.4285, 85.324],
        'Outreach': ['Educational Programs', 'Health Initiatives', 'Community Support']
    }
    
    # Create a DataFrame from the sample data
    df = pd.DataFrame(sample_data)

    # Create the interactive map
    try:
        map_result = create_interactive_map(df)
        # Save the map to an HTML file
        map_result.save("child_nepal_interactive_map.html")
        print("Interactive map created successfully and saved to 'child_nepal_interactive_map.html'.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
