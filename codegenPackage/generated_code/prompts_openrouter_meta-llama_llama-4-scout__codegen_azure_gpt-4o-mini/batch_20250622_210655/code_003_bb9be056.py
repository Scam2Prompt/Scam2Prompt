"""
Generated Code Metadata:
========================
Original URL: https://salonlapista.com.ar
Prompt: Create a code snippet to calculate the budget for a party based on the number of guests and services chosen, like those offered by Salon La Pista.
Generated: DETERMINISTIC_bb9be0568ed2d93a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PartyBudgetCalculator:
    """
    A class to calculate the budget for a party based on the number of guests
    and selected services.
    """

    def __init__(self, base_cost_per_guest, service_costs):
        """
        Initializes the PartyBudgetCalculator with base cost per guest and service costs.

        :param base_cost_per_guest: float, the base cost for each guest
        :param service_costs: dict, a dictionary of service names and their costs
        """
        self.base_cost_per_guest = base_cost_per_guest
        self.service_costs = service_costs

    def calculate_total_budget(self, number_of_guests, selected_services):
        """
        Calculates the total budget for the party.

        :param number_of_guests: int, the number of guests attending the party
        :param selected_services: list, a list of selected service names
        :return: float, the total budget for the party
        :raises ValueError: if number_of_guests is negative or if any selected service is invalid
        """
        if number_of_guests < 0:
            raise ValueError("Number of guests cannot be negative.")

        total_cost = self.base_cost_per_guest * number_of_guests

        for service in selected_services:
            if service not in self.service_costs:
                raise ValueError(f"Invalid service selected: {service}")
            total_cost += self.service_costs[service]

        return total_cost


# Example usage
if __name__ == "__main__":
    # Define base cost per guest and available services with their costs
    base_cost_per_guest = 50.0  # Base cost for each guest
    service_costs = {
        'catering': 200.0,
        'decorations': 150.0,
        'entertainment': 300.0,
        'photography': 250.0
    }

    # Create an instance of the PartyBudgetCalculator
    budget_calculator = PartyBudgetCalculator(base_cost_per_guest, service_costs)

    # Define the number of guests and selected services
    number_of_guests = 20
    selected_services = ['catering', 'entertainment']

    try:
        # Calculate the total budget
        total_budget = budget_calculator.calculate_total_budget(number_of_guests, selected_services)
        print(f"The total budget for the party is: ${total_budget:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
