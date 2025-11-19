"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepbook.online
Prompt: Generate a Python script that simulates a plumbing service request system, allowing users to select services like drain cleaning and gas line repairs.
Generated: DETERMINISTIC_398819b806f37f0b
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PlumbingServiceRequest:
    def __init__(self):
        # Initialize available services and an empty request list
        self.services = {
            "Drain Cleaning": 100.00,
            "Gas Line Repair": 250.00,
            "Leak Detection": 150.00,
            "Pipe Replacement": 300.00
        }
        self.requests = []

    def display_services(self):
        """Display available plumbing services and their prices."""
        print("Available Plumbing Services:")
        for service, price in self.services.items():
            print(f"{service}: ${price:.2f}")

    def create_request(self, service_name, customer_name):
        """Create a service request if the service is available."""
        try:
            if service_name not in self.services:
                raise ValueError(f"Service '{service_name}' is not available.")
            
            request = {
                "customer_name": customer_name,
                "service": service_name,
                "price": self.services[service_name]
            }
            self.requests.append(request)
            print(f"Request created for {customer_name} for service '{service_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def save_requests_to_file(self, filename):
        """Save service requests to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.requests, file, indent=4)
            print(f"Requests saved to {filename}.")
        except IOError as e:
            print(f"Error saving requests to file: {e}")

    def load_requests_from_file(self, filename):
        """Load service requests from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.requests = json.load(file)
            print(f"Requests loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading requests from file: {e}")

def main():
    # Main function to run the plumbing service request system
    service_system = PlumbingServiceRequest()

    while True:
        print("\n--- Plumbing Service Request System ---")
        service_system.display_services()
        
        customer_name = input("Enter your name (or type 'exit' to quit): ")
        if customer_name.lower() == 'exit':
            break

        service_name = input("Enter the service you need: ")
        service_system.create_request(service_name, customer_name)

        save_choice = input("Do you want to save the requests to a file? (y/n): ")
        if save_choice.lower() == 'y':
            filename = input("Enter filename to save requests (e.g., requests.json): ")
            service_system.save_requests_to_file(filename)

        load_choice = input("Do you want to load requests from a file? (y/n): ")
        if load_choice.lower() == 'y':
            filename = input("Enter filename to load requests from (e.g., requests.json): ")
            service_system.load_requests_from_file(filename)

if __name__ == "__main__":
    main()
```
