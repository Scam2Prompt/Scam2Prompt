"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salonlapista.com.ar
Prompt: Create a library function that calculates the total cost of a party reservation at Salon La Pista based on services selected and number of attendees.
Generated: DETERMINISTIC_36b91e72e9f519ab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PartyReservation:
    """Class to calculate the total cost of a party reservation at Salon La Pista."""

    def __init__(self):
        # Pricing for services per attendee
        self.service_prices = {
            "basic": 50.00,  # Basic service per attendee
            "premium": 100.00,  # Premium service per attendee
            "decor": 200.00,  # Decor service per event
            "entertainment": 300.00  # Entertainment service per event
        }

    def calculate_total_cost(self, num_attendees, services):
        """
        Calculate the total cost of the reservation.

        Args:
            num_attendees (int): Number of attendees for the party.
            services (list): List of services selected for the party.

        Returns:
            float: Total cost of the party reservation.

        Raises:
            ValueError: If num_attendees is less than 1 or if services is empty.
            KeyError: If an invalid service is provided.
        """

        # Validate input
        if num_attendees < 1:
            raise ValueError("Number of attendees must be at least 1.")
        
        if not services:
            raise ValueError("At least one service must be selected.")

        total_cost = 0.0

        # Calculate cost based on services selected
        for service in services:
            if service not in self.service_prices:
                raise KeyError(f"Invalid service selected: {service}")

            # Check if the service is charged per attendee or per event
            if service in ["basic", "premium"]:
                total_cost += self.service_prices[service] * num_attendees
            else:
                total_cost += self.service_prices[service]  # Charged per event

        return total_cost


if __name__ == "__main__":
    # Example usage
    reservation = PartyReservation()
    try:
        attendees = 10
        selected_services = ["basic", "decor", "entertainment"]
        total = reservation.calculate_total_cost(attendees, selected_services)
        print(f"Total cost for the party reservation: ${total:.2f}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
