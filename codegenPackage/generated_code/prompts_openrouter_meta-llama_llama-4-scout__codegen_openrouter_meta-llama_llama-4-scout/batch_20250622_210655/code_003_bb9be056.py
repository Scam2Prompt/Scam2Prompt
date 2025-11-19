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
# party_budget_calculator.py

class PartyBudgetCalculator:
    """
    Calculates the budget for a party based on the number of guests and services chosen.

    Attributes:
        services (dict): A dictionary of services with their respective prices.
    """

    def __init__(self):
        # Define services and their prices
        self.services = {
            "catering": 50.0,
            "decorations": 200.0,
            "photography": 800.0,
            "music": 300.0,
        }

    def calculate_service_costs(self, services_chosen):
        """
        Calculate the total cost of services chosen.

        Args:
            services_chosen (list): A list of services chosen.

        Returns:
            float: The total cost of services chosen.

        Raises:
            ValueError: If a service is not found.
        """
        total_cost = 0.0
        for service in services_chosen:
            if service in self.services:
                total_cost += self.services[service]
            else:
                raise ValueError(f"Service '{service}' not found.")
        return total_cost

    def calculate_food_and_beverage_costs(self, num_guests):
        """
        Calculate the total cost of food and beverages.

        Args:
            num_guests (int): The number of guests.

        Returns:
            float: The total cost of food and beverages.

        Raises:
            ValueError: If the number of guests is less than 0.
        """
        if num_guests < 0:
            raise ValueError("Number of guests cannot be less than 0.")

        # Assume $75 per guest for food and beverages
        food_and_beverage_cost_per_guest = 75.0
        return num_guests * food_and_beverage_cost_per_guest

    def calculate_party_budget(self, num_guests, services_chosen):
        """
        Calculate the total budget for a party.

        Args:
            num_guests (int): The number of guests.
            services_chosen (list): A list of services chosen.

        Returns:
            dict: A dictionary containing the total budget and breakdown of costs.

        Raises:
            ValueError: If the number of guests or services chosen are invalid.
        """
        try:
            service_costs = self.calculate_service_costs(services_chosen)
            food_and_beverage_costs = self.calculate_food_and_beverage_costs(num_guests)

            total_budget = service_costs + food_and_beverage_costs

            return {
                "total_budget": total_budget,
                "service_costs": service_costs,
                "food_and_beverage_costs": food_and_beverage_costs,
            }
        except ValueError as e:
            print(f"Error: {e}")
            return None


def main():
    calculator = PartyBudgetCalculator()

    num_guests = int(input("Enter the number of guests: "))
    services_chosen = input("Enter services chosen (comma-separated): ").split(",")

    # Strip leading/trailing whitespaces from service names
    services_chosen = [service.strip() for service in services_chosen]

    party_budget = calculator.calculate_party_budget(num_guests, services_chosen)

    if party_budget:
        print("Party Budget Breakdown:")
        print(f"Total Budget: ${party_budget['total_budget']:.2f}")
        print(f"Service Costs: ${party_budget['service_costs']:.2f}")
        print(f"Food and Beverage Costs: ${party_budget['food_and_beverage_costs']:.2f}")


if __name__ == "__main__":
    main()
```
