"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Generate a Python script to calculate the optimal tractor model for agricultural tasks based on user input, considering SCOUT's specifications and features.
Generated: DETERMINISTIC_bc19267b0aa81484
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class Tractor:
    """
    Represents a tractor model with specifications and features.
    """
    def __init__(self, model_name, horsepower, fuel_efficiency, price, features):
        self.model_name = model_name
        self.horsepower = horsepower
        self.fuel_efficiency = fuel_efficiency  # in km per liter
        self.price = price  # in USD
        self.features = features  # List of features

    def __str__(self):
        return f"{self.model_name} (HP: {self.horsepower}, Fuel Efficiency: {self.fuel_efficiency} km/l, Price: ${self.price}, Features: {', '.join(self.features)})"


def get_user_input():
    """
    Collects user input for agricultural task requirements.
    Returns a dictionary of requirements.
    """
    try:
        print("Enter your agricultural task requirements:")
        horsepower = int(input("Minimum horsepower required: "))
        fuel_efficiency = float(input("Minimum fuel efficiency required (km/l): "))
        max_price = float(input("Maximum budget (USD): "))
        required_features = input("Required features (comma-separated): ").split(',')
        required_features = [feature.strip().lower() for feature in required_features]
        return {
            "horsepower": horsepower,
            "fuel_efficiency": fuel_efficiency,
            "max_price": max_price,
            "required_features": required_features
        }
    except ValueError:
        print("Invalid input. Please enter numeric values for horsepower, fuel efficiency, and price.")
        sys.exit(1)


def find_optimal_tractor(tractors, requirements):
    """
    Finds the optimal tractor model based on user requirements.
    Returns the best matching tractor or None if no match is found.
    """
    matching_tractors = []

    for tractor in tractors:
        # Check if the tractor meets the requirements
        if (
            tractor.horsepower >= requirements["horsepower"]
            and tractor.fuel_efficiency >= requirements["fuel_efficiency"]
            and tractor.price <= requirements["max_price"]
            and all(feature in tractor.features for feature in requirements["required_features"])
        ):
            matching_tractors.append(tractor)

    # Sort matching tractors by price (ascending) and fuel efficiency (descending)
    matching_tractors.sort(key=lambda t: (t.price, -t.fuel_efficiency))

    # Return the best match or None if no tractors match
    return matching_tractors[0] if matching_tractors else None


def main():
    """
    Main function to execute the tractor selection process.
    """
    # Predefined tractor models (SCOUT's specifications and features)
    tractors = [
        Tractor("SCOUT Model A", 100, 15.0, 25000, ["gps", "auto-steering", "plow"]),
        Tractor("SCOUT Model B", 120, 12.5, 30000, ["gps", "auto-steering", "harvester"]),
        Tractor("SCOUT Model C", 90, 18.0, 20000, ["gps", "plow"]),
        Tractor("SCOUT Model D", 150, 10.0, 40000, ["auto-steering", "harvester", "plow"]),
    ]

    # Get user requirements
    requirements = get_user_input()

    # Find the optimal tractor
    optimal_tractor = find_optimal_tractor(tractors, requirements)

    # Display the result
    if optimal_tractor:
        print("\nOptimal Tractor Model:")
        print(optimal_tractor)
    else:
        print("\nNo tractor models match your requirements.")


if __name__ == "__main__":
    main()
```
