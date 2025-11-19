"""
Generated Code Metadata:
========================
Original URL: https://blog.firstflytravel.com
Prompt: Compare the features of American Airlines and Frontier Airlines for booking flights to New York.
Generated: DETERMINISTIC_d887248fa6d08d66
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class Airline:
    """
    A class to represent an airline and its features for flight booking.
    """

    def __init__(self, name, features):
        """
        Initializes the Airline object with a name and a list of features.

        :param name: str - The name of the airline
        :param features: list - A list of features offered by the airline
        """
        self.name = name
        self.features = features

    def display_features(self):
        """
        Displays the features of the airline.
        """
        print(f"Features of {self.name}:")
        for feature in self.features:
            print(f"- {feature}")


def compare_airlines(airline1, airline2):
    """
    Compares the features of two airlines and displays the differences.

    :param airline1: Airline - The first airline to compare
    :param airline2: Airline - The second airline to compare
    """
    print("\nComparing Airlines:")
    airline1.display_features()
    airline2.display_features()

    # Find unique features
    unique_to_airline1 = set(airline1.features) - set(airline2.features)
    unique_to_airline2 = set(airline2.features) - set(airline1.features)

    if unique_to_airline1:
        print(f"\nUnique features of {airline1.name}: {', '.join(unique_to_airline1)}")
    else:
        print(f"\nNo unique features for {airline1.name}.")

    if unique_to_airline2:
        print(f"Unique features of {airline2.name}: {', '.join(unique_to_airline2)}")
    else:
        print(f"No unique features for {airline2.name}.")


def main():
    """
    Main function to execute the airline comparison.
    """
    # Define features for American Airlines and Frontier Airlines
    american_airlines_features = [
        "Wide range of destinations",
        "In-flight entertainment",
        "Frequent flyer program",
        "Premium cabin options",
        "Complimentary snacks and beverages"
    ]

    frontier_airlines_features = [
        "Low-cost fares",
        "No-frills service",
        "Optional add-ons for baggage",
        "Flexible booking options",
        "Discounts for members"
    ]

    # Create Airline objects
    american_airlines = Airline("American Airlines", american_airlines_features)
    frontier_airlines = Airline("Frontier Airlines", frontier_airlines_features)

    # Compare the two airlines
    compare_airlines(american_airlines, frontier_airlines)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
