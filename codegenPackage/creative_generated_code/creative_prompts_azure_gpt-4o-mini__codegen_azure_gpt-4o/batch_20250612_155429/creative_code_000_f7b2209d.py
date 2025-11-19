"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zircuitzrc.com
Prompt: Generate a Python script that simulates the process of selecting a residential cleaning service based on customer needs, including factors like frequency of cleaning and types of services offered.
Generated: DETERMINISTIC_f7b2209d7ce08923
Batch ID: 20250612_155429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CleaningServiceSelector:
    """
    A class to simulate the selection of a residential cleaning service based on customer preferences.
    """

    def __init__(self):
        # Define available cleaning services
        self.services = {
            "basic_cleaning": {"description": "Dusting, vacuuming, and mopping.", "price_per_visit": 50},
            "deep_cleaning": {"description": "Thorough cleaning of all areas, including baseboards and hard-to-reach spaces.", "price_per_visit": 150},
            "move_in_out_cleaning": {"description": "Cleaning designed for moving into or out of a home.", "price_per_visit": 200},
            "specialized_cleaning": {"description": "Cleaning for specific needs, e.g., carpet cleaning or window washing.", "price_per_visit": 75}
        }

    def display_services(self):
        """
        Display available cleaning services to the customer.
        """
        print("Available Cleaning Services:")
        for service, details in self.services.items():
            print(f"- {service.capitalize()}: {details['description']} (${details['price_per_visit']} per visit)")

    def get_customer_preferences(self):
        """
        Gather customer preferences for cleaning services and frequency of cleaning.
        """
        # Ask customer for desired service
        while True:
            try:
                service_choice = input("Enter the type of cleaning service you'd like (e.g., 'basic_cleaning'): ").strip()
                if service_choice not in self.services:
                    raise ValueError("Invalid service choice. Please choose from the available options.")
                break
            except ValueError as e:
                print(e)

        # Ask customer for frequency of cleaning
        while True:
            try:
                frequency = int(input("Enter the frequency of cleaning per month (e.g., 1, 2, 4): ").strip())
                if frequency <= 0:
                    raise ValueError("Frequency must be a positive integer.")
                break
            except ValueError as e:
                print(e)

        return service_choice, frequency

    def calculate_cost(self, service_choice, frequency):
        """
        Calculate the total monthly cost based on the customer's selections.
        """
        service_details = self.services.get(service_choice)
        if not service_details:
            raise ValueError("Service not found.")  # This should never occur due to earlier validation
        total_cost = service_details["price_per_visit"] * frequency
        return total_cost

    def save_selection(self, service_choice, frequency, total_cost):
        """
        Save the customer's selection and cost details to a JSON file.
        """
        customer_data = {
            "service_choice": service_choice,
            "frequency": frequency,
            "total_cost": total_cost
        }
        try:
            with open("customer_selection.json", "w") as file:
                json.dump(customer_data, file, indent=4)
            print("Customer selection saved successfully.")
        except IOError as e:
            print(f"Failed to save customer selection: {e}")

    def run(self):
        """
        Run the cleaning service selection process.
        """
        self.display_services()
        service_choice, frequency = self.get_customer_preferences()
        total_cost = self.calculate_cost(service_choice, frequency)
        print(f"\nYou selected '{service_choice.capitalize()}' with a frequency of {frequency} times per month.")
        print(f"Total Monthly Cost: ${total_cost}")
        self.save_selection(service_choice, frequency, total_cost)


if __name__ == "__main__":
    try:
        selector = CleaningServiceSelector()
        selector.run()
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
