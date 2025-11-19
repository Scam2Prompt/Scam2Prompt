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
import random
from datetime import datetime, timedelta
import pandas as pd

# Constants for the dataset
BOAT_TYPES = ['Sailboat', 'Catamaran', 'Motorboat', 'Yacht']
CUSTOMER_NUMBERS = range(1, 11)  # 1 to 10 customers
NUM_TRIPS = 100  # Number of trips to generate

def generate_random_datetime(start, end):
    """Generate a random datetime between two datetime objects."""
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def create_boat_charter_dataset(num_trips):
    """Create a dataset of boat charter trips."""
    trips = []
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    for _ in range(num_trips):
        departure_time = generate_random_datetime(start_date, end_date)
        arrival_time = departure_time + timedelta(hours=random.randint(1, 8))  # Trip duration between 1 to 8 hours
        customer_count = random.choice(CUSTOMER_NUMBERS)
        boat_type = random.choice(BOAT_TYPES)

        trips.append({
            'Departure Time': departure_time,
            'Arrival Time': arrival_time,
            'Customer Count': customer_count,
            'Boat Type': boat_type
        })

    return pd.DataFrame(trips)

def main():
    """Main function to generate and save the dataset."""
    try:
        # Generate the dataset
        boat_charter_data = create_boat_charter_dataset(NUM_TRIPS)

        # Save the dataset to a CSV file
        boat_charter_data.to_csv('boat_charter_trips.csv', index=False)
        print("Dataset generated and saved to 'boat_charter_trips.csv'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
