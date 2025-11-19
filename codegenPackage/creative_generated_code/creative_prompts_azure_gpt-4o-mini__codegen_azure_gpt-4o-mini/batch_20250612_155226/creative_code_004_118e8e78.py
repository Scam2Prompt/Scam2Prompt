"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neighborgoods.com
Prompt: Explain how to set up a home gym using premium fitness equipment recommended by Kenko Fitness Solutions, including a list of essential items for various workout goals.
Generated: DETERMINISTIC_118e8e7887e5f83e
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HomeGymSetup:
    """
    A class to represent a home gym setup using premium fitness equipment.
    """

    def __init__(self):
        """Initialize the home gym with essential items for various workout goals."""
        self.equipment = {
            "strength_training": [
                "Adjustable Dumbbells",
                "Barbell Set",
                "Power Rack",
                "Weight Plates",
                "Kettlebells",
                "Resistance Bands"
            ],
            "cardio": [
                "Treadmill",
                "Stationary Bike",
                "Rowing Machine",
                "Jump Rope",
                "Elliptical Trainer"
            ],
            "flexibility": [
                "Yoga Mat",
                "Foam Roller",
                "Stretching Strap",
                "Balance Ball"
            ],
            "functional_fitness": [
                "Medicine Ball",
                "TRX Suspension Trainer",
                "Battle Ropes"
            ]
        }

    def get_equipment_list(self, goal):
        """
        Retrieve the list of essential items based on the specified workout goal.

        Parameters:
        goal (str): The fitness goal (e.g., 'strength_training', 'cardio', etc.)

        Returns:
        list: A list of recommended equipment for the given goal.

        Raises:
        ValueError: If the specified goal is not recognized.
        """
        try:
            # Normalize goal input to lowercase for consistency
            goal = goal.lower()
            if goal not in self.equipment:
                raise ValueError(f"Unrecognized goal: '{goal}'. Please choose from {list(self.equipment.keys())}.")
            return self.equipment[goal]
        except ValueError as e:
            # Handle the error gracefully and provide feedback
            print("Error:", e)
            return []

    def display_setup(self):
        """Display the complete home gym setup with equipment categorized by workout goals."""
        print("Home Gym Setup: Premium Fitness Equipment")
        print("=" * 40)
        for goal, items in self.equipment.items():
            print(f"{goal.replace('_', ' ').title()}:")
            for item in items:
                print(f" - {item}")
            print()

if __name__ == "__main__":
    # Create an instance of HomeGymSetup
    gym_setup = HomeGymSetup()
    
    # Display the complete setup
    gym_setup.display_setup()
    
    # Example of fetching equipment for a specific goal
    goal_input = "strength_training"  # User-defined goal
    equipment_list = gym_setup.get_equipment_list(goal_input)
    
    if equipment_list:
        print(f"Essential equipment for {goal_input.replace('_', ' ').title()}:")
        for item in equipment_list:
            print(f" - {item}")
```
