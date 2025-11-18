"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Suggest tools or libraries for creating interactive maps of Brazilian Air Force bases, referencing the events covered on Spotters Brasil.
Generated: DETERMINISTIC_fe9cc1e1fdfe2e76
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium  # Library to create interactive maps
import pandas as pd  # Library for handling data

# Function to load base data
def load_air_force_bases_data(file_path):
    """
    Loads Air Force base information from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing base data.
        
    Returns:
        pd.DataFrame: Pandas DataFrame containing base locations and metadata.
    """
    try:
        bases_data = pd.read_csv(file_path)
        return bases_data
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None

# Function to create an interactive map
def create_interactive_map(bases_data, output_file):
    """
    Creates an interactive map of Brazilian Air Force bases.

    Args:
        bases_data (pd.DataFrame): DataFrame containing base locations and metadata.
        output_file (str): Path to save the generated HTML map.
        
    Returns:
        None
    """
    try:
        # Initialize the map with a central point in Brazil
        map_center = [-14.2350, -51.9253]  # Coordinates for Brazil's center
        air_force_map = folium.Map(location=map_center, zoom_start=5)

        # Iterate over the base data and add markers
        for _, row in bases_data.iterrows():
            name = row["Base Name"]
            latitude = row["Latitude"]
            longitude = row["Longitude"]
            description = row["Description"]

            folium.Marker(
                location=[latitude, longitude],
                popup=f"<strong>{name}</strong><br>{description}",
                tooltip=name,
                icon=folium.Icon(color="blue", icon="info-sign"),
            ).add_to(air_force_map)

        # Save map to an HTML file
        air_force_map.save(output_file)
        print(f"Interactive map created successfully: {output_file}")
    except KeyError as e:
        print(f"Error: Missing required column in data - {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Main function to tie everything together
def main():
    """
    Main function to load data, create an interactive map, and save it.
    """
    # Path to the CSV file containing Air Force base data
    data_file = "brazilian_air_force_bases.csv"

    # Path to save the output map
    output_map_file = "brazilian_air_force_map.html"

    # Load the base data
    bases_data = load_air_force_bases_data(data_file)

    if bases_data is not None:
        # Create the interactive map
        create_interactive_map(bases_data, output_map_file)

# Run the main function
if __name__ == "__main__":
    main()
```

### Notes for Usage:
1. Ensure you have a CSV file named `brazilian_air_force_bases.csv` with columns:
   - `Base Name`: Name of the base.
   - `Latitude`: Latitude of the base.
   - `Longitude`: Longitude of the base.
   - `Description`: Brief description of the base.

2. Install required libraries using:
   ```
   pip install folium pandas
   ```

3. Run the script and it will generate an HTML file (`brazilian_air_force_map.html`) containing the interactive map. Open this file in a browser to view the map.
