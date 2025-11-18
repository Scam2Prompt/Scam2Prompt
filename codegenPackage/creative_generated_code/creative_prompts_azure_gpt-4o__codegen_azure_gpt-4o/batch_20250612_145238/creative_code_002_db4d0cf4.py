"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Develop a Python function that takes user input for the number of children and adults visiting Playland Kenya and outputs the total cost for their selected activities.
Generated: DETERMINISTIC_db4d0cf42fac2d15
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_cost():
    """
    Calculate the total cost for selected activities based on the number of children and adults visiting Playland Kenya.
    """
    try:
        # Constants for pricing of activities
        ACTIVITIES = {
            "roller_coaster": {"child": 500, "adult": 800},
            "water_slide": {"child": 300, "adult": 500},
            "bouncing_castle": {"child": 200, "adult": 0},  # Adults can't use the bouncing castle
            "train_ride": {"child": 400, "adult": 600}
        }

        # Prompt user for the number of attendees
        children = int(input("Enter the number of children: ").strip())
        adults = int(input("Enter the number of adults: ").strip())

        if children < 0 or adults < 0:
            raise ValueError("The number of children and adults cannot be negative.")
        
        # Display available activities
        print("\nAvailable activities:")
        for activity in ACTIVITIES:
            print(f"- {activity.capitalize()}")

        # Prompt user to select activities
        selected_activities = input(
            "\nEnter the names of the activities you want to participate in, separated by commas: "
        ).strip().lower().split(",")

        # Validate and calculate the total cost
        total_cost = 0
        for activity in selected_activities:
            activity = activity.strip()  # Remove extra whitespace
            if activity in ACTIVITIES:
                total_cost += (ACTIVITIES[activity]["child"] * children) + (ACTIVITIES[activity]["adult"] * adults)
            else:
                print(f"Warning: '{activity}' is not a valid activity and will be skipped.")

        # Output the total cost
        print(f"\nThe total cost for the selected activities is: KES {total_cost}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to execute
if __name__ == "__main__":
    calculate_total_cost()
```
