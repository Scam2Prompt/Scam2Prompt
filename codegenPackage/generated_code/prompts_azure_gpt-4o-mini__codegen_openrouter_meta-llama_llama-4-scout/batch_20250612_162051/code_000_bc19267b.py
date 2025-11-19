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
# tractor_selector.py

class TractorModel:
    def __init__(self, name, horsepower, fuel_efficiency, price):
        """
        Initialize a TractorModel object.

        Args:
            name (str): Name of the tractor model.
            horsepower (int): Horsepower of the tractor model.
            fuel_efficiency (float): Fuel efficiency of the tractor model (km/l).
            price (float): Price of the tractor model.
        """
        self.name = name
        self.horsepower = horsepower
        self.fuel_efficiency = fuel_efficiency
        self.price = price

class SCOUT:
    def __init__(self):
        """
        Initialize a SCOUT object with available tractor models.
        """
        self.tractor_models = [
            TractorModel("SC-100", 100, 10.5, 50000.0),
            TractorModel("SC-150", 150, 9.8, 65000.0),
            TractorModel("SC-200", 200, 9.2, 80000.0),
        ]

    def get_tractor_models(self):
        """
        Get a list of available tractor models.

        Returns:
            list[TractorModel]: List of available tractor models.
        """
        return self.tractor_models

def calculate_optimal_tractor(scout, required_horsepower, budget):
    """
    Calculate the optimal tractor model based on user input.

    Args:
        scout (SCOUT): SCOUT object with available tractor models.
        required_horsepower (int): Required horsepower for the task.
        budget (float): Budget for the tractor.

    Returns:
        TractorModel: Optimal tractor model for the task.

    Raises:
        ValueError: If no suitable tractor model is found.
    """
    suitable_models = [
        model for model in scout.get_tractor_models()
        if model.horsepower >= required_horsepower and model.price <= budget
    ]

    if not suitable_models:
        raise ValueError("No suitable tractor model found.")

    optimal_model = min(suitable_models, key=lambda model: model.price)
    return optimal_model

def main():
    try:
        scout = SCOUT()

        print("Available Tractor Models:")
        for i, model in enumerate(scout.get_tractor_models()):
            print(f"{i+1}. {model.name} - {model.horsepower} HP, ${model.price:.2f}")

        required_horsepower = int(input("Enter the required horsepower: "))
        budget = float(input("Enter your budget: $"))

        optimal_tractor = calculate_optimal_tractor(scout, required_horsepower, budget)

        print(f"\nOptimal Tractor Model: {optimal_tractor.name}")
        print(f"Horsepower: {optimal_tractor.horsepower} HP")
        print(f"Fuel Efficiency: {optimal_tractor.fuel_efficiency} km/l")
        print(f"Price: ${optimal_tractor.price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
