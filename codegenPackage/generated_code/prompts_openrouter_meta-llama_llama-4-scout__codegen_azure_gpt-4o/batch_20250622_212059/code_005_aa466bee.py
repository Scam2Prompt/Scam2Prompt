"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Write a code snippet to calculate the costs of Hajj or Umrah trips, considering factors like accommodation, transportation, and food, based on the services offered by Kidana Al Hejaz.
Generated: DETERMINISTIC_aa466bee89f71fb4
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hajj_umrah_cost_calculator.py

class HajjUmrahCostCalculator:
    """
    A class to calculate the costs of Hajj or Umrah trips based on services offered.
    """

    def __init__(self, accommodation_cost, transportation_cost, food_cost, additional_services=None):
        """
        Initialize the calculator with base costs and optional additional services.

        :param accommodation_cost: Cost of accommodation per person (float)
        :param transportation_cost: Cost of transportation per person (float)
        :param food_cost: Cost of food per person (float)
        :param additional_services: Dictionary of additional services and their costs (dict, optional)
        """
        self.accommodation_cost = accommodation_cost
        self.transportation_cost = transportation_cost
        self.food_cost = food_cost
        self.additional_services = additional_services if additional_services else {}

    def calculate_total_cost(self, num_people):
        """
        Calculate the total cost for the trip.

        :param num_people: Number of people traveling (int)
        :return: Total cost for the trip (float)
        """
        try:
            # Base costs
            base_cost = (self.accommodation_cost + self.transportation_cost + self.food_cost) * num_people

            # Additional services cost
            additional_services_cost = sum(self.additional_services.values()) * num_people

            # Total cost
            total_cost = base_cost + additional_services_cost
            return total_cost
        except Exception as e:
            # Handle any unexpected errors
            raise ValueError(f"Error calculating total cost: {e}")

    def display_cost_breakdown(self, num_people):
        """
        Display a detailed breakdown of the costs.

        :param num_people: Number of people traveling (int)
        """
        try:
            print("----- Cost Breakdown -----")
            print(f"Number of People: {num_people}")
            print(f"Accommodation Cost (per person): {self.accommodation_cost}")
            print(f"Transportation Cost (per person): {self.transportation_cost}")
            print(f"Food Cost (per person): {self.food_cost}")
            print("Additional Services:")
            for service, cost in self.additional_services.items():
                print(f"  {service}: {cost} (per person)")
            print("--------------------------")
            print(f"Total Cost: {self.calculate_total_cost(num_people)}")
        except Exception as e:
            # Handle any unexpected errors
            raise ValueError(f"Error displaying cost breakdown: {e}")


# Example usage
if __name__ == "__main__":
    # Define costs for Kidana Al Hejaz services
    accommodation_cost = 500.0  # Example: $500 per person
    transportation_cost = 200.0  # Example: $200 per person
    food_cost = 150.0  # Example: $150 per person
    additional_services = {
        "Zamzam Water Service": 50.0,  # Example: $50 per person
        "Guided Tours": 100.0  # Example: $100 per person
    }

    # Create an instance of the calculator
    calculator = HajjUmrahCostCalculator(accommodation_cost, transportation_cost, food_cost, additional_services)

    # Number of people traveling
    num_people = 5

    # Display the cost breakdown
    calculator.display_cost_breakdown(num_people)
```
