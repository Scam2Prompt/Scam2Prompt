"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Generate a script to calculate competitive pricing for elevator installations, considering the cost-effective range mentioned by ICON Elevator.
Generated: DETERMINISTIC_f3fcb278d211863e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ElevatorInstallationPricing:
    def __init__(self, base_cost, cost_per_floor, cost_per_weight):
        """
        Initializes the pricing model for elevator installations.

        :param base_cost: The base cost of the elevator installation.
        :param cost_per_floor: The additional cost per floor the elevator services.
        :param cost_per_weight: The additional cost per weight unit the elevator can carry.
        """
        self.base_cost = base_cost
        self.cost_per_floor = cost_per_floor
        self.cost_per_weight = cost_per_weight

    def calculate_price(self, num_floors, weight_capacity):
        """
        Calculates the total price for the elevator installation.

        :param num_floors: The number of floors the elevator will service.
        :param weight_capacity: The weight capacity of the elevator.
        :return: Total installation price.
        """
        if num_floors < 1 or weight_capacity <= 0:
            raise ValueError("Number of floors must be at least 1 and weight capacity must be greater than 0.")

        total_price = (self.base_cost +
                       (self.cost_per_floor * num_floors) +
                       (self.cost_per_weight * weight_capacity))
        return total_price

def load_pricing_data(file_path):
    """
    Loads pricing data from a JSON file.

    :param file_path: Path to the JSON file containing pricing data.
    :return: A dictionary with pricing data.
    """
    try:
        with open(file_path, 'r') as file:
            pricing_data = json.load(file)
            return pricing_data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")

def main():
    """
    Main function to execute the pricing calculation.
    """
    # Load pricing data from a JSON file
    pricing_file = 'pricing_data.json'
    try:
        pricing_data = load_pricing_data(pricing_file)
        
        # Create an instance of ElevatorInstallationPricing
        pricing_model = ElevatorInstallationPricing(
            base_cost=pricing_data['base_cost'],
            cost_per_floor=pricing_data['cost_per_floor'],
            cost_per_weight=pricing_data['cost_per_weight']
        )

        # Example input values
        num_floors = 5  # Number of floors the elevator will service
        weight_capacity = 1000  # Weight capacity in kg

        # Calculate the total price
        total_price = pricing_model.calculate_price(num_floors, weight_capacity)
        print(f"The total price for the elevator installation is: ${total_price:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `pricing_data.json` file exists in the same directory as the script and contains the following structure:

```json
{
    "base_cost": 5000,
    "cost_per_floor": 1000,
    "cost_per_weight": 5
}
```
