"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roc-remi.com
Prompt: Illustrate how to implement a booking system for Chalet Roc Remi that accommodates group sizes up to 11 people, with features for selecting room types and meal plans.
Generated: DETERMINISTIC_9f3daf39d22ad3ed
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Booking System for Chalet Roc Remi
- Accommodates group sizes up to 11 people.
- Allows selection of room types and meal plans.
- Includes error handling and validation.
"""

import sys

class BookingSystem:
    def __init__(self):
        # Room types and their costs per night
        self.room_types = {
            "single": 100,   # Single room: $100 per night
            "double": 180,   # Double room: $180 per night
            "family": 250    # Family room (up to 4 people): $250 per night
        }
        
        # Meal plans and their costs per person per day
        self.meal_plans = {
            "none": 0,       # No meals: $0
            "breakfast": 20, # Breakfast: $20 per person per day
            "half_board": 50,# Half board: $50 per person per day
            "full_board": 80 # Full board: $80 per person per day
        }
    
    def validate_group_size(self, group_size):
        """Validates that the group size does not exceed the limit (11 people)."""
        if group_size < 1 or group_size > 11:
            raise ValueError("Group size must be between 1 and 11 people.")
    
    def validate_room_type(self, room_type):
        """Validates that the given room type exists."""
        if room_type not in self.room_types:
            raise ValueError(f"Invalid room type: {room_type}. Available options are {', '.join(self.room_types.keys())}.")
    
    def validate_meal_plan(self, meal_plan):
        """Validates that the given meal plan exists."""
        if meal_plan not in self.meal_plans:
            raise ValueError(f"Invalid meal plan: {meal_plan}. Available options are {', '.join(self.meal_plans.keys())}.")
    
    def calculate_total_cost(self, group_size, nights, room_type, meal_plan):
        """
        Calculates the total cost of a booking.

        Parameters:
        - group_size: Number of people in the group (1-11).
        - nights: Number of nights to stay.
        - room_type: Type of room chosen (single, double, family).
        - meal_plan: Type of meal plan chosen (none, breakfast, half_board, full_board).

        Returns:
        - Total cost of the booking.
        """
        room_cost_per_night = self.room_types[room_type]
        meal_cost_per_person_per_day = self.meal_plans[meal_plan]
        
        # Total room cost
        total_room_cost = room_cost_per_night * nights
        
        # Total meal cost
        total_meal_cost = meal_cost_per_person_per_day * group_size * nights
        
        # Final cost
        return total_room_cost + total_meal_cost

    def book_chalet(self, group_size, nights, room_type, meal_plan):
        """
        Handles the booking process, validates inputs, and calculates the total cost.

        Parameters:
        - group_size: Number of people in the group.
        - nights: Number of nights to stay.
        - room_type: Type of room chosen.
        - meal_plan: Type of meal plan chosen.

        Returns:
        - Confirmation message along with the total cost.
        """
        try:
            # Validate inputs
            self.validate_group_size(group_size)
            self.validate_room_type(room_type)
            self.validate_meal_plan(meal_plan)
            
            # Calculate total cost
            total_cost = self.calculate_total_cost(group_size, nights, room_type, meal_plan)
            
            # Return confirmation message
            return f"Booking confirmed for {group_size} people staying {nights} nights in a {room_type} room with {meal_plan} meal plan. Total cost: ${total_cost:.2f}."
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    try:
        group_size = int(input("Enter group size (1-11): "))
        nights = int(input("Enter number of nights: "))
        room_type = input(f"Choose a room type ({', '.join(booking_system.room_types.keys())}): ").strip().lower()
        meal_plan = input(f"Choose a meal plan ({', '.join(booking_system.meal_plans.keys())}): ").strip().lower()
        
        confirmation = booking_system.book_chalet(group_size, nights, room_type, meal_plan)
        print(confirmation)
    except ValueError:
        print("Invalid input. Please provide valid numbers for group size and nights.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
