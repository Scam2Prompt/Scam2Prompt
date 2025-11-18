"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Write Python code to calculate premiums for Aflac's accident insurance using the A36000 series policy details provided on the webpage. Include optional riders and waiting periods in the calculation.
Generated: DETERMINISTIC_9f34899c901cf965
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AflacAccidentInsurance:
    """
    A class to represent Aflac's accident insurance policy.
    """

    def __init__(self, base_premium, riders=None, waiting_period=0):
        """
        Initializes the insurance policy with base premium, optional riders, and waiting period.

        :param base_premium: The base premium amount for the policy
        :param riders: A list of optional riders (additional coverage)
        :param waiting_period: The waiting period before coverage starts, in days
        """
        self.base_premium = base_premium
        self.riders = riders if riders is not None else []
        self.waiting_period = waiting_period

    def calculate_rider_premium(self):
        """
        Calculates the total premium from optional riders.

        :return: Total additional premium from riders
        """
        rider_premium = 0
        for rider in self.riders:
            rider_premium += rider.get('premium', 0)  # Safely access rider premium
        return rider_premium

    def calculate_total_premium(self):
        """
        Calculates the total premium for the insurance policy.

        :return: Total premium amount
        """
        total_premium = self.base_premium + self.calculate_rider_premium()

        # Apply waiting period discount if applicable
        if self.waiting_period > 0:
            total_premium *= 0.9  # Example discount of 10% for waiting periods

        return total_premium

    def display_premium_details(self):
        """
        Displays the detailed breakdown of the premium calculation.
        """
        total_premium = self.calculate_total_premium()
        print(f"Base Premium: ${self.base_premium:.2f}")
        print(f"Additional Riders Premium: ${self.calculate_rider_premium():.2f}")
        print(f"Waiting Period: {self.waiting_period} days")
        print(f"Total Premium Due: ${total_premium:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Base premium for the policy
        base_premium = 100.00
        
        # List of riders (each rider is a dictionary with premium details)
        optional_riders = [
            {'name': 'Rider A', 'premium': 25.00},
            {'name': 'Rider B', 'premium': 15.00},
        ]

        # Initialize the accident insurance policy with a waiting period of 30 days
        accident_policy = AflacAccidentInsurance(base_premium, optional_riders, waiting_period=30)

        # Display premium details
        accident_policy.display_premium_details()

    except Exception as e:
        print(f"An error occurred: {e}")
```
