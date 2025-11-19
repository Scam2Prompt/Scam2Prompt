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
class RoomType:
    """Enum for different room types available in the chalet."""
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"


class MealPlan:
    """Enum for different meal plans available in the chalet."""
    NO_MEALS = "No Meals"
    BREAKFAST_ONLY = "Breakfast Only"
    FULL_BOARD = "Full Board"


class Booking:
    """Class to represent a booking for Chalet Roc Remi."""
    
    def __init__(self, group_size, room_type, meal_plan):
        self.group_size = group_size
        self.room_type = room_type
        self.meal_plan = meal_plan
        self.validate_booking()

    def validate_booking(self):
        """Validates the booking details."""
        if not (1 <= self.group_size <= 11):
            raise ValueError("Group size must be between 1 and 11.")
        if self.room_type not in [RoomType.SINGLE, RoomType.DOUBLE, RoomType.SUITE]:
            raise ValueError("Invalid room type selected.")
        if self.meal_plan not in [MealPlan.NO_MEALS, MealPlan.BREAKFAST_ONLY, MealPlan.FULL_BOARD]:
            raise ValueError("Invalid meal plan selected.")

    def calculate_cost(self):
        """Calculates the total cost of the booking based on room type and meal plan."""
        room_cost = self.get_room_cost()
        meal_cost = self.get_meal_cost()
        total_cost = room_cost + meal_cost
        return total_cost

    def get_room_cost(self):
        """Returns the cost of the room based on the selected room type."""
        room_prices = {
            RoomType.SINGLE: 100,
            RoomType.DOUBLE: 180,
            RoomType.SUITE: 250
        }
        return room_prices[self.room_type] * self.group_size

    def get_meal_cost(self):
        """Returns the cost of the meal plan based on the selected meal plan."""
        meal_prices = {
            MealPlan.NO_MEALS: 0,
            MealPlan.BREAKFAST_ONLY: 15 * self.group_size,
            MealPlan.FULL_BOARD: 50 * self.group_size
        }
        return meal_prices[self.meal_plan]

    def __str__(self):
        """Returns a string representation of the booking details."""
        return (f"Booking Details:\n"
                f"Group Size: {self.group_size}\n"
                f"Room Type: {self.room_type}\n"
                f"Meal Plan: {self.meal_plan}\n"
                f"Total Cost: ${self.calculate_cost():.2f}")


def main():
    """Main function to run the booking system."""
    try:
        # Example booking
        group_size = 5
        room_type = RoomType.DOUBLE
        meal_plan = MealPlan.FULL_BOARD
        
        booking = Booking(group_size, room_type, meal_plan)
        print(booking)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
