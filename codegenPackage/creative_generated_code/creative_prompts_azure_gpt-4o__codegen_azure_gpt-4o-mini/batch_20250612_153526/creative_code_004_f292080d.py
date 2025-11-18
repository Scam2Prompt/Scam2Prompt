"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Suggest tools or libraries for building an interactive map that highlights public art projects like the "Kibera Peace Walls" murals, showcasing their locations and descriptions.
Generated: DETERMINISTIC_f292080db4a0d270
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import folium  # For creating interactive maps
import pandas as pd  # For handling data structures

# Define a function to create an interactive map with public art projects
def create_interactive_map(art_projects, map_location=[-1.2921, 36.8219], zoom_start=12):
    """
    Create an interactive map showing public art projects with markers.

    Parameters:
    art_projects (DataFrame): A pandas DataFrame containing art project data
    map_location (list): Latitude and Longitude for centering the map
    zoom_start (int): Initial zoom level of the map

    Returns:
    folium.Map: An interactive map object
    """
    
    # Initialize a Folium map
    art_map = folium.Map(location=map_location, zoom_start=zoom_start)

    # Iterate over each art project and add markers to the map
    for _, project in art_projects.iterrows():
        try:
            # Create a marker for each project
            folium.Marker(
                location=[project['latitude'], project['longitude']],
                popup=folium.Popup(f"<strong>{project['name']}</strong><br>{project['description']}", parse_html=True),
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(art_map)
        except KeyError as e:
            print(f"Missing data for project: {project}. Error: {e}")
        except Exception as e:
            print(f"An error occurred while adding a marker for project {project['name']}: {e}")

    return art_map

# Example usage
if __name__ == "__main__":
    # Sample data for public art projects
    data = {
        'name': ['Kibera Peace Wall 1', 'Kibera Peace Wall 2'],
        'description': ['A beautiful mural depicting peace.', 'A colorful representation of community spirit.'],
        'latitude': [-1.2921, -1.2930],
        'longitude': [36.8219, 36.8220]
    }

    # Create a DataFrame from the sample data
    art_projects_df = pd.DataFrame(data)

    # Create the interactive map
    interactive_art_map = create_interactive_map(art_projects_df)

    # Save the map to an HTML file
    try:
        interactive_art_map.save('art_projects_map.html')
        print("Map has been created and saved to 'art_projects_map.html'")
    except Exception as e:
        print(f"An error occurred while saving the map: {e}")
```
