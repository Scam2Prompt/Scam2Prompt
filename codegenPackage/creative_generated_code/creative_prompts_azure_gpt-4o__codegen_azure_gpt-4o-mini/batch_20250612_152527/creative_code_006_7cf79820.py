"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://larpradar.com
Prompt: Create a visualization tool that uses Larp Radar's interactive map data to show clusters of LARP events across Europe and highlight lesser-known locations.
Generated: DETERMINISTIC_7cf7982042b0f45e
Batch ID: 20250612_152527
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
import numpy as np

# Load LARP event data
def load_larp_data(file_path):
    """
    Load LARP event data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file containing LARP events.
        
    Returns:
        DataFrame: A pandas DataFrame containing the LARP events data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# Create a folium map with LARP events
def create_larp_map(event_data):
    """
    Create a folium map visualizing LARP events.
    
    Args:
        event_data (DataFrame): A pandas DataFrame containing LARP event data.
        
    Returns:
        folium.Map: A folium map object with LARP events plotted.
    """
    # Initialize the map centered around Europe
    larp_map = folium.Map(location=[50.0, 10.0], zoom_start=4)

    # Add event locations to the map
    for _, event in event_data.iterrows():
        try:
            folium.Marker(
                location=[event['Latitude'], event['Longitude']],
                popup=f"<b>{event['Name']}</b><br>{event['Description']}",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(larp_map)
        except KeyError as e:
            print(f"Missing data in event record: {e}")
    
    return larp_map

# Highlight lesser-known locations
def highlight_lesser_known_locations(event_data, threshold=5):
    """
    Highlight lesser-known LARP event locations on the map.
    
    Args:
        event_data (DataFrame): A pandas DataFrame containing LARP event data.
        threshold (int): The minimum number of events to be considered known.
        
    Returns:
        list: A list of locations considered lesser-known.
    """
    # Group by location and count events
    location_counts = event_data.groupby(['Latitude', 'Longitude']).size()
    
    # Find lesser-known locations
    lesser_known = location_counts[location_counts < threshold].index.tolist()
    
    return lesser_known

# Main function to run the visualization tool
def main(file_path):
    """
    Main function to run the LARP visualization tool.
    
    Args:
        file_path (str): The path to the CSV file containing LARP events.
    """
    # Load the LARP event data
    larp_data = load_larp_data(file_path)

    if larp_data.empty:
        print("No data to visualize.")
        return
    
    # Create the map
    larp_map = create_larp_map(larp_data)

    # Highlight lesser-known locations
    lesser_known_locations = highlight_lesser_known_locations(larp_data)
    
    for lat, lon in lesser_known_locations:
        folium.Marker(
            location=[lat, lon],
            popup="Lesser Known Location",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(larp_map)

    # Save the map to an HTML file
    larp_map.save("larp_events_map.html")
    print("Map has been created and saved as 'larp_events_map.html'.")

# Run the visualization tool with a given file path
if __name__ == "__main__":
    file_path = "larp_events.csv"  # Replace with your actual CSV file path
    main(file_path)
```
