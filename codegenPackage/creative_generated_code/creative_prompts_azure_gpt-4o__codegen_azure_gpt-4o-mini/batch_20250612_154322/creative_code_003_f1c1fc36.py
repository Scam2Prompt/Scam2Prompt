"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Create a script to analyze and prioritize incoming requests for vehicles based on urgency and location, inspired by Dysnix's process of handling ZSU requests.
Generated: DETERMINISTIC_f1c1fc36cfdb88c8
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict
from datetime import datetime

class Request:
    def __init__(self, request_id: int, urgency: int, location: str, timestamp: str):
        """
        Initializes a new vehicle request.

        :param request_id: Unique identifier for the request
        :param urgency: Urgency level of the request (1-5, where 5 is most urgent)
        :param location: Location of the request in a string format (e.g., "City, State")
        :param timestamp: Time at which the request was created in ISO format
        """
        self.request_id = request_id
        self.urgency = urgency
        self.location = location
        self.timestamp = datetime.fromisoformat(timestamp)

    def __repr__(self):
        return f"<Request(id={self.request_id}, urgency={self.urgency}, location={self.location}, timestamp={self.timestamp})>"

class RequestAnalyzer:
    def __init__(self):
        """
        Initializes the RequestAnalyzer with an empty list of requests.
        """
        self.requests: List[Request] = []

    def add_request(self, request: Request):
        """
        Adds a new request to the analyzer.

        :param request: The Request object to be added
        """
        self.requests.append(request)

    def prioritize_requests(self) -> List[Request]:
        """
        Prioritizes requests based on urgency and timestamp.

        :return: A sorted list of requests by urgency (high to low) then by timestamp (oldest to newest)
        """
        return sorted(self.requests, key=lambda r: (-r.urgency, r.timestamp))

def load_requests_from_file(file_path: str) -> List[Request]:
    """
    Loads requests from a JSON file.

    :param file_path: The path to the JSON file containing requests
    :return: A list of Request objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Request(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def save_prioritized_requests(file_path: str, requests: List[Request]):
    """
    Saves the prioritized requests to a JSON file.

    :param file_path: The path to the JSON file where requests will be saved
    :param requests: The list of prioritized Request objects to be saved
    """
    try:
        with open(file_path, 'w') as file:
            json.dump([request.__dict__ for request in requests], file, default=str)
    except Exception as e:
        print(f"An error occurred while saving to {file_path}: {e}")

if __name__ == '__main__':
    analyzer = RequestAnalyzer()

    # Load requests from a JSON file
    input_file = 'requests.json'
    requests = load_requests_from_file(input_file)
    
    for req in requests:
        analyzer.add_request(req)

    # Prioritize the requests
    prioritized_requests = analyzer.prioritize_requests()

    # Save the prioritized requests to a new JSON file
    output_file = 'prioritized_requests.json'
    save_prioritized_requests(output_file, prioritized_requests)

    # Output the prioritized requests to console for verification
    print("Prioritized Requests:")
    for req in prioritized_requests:
        print(req)
```
