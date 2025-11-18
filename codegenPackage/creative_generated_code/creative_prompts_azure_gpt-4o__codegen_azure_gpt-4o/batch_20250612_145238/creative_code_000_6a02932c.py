"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Write a Python script to calculate the total cost for a family visiting Playland Kenya, including activities like trampoline, bowling, and virtual reality, based on the pricing details provided on the website.
Generated: DETERMINISTIC_6a02932c657aa3f4
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Script to Calculate Total Cost for a Family Visiting Playland Kenya

# Define pricing for activities based on the website's information
class Pricing:
    TRAMPOLINE = 500  # Price per person in KES
    BOWLING = 700     # Price per person in KES
    VIRTUAL_REALITY = 1000  # Price per person in KES

# Function to calculate total cost
def calculate_total_cost(family_members, activity_selection):
    """
    Calculate the total cost for a family visiting Playland Kenya.

    Parameters:
        family_members (int): Number of family members.
        activity_selection (list): List of selected activities (as strings). 
                                   Valid options: ['trampoline', 'bowling', 'virtual_reality'].

    Returns:
        int: Total cost in KES.
    """
    try:
        if family_members <= 0:
            raise ValueError("Number of family members must be greater than 0.")
        
        # Initialize total cost
        total_cost = 0
        
        # Map activity names to their respective prices
        activity_prices = {
            "trampoline": Pricing.TRAMPOLINE,
            "bowling": Pricing.BOWLING,
            "virtual_reality": Pricing.VIRTUAL_REALITY
        }
        
        # Calculate cost for each selected activity
        for activity in activity_selection:
            if activity not in activity_prices:
                raise ValueError(f"Invalid activity selected: {activity}")
            total_cost += family_members * activity_prices[activity]

        return total_cost

    except Exception as e:
        # Handle any errors that occur during the calculation
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    try:
        print("Welcome to Playland Kenya Cost Calculator!")

        # Input family size
        family_members = int(input("Enter the number of family members: "))

        # Input activity selection
        print("Select activities (available options: trampoline, bowling, virtual_reality):")
        activity_selection = input(
            "Enter your selected activities separated by commas (e.g., trampoline,bowling): "
        ).strip().lower().split(',')

        # Remove any extra spaces and validate input
        activity_selection = [activity.strip() for activity in activity_selection]

        # Calculate total cost
        total_cost = calculate_total_cost(family_members, activity_selection)
        
        if total_cost is not None:
            print(f"The total cost for {family_members} family member(s) is: {total_cost} KES")
        else:
            print("Failed to calculate total cost. Please check your input.")

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Invalid input: {ve}")
    except Exception as ex:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {ex}")
```
