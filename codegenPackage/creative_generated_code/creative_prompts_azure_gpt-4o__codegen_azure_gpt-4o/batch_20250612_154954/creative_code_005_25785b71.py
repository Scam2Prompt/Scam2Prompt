"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Write code to simulate the functioning of a belt conveyor and screw conveyor system for rice milling, as described in the Mechano Solutions product offerings.
Generated: DETERMINISTIC_25785b717e2a6aab
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class ConveyorSystem:
    """
    A class to simulate the functioning of a conveyor system in rice milling.

    Attributes:
        capacity_per_second (int): The capacity of the conveyor per second in kg.
        conveyor_type (str): The type of conveyor (belt or screw).
    """
    def __init__(self, capacity_per_second, conveyor_type="belt"):
        """
        Initializes the ConveyorSystem object.

        Args:
            capacity_per_second (int): The capacity of the conveyor per second in kg.
            conveyor_type (str): The type of conveyor, either 'belt' or 'screw'.
        """
        if conveyor_type not in ["belt", "screw"]:
            raise ValueError("Invalid conveyor type. Expected 'belt' or 'screw'.")
        self.capacity_per_second = capacity_per_second
        self.conveyor_type = conveyor_type

    def transport_material(self, total_weight):
        """
        Simulates the transport of material through the conveyor system.

        Args:
            total_weight (int): The total weight of material to be processed in kg.

        Returns:
            None
        """
        if total_weight <= 0:
            raise ValueError("Total weight must be a positive integer.")

        print(f"Starting {self.conveyor_type} conveyor...")
        print(f"Processing total weight: {total_weight} kg")

        transported = 0
        while transported < total_weight:
            # Simulate the transportation
            time.sleep(1)  # Simulate real-time operation (1 second delay)
            transported += self.capacity_per_second
            if transported > total_weight:
                transported = total_weight  # Avoid overshooting the weight
            print(f"{self.conveyor_type.capitalize()} conveyor has transported: {transported} kg")

        print(f"{self.conveyor_type.capitalize()} conveyor finished operation. Total transported: {transported} kg")


# Main function to simulate the system
if __name__ == "__main__":
    try:
        # Simulating a belt conveyor system for rice milling
        belt_conveyor = ConveyorSystem(capacity_per_second=100, conveyor_type="belt")
        belt_conveyor.transport_material(total_weight=500)

        print("\n==============================\n")

        # Simulating a screw conveyor system for rice milling
        screw_conveyor = ConveyorSystem(capacity_per_second=75, conveyor_type="screw")
        screw_conveyor.transport_material(total_weight=450)

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
```
