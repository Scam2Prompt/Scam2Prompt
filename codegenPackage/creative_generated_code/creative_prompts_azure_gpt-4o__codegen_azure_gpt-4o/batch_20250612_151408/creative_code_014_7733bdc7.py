"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write a Python program to simulate Engel cooler usage scenarios, such as camping trips or fishing expeditions, and recommend the best cooler model based on user needs.
Generated: DETERMINISTIC_7733bdc71ba3d740
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class EngelCooler:
    """
    A class to represent Engel Cooler models and recommend the best model
    for user scenarios.
    """
    def __init__(self, model_name, capacity_liters, weight_kg, ideal_use_cases, price_usd):
        self.model_name = model_name
        self.capacity_liters = capacity_liters
        self.weight_kg = weight_kg
        self.ideal_use_cases = ideal_use_cases
        self.price_usd = price_usd

    def __str__(self):
        return f"{self.model_name} - Capacity: {self.capacity_liters}L, Weight: {self.weight_kg}kg, " \
               f"Price: ${self.price_usd}, Ideal for: {', '.join(self.ideal_use_cases)}"

def recommend_cooler(activity, group_size, budget):
    """
    Recommends the best Engel cooler model based on the given activity, group size, and budget.

    :param activity: The activity type (e.g., 'camping', 'fishing').
    :param group_size: The number of people involved in the activity.
    :param budget: The maximum amount the user is willing to spend.
    :return: Recommended cooler model or a message indicating no suitable model found.
    """
    try:
        # Cooler data (In production, this might be fetched from a database)
        cooler_models = [
            EngelCooler("Engel MT45F-U1", 40, 22, ["camping", "fishing"], 699),
            EngelCooler("Engel MT35F-U1", 32, 20, ["camping", "road trips"], 599),
            EngelCooler("Engel MT60F-U1", 60, 28, ["fishing", "large groups"], 899),
            EngelCooler("Engel Cooler/Dry Box 19", 19, 3, ["day trips", "picnics"], 79),
        ]

        # Filter coolers based on user needs
        suitable_coolers = [
            cooler for cooler in cooler_models
            if activity in cooler.ideal_use_cases and cooler.price_usd <= budget
        ]

        # Further narrow down based on group size
        if group_size <= 2:
            suitable_coolers = [cooler for cooler in suitable_coolers if cooler.capacity_liters <= 32]
        elif group_size <= 5:
            suitable_coolers = [cooler for cooler in suitable_coolers if cooler.capacity_liters <= 60]
        else:
            suitable_coolers = [cooler for cooler in suitable_coolers if cooler.capacity_liters > 60]

        if suitable_coolers:
            # Recommend the most affordable suitable cooler
            recommended_cooler = min(suitable_coolers, key=lambda c: c.price_usd)
            return f"Recommended Cooler:\n{recommended_cooler}"
        else:
            return "No suitable cooler found for the given criteria."

    except Exception as e:
        # Handle unexpected errors
        return f"An error occurred: {str(e)}"

def main():
    """
    Main function to interact with the user and recommend an Engel cooler.
    """
    try:
        print("Welcome to Engel Cooler Recommendation System!")
        activity = input("Enter the activity (e.g., camping, fishing): ").strip().lower()
        group_size = int(input("Enter the group size: ").strip())
        budget = float(input("Enter your budget ($): ").strip())

        recommendation = recommend_cooler(activity, group_size, budget)
        print("\n" + recommendation)

    except ValueError:
        print("Invalid input. Please ensure group size is a number and budget is a valid amount.")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Entry point for the Python program
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        sys.exit(0)
```
