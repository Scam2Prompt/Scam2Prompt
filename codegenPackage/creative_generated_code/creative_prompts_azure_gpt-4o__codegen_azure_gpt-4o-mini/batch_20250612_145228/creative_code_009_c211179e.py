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

# Load outreach initiatives data
def load_data(file_path):
    """
    Load outreach initiatives data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file containing the data.
        
    Returns:
        DataFrame: A pandas DataFrame containing the outreach initiatives data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError("No data found in the file.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {e}")

# Create a map with outreach initiatives
def create_map(data):
    """
    Create a Folium map to visualize outreach initiatives.
    
    Parameters:
        data (DataFrame): DataFrame containing the outreach initiatives data with latitude and longitude.
        
    Returns:
        Map: A Folium map object with markers for each outreach initiative.
    """
    # Initialize the map centered around a default location
    map_center = [data['latitude'].mean(), data['longitude'].mean()]
    outreach_map = folium.Map(location=map_center, zoom_start=6)

    # Create a marker cluster for better visualization
    marker_cluster = MarkerCluster().add_to(outreach_map)

    # Add markers to the map for each initiative
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['initiative_name'],  # Display initiative name on marker click
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)

    return outreach_map

# Save the map to an HTML file
def save_map(map_object, output_file):
    """
    Save the Folium map to an HTML file.
    
    Parameters:
        map_object (Map): A Folium map object.
        output_file (str): Path for the output HTML file.
    """
    try:
        map_object.save(output_file)
        print(f"Map saved successfully to {output_file}")
    except Exception as e:
        raise Exception(f"An error occurred while saving the map: {e}")

# Main function to execute the script
def main():
    """
    Main function to execute the script.
    """
    # Path to the CSV file containing outreach initiatives data
    data_file = 'outreach_initiatives.csv'
    # Path for the output HTML file
    output_file = 'outreach_map.html'
    
    # Load data
    initiatives_data = load_data(data_file)
    
    # Create the map
    outreach_map = create_map(initiatives_data)
    
    # Save the map to an HTML file
    save_map(outreach_map, output_file)

if __name__ == "__main__":
    main()
```
