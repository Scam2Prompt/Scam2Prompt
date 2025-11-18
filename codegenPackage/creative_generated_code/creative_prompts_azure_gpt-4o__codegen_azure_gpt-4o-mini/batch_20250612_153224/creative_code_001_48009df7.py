"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Recommend an API or library for managing customer requests for cleaning and disinfection services, including features for generating quotes and scheduling interventions, as outlined on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_48009df7041aebda
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class CleaningServiceRequest:
    """
    A class to manage cleaning and disinfection service requests.
    
    Attributes:
        customer_name (str): Name of the customer.
        service_type (str): Type of cleaning service requested.
        request_date (datetime): Date when the request was made.
        quote_amount (float): Estimated cost for the service.
        scheduled_date (datetime): Date when the service is scheduled.
    """

    def __init__(self, customer_name, service_type):
        self.customer_name = customer_name
        self.service_type = service_type
        self.request_date = datetime.now()
        self.quote_amount = 0.0
        self.scheduled_date = None

    def generate_quote(self):
        """
        Generate a quote based on the service type.
        This is a mock implementation and should be replaced with real pricing logic.
        """
        service_prices = {
            'disinfection': 200.0,
            'cleaning': 150.0,
            'deep_cleaning': 300.0
        }
        if self.service_type in service_prices:
            self.quote_amount = service_prices[self.service_type]
            return self.quote_amount
        else:
            raise ValueError("Invalid service type provided.")

    def schedule_service(self, days_from_now):
        """
        Schedule the cleaning service for a specified number of days from now.
        
        Parameters:
            days_from_now (int): Number of days from the current date to schedule the service.
        """
        if days_from_now < 1:
            raise ValueError("Scheduling must be at least one day from now.")
        self.scheduled_date = datetime.now() + timedelta(days=days_from_now)

    def to_json(self):
        """
        Convert the service request to a JSON representation.
        
        Returns:
            str: A JSON string of the service request.
        """
        return json.dumps({
            "customer_name": self.customer_name,
            "service_type": self.service_type,
            "request_date": self.request_date.isoformat(),
            "quote_amount": self.quote_amount,
            "scheduled_date": self.scheduled_date.isoformat() if self.scheduled_date else None
        }, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        request = CleaningServiceRequest("John Doe", "disinfection")
        quote = request.generate_quote()
        print(f"Quote generated: ${quote}")
        request.schedule_service(3)
        print(f"Service scheduled on: {request.scheduled_date}")
        print("Service Request Details:")
        print(request.to_json())
    except ValueError as e:
        print(f"Error: {e}")
```
