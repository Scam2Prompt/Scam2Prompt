"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Develop a code for a basic CRM system to manage customer information and service requests for a business offering installation, reparación, and mantenimiento of equipos de osmosis inversa in Murcia.
Generated: DETERMINISTIC_13d36bce5f552e17
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crm_system.py

class Customer:
    """Represents a customer in the CRM system."""

    def __init__(self, customer_id, name, email, phone):
        """
        Initializes a Customer object.

        Args:
            customer_id (int): Unique identifier for the customer.
            name (str): Customer name.
            email (str): Customer email.
            phone (str): Customer phone number.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer {self.customer_id}: {self.name}, {self.email}, {self.phone}"


class ServiceRequest:
    """Represents a service request in the CRM system."""

    def __init__(self, request_id, customer_id, service_type, description):
        """
        Initializes a ServiceRequest object.

        Args:
            request_id (int): Unique identifier for the service request.
            customer_id (int): Foreign key referencing the Customer object.
            service_type (str): Type of service requested (installation, reparación, or mantenimiento).
            description (str): Description of the service request.
        """
        self.request_id = request_id
        self.customer_id = customer_id
        self.service_type = service_type
        self.description = description

    def __str__(self):
        return f"Service Request {self.request_id}: {self.service_type} for Customer {self.customer_id}"


class CRMSystem:
    """Represents the CRM system."""

    def __init__(self):
        """
        Initializes the CRM system with empty customer and service request lists.
        """
        self.customers = []
        self.service_requests = []

    def add_customer(self, customer):
        """
        Adds a customer to the CRM system.

        Args:
            customer (Customer): Customer object to add.

        Raises:
            ValueError: If a customer with the same ID already exists.
        """
        if any(c.customer_id == customer.customer_id for c in self.customers):
            raise ValueError("Customer with the same ID already exists")
        self.customers.append(customer)

    def add_service_request(self, service_request):
        """
        Adds a service request to the CRM system.

        Args:
            service_request (ServiceRequest): Service request object to add.

        Raises:
            ValueError: If a service request with the same ID already exists.
        """
        if any(sr.request_id == service_request.request_id for sr in self.service_requests):
            raise ValueError("Service request with the same ID already exists")
        self.service_requests.append(service_request)

    def get_customer(self, customer_id):
        """
        Retrieves a customer by ID.

        Args:
            customer_id (int): ID of the customer to retrieve.

        Returns:
            Customer: Customer object if found, None otherwise.
        """
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def get_service_requests(self, customer_id):
        """
        Retrieves all service requests for a customer.

        Args:
            customer_id (int): ID of the customer.

        Returns:
            list[ServiceRequest]: List of service requests for the customer.
        """
        return [sr for sr in self.service_requests if sr.customer_id == customer_id]


def main():
    crm = CRMSystem()

    # Create customers
    customer1 = Customer(1, "John Doe", "john.doe@example.com", "123456789")
    customer2 = Customer(2, "Jane Smith", "jane.smith@example.com", "987654321")

    # Add customers to CRM system
    crm.add_customer(customer1)
    crm.add_customer(customer2)

    # Create service requests
    request1 = ServiceRequest(1, 1, "installation", "Install osmosis inversa equipment")
    request2 = ServiceRequest(2, 1, "reparación", "Repair osmosis inversa equipment")
    request3 = ServiceRequest(3, 2, "mantenimiento", "Perform maintenance on osmosis inversa equipment")

    # Add service requests to CRM system
    crm.add_service_request(request1)
    crm.add_service_request(request2)
    crm.add_service_request(request3)

    # Retrieve customer and service requests
    customer = crm.get_customer(1)
    print(customer)
    service_requests = crm.get_service_requests(1)
    for request in service_requests:
        print(request)


if __name__ == "__main__":
    main()
```
