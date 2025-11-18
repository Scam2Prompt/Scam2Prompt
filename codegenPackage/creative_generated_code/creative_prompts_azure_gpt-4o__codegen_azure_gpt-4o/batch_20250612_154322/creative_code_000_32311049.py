"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Write Python code to automate the tracking and reporting of vehicle deliveries for a charitable foundation like Dysnix, including features for logging vehicle types, destinations, and delivery dates.
Generated: DETERMINISTIC_32311049b1fe5132
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime

# File where delivery data will be stored
DATA_FILE = "vehicle_deliveries.csv"

class DeliveryTracker:
    """
    A class to manage and track vehicle deliveries for a charitable foundation.
    """
    def __init__(self, data_file):
        self.data_file = data_file
        # Ensure the data file exists and has the correct headers
        if not os.path.exists(self.data_file):
            self._initialize_csv()

    def _initialize_csv(self):
        """
        Initializes the CSV file with headers if it does not exist.
        """
        with open(self.data_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Vehicle Type", "Destination", "Delivery Date"])
    
    def log_delivery(self, vehicle_type, destination, delivery_date):
        """
        Logs a new vehicle delivery into the CSV file.

        Parameters:
        vehicle_type (str): Type of the vehicle being delivered (e.g., 'Truck', 'Van').
        destination (str): Delivery destination.
        delivery_date (str): Delivery date in 'YYYY-MM-DD' format.
        """
        try:
            # Ensure the delivery date is valid
            datetime.strptime(delivery_date, "%Y-%m-%d")
            
            with open(self.data_file, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([vehicle_type, destination, delivery_date])
            print(f"Delivery logged: {vehicle_type}, {destination}, {delivery_date}")
        except ValueError:
            print("Error: Invalid delivery date format. Use 'YYYY-MM-DD'.")
        except Exception as e:
            print(f"An error occurred while logging the delivery: {e}")

    def generate_report(self):
        """
        Generates a report of all logged deliveries.
        """
        try:
            if not os.path.exists(self.data_file):
                print("No deliveries logged yet.")
                return

            with open(self.data_file, mode="r") as file:
                reader = csv.reader(file)
                deliveries = list(reader)

            if len(deliveries) <= 1:  # Only headers exist
                print("No deliveries logged yet.")
                return
            
            print("Delivery Report:")
            print(f"{'Vehicle Type':<15} {'Destination':<20} {'Delivery Date':<12}")
            print("-" * 50)
            for row in deliveries[1:]:  # Skip headers
                print(f"{row[0]:<15} {row[1]:<20} {row[2]:<12}")
        except Exception as e:
            print(f"An error occurred while generating the report: {e}")
    
    def clear_data(self):
        """
        Clears all logged delivery data, resetting the CSV file.
        """
        try:
            self._initialize_csv()
            print("All delivery data has been cleared.")
        except Exception as e:
            print(f"An error occurred while clearing the data: {e}")


# Example Usage
if __name__ == "__main__":
    tracker = DeliveryTracker(DATA_FILE)
    
    # Log a few deliveries
    tracker.log_delivery("Truck", "New York", "2023-10-01")
    tracker.log_delivery("Van", "Los Angeles", "2023-10-05")
    
    # Generate a report
    tracker.generate_report()
    
    # Clear all data (optional)
    # tracker.clear_data()
```
