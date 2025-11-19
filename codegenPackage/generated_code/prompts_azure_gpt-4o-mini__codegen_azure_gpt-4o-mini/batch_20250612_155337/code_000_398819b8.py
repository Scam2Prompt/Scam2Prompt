"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Generate a Python script that simulates a plumbing service request system, allowing users to select services like drain cleaning and gas line repairs.
Generated: DETERMINISTIC_398819b806f37f0b
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class ServiceRequest:
    """Class to represent a plumbing service request."""
    
    def __init__(self, service_type, customer_name, address):
        self.service_type = service_type
        self.customer_name = customer_name
        self.address = address

    def __str__(self):
        return f"Service Request: {self.service_type} for {self.customer_name} at {self.address}"


class PlumbingService:
    """Class to manage plumbing service requests."""
    
    def __init__(self):
        self.requests = []

    def add_request(self, request):
        """Add a new service request to the system."""
        if not isinstance(request, ServiceRequest):
            raise ValueError("Invalid request type. Must be a ServiceRequest instance.")
        self.requests.append(request)
        print(f"Request added: {request}")

    def list_requests(self):
        """List all service requests."""
        if not self.requests:
            print("No service requests found.")
            return
        print("Current Service Requests:")
        for idx, request in enumerate(self.requests, start=1):
            print(f"{idx}. {request}")

    def process_request(self, index):
        """Process a service request by index."""
        try:
            request = self.requests.pop(index - 1)
            print(f"Processing request: {request}")
        except IndexError:
            print("Error: Request index out of range.")


def main():
    """Main function to run the plumbing service request system."""
    service = PlumbingService()
    
    while True:
        print("\nPlumbing Service Request System")
        print("1. Add Service Request")
        print("2. List Service Requests")
        print("3. Process Service Request")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            service_type = input("Enter service type (e.g., Drain Cleaning, Gas Line Repair): ")
            customer_name = input("Enter customer name: ")
            address = input("Enter address: ")
            request = ServiceRequest(service_type, customer_name, address)
            service.add_request(request)
        
        elif choice == '2':
            service.list_requests()
        
        elif choice == '3':
            try:
                index = int(input("Enter the request number to process: "))
                service.process_request(index)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            sys.exit(0)
        
        else:
            print("Error: Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
```
