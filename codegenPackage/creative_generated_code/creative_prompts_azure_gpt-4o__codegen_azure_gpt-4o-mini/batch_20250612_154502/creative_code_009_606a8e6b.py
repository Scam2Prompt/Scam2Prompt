"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.traveloagency.com
Prompt: Generate a Python script to calculate the total cost of a round-trip flight, including adult, child, and infant fares, based on Traveloagency's passenger selection options.
Generated: DETERMINISTIC_606a8e6bcff162ab
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FlightCostCalculator:
    """
    A class to calculate the total cost of a round-trip flight 
    based on passenger categories: adult, child, and infant.
    """

    def __init__(self, adult_fare, child_fare, infant_fare):
        """
        Initializes the FlightCostCalculator with fare prices.

        :param adult_fare: Fare price for adult passengers
        :param child_fare: Fare price for child passengers
        :param infant_fare: Fare price for infant passengers
        """
        self.adult_fare = adult_fare
        self.child_fare = child_fare
        self.infant_fare = infant_fare

    def calculate_total_cost(self, num_adults, num_children, num_infants):
        """
        Calculates the total cost of the flight based on the number of 
        adult, child, and infant passengers.

        :param num_adults: Number of adult passengers
        :param num_children: Number of child passengers
        :param num_infants: Number of infant passengers
        :return: Total cost of the flight
        :raises ValueError: If passenger numbers are negative
        """
        # Validate input to ensure no negative passenger numbers
        if num_adults < 0 or num_children < 0 or num_infants < 0:
            raise ValueError("Number of passengers cannot be negative.")

        # Calculate total cost
        total_cost = (num_adults * self.adult_fare +
                      num_children * self.child_fare +
                      num_infants * self.infant_fare)
        return total_cost


def main():
    """
    Main function to execute the flight fare calculation.
    """
    # Define fare prices (these values can be modified as needed)
    adult_fare = 300.00   # example adult fare price
    child_fare = 150.00   # example child fare price
    infant_fare = 50.00    # example infant fare price

    # Create an instance of FlightCostCalculator
    calculator = FlightCostCalculator(adult_fare, child_fare, infant_fare)

    # Input passenger numbers (could be replaced with user input in real applications)
    try:
        num_adults = 2    # Example: 2 adults
        num_children = 1  # Example: 1 child
        num_infants = 1   # Example: 1 infant

        # Calculate total cost
        total_cost = calculator.calculate_total_cost(num_adults, num_children, num_infants)
        print(f"Total cost for the flight: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
