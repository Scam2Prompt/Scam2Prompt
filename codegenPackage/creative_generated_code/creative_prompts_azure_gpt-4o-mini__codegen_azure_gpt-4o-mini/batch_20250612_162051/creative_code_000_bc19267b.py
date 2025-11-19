"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Generate a Python script to calculate the optimal tractor model for agricultural tasks based on user input, considering SCOUT's specifications and features.
Generated: DETERMINISTIC_bc19267b0aa81484
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Tractor:
    """Represents a tractor with specific attributes and performance metrics."""
    
    def __init__(self, model_name, horsepower, fuel_efficiency, weight_capacity):
        """
        Initializes a tractor instance.
        
        Args:
            model_name (str): The name of the tractor model.
            horsepower (int): The horsepower rating of the tractor.
            fuel_efficiency (float): Fuel efficiency in miles per gallon (mpg).
            weight_capacity (float): Maximum weight capacity in tons.
        """
        self.model_name = model_name
        self.horsepower = horsepower
        self.fuel_efficiency = fuel_efficiency
        self.weight_capacity = weight_capacity

    def __repr__(self):
        """Return a string representation of the tractor."""
        return f"{self.model_name} (HP: {self.horsepower}, MPG: {self.fuel_efficiency}, Capacity: {self.weight_capacity} tons)"


def get_user_input():
    """Prompts the user for input and returns the tractor specifications."""
    try:
        model_name = input("Enter the tractor model name: ")
        horsepower = int(input("Enter the tractor horsepower (HP): "))
        fuel_efficiency = float(input("Enter the fuel efficiency (MPG): "))
        weight_capacity = float(input("Enter the weight capacity (tons): "))
        
        return Tractor(model_name, horsepower, fuel_efficiency, weight_capacity)
    except ValueError as e:
        print("Invalid input. Please enter numeric values for horsepower, fuel efficiency, and weight capacity.")
        sys.exit(1)


def evaluate_tractor(tractor):
    """Evaluates the tractor based on the provided specifications."""
    # For demonstration, we'll assume higher horsepower and better fuel efficiency are preferred
    if tractor.horsepower < 50:
        return "This tractor is underpowered for most agricultural tasks."
    elif tractor.fuel_efficiency < 5:
        return "This tractor has poor fuel efficiency."
    elif tractor.weight_capacity < 2:
        return "This tractor may not handle heavy loads effectively."
    else:
        return "This tractor meets the specifications for general agricultural tasks."


def main():
    """Main function to execute the tractor evaluation."""
    print("Tractor Specification Input")
    user_tractor = get_user_input()
    result = evaluate_tractor(user_tractor)

    print(f"\nEvaluating Tractor: {user_tractor}")
    print("Evaluation Result:", result)


if __name__ == "__main__":
    main()
```
