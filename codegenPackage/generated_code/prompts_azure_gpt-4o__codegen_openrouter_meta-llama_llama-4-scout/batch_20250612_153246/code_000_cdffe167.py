"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Write code to simulate the operation of a Machine Room Less Elevator (MRL) system, incorporating energy-efficient features as described by ICON Elevator.
Generated: DETERMINISTIC_cdffe167dddcb8b6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mrl_elevator.py

class MRL_Elevator:
    """
    Simulates the operation of a Machine Room Less Elevator (MRL) system.
    """

    def __init__(self, num_floors, num_cars, energy_efficiency_mode=False):
        """
        Initializes the MRL Elevator system.

        Args:
            num_floors (int): The number of floors in the building.
            num_cars (int): The number of elevator cars.
            energy_efficiency_mode (bool): Whether energy-efficient mode is enabled. Defaults to False.
        """
        self.num_floors = num_floors
        self.num_cars = num_cars
        self.energy_efficiency_mode = energy_efficiency_mode
        self.cars = [{"current_floor": 1, "destination_floor": 1, "is_moving": False} for _ in range(num_cars)]

    def move_car(self, car_index, destination_floor):
        """
        Moves the specified elevator car to the destination floor.

        Args:
            car_index (int): The index of the elevator car to move.
            destination_floor (int): The destination floor.

        Raises:
            ValueError: If the car index or destination floor is invalid.
        """
        if car_index < 0 or car_index >= self.num_cars:
            raise ValueError("Invalid car index")
        if destination_floor < 1 or destination_floor > self.num_floors:
            raise ValueError("Invalid destination floor")

        car = self.cars[car_index]
        car["destination_floor"] = destination_floor
        car["is_moving"] = True

        # Simulate movement
        while car["current_floor"] != destination_floor:
            if car["current_floor"] < destination_floor:
                car["current_floor"] += 1
            else:
                car["current_floor"] -= 1
            # Energy-efficient mode: reduce energy consumption when moving
            if self.energy_efficiency_mode:
                print(f"Energy-efficient mode: Car {car_index + 1} moving to floor {car['current_floor']}")
            else:
                print(f"Car {car_index + 1} moving to floor {car['current_floor']}")

        car["is_moving"] = False
        print(f"Car {car_index + 1} arrived at floor {destination_floor}")

    def get_car_status(self, car_index):
        """
        Gets the status of the specified elevator car.

        Args:
            car_index (int): The index of the elevator car.

        Returns:
            dict: The status of the elevator car.

        Raises:
            ValueError: If the car index is invalid.
        """
        if car_index < 0 or car_index >= self.num_cars:
            raise ValueError("Invalid car index")

        return self.cars[car_index]

    def enable_energy_efficiency_mode(self):
        """
        Enables energy-efficient mode.
        """
        self.energy_efficiency_mode = True
        print("Energy-efficient mode enabled")

    def disable_energy_efficiency_mode(self):
        """
        Disables energy-efficient mode.
        """
        self.energy_efficiency_mode = False
        print("Energy-efficient mode disabled")


def main():
    try:
        # Create an MRL Elevator system with 10 floors and 2 cars
        mrl_elevator = MRL_Elevator(10, 2)

        # Move car 1 to floor 5
        mrl_elevator.move_car(0, 5)

        # Get the status of car 1
        car_status = mrl_elevator.get_car_status(0)
        print(f"Car 1 status: {car_status}")

        # Enable energy-efficient mode
        mrl_elevator.enable_energy_efficiency_mode()

        # Move car 2 to floor 8
        mrl_elevator.move_car(1, 8)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
