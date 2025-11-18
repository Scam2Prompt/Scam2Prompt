"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springbokinfo.co.za
Prompt: Write code to display a map with markers for businesses listed in Springbok Info, using the location data provided on the site.
Generated: DETERMINISTIC_07220f145d86a8f9
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import folium  # Library for creating interactive maps
import csv     # Library for handling CSV files

def load_business_data(file_path):
    """
    Load business data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing business information.
        
    Returns:
        list: List of dictionaries containing business data (name, latitude, longitude).
    """
    businesses = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure latitude and longitude are valid before adding to the list
                try:
                    latitude = float(row['latitude'])
                    longitude = float(row['longitude'])
                    businesses.append({
                        'name': row['name'],
                        'latitude': latitude,
                        'longitude': longitude
                    })
                except ValueError:
                    # Skip rows with invalid latitude or longitude
                    continue
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"Error loading the file: {e}")
    
    return businesses

def create_business_map(businesses, output_file='business_map.html'):
    """
    Create an interactive map with markers for businesses.
    
    Args:
        businesses (list): List of dictionaries containing business data.
        output_file (str): Path for the output HTML file containing the map.
    """
    # Set a default starting point for the map (Springbok, South Africa)
    start_lat = -29.6644
    start_lon = 17.8865
    
    # Create the map centered on Springbok
    business_map = folium.Map(location=[start_lat, start_lon], zoom_start=13)
    
    # Add markers for each business
    for business in businesses:
        folium.Marker(
            location=[business['latitude'], business['longitude']],
            popup=business['name'],  # Show the business name on click
            icon=folium.Icon(icon='info-sign')
        ).add_to(business_map)
    
    # Save the map to an HTML file
    try:
        business_map.save(output_file)
        print(f"Map saved to {output_file}")
    except Exception as e:
        print(f"Error saving map: {e}")

if __name__ == "__main__":
    # Path to the CSV file containing business data
    csv_file_path = 'springbok_info.csv'
    
    # Load business data into memory
    business_data = load_business_data(csv_file_path)
    
    # Check if any data was loaded
    if not business_data:
        print("No business data found. Exiting...")
    else:
        # Create and save the map
        create_business_map(business_data)
```
