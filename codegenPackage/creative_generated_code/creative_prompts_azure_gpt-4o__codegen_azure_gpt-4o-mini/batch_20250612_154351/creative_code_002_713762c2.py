"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Generate a program to calculate the load capacity and lifting height for electric pallet trucks, referencing the specifications of Climax Polska's products.
Generated: DETERMINISTIC_713762c2828ce37d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ElectricPalletTruck:
    """
    A class to represent an electric pallet truck and calculate its load capacity and lifting height.
    """

    def __init__(self, model, load_capacity, lifting_height):
        """
        Initialize the electric pallet truck with model specifications.

        Args:
            model (str): The model name of the electric pallet truck.
            load_capacity (float): Maximum load capacity in kilograms.
            lifting_height (float): Maximum lifting height in meters.
        """
        self.model = model
        self.load_capacity = load_capacity  # Load capacity in kg
        self.lifting_height = lifting_height  # Lifting height in meters

    def calculate_load_capacity(self, additional_load):
        """
        Calculate the remaining load capacity after adding an additional load.

        Args:
            additional_load (float): The additional load in kilograms.

        Returns:
            float: The remaining load capacity in kilograms.

        Raises:
            ValueError: If the additional load exceeds the load capacity.
        """
        if additional_load < 0:
            raise ValueError("Additional load must be a non-negative value.")

        remaining_capacity = self.load_capacity - additional_load
        if remaining_capacity < 0:
            raise ValueError("Cannot exceed the maximum load capacity.")

        return remaining_capacity

    def can_lift_height(self, height):
        """
        Determine if the pallet truck can lift to a specified height.

        Args:
            height (float): The height in meters to check.

        Returns:
            bool: True if the truck can lift to the specified height, False otherwise.
        """
        if height < 0:
            raise ValueError("Height must be a non-negative value.")

        return height <= self.lifting_height

    def __str__(self):
        """
        Return a string representation of the electric pallet truck.

        Returns:
            str: Description of the electric pallet truck specifications.
        """
        return f"Model: {self.model}, Load Capacity: {self.load_capacity}kg, Lifting Height: {self.lifting_height}m"


def main():
    """
    Main function to illustrate the usage of the ElectricPalletTruck class.
    """
    try:
        # Creating an instance of ElectricPalletTruck with example specifications
        truck = ElectricPalletTruck("Climax Model A", 1500, 2.5)

        print(truck)  # Display truck specifications

        # Calculate remaining load capacity
        additional_load = 300  # Example additional load
        remaining_capacity = truck.calculate_load_capacity(additional_load)
        print(f"Remaining Load Capacity after adding {additional_load}kg: {remaining_capacity}kg")

        # Check if the truck can lift to a specified height
        height_to_check = 2.0  # Example height
        can_lift = truck.can_lift_height(height_to_check)
        print(f"Can lift to {height_to_check}m: {'Yes' if can_lift else 'No'}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
