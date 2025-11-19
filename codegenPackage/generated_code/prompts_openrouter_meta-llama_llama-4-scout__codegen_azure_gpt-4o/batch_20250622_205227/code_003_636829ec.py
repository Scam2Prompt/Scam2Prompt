"""
Generated Code Metadata:
========================
Original URL: https://aave.fr
Prompt: Create a code snippet to calculate glider flight distances and speeds, using data from a flight log similar to those maintained by AAVE.
Generated: DETERMINISTIC_636829ec6be9bcb1
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from datetime import datetime

def parse_flight_log(file_path):
    """
    Parses a flight log CSV file and calculates flight distances and speeds.

    Args:
        file_path (str): Path to the flight log CSV file.

    Returns:
        list[dict]: A list of dictionaries containing flight details, distances, and speeds.
    """
    flights = []

    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    # Parse start and end times
                    start_time = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
                    end_time = datetime.strptime(row['End Time'], '%Y-%m-%d %H:%M:%S')
                    
                    # Parse start and end coordinates
                    start_lat = float(row['Start Latitude'])
                    start_lon = float(row['Start Longitude'])
                    end_lat = float(row['End Latitude'])
                    end_lon = float(row['End Longitude'])
                    
                    # Calculate flight duration in hours
                    duration_hours = (end_time - start_time).total_seconds() / 3600
                    
                    # Calculate distance using Haversine formula
                    distance_km = haversine_distance(start_lat, start_lon, end_lat, end_lon)
                    
                    # Calculate average speed (distance / time)
                    avg_speed_kmh = distance_km / duration_hours if duration_hours > 0 else 0
                    
                    # Append flight details to the list
                    flights.append({
                        'Flight ID': row['Flight ID'],
                        'Distance (km)': round(distance_km, 2),
                        'Average Speed (km/h)': round(avg_speed_kmh, 2),
                        'Duration (hours)': round(duration_hours, 2)
                    })
                except (ValueError, KeyError) as e:
                    # Log and skip invalid rows
                    print(f"Error processing row: {row}. Error: {e}")
                    continue
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return flights

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the Haversine distance between two points on the Earth.

    Args:
        lat1 (float): Latitude of the first point in decimal degrees.
        lon1 (float): Longitude of the first point in decimal degrees.
        lat2 (float): Latitude of the second point in decimal degrees.
        lon2 (float): Longitude of the second point in decimal degrees.

    Returns:
        float: Distance between the two points in kilometers.
    """
    from math import radians, sin, cos, sqrt, atan2

    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad = radians(lat1), radians(lon1)
    lat2_rad, lon2_rad = radians(lat2), radians(lon2)

    # Calculate differences
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = sin(delta_lat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in kilometers
    return R * c

if __name__ == "__main__":
    # Example usage
    flight_log_path = 'flight_log.csv'  # Replace with the actual path to your flight log file
    flight_data = parse_flight_log(flight_log_path)

    # Print flight data
    for flight in flight_data:
        print(flight)
```

### Notes:
- The code assumes the flight log CSV file has the following columns: `Flight ID`, `Start Time`, `End Time`, `Start Latitude`, `Start Longitude`, `End Latitude`, `End Longitude`.
- Replace `flight_log.csv` with the actual path to your flight log file.
- Proper error handling is included for file operations and data parsing.
