"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Write a Python script to manage customer requests for appliance repair services, including fields for appliance type, brand, and issue description. Include a feature to prioritize urgent requests.
Generated: DETERMINISTIC_8e40e93018af75d3
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RepairRequest:
    """
    A class to represent a repair request for an appliance.
    """

    def __init__(self, customer_name, appliance_type, brand, issue_description, urgent=False):
        """
        Initializes a new repair request.
        
        :param customer_name: Name of the customer
        :param appliance_type: Type of appliance (e.g., refrigerator, washer)
        :param brand: Brand of the appliance
        :param issue_description: Description of the issue
        :param urgent: Boolean indicating if the request is urgent (default: False)
        """
        self.customer_name = customer_name
        self.appliance_type = appliance_type
        self.brand = brand
        self.issue_description = issue_description
        self.urgent = urgent
        self.timestamp = datetime.datetime.now()  # Timestamp to record request creation time

    def __str__(self):
        """
        Returns a string representation of the repair request.
        """
        urgency_status = "Urgent" if self.urgent else "Normal"
        return (f"Customer: {self.customer_name}, Appliance: {self.appliance_type} ({self.brand}), "
                f"Issue: {self.issue_description}, Status: {urgency_status}, "
                f"Requested On: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")


class RepairRequestManager:
    """
    A class to manage repair requests.
    """

    def __init__(self):
        """
        Initializes the repair request manager with an empty list of requests.
        """
        self.requests = []

    def add_request(self, request):
        """
        Adds a new repair request.
        
        :param request: An instance of the RepairRequest class
        """
        if not isinstance(request, RepairRequest):
            raise ValueError("Invalid request: Must be an instance of RepairRequest.")
        self.requests.append(request)

    def get_requests(self, urgent_only=False):
        """
        Retrieves repair requests, optionally filtering for urgent requests only.
        
        :param urgent_only: Boolean indicating if only urgent requests should be retrieved (default: False)
        :return: List of repair requests
        """
        if urgent_only:
            return [req for req in self.requests if req.urgent]
        return self.requests

    def display_requests(self, urgent_only=False):
        """
        Prints all repair requests to the console, optionally filtering for urgent requests.
        
        :param urgent_only: Boolean indicating if only urgent requests should be displayed (default: False)
        """
        requests_to_display = self.get_requests(urgent_only)
        if not requests_to_display:
            print("No repair requests found.")
        else:
            print("Repair Requests:")
            for req in requests_to_display:
                print(req)


# Example usage:
if __name__ == "__main__":
    try:
        # Create repair request manager
        manager = RepairRequestManager()

        # Add sample repair requests
        manager.add_request(RepairRequest(customer_name="Alice", appliance_type="Refrigerator", 
                                          brand="Samsung", issue_description="Not cooling", urgent=True))
        manager.add_request(RepairRequest(customer_name="Bob", appliance_type="Washing Machine", 
                                          brand="LG", issue_description="Leaking water"))
        manager.add_request(RepairRequest(customer_name="Charlie", appliance_type="Microwave", 
                                          brand="Panasonic", issue_description="Not heating", urgent=True))

        # Display all requests
        print("\nAll Requests:")
        manager.display_requests()

        # Display only urgent requests
        print("\nUrgent Requests:")
        manager.display_requests(urgent_only=True)
    except Exception as e:
        # Catch and display any unexpected errors
        print(f"An error occurred: {e}")
```
