"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Create a program that calculates the load capacity for a parking lift system, using the range of 500 kg to 10 tons mentioned on OHC Lift's website.
Generated: DETERMINISTIC_1da099608db3dded
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ParkingLift:
    """
    A class to represent a Parking Lift system that calculates its load capacity.
    """

    def __init__(self, weight_capacity_kg):
        """
        Initializes the ParkingLift with a specified weight capacity in kg.

        Args:
            weight_capacity_kg (float): The weight capacity of the lift in kilograms.
        """
        self.weight_capacity_kg = self.validate_capacity(weight_capacity_kg)

    @staticmethod
    def validate_capacity(weight_capacity_kg):
        """
        Validates the weight capacity to ensure it is within the acceptable limits.

        Args:
            weight_capacity_kg (float): The weight capacity in kilograms.

        Returns:
            float: The validated weight capacity in kilograms.

        Raises:
            ValueError: If the weight capacity is not within the range of 500 kg to 10,000 kg.
        """
        if weight_capacity_kg < 500 or weight_capacity_kg > 10000:
            raise ValueError("Weight capacity must be between 500 kg and 10,000 kg.")
        return weight_capacity_kg

    def get_capacity_tons(self):
        """
        Converts the weight capacity from kilograms to tons.

        Returns:
            float: The weight capacity in tons.
        """
        return self.weight_capacity_kg / 1000

    def __str__(self):
        """
        String representation of the ParkingLift object.

        Returns:
            str: A string describing the ParkingLift with its weight capacity.
        """
        return f"Parking Lift Capacity: {self.weight_capacity_kg} kg ({self.get_capacity_tons()} tons)"


def main():
    """
    Main function to demonstrate the usage of the ParkingLift class.
    """
    try:
        # Example weight capacities for testing
        capacities_to_test = [500, 2500, 10000, 15000]  # 15000 kg is out of range

        for capacity in capacities_to_test:
            print(f"Testing with capacity: {capacity} kg")
            lift = ParkingLift(capacity)
            print(lift)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
