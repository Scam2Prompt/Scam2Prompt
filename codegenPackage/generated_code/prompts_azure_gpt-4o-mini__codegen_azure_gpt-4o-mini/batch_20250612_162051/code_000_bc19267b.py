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
import json

class Tractor:
    """Class representing a tractor model with its specifications and features."""
    
    def __init__(self, model, horsepower, fuel_efficiency, price, features):
        """
        Initialize a Tractor instance.

        Args:
            model (str): The model name of the tractor.
            horsepower (int): The horsepower of the tractor.
            fuel_efficiency (float): The fuel efficiency in liters per hour.
            price (float): The price of the tractor.
            features (list): A list of features available in the tractor.
        """
        self.model = model
        self.horsepower = horsepower
        self.fuel_efficiency = fuel_efficiency
        self.price = price
        self.features = features

    def __repr__(self):
        """Return a string representation of the tractor model."""
        return f"{self.model} (HP: {self.horsepower}, Fuel Efficiency: {self.fuel_efficiency} L/h, Price: ${self.price})"


class TractorSelector:
    """Class to select the optimal tractor based on user input."""
    
    def __init__(self, tractors):
        """
        Initialize the TractorSelector with a list of tractors.

        Args:
            tractors (list): A list of Tractor instances.
        """
        self.tractors = tractors

    def find_optimal_tractor(self, min_horsepower, max_price, required_features):
        """
        Find the optimal tractor based on user requirements.

        Args:
            min_horsepower (int): Minimum horsepower required.
            max_price (float): Maximum price the user is willing to pay.
            required_features (list): List of features that must be included.

        Returns:
            list: A list of optimal tractor models that meet the criteria.
        """
        optimal_tractors = []
        
        for tractor in self.tractors:
            if (tractor.horsepower >= min_horsepower and 
                tractor.price <= max_price and 
                all(feature in tractor.features for feature in required_features)):
                optimal_tractors.append(tractor)
        
        return optimal_tractors


def load_tractors_from_json(file_path):
    """
    Load tractor data from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing tractor data.

    Returns:
        list: A list of Tractor instances.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Tractor(**item) for item in data]
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except json.JSONDecodeError as e:
        print("Error: Failed to decode JSON from the file.")
        raise e


def main():
    """Main function to execute the tractor selection process."""
    # Load tractors from a JSON file
    tractors = load_tractors_from_json('tractors.json')

    # User input for tractor selection criteria
    try:
        min_horsepower = int(input("Enter minimum horsepower required: "))
        max_price = float(input("Enter maximum price you are willing to pay: "))
        required_features = input("Enter required features (comma-separated): ").split(',')

        # Create a TractorSelector instance
        selector = TractorSelector(tractors)

        # Find optimal tractors based on user input
        optimal_tractors = selector.find_optimal_tractor(min_horsepower, max_price, [feature.strip() for feature in required_features])

        # Display the results
        if optimal_tractors:
            print("Optimal tractors found:")
            for tractor in optimal_tractors:
                print(tractor)
        else:
            print("No tractors found that meet the criteria.")

    except ValueError as e:
        print("Error: Invalid input. Please enter numeric values for horsepower and price.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
