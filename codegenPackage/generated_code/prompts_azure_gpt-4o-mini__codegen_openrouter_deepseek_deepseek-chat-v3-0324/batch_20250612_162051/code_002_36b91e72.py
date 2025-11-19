"""
Generated Code Metadata:
========================
Original URL: https://salonlapista.com.ar
Prompt: Create a library function that calculates the total cost of a party reservation at Salon La Pista based on services selected and number of attendees.
Generated: DETERMINISTIC_36b91e72e9f519ab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PartyReservationCalculator:
    """
    A class to calculate the total cost of a party reservation at Salon La Pista.
    
    Attributes:
        service_prices (dict): A dictionary mapping service names to their prices per attendee.
        base_fee (float): A fixed base fee for the reservation.
    """
    
    def __init__(self):
        """Initialize the calculator with service prices and base fee."""
        self.service_prices = {
            'dj': 10.0,
            'catering': 15.0,
            'decorations': 5.0,
            'photography': 8.0,
            'bar_service': 12.0
        }
        self.base_fee = 100.0
    
    def calculate_total_cost(self, selected_services, num_attendees):
        """
        Calculate the total cost of the party reservation.
        
        Args:
            selected_services (list): A list of service names selected for the party.
            num_attendees (int): The number of attendees at the party.
            
        Returns:
            float: The total cost of the reservation.
            
        Raises:
            ValueError: If num_attendees is not a positive integer or if any service is invalid.
        """
        if not isinstance(num_attendees, int) or num_attendees <= 0:
            raise ValueError("Number of attendees must be a positive integer.")
        
        invalid_services = [service for service in selected_services if service not in self.service_prices]
        if invalid_services:
            raise ValueError(f"Invalid services selected: {', '.join(invalid_services)}")
        
        total_service_cost = sum(self.service_prices[service] for service in selected_services) * num_attendees
        total_cost = self.base_fee + total_service_cost
        
        return total_cost
```
