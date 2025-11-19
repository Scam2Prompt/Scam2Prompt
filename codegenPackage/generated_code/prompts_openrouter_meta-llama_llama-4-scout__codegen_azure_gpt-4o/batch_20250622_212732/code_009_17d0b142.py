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
import datetime
import csv

# Function to generate random datetime within a given range
def random_datetime(start, end):
    """
    Generate a random datetime between two datetime objects.
    :param start: Start datetime
    :param end: End datetime
    :return: Random datetime object
    """
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + datetime.timedelta(seconds=random_seconds)

# Function to generate a random boat charter trip dataset
def generate_boat_charter_data(num_records, output_file):
    """
    Generate a dataset of boat charter trips and save it to a CSV file.
    :param num_records: Number of records to generate
    :param output_file: Output CSV file name
    """
    # Define constants
    boat_types = ["Sailboat", "Motorboat", "Catamaran", "Yacht"]
    customer_range = (1, 12)  # Min and max number of customers per trip
    start_date = datetime.datetime(2023, 1, 1, 6, 0)  # Earliest departure time
    end_date = datetime.datetime(2023, 12, 31, 18, 0)  # Latest departure time
    trip_duration_range = (1, 8)  # Min and max trip duration in hours

    # Prepare dataset
    dataset = []
    for _ in range(num_records):
        # Generate random departure time
        departure_time = random_datetime(start_date, end_date)
        
        # Generate random trip duration
        trip_duration = random.randint(*trip_duration_range)
        
        # Calculate arrival time
        arrival_time = departure_time + datetime.timedelta(hours=trip_duration)
        
        # Generate random number of customers
        num_customers = random.randint(*customer_range)
        
        # Select random boat type
        boat_type = random.choice(boat_types)
        
        # Append record to dataset
        dataset.append({
            "Departure Time": departure_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Arrival Time": arrival_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Number of Customers": num_customers,
            "Boat Type": boat_type
        })

    # Write dataset to CSV file
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Departure Time", "Arrival Time", "Number of Customers", "Boat Type"])
            writer.writeheader()
            writer.writerows(dataset)
        print(f"Dataset successfully written to {output_file}")
    except Exception as e:
        print(f"Error writing dataset to file: {e}")

# Main execution
if __name__ == "__main__":
    # Generate 100 sample records and save to 'boat_charter_data.csv'
    generate_boat_charter_data(num_records=100, output_file="boat_charter_data.csv")
```
