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
# plumbing_service_request_system.py

class PlumbingService:
    """Represents a plumbing service."""

    def __init__(self, name, description, price):
        """
        Initializes a PlumbingService.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.
            price (float): The price of the service.
        """
        self.name = name
        self.description = description
        self.price = price

class PlumbingServiceRequestSystem:
    """Simulates a plumbing service request system."""

    def __init__(self):
        """
        Initializes a PlumbingServiceRequestSystem.

        Attributes:
            services (dict): A dictionary of available plumbing services.
        """
        self.services = {
            "1": PlumbingService("Drain Cleaning", "Clear clogs and clean drains.", 100.0),
            "2": PlumbingService("Gas Line Repairs", "Repair and replace gas lines.", 200.0),
            "3": PlumbingService("Leak Detection", "Detect and fix leaks.", 150.0),
            "4": PlumbingService("Toilet Installation", "Install new toilets.", 300.0),
        }

    def display_services(self):
        """
        Displays available plumbing services.
        """
        print("Available Services:")
        for key, service in self.services.items():
            print(f"{key}. {service.name}: {service.description} - ${service.price:.2f}")

    def request_service(self):
        """
        Allows users to select and request a plumbing service.

        Returns:
            tuple: The selected service and its price.
        """
        self.display_services()
        while True:
            choice = input("Enter the service number you'd like to request: ")
            if choice in self.services:
                selected_service = self.services[choice]
                print(f"\nYou've selected: {selected_service.name}")
                print(f"Description: {selected_service.description}")
                print(f"Price: ${selected_service.price:.2f}")
                confirm = input("Confirm request (yes/no): ")
                if confirm.lower() == "yes":
                    return selected_service, selected_service.price
                else:
                    print("Request cancelled.")
            else:
                print("Invalid service number. Please try again.")

    def process_payment(self, price):
        """
        Simulates payment processing.

        Args:
            price (float): The price of the service.

        Returns:
            bool: True if payment is successful, False otherwise.
        """
        try:
            payment_method = input("Enter payment method (cash/credit): ")
            if payment_method.lower() == "cash":
                print("Please pay in cash.")
                return True
            elif payment_method.lower() == "credit":
                card_number = input("Enter credit card number: ")
                expiration_date = input("Enter expiration date (MM/YYYY): ")
                # Simulate payment processing (replace with actual payment gateway)
                print("Payment processed successfully.")
                return True
            else:
                print("Invalid payment method.")
                return False
        except Exception as e:
            print(f"Error processing payment: {str(e)}")
            return False

def main():
    system = PlumbingServiceRequestSystem()
    selected_service, price = system.request_service()
    if system.process_payment(price):
        print(f"\nService requested: {selected_service.name}")
        print("Thank you for using our plumbing service!")
    else:
        print("Payment failed. Request cancelled.")

if __name__ == "__main__":
    main()
```
