"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Illustrate how to implement a booking system for Chalet Roc Remi that accommodates group sizes up to 11 people, with features for selecting room types and meal plans.
Generated: DETERMINISTIC_9f3daf39d22ad3ed
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# booking_system.py

import sys

class BookingSystem:
    """
    A booking system for Chalet Roc Remi that accommodates group sizes up to 11 people.
    Allows users to select room types and meal plans.
    """

    def __init__(self):
        # Initialize available room types and meal plans
        self.room_types = {
            "single": 100,  # Price per night
            "double": 150,
            "suite": 250
        }
        self.meal_plans = {
            "none": 0,  # Price per person per day
            "breakfast": 20,
            "half_board": 50,
            "full_board": 80
        }
        self.max_group_size = 11

    def display_options(self):
        """Display available room types and meal plans."""
        print("\nAvailable Room Types:")
        for room, price in self.room_types.items():
            print(f"  {room.capitalize()} - ${price} per night")

        print("\nAvailable Meal Plans:")
        for plan, price in self.meal_plans.items():
            print(f"  {plan.capitalize()} - ${price} per person per day")

    def calculate_cost(self, group_size, room_type, meal_plan, nights):
        """
        Calculate the total cost of the booking.
        :param group_size: Number of people in the group
        :param room_type: Selected room type
        :param meal_plan: Selected meal plan
        :param nights: Number of nights staying
        :return: Total cost of the booking
        """
        try:
            # Validate inputs
            if group_size < 1 or group_size > self.max_group_size:
                raise ValueError(f"Group size must be between 1 and {self.max_group_size}.")
            if room_type not in self.room_types:
                raise ValueError(f"Invalid room type: {room_type}.")
            if meal_plan not in self.meal_plans:
                raise ValueError(f"Invalid meal plan: {meal_plan}.")
            if nights < 1:
                raise ValueError("Number of nights must be at least 1.")

            # Calculate costs
            room_cost = self.room_types[room_type] * nights
            meal_cost = self.meal_plans[meal_plan] * group_size * nights
            total_cost = room_cost + meal_cost

            return total_cost
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def book(self):
        """Handle the booking process."""
        try:
            print("\nWelcome to Chalet Roc Remi Booking System!")
            self.display_options()

            # Gather user input
            group_size = int(input("\nEnter the number of people in your group: "))
            room_type = input("Enter the room type (single, double, suite): ").lower()
            meal_plan = input("Enter the meal plan (none, breakfast, half_board, full_board): ").lower()
            nights = int(input("Enter the number of nights you want to stay: "))

            # Calculate total cost
            total_cost = self.calculate_cost(group_size, room_type, meal_plan, nights)
            if total_cost is not None:
                print(f"\nBooking Summary:")
                print(f"  Group Size: {group_size}")
                print(f"  Room Type: {room_type.capitalize()}")
                print(f"  Meal Plan: {meal_plan.capitalize()}")
                print(f"  Nights: {nights}")
                print(f"  Total Cost: ${total_cost}")
                print("\nThank you for booking with Chalet Roc Remi!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)


# Entry point for the program
if __name__ == "__main__":
    booking_system = BookingSystem()
    booking_system.book()
```
