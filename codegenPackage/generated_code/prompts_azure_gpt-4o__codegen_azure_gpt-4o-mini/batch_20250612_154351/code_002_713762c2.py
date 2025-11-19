"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Generate a program to calculate the load capacity and lifting height for electric pallet trucks, referencing the specifications of Climax Polska's products.
Generated: DETERMINISTIC_713762c2828ce37d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ElectricPalletTruck:
    """
    A class to represent an electric pallet truck and calculate its load capacity and lifting height.
    """

    def __init__(self, model, load_capacity, lifting_height):
        """
        Initializes the ElectricPalletTruck with model, load capacity, and lifting height.

        :param model: str - The model name of the electric pallet truck
        :param load_capacity: float - The maximum load capacity in kilograms
        :param lifting_height: float - The maximum lifting height in meters
        """
        self.model = model
        self.load_capacity = load_capacity
        self.lifting_height = lifting_height

    def calculate_load_capacity(self, weight):
        """
        Calculates if the given weight is within the load capacity.

        :param weight: float - The weight to be checked in kilograms
        :return: bool - True if the weight is within capacity, False otherwise
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        return weight <= self.load_capacity

    def calculate_lifting_height(self, height):
        """
        Checks if the given height is within the lifting height.

        :param height: float - The height to be checked in meters
        :return: bool - True if the height is within lifting height, False otherwise
        """
        if height < 0:
            raise ValueError("Height cannot be negative.")
        return height <= self.lifting_height

    def display_specifications(self):
        """
        Displays the specifications of the electric pallet truck.
        """
        print(f"Model: {self.model}")
        print(f"Load Capacity: {self.load_capacity} kg")
        print(f"Lifting Height: {self.lifting_height} m")


def main():
    """
    Main function to demonstrate the ElectricPalletTruck functionality.
    """
    # Example specifications for Climax Polska's electric pallet truck
    model = "Climax EPT-2000"
    load_capacity = 2000.0  # in kilograms
    lifting_height = 2.5     # in meters

    # Create an instance of ElectricPalletTruck
    truck = ElectricPalletTruck(model, load_capacity, lifting_height)

    # Display the specifications
    truck.display_specifications()

    # Example weight and height to check
    weight_to_check = 1500.0  # in kilograms
    height_to_check = 2.0      # in meters

    # Check load capacity
    if truck.calculate_load_capacity(weight_to_check):
        print(f"The weight of {weight_to_check} kg is within the load capacity.")
    else:
        print(f"The weight of {weight_to_check} kg exceeds the load capacity.")

    # Check lifting height
    if truck.calculate_lifting_height(height_to_check):
        print(f"The height of {height_to_check} m is within the lifting height.")
    else:
        print(f"The height of {height_to_check} m exceeds the lifting height.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
```
