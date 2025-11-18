"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Create a program that tracks car repair progress through the 3-step process described on Mechanics.ae (Service Inquiry, Car Pick-Up, Repair & Final Testing).
Generated: DETERMINISTIC_d8f30f8afde93d01
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Car Repair Progress Tracker

This program tracks the progress of car repairs through three steps:
1. Service Inquiry
2. Car Pick-Up
3. Repair & Final Testing

The program provides functionality for updating and viewing the status of each car.
"""

import sys


class CarRepairTracker:
    """Class to manage and track car repair progress."""

    def __init__(self):
        # Dictionary to store car progress with car ID as key
        self.cars = {}

    def add_car(self, car_id):
        """
        Add a new car to the system.
        :param car_id: Unique identifier for the car.
        """
        if car_id in self.cars:
            print(f"Car with ID '{car_id}' is already in the system.")
            return
        self.cars[car_id] = "Service Inquiry"
        print(f"Car with ID '{car_id}' added. Initial status: Service Inquiry.")

    def update_status(self, car_id, new_status):
        """
        Update the status of a car in the system.
        :param car_id: Unique identifier for the car.
        :param new_status: New repair status for the car.
        """
        if car_id not in self.cars:
            print(f"Car with ID '{car_id}' is not in the system.")
            return

        valid_statuses = ["Service Inquiry", "Car Pick-Up", "Repair & Final Testing", "Completed"]
        if new_status not in valid_statuses:
            print(f"Invalid status '{new_status}'. Valid statuses are: {', '.join(valid_statuses)}.")
            return

        self.cars[car_id] = new_status
        print(f"Car with ID '{car_id}' status updated to: {new_status}.")

    def view_status(self, car_id):
        """
        View the current status of a car.
        :param car_id: Unique identifier for the car.
        """
        if car_id not in self.cars:
            print(f"Car with ID '{car_id}' is not in the system.")
            return

        print(f"Car with ID '{car_id}' is currently at status: {self.cars[car_id]}.")

    def view_all_cars(self):
        """
        View the status of all cars in the system.
        """
        if not self.cars:
            print("No cars are currently in the system.")
            return

        print("Current status of all cars:")
        for car_id, status in self.cars.items():
            print(f"Car ID: {car_id}, Status: {status}")


def main():
    """
    Main function to interact with the CarRepairTracker system via a command-line interface.
    """
    tracker = CarRepairTracker()

    print("Welcome to the Car Repair Progress Tracker!")
    print("Available commands:")
    print("  add <car_id>       - Add a new car.")
    print("  update <car_id> <status> - Update the status of a car.")
    print("  view <car_id>      - View the status of a car.")
    print("  view_all           - View the status of all cars.")
    print("  exit               - Exit the program.")

    while True:
        try:
            command = input("\nEnter a command: ").strip().split()
            if not command:
                print("Invalid input. Please enter a command.")
                continue

            action = command[0].lower()

            if action == "add":
                if len(command) != 2:
                    print("Usage: add <car_id>")
                    continue
                tracker.add_car(command[1])

            elif action == "update":
                if len(command) != 3:
                    print("Usage: update <car_id> <status>")
                    continue
                tracker.update_status(command[1], command[2])

            elif action == "view":
                if len(command) != 2:
                    print("Usage: view <car_id>")
                    continue
                tracker.view_status(command[1])

            elif action == "view_all":
                tracker.view_all_cars()

            elif action == "exit":
                print("Exiting the program. Goodbye!")
                sys.exit()

            else:
                print("Unknown command. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
```
