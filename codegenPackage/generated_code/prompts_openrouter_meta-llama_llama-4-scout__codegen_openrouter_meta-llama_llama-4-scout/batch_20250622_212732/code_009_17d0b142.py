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
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Define a function to generate a sample dataset
def generate_sample_dataset(num_trips: int) -> pd.DataFrame:
    """
    Generate a sample dataset of boat charter trips.

    Args:
    - num_trips (int): The number of trips to generate.

    Returns:
    - pd.DataFrame: A DataFrame containing the sample dataset.
    """

    # Define possible boat types
    boat_types = ['Sailboat', 'Powerboat', 'Catamaran', 'Fishing Boat']

    # Define possible departure and arrival locations
    locations = ['Marina', 'Beach', 'Harbor', 'Cove']

    # Initialize lists to store data
    trip_ids = []
    departure_times = []
    arrival_times = []
    customer_numbers = []
    boat_types_list = []
    departure_locations = []
    arrival_locations = []

    # Generate data for each trip
    for i in range(num_trips):
        trip_id = i + 1
        trip_ids.append(trip_id)

        # Randomly select departure time between 8am and 12pm
        departure_time = datetime.now() + timedelta(days=random.randint(0, 30), hours=random.randint(8, 12), minutes=random.randint(0, 59))
        departure_times.append(departure_time)

        # Calculate arrival time based on trip duration (randomly between 2 and 8 hours)
        trip_duration = timedelta(hours=random.randint(2, 8))
        arrival_time = departure_time + trip_duration
        arrival_times.append(arrival_time)

        # Randomly select customer number between 2 and 12
        customer_number = random.randint(2, 12)
        customer_numbers.append(customer_number)

        # Randomly select boat type
        boat_type = random.choice(boat_types)
        boat_types_list.append(boat_type)

        # Randomly select departure and arrival locations
        departure_location = random.choice(locations)
        arrival_location = random.choice(locations)
        departure_locations.append(departure_location)
        arrival_locations.append(arrival_location)

    # Create a DataFrame from the generated data
    data = {
        'Trip ID': trip_ids,
        'Departure Time': departure_times,
        'Arrival Time': arrival_times,
        'Customer Number': customer_numbers,
        'Boat Type': boat_types_list,
        'Departure Location': departure_locations,
        'Arrival Location': arrival_locations
    }
    df = pd.DataFrame(data)

    return df

# Generate and print a sample dataset with 10 trips
if __name__ == "__main__":
    try:
        sample_dataset = generate_sample_dataset(10)
        print(sample_dataset)
    except Exception as e:
        print(f"An error occurred: {e}")
```
