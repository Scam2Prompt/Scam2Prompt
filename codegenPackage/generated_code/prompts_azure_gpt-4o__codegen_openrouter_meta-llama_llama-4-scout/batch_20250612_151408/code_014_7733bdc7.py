"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Write a Python program to simulate Engel cooler usage scenarios, such as camping trips or fishing expeditions, and recommend the best cooler model based on user needs.
Generated: DETERMINISTIC_7733bdc71ba3d740
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# engel_cooler_simulator.py

class EngelCooler:
    def __init__(self, model, capacity, ice_retention, price):
        """
        Initialize an Engel cooler model.

        Args:
            model (str): Cooler model name.
            capacity (float): Cooler capacity in quarts.
            ice_retention (int): Cooler ice retention in days.
            price (float): Cooler price.
        """
        self.model = model
        self.capacity = capacity
        self.ice_retention = ice_retention
        self.price = price

    def __str__(self):
        return f"{self.model}: {self.capacity}qt, {self.ice_retention} days ice retention, ${self.price:.2f}"


class CoolerSimulator:
    def __init__(self):
        self.cooler_models = [
            EngelCooler(" Engel MR40F-U1", 40, 7, 899.99),
            EngelCooler("Engel MR20F-U1", 20, 5, 499.99),
            EngelCooler("Engel MR60F-U1", 60, 10, 1299.99),
        ]

    def simulate_trip(self, trip_duration, required_capacity):
        """
        Simulate a trip and recommend the best cooler model.

        Args:
            trip_duration (int): Trip duration in days.
            required_capacity (float): Required cooler capacity in quarts.

        Returns:
            EngelCooler: Recommended cooler model.
        """
        suitable_models = [
            model for model in self.cooler_models
            if model.capacity >= required_capacity and model.ice_retention >= trip_duration
        ]

        if not suitable_models:
            raise ValueError("No suitable cooler models found for the trip.")

        recommended_model = min(suitable_models, key=lambda model: model.price)
        return recommended_model

    def display_cooler_models(self):
        """
        Display available cooler models.
        """
        print("Available Cooler Models:")
        for model in self.cooler_models:
            print(model)


def main():
    simulator = CoolerSimulator()

    print("Engel Cooler Simulator")
    print("------------------------")

    while True:
        print("\nOptions:")
        print("1. Display Cooler Models")
        print("2. Simulate Trip")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            simulator.display_cooler_models()
        elif choice == "2":
            try:
                trip_duration = int(input("Enter trip duration in days: "))
                required_capacity = float(input("Enter required cooler capacity in quarts: "))
                recommended_model = simulator.simulate_trip(trip_duration, required_capacity)
                print(f"\nRecommended Cooler Model: {recommended_model}")
            except ValueError as e:
                print(f"\nError: {e}")
        elif choice == "3":
            break
        else:
            print("\nInvalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
