"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Create Python code to simulate the stacking mechanism of a parking lift system, optimizing for space efficiency as discussed on OHC Lift's website.
Generated: DETERMINISTIC_952dbf2a5966b117
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
    def __init__(self, capacity):
        """
        Initialize the ParkingLift with a specified capacity.

        :param capacity: Maximum number of cars the lift can hold.
        """
        self.capacity = capacity
        self.current_stack = []  # List to represent the stack of parked cars

    def park_car(self, car_id):
        """
        Park a car in the lift.

        :param car_id: Unique identifier for the car.
        :raises OverflowError: If the lift is at full capacity.
        """
        if len(self.current_stack) >= self.capacity:
            raise OverflowError("Cannot park car: Lift is full.")
        self.current_stack.append(car_id)
        print(f"Car {car_id} parked. Current stack: {self.current_stack}")

    def retrieve_car(self):
        """
        Retrieve the top car from the lift.

        :returns: Unique identifier of the retrieved car.
        :raises IndexError: If there are no cars to retrieve.
        """
        if not self.current_stack:
            raise IndexError("Cannot retrieve car: Lift is empty.")
        car_id = self.current_stack.pop()
        print(f"Car {car_id} retrieved. Current stack: {self.current_stack}")
        return car_id

    def view_stack(self):
        """
        View the current stack of parked cars.

        :returns: List of cars currently parked in the lift.
        """
        return self.current_stack.copy()  # Return a copy to prevent modification

    def is_full(self):
        """
        Check if the lift is at full capacity.

        :returns: True if full, False otherwise.
        """
        return len(self.current_stack) >= self.capacity

    def is_empty(self):
        """
        Check if the lift is empty.

        :returns: True if empty, False otherwise.
        """
        return len(self.current_stack) == 0


# Example Usage
if __name__ == "__main__":
    try:
        # Create a parking lift with a capacity of 3 cars
        parking_lift = ParkingLift(capacity=3)

        # Park some cars
        parking_lift.park_car('Car1')
        parking_lift.park_car('Car2')
        parking_lift.park_car('Car3')

        # Attempt to park another car to demonstrate error handling
        try:
            parking_lift.park_car('Car4')
        except OverflowError as e:
            print(e)

        # Retrieve cars
        parking_lift.retrieve_car()
        parking_lift.retrieve_car()

        # Check if the lift is empty or full
        print(f"Is lift full? {parking_lift.is_full()}")
        print(f"Is lift empty? {parking_lift.is_empty()}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
