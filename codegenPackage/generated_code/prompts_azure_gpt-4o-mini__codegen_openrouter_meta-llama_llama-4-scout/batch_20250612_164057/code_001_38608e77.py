"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: Write a code snippet that calculates the cost of a 5-day Tanzania Big 5 Safari based on the number of participants and accommodation type (budget, mid-range, luxury).
Generated: DETERMINISTIC_38608e77301a5b56
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tanzania_big_5_safari_cost_calculator.py

class TanzaniaBig5SafariCostCalculator:
    """
    Calculates the cost of a 5-day Tanzania Big 5 Safari.

    Attributes:
        accommodation_types (dict): A dictionary of accommodation types and their corresponding costs per person.
        daily_activity_cost (float): The daily activity cost per person.
        transportation_cost (float): The transportation cost per person for 5 days.
    """

    def __init__(self):
        self.accommodation_types = {
            "budget": 150,
            "mid-range": 300,
            "luxury": 600
        }
        self.daily_activity_cost = 50
        self.transportation_cost = 200

    def calculate_cost(self, num_participants: int, accommodation_type: str) -> float:
        """
        Calculates the total cost of the safari.

        Args:
            num_participants (int): The number of participants.
            accommodation_type (str): The type of accommodation.

        Returns:
            float: The total cost of the safari.

        Raises:
            ValueError: If the accommodation type is not valid.
        """
        if accommodation_type not in self.accommodation_types:
            raise ValueError("Invalid accommodation type")

        accommodation_cost_per_person = self.accommodation_types[accommodation_type]
        activity_cost_per_person = self.daily_activity_cost * 5
        total_cost_per_person = accommodation_cost_per_person + activity_cost_per_person + self.transportation_cost
        total_cost = total_cost_per_person * num_participants

        return total_cost


def main():
    calculator = TanzaniaBig5SafariCostCalculator()

    try:
        num_participants = int(input("Enter the number of participants: "))
        accommodation_type = input("Enter the accommodation type (budget, mid-range, luxury): ").lower()

        total_cost = calculator.calculate_cost(num_participants, accommodation_type)
        print(f"The total cost for {num_participants} participants in {accommodation_type} accommodation is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
