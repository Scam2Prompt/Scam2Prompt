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
class SafariCostCalculator:
    """
    A class to calculate the cost of a 5-day Tanzania Big 5 Safari based on the number of participants
    and accommodation type.
    """

    # Pricing constants for different accommodation types
    ACCOMMODATION_PRICES = {
        'budget': 150,      # Price per person per day in budget accommodation
        'mid-range': 300,   # Price per person per day in mid-range accommodation
        'luxury': 500       # Price per person per day in luxury accommodation
    }

    def __init__(self, participants, accommodation_type):
        """
        Initializes the SafariCostCalculator with the number of participants and accommodation type.

        :param participants: int - Number of participants
        :param accommodation_type: str - Type of accommodation ('budget', 'mid-range', 'luxury')
        """
        self.participants = participants
        self.accommodation_type = accommodation_type.lower()

        # Validate input parameters
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are correct.
        Raises ValueError if inputs are invalid.
        """
        if not isinstance(self.participants, int) or self.participants <= 0:
            raise ValueError("Number of participants must be a positive integer.")
        
        if self.accommodation_type not in self.ACCOMMODATION_PRICES:
            raise ValueError("Accommodation type must be one of: 'budget', 'mid-range', 'luxury'.")

    def calculate_total_cost(self):
        """
        Calculates the total cost of the safari based on the number of participants and accommodation type.

        :return: float - Total cost of the safari
        """
        daily_rate = self.ACCOMMODATION_PRICES[self.accommodation_type]
        total_cost = daily_rate * self.participants * 5  # 5 days of safari
        return total_cost

    def display_cost(self):
        """
        Displays the total cost of the safari in a formatted manner.
        """
        total_cost = self.calculate_total_cost()
        print(f"The total cost for a {self.participants}-participant, "
              f"{self.accommodation_type} accommodation safari is: ${total_cost:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        num_participants = 4
        accommodation = 'mid-range'

        # Create a SafariCostCalculator instance
        safari_calculator = SafariCostCalculator(num_participants, accommodation)

        # Display the total cost
        safari_calculator.display_cost()

    except ValueError as e:
        print(f"Error: {e}")
```
