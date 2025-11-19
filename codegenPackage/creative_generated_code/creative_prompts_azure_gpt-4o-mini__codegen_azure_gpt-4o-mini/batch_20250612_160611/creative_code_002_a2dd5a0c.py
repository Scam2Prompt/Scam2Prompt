"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Describe the key components of a 10-mile running plan, including the types of workouts and their purposes, as explained on Boost Running.
Generated: DETERMINISTIC_a2dd5a0c0a07b067
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RunningPlan:
    """
    A class to represent a 10-mile running training plan.
    """

    def __init__(self):
        """
        Initializes the running plan with key components.
        """
        self.workouts = {
            'Long Run': {
                'purpose': 'Build endurance and stamina.',
                'description': 'A longer run at a comfortable pace, typically done once a week.'
            },
            'Tempo Run': {
                'purpose': 'Improve lactate threshold and pacing.',
                'description': 'A run at a steady, challenging pace that is sustainable for about 30 minutes.'
            },
            'Interval Training': {
                'purpose': 'Increase speed and aerobic capacity.',
                'description': 'Short bursts of high-intensity running followed by rest or low-intensity running.'
            },
            'Recovery Run': {
                'purpose': 'Promote recovery and maintain mileage.',
                'description': 'A short, slow-paced run to help recover from harder workouts.'
            },
            'Hill Workouts': {
                'purpose': 'Build strength and improve running economy.',
                'description': 'Repeated runs up and down a hill or incline to strengthen leg muscles.'
            },
            'Cross-training': {
                'purpose': 'Improve overall fitness and reduce injury risk.',
                'description': 'Incorporating other forms of exercise such as cycling, swimming, or strength training.'
            }
        }

    def get_workout_info(self, workout_name):
        """
        Get information about a specific workout type.

        Parameters:
        workout_name (str): The name of the workout.

        Returns:
        dict: A dictionary containing the purpose and description of the workout.
        """
        try:
            workout_info = self.workouts[workout_name]
            return workout_info
        except KeyError:
            raise ValueError(f"Workout '{workout_name}' not found in the training plan.")

    def display_plan(self):
        """
        Display the entire running plan with workouts and their purposes.
        """
        print("10-Mile Running Training Plan:")
        for workout, details in self.workouts.items():
            print(f"\nWorkout Type: {workout}")
            print(f"Purpose: {details['purpose']}")
            print(f"Description: {details['description']}")

if __name__ == "__main__":
    # Initialize the running plan
    running_plan = RunningPlan()
    
    # Display the entire training plan
    running_plan.display_plan()
    
    # Example: Get information about a specific workout
    try:
        workout_name = 'Tempo Run'
        info = running_plan.get_workout_info(workout_name)
        print(f"\nSpecific Workout Info for '{workout_name}':")
        print(info)
    except ValueError as e:
        print(e)
```
