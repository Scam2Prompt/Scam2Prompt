"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token2049.0xsmit.com
Prompt: What libraries can I use to create a dynamic map for Token2049 side events?
Generated: DETERMINISTIC_fd1c98eeb029b67b
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium  # Library for creating interactive maps
import pandas as pd  # Library for data manipulation

def create_dynamic_map(dataframe, map_location=[1.3521, 103.8198], zoom_start=12):
    """
    Creates a dynamic map with markers from the provided dataframe.

    Args:
        dataframe (pd.DataFrame): DataFrame containing 'latitude', 'longitude', and 'event_name' columns.
        map_location (list): Initial latitude and longitude for the map center.
        zoom_start (int): Initial zoom level for the map.

    Returns:
        folium.Map: A folium Map object with markers added.
    """
    # Validate that required columns are in the DataFrame
    required_columns = ['latitude', 'longitude', 'event_name']
    for col in required_columns:
        if col not in dataframe.columns:
            raise ValueError(f"Missing required column: {col}")

    # Create a folium map centered at the specified location
    dynamic_map = folium.Map(location=map_location, zoom_start=zoom_start)

    # Add markers for each event in the DataFrame
    for _, row in dataframe.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['event_name'],
            icon=folium.Icon(icon='info-sign')
        ).add_to(dynamic_map)

    return dynamic_map

# Example usage:
if __name__ == "__main__":
    # Sample data for events (latitude, longitude, event_name)
    data = {
        'latitude': [1.3521, 1.3641],
        'longitude': [103.8198, 103.8471],
        'event_name': ['Token2049 Main Event', 'Token2049 After Party']
    }
    
    # Create a DataFrame from the sample data
    events_df = pd.DataFrame(data)

    try:
        # Generate the dynamic map
        map_output = create_dynamic_map(events_df)

        # Save the map to an HTML file
        map_output.save('token2049_events_map.html')
        print("Map generated and saved as 'token2049_events_map.html'.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
