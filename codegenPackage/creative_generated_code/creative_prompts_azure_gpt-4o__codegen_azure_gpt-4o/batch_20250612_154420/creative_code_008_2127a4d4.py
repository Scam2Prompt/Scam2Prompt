"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Create a program that schedules 24/7 HVAC repair services, prioritizing Comfort Club members for front-of-the-line service, and generates invoices with no overtime charges for repairs.
Generated: DETERMINISTIC_2127a4d4833330ce
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid


class Customer:
    """
    Represents a customer. Tracks membership status and basic customer details.
    """
    def __init__(self, name, phone, is_comfort_club_member=False):
        self.id = str(uuid.uuid4())  # Unique customer ID
        self.name = name
        self.phone = phone
        self.is_comfort_club_member = is_comfort_club_member


class ServiceRequest:
    """
    Represents a service request for HVAC repair.
    """
    def __init__(self, customer, requested_datetime=None):
        self.id = str(uuid.uuid4())  # Unique service request ID
        self.customer = customer
        self.requested_datetime = requested_datetime or datetime.datetime.now()
        self.is_completed = False
        self.invoice_generated = False


class Invoice:
    """
    Represents an invoice for a completed service request.
    """
    def __init__(self, service_request):
        self.invoice_id = str(uuid.uuid4())  # Unique invoice ID
        self.service_request_id = service_request.id
        self.customer_id = service_request.customer.id
        self.date_generated = datetime.datetime.now()
        self.total_amount = self.calculate_total(service_request)
        self.contains_overtime_charges = False  # Comfort Club members don't pay overtime

    def calculate_total(self, service_request):
        # Example pricing logic:
        base_rate = 100
        if service_request.customer.is_comfort_club_member:
            # Comfort Club members receive prioritized service and no overtime charges
            return base_rate
        else:
            # Normal customers may incur overtime charges
            hour = service_request.requested_datetime.hour
            if hour < 8 or hour > 18:  # Overtime hours (before 8 AM or after 6 PM)
                self.contains_overtime_charges = True
                return base_rate + 50  # Add $50 for overtime
            return base_rate


class HVACRepairServiceScheduler:
    """
    Manages service scheduling and invoice generation.
    """
    def __init__(self):
        self.service_requests = []

    def add_service_request(self, customer):
        """
        Add a new service request to the scheduler.
        """
        service_request = ServiceRequest(customer)
        self.service_requests.append(service_request)
        # Prioritize Comfort Club members
        self.service_requests.sort(key=lambda req: not req.customer.is_comfort_club_member)
        print(f"Service request added: {service_request.id}")
        return service_request

    def complete_service_request(self, service_request_id):
        """
        Mark a service request as completed and generate an invoice.
        """
        service_request = next(
            (req for req in self.service_requests if req.id == service_request_id), None
        )
        if not service_request:
            raise ValueError("Service request not found.")
        if service_request.is_completed:
            raise ValueError("Service request is already completed.")

        service_request.is_completed = True
        invoice = Invoice(service_request)
        service_request.invoice_generated = True
        print(f"Service completed. Invoice generated: {invoice.invoice_id}")
        return invoice

    def list_pending_requests(self):
        """
        List all pending service requests.
        """
        return [req for req in self.service_requests if not req.is_completed]


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize scheduler
        scheduler = HVACRepairServiceScheduler()

        # Create customers
        customer1 = Customer("John Doe", "555-1234", is_comfort_club_member=True)
        customer2 = Customer("Jane Smith", "555-5678", is_comfort_club_member=False)

        # Add service requests
        scheduler.add_service_request(customer1)
        scheduler.add_service_request(customer2)

        # View pending requests
        pending_requests = scheduler.list_pending_requests()
        print(f"Pending requests: {[req.id for req in pending_requests]}")

        # Complete a service request
        invoice = scheduler.complete_service_request(pending_requests[0].id)
        print(f"Invoice details: ID {invoice.invoice_id}, Total ${invoice.total_amount}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
