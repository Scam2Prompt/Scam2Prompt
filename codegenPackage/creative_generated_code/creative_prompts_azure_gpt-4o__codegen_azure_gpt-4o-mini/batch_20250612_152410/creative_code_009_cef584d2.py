"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Create a tool to visualize the geographical distribution of Westpoint Construction's offices and projects across the UK.
Generated: DETERMINISTIC_cef584d2d01355c3
Batch ID: 20250612_152410
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

class GeoVisualizer:
    """
    A class to visualize the geographical distribution of Westpoint Construction's offices and projects across the UK.
    """

    def __init__(self, data_file):
        """
        Initializes the GeoVisualizer with a data file containing office and project locations.
        
        :param data_file: Path to the CSV file containing location data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the CSV data into a DataFrame and checks for required columns.
        
        :return: A DataFrame containing location data.
        """
        try:
            data = pd.read_csv(self.data_file)
            if {'Latitude', 'Longitude', 'Name', 'Type'}.issubset(data.columns):
                return data
            else:
                raise ValueError("CSV must contain 'Latitude', 'Longitude', 'Name', and 'Type' columns.")
        except Exception as e:
            raise RuntimeError(f"Error loading data: {e}")

    def create_map(self):
        """
        Creates a Folium map centered around the average location of the offices/projects.
        
        :return: A Folium map object.
        """
        try:
            # Compute the average latitude and longitude
            avg_lat = self.data['Latitude'].mean()
            avg_lon = self.data['Longitude'].mean()

            # Create a Folium map
            m = folium.Map(location=[avg_lat, avg_lon], zoom_start=6)

            # Add markers for each office/project
            for _, row in self.data.iterrows():
                folium.Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=f"{row['Name']} ({row['Type']})",
                    icon=folium.Icon(color='blue' if row['Type'] == 'Office' else 'green')
                ).add_to(m)

            return m
        except Exception as e:
            raise RuntimeError(f"Error creating map: {e}")

    def save_map(self, output_file):
        """
        Saves the generated map to an HTML file.
        
        :param output_file: Path to the output HTML file.
        """
        try:
            map_object = self.create_map()
            map_object.save(output_file)
            print(f"Map saved successfully to {output_file}")
        except Exception as e:
            raise RuntimeError(f"Error saving map: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        data_file = 'westpoint_locations.csv'  # Path to your CSV file
        output_file = 'westpoint_map.html'      # Path to save the output map

        visualizer = GeoVisualizer(data_file)
        visualizer.save_map(output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
```
