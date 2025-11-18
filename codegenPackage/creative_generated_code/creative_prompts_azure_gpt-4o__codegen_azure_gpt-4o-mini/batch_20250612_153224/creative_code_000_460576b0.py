"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Write a Python script to calculate the cost of consulting services for architectural projects, factoring in additional services beyond the initial agreement as described by TWM Associates.
Generated: DETERMINISTIC_460576b00c7d6969
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConsultingServiceCalculator:
    """
    A class to calculate the total cost of consulting services for architectural projects.
    """

    def __init__(self, base_rate, initial_hours):
        """
        Initializes the calculator with a base rate and initial hours for the project.

        :param base_rate: The hourly rate charged for consulting services.
        :param initial_hours: The number of hours included in the initial agreement.
        """
        self.base_rate = base_rate
        self.initial_hours = initial_hours
        self.additional_services = {}  # Dictionary to store additional services and their hours

    def add_additional_service(self, service_name, hours):
        """
        Adds an additional service to the calculation.

        :param service_name: A string representing the name of the additional service.
        :param hours: The number of hours required for the additional service.
        :raises ValueError: If hours are negative or zero.
        """
        if hours <= 0:
            raise ValueError("Hours for additional services must be greater than zero.")
        self.additional_services[service_name] = hours

    def calculate_total_cost(self):
        """
        Calculates the total cost of the consulting services including additional services.

        :return: The total cost of the consulting services.
        """
        try:
            total_hours = self.initial_hours + sum(self.additional_services.values())
            total_cost = total_hours * self.base_rate
            return total_cost
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating total cost: {e}")

    def display_cost_breakdown(self):
        """
        Displays the breakdown of the costs including base, additional services, and total.

        :return: A string representation of the cost breakdown.
        """
        breakdown = f"Base rate: ${self.base_rate}/hour\n"
        breakdown += f"Initial hours: {self.initial_hours} hours\n"
        breakdown += f"Additional services:\n"

        for service, hours in self.additional_services.items():
            breakdown += f"  - {service}: {hours} hours\n"

        total_cost = self.calculate_total_cost()
        breakdown += f"Total cost: ${total_cost:.2f}\n"
        return breakdown


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize the calculator with base rate and initial hours
        calculator = ConsultingServiceCalculator(base_rate=150.00, initial_hours=10)

        # Add additional services as needed
        calculator.add_additional_service("Site Analysis", 5)
        calculator.add_additional_service("Project Management", 8)

        # Display the cost breakdown
        print(calculator.display_cost_breakdown())
    except Exception as e:
        print(f"Error: {e}")
```
