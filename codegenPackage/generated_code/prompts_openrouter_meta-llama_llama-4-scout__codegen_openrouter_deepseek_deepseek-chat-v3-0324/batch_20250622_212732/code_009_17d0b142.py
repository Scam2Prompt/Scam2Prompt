"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Generate a sample dataset of boat charter trips, including departure and arrival times, customer numbers, and boat types, for use in testing analytics or operational tools for Salty Daze Charters."
Generated: DETERMINISTIC_17d0b142a1313ded
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import random
from datetime import datetime, timedelta

# Constants
BOAT_TYPES = ['Sailboat', 'Motorboat', 'Catamaran', 'Yacht', 'Fishing Boat']
CUSTOMER_MIN = 1
CUSTOMER_MAX = 10
TRIP_DURATION_MIN = 1  # hours
TRIP_DURATION_MAX = 8  # hours
OUTPUT_FILE = 'boat_charter_trips.csv'
NUM_RECORDS = 100

def generate_trip_data(num_records):
    """Generate sample boat charter trip data."""
    data = []
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    for i in range(num_records):
        # Generate random trip details
        boat_type = random.choice(BOAT_TYPES)
        customer_count = random.randint(CUSTOMER_MIN, CUSTOMER_MAX)
        trip_duration = random.randint(TRIP_DURATION_MIN, TRIP_DURATION_MAX)
        
        # Generate random departure time (within next 30 days)
        days_offset = random.randint(0, 30)
        hours_offset = random.randint(6, 20)  # Between 6AM and 8PM
        departure_time = base_date + timedelta(days=days_offset, hours=hours_offset)
        
        # Calculate arrival time
        arrival_time = departure_time + timedelta(hours=trip_duration)
        
        # Format dates for CSV
        departure_str = departure_time.strftime('%Y-%m-%d %H:%M')
        arrival_str = arrival_time.strftime('%Y-%m-%d %H:%M')
        
        trip_id = f"TRIP{i+1:04d}"
        
        data.append([
            trip_id,
            departure_str,
            arrival_str,
            boat_type,
            customer_count,
            trip_duration
        ])
    
    return data

def write_to_csv(data, filename):
    """Write trip data to CSV file."""
    headers = ['trip_id', 'departure_time', 'arrival_time', 'boat_type', 'customer_count', 'trip_duration_hours']
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)
        print(f"Successfully generated {len(data)} records to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == '__main__':
    trip_data = generate_trip_data(NUM_RECORDS)
    write_to_csv(trip_data, OUTPUT_FILE)
```
