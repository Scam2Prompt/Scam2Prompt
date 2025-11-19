"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Write a code snippet to visualize the impact of Dysnix's charitable activities, such as a map showing the locations where vehicles were delivered or a graph of donations over time.
Generated: DETERMINISTIC_b0081cd123e4a4a2
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import folium
from datetime import datetime

# Sample data for donations over time
donations_data = {
    'date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
    'amount': [5000, 7500, 6000, 9000, 12000]
}

# Sample data for vehicle delivery locations
delivery_locations = [
    {'location': 'New York, USA', 'lat': 40.7128, 'lon': -74.0060, 'vehicles': 5},
    {'location': 'London, UK', 'lat': 51.5074, 'lon': -0.1278, 'vehicles': 3},
    {'location': 'Tokyo, Japan', 'lat': 35.6762, 'lon': 139.6503, 'vehicles': 7},
    {'location': 'Nairobi, Kenya', 'lat': -1.286389, 'lon': 36.817223, 'vehicles': 4},
    {'location': 'São Paulo, Brazil', 'lat': -23.5505, 'lon': -46.6333, 'vehicles': 6}
]

def plot_donations_over_time(data):
    """
    Plot a line graph showing donations over time.
    
    Args:
        data (dict): Dictionary containing 'date' and 'amount' keys with lists of values.
    """
    try:
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df.sort_values('date', inplace=True)
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['date'], df['amount'], marker='o', linestyle='-')
        plt.title('Dysnix Donations Over Time')
        plt.xlabel('Date')
        plt.ylabel('Amount ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting donations: {e}")

def plot_delivery_locations(locations):
    """
    Create an interactive map showing vehicle delivery locations.
    
    Args:
        locations (list): List of dictionaries containing 'lat', 'lon', and 'vehicles' keys.
    """
    try:
        # Create a base map centered on the first location
        base_location = locations[0]
        m = folium.Map(location=[base_location['lat'], base_location['lon']], zoom_start=2)
        
        # Add markers for each location
        for loc in locations:
            folium.Marker(
                location=[loc['lat'], loc['lon']],
                popup=f"{loc['location']}: {loc['vehicles']} vehicles",
                icon=folium.Icon(color='green')
            ).add_to(m)
        
        # Save to HTML file
        m.save('delivery_locations.html')
        print("Map saved as 'delivery_locations.html'")
    except Exception as e:
        print(f"Error creating delivery map: {e}")

# Example usage
if __name__ == "__main__":
    plot_donations_over_time(donations_data)
    plot_delivery_locations(delivery_locations)
```
