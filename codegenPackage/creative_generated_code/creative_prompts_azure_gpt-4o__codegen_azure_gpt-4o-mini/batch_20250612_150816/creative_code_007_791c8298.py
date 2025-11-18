"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visa-pwr.com
Prompt: Generate code to visualize the distribution of visapwr's visa application centres across 90 countries, using geolocation data.
Generated: DETERMINISTIC_791c8298916f0564
Batch ID: 20250612_150816
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
import matplotlib.pyplot as plt

# Function to visualize visa application centres on a world map
def visualize_visa_centres(data_file):
    """
    Visualizes the distribution of visa application centres across countries using geolocation data.

    Parameters:
        data_file (str): Path to the CSV file containing visa application centre data with 
                         'Country', 'Latitude', and 'Longitude' columns.

    Returns:
        None: Displays the map with visa application centres.
    """
    # Load visa application centres data from a CSV file
    try:
        visa_data = pd.read_csv(data_file)
    except FileNotFoundError:
        print(f"Error: The file {data_file} was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The provided CSV file is empty.")
        return
    except pd.errors.ParserError:
        print("Error: There was an issue parsing the CSV file.")
        return

    # Validate required columns in the dataframe
    required_columns = ['Country', 'Latitude', 'Longitude']
    if not all(col in visa_data.columns for col in required_columns):
        print(f"Error: The CSV file must contain the following columns: {', '.join(required_columns)}")
        return

    # Create a folium map centered around a median location
    median_lat = visa_data['Latitude'].median()
    median_lon = visa_data['Longitude'].median()
    visa_map = folium.Map(location=[median_lat, median_lon], zoom_start=2)

    # Create a Marker Cluster to manage multiple markers
    marker_cluster = MarkerCluster().add_to(visa_map)

    # Adding markers to the map for each visa application centre
    for _, row in visa_data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Country'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)

    # Save the map to an HTML file
    output_file = "visa_application_centres_map.html"
    visa_map.save(output_file)
    print(f"Map has been saved to {output_file}. Open it in a web browser to view.")

# Example usage
if __name__ == "__main__":
    data_file_path = "visa_centres_data.csv"  # Specify the correct path to your data
    visualize_visa_centres(data_file_path)
```
