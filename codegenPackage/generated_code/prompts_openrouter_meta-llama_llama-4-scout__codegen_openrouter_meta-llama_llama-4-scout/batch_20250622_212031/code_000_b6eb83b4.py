"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Write a Python code snippet to compare the features of Gree Bora A4 Silver air conditioners with different BTU ratings."
Generated: DETERMINISTIC_b6eb83b48822c5b1
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent an air conditioner
class AirConditioner:
    def __init__(self, model, btu_rating, price, energy_efficiency, cooling_capacity):
        """
        Initialize an air conditioner object.

        Args:
            model (str): The model of the air conditioner.
            btu_rating (int): The BTU rating of the air conditioner.
            price (float): The price of the air conditioner.
            energy_efficiency (float): The energy efficiency of the air conditioner.
            cooling_capacity (float): The cooling capacity of the air conditioner.
        """
        self.model = model
        self.btu_rating = btu_rating
        self.price = price
        self.energy_efficiency = energy_efficiency
        self.cooling_capacity = cooling_capacity

# Define a function to compare air conditioners
def compare_air_conditioners(air_conditioners):
    """
    Compare the features of different air conditioners.

    Args:
        air_conditioners (list): A list of air conditioner objects.

    Returns:
        None
    """
    # Print the header
    print(f"{'Model':^20} | {'BTU Rating':^15} | {'Price':^10} | {'Energy Efficiency':^20} | {'Cooling Capacity':^20}")
    print("-" * 85)

    # Iterate over the air conditioners and print their features
    for air_conditioner in air_conditioners:
        print(f"{air_conditioner.model:^20} | {air_conditioner.btu_rating:^15} | {air_conditioner.price:^10.2f} | {air_conditioner.energy_efficiency:^20.2f} | {air_conditioner.cooling_capacity:^20.2f}")

# Define the main function
def main():
    try:
        # Create air conditioner objects
        gree_bora_a4_silver_9000 = AirConditioner("Gree Bora A4 Silver 9000", 9000, 899.99, 3.2, 2600)
        gree_bora_a4_silver_12000 = AirConditioner("Gree Bora A4 Silver 12000", 12000, 1099.99, 3.5, 3500)
        gree_bora_a4_silver_18000 = AirConditioner("Gree Bora A4 Silver 18000", 18000, 1499.99, 3.8, 5200)

        # Compare the air conditioners
        air_conditioners = [gree_bora_a4_silver_9000, gree_bora_a4_silver_12000, gree_bora_a4_silver_18000]
        compare_air_conditioners(air_conditioners)

    except Exception as e:
        # Handle any exceptions
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
