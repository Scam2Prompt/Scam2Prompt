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
import json

class EngelCooler:
    """Class representing an Engel cooler with its specifications."""
    
    def __init__(self, model, capacity, power_source, weight, price):
        self.model = model
        self.capacity = capacity  # in liters
        self.power_source = power_source  # e.g., '12V', 'AC'
        self.weight = weight  # in kg
        self.price = price  # in USD

    def __str__(self):
        return f"{self.model} - Capacity: {self.capacity}L, Power: {self.power_source}, Weight: {self.weight}kg, Price: ${self.price}"

def load_coolers_from_json(file_path):
    """Load cooler specifications from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            coolers_data = json.load(file)
            return [EngelCooler(**cooler) for cooler in coolers_data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []

def recommend_cooler(coolers, usage_type):
    """Recommend a cooler based on the usage type."""
    recommendations = {
        'camping': lambda cooler: cooler.capacity >= 30 and cooler.weight <= 10,
        'fishing': lambda cooler: cooler.capacity >= 20 and cooler.weight <= 15,
        'beach': lambda cooler: cooler.capacity >= 40 and cooler.weight <= 12,
    }

    if usage_type not in recommendations:
        print("Error: Invalid usage type. Please choose from 'camping', 'fishing', or 'beach'.")
        return []

    suitable_coolers = [cooler for cooler in coolers if recommendations[usage_type](cooler)]
    
    if not suitable_coolers:
        print("No suitable coolers found for the specified usage type.")
    return suitable_coolers

def main():
    """Main function to run the cooler recommendation program."""
    coolers = load_coolers_from_json('coolers.json')
    
    if not coolers:
        return  # Exit if no coolers are loaded

    print("Welcome to the Engel Cooler Recommendation System!")
    usage_type = input("Enter your usage type (camping, fishing, beach): ").strip().lower()
    
    recommended_coolers = recommend_cooler(coolers, usage_type)
    
    if recommended_coolers:
        print("\nRecommended Coolers:")
        for cooler in recommended_coolers:
            print(cooler)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `coolers.json` file in the same directory with the following structure for the code to work:

```json
[
    {
        "model": "Engel MT45F-U1",
        "capacity": 40,
        "power_source": "12V",
        "weight": 18,
        "price": 799.99
    },
    {
        "model": "Engel MR040F-U1",
        "capacity": 38,
        "power_source": "12V",
        "weight": 15,
        "price": 699.99
    },
    {
        "model": "Engel HD30F",
        "capacity": 30,
        "power_source": "AC",
        "weight": 10,
        "price": 499.99
    }
]
```
