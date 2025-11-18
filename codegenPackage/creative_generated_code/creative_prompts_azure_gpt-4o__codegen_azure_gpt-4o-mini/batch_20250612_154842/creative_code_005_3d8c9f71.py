"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Write a script to simulate booking services on the Swell Creative Management website, including selecting services like packaging design or experiential marketing.
Generated: DETERMINISTIC_3d8c9f71e5bb03ae
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Service:
    """Represents a service offered by Swell Creative Management."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Booking:
    """Handles the booking of services."""
    
    def __init__(self):
        self.available_services = []
        self.selected_services = []

    def add_service(self, service):
        """Adds a service to the list of available services."""
        if isinstance(service, Service):
            self.available_services.append(service)
        else:
            raise ValueError("Only Service instances can be added.")

    def select_service(self, service_name):
        """Selects a service for booking based on the service name."""
        for service in self.available_services:
            if service.name.lower() == service_name.lower():
                self.selected_services.append(service)
                return
        raise ValueError(f"Service '{service_name}' not found in available services.")

    def calculate_total(self):
        """Calculates the total cost of the selected services."""
        return sum(service.price for service in self.selected_services)

    def confirm_booking(self):
        """Confirms the booking and returns a summary."""
        if not self.selected_services:
            raise RuntimeError("No services selected for booking.")
        
        total_cost = self.calculate_total()
        summary = {
            "services": [str(service) for service in self.selected_services],
            "total_cost": total_cost
        }
        return json.dumps(summary, indent=4)

def main():
    """Main function to simulate booking services."""
    try:
        booking = Booking()
        
        # Adding available services
        booking.add_service(Service("Packaging Design", 1500))
        booking.add_service(Service("Experiential Marketing", 3000))
        
        # Simulating user selecting services
        booking.select_service("Packaging Design")
        booking.select_service("Experiential Marketing")
        
        # Confirming the booking
        booking_summary = booking.confirm_booking()
        print("Booking Confirmed:\n", booking_summary)

    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
