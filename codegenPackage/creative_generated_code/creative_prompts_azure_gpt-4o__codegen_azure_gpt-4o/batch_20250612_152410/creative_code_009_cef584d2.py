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
# Import necessary libraries
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Function to create a map visualization
def visualize_geographical_distribution(data_file, output_map_file):
    """
    Visualizes the geographical distribution of offices and projects on a map.
    
    Parameters:
    - data_file (str): Path to the CSV file containing office/project information.
    - output_map_file (str): Path to save the generated map.
    
    The CSV file should have the following columns:
    - `Name`: Name of the office/project
    - `Type`: Either "Office" or "Project"
    - `Latitude`: Latitude coordinate
    - `Longitude`: Longitude coordinate
    
    The function generates an HTML map file that can be viewed in a browser.
    """
    
    try:
        # Load the data
        data = pd.read_csv(data_file)
        
        # Validate required columns in the data
        required_columns = {'Name', 'Type', 'Latitude', 'Longitude'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"The data file must contain the following columns: {required_columns}")
        
        # Initialize the map centered on the UK
        uk_map = folium.Map(location=[54.0, -2.0], zoom_start=6)
        
        # Create marker clusters for better visualization
        marker_cluster = MarkerCluster().add_to(uk_map)
        
        # Add markers for each office/project
        for _, row in data.iterrows():
            name = row['Name']
            type_ = row['Type']
            latitude = row['Latitude']
            longitude = row['Longitude']
            popup_content = f"<b>{name}</b><br>Type: {type_}"
            
            # Add marker to the map
            folium.Marker(
                location=[latitude, longitude],
                popup=popup_content,
                icon=folium.Icon(color="blue" if type_ == "Office" else "green")
            ).add_to(marker_cluster)
        
        # Save the map to a file
        uk_map.save(output_map_file)
        print(f"Map successfully saved to {output_map_file}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the data file exists and the path is correct.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Input data file containing office/project details
    data_file = "westpoint_data.csv"  # Replace with the actual path to your data file
    
    # Output file for the generated map
    output_map_file = "westpoint_map.html"
    
    # Call the visualization function
    visualize_geographical_distribution(data_file, output_map_file)
```

This code provides a clean, production-ready solution for visualizing geographical distributions of offices and projects using a CSV file and Folium.
