"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Write a Python script to manage cleaning service requests for a company like Maria HouseKeepers, including scheduling and customer information.
Generated: DETERMINISTIC_b9e614f57eac0928
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import List, Dict, Optional

class CleaningServiceRequest:
    """Class to represent a cleaning service request."""
    
    def __init__(self, customer_name: str, address: str, date: str, time: str):
        self.customer_name = customer_name
        self.address = address
        self.date = self.validate_date(date)
        self.time = self.validate_time(time)

    def validate_date(self, date: str) -> datetime.date:
        """Validate and return a date object from a string."""
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def validate_time(self, time: str) -> datetime.time:
        """Validate and return a time object from a string."""
        try:
            return datetime.datetime.strptime(time, "%H:%M").time()
        except ValueError:
            raise ValueError("Time must be in HH:MM format.")

    def to_dict(self) -> Dict:
        """Convert the request to a dictionary for easy serialization."""
        return {
            "customer_name": self.customer_name,
            "address": self.address,
            "date": str(self.date),
            "time": str(self.time)
        }

class CleaningServiceManager:
    """Class to manage cleaning service requests."""
    
    def __init__(self):
        self.requests: List[CleaningServiceRequest] = []

    def add_request(self, request: CleaningServiceRequest) -> None:
        """Add a new cleaning service request."""
        self.requests.append(request)

    def get_requests(self) -> List[Dict]:
        """Get all cleaning service requests as a list of dictionaries."""
        return [request.to_dict() for request in self.requests]

    def save_requests_to_file(self, filename: str) -> None:
        """Save the requests to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_requests(), file, indent=4)
        except IOError as e:
            print(f"Error saving requests to file: {e}")

    def load_requests_from_file(self, filename: str) -> None:
        """Load requests from a JSON file."""
        try:
            with open(filename, 'r') as file:
                requests_data = json.load(file)
                for request_data in requests_data:
                    request = CleaningServiceRequest(
                        customer_name=request_data["customer_name"],
                        address=request_data["address"],
                        date=request_data["date"],
                        time=request_data["time"]
                    )
                    self.add_request(request)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading requests from file: {e}")

def main():
    """Main function to run the cleaning service manager."""
    manager = CleaningServiceManager()

    # Example usage
    try:
        # Adding a new cleaning service request
        request1 = CleaningServiceRequest("John Doe", "123 Main St", "2023-10-15", "14:00")
        manager.add_request(request1)

        # Saving requests to a file
        manager.save_requests_to_file("cleaning_requests.json")

        # Loading requests from a file
        manager.load_requests_from_file("cleaning_requests.json")

        # Displaying all requests
        print("Current Cleaning Service Requests:")
        for request in manager.get_requests():
            print(request)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
