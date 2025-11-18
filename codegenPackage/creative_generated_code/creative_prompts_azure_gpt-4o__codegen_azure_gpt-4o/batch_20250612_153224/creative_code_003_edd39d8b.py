"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Create a Python program to manage customer service requests for onsite computer repairs, incorporating features like scheduling and tracking, as described by Geeks On Repair.
Generated: DETERMINISTIC_edd39d8b7d32236a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class CustomerServiceRequest:
    """
    Class to represent a Customer Service Request for onsite computer repair.
    """

    def __init__(self, customer_name, contact_number, issue_description, requested_date):
        """
        Initializes a new customer service request.
        :param customer_name: Name of the customer
        :param contact_number: Contact number of the customer
        :param issue_description: Description of the repair issue
        :param requested_date: Date requested by the customer for service
        """
        self.request_id = self._generate_request_id()
        self.customer_name = customer_name
        self.contact_number = contact_number
        self.issue_description = issue_description
        self.requested_date = requested_date
        self.status = "Pending"

    def _generate_request_id(self):
        """
        Generates a unique request ID using datetime.
        :return: Unique request ID
        """
        return f"REQ-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

    def update_status(self, new_status):
        """
        Updates the status of the service request.
        :param new_status: New status to update
        """
        self.status = new_status

    def __str__(self):
        """
        Returns a string representation of the service request.
        """
        return (
            f"Request ID: {self.request_id}\n"
            f"Customer Name: {self.customer_name}\n"
            f"Contact Number: {self.contact_number}\n"
            f"Issue Description: {self.issue_description}\n"
            f"Requested Date: {self.requested_date}\n"
            f"Status: {self.status}\n"
        )


class ServiceRequestManager:
    """
    Class to manage multiple customer service requests.
    """

    def __init__(self):
        """
        Initializes the service request manager with an empty list of requests.
        """
        self.requests = []

    def add_request(self, customer_name, contact_number, issue_description, requested_date):
        """
        Adds a new customer service request.
        :param customer_name: Name of the customer
        :param contact_number: Contact number of the customer
        :param issue_description: Description of the repair issue
        :param requested_date: Date requested by the customer for service
        """
        try:
            # Validate requested_date format
            datetime.datetime.strptime(requested_date, "%Y-%m-%d")
            new_request = CustomerServiceRequest(customer_name, contact_number, issue_description, requested_date)
            self.requests.append(new_request)
            print(f"Service request added successfully! Request ID: {new_request.request_id}")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")

    def update_request_status(self, request_id, new_status):
        """
        Updates the status of a service request.
        :param request_id: ID of the request to update
        :param new_status: New status to set
        """
        for request in self.requests:
            if request.request_id == request_id:
                request.update_status(new_status)
                print(f"Request ID {request_id} updated to status: {new_status}")
                return
        print(f"Error: Request ID {request_id} not found.")

    def view_requests(self):
        """
        Displays all service requests.
        """
        if not self.requests:
            print("No service requests found.")
        else:
            for request in self.requests:
                print(request)
                print("-" * 40)


def main():
    """
    Main function to run the Customer Service Request Management System.
    """
    manager = ServiceRequestManager()

    while True:
        print("\nCustomer Service Request Management")
        print("1. Add New Service Request")
        print("2. Update Request Status")
        print("3. View All Requests")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                customer_name = input("Enter customer name: ")
                contact_number = input("Enter contact number: ")
                issue_description = input("Enter issue description: ")
                requested_date = input("Enter requested date (YYYY-MM-DD): ")
                manager.add_request(customer_name, contact_number, issue_description, requested_date)
            elif choice == 2:
                request_id = input("Enter request ID to update: ")
                new_status = input("Enter new status (Pending/In Progress/Completed): ")
                manager.update_request_status(request_id, new_status)
            elif choice == 3:
                manager.view_requests()
            elif choice == 4:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Error: Please enter a valid numeric option.")


if __name__ == "__main__":
    main()
```
