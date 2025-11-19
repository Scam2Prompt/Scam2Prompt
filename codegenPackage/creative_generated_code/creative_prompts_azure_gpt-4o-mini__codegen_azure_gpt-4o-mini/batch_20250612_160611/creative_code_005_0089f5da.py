"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Explain the importance of back-to-back long runs in ultra marathon training, referencing the training strategies discussed on Boost Running.
Generated: DETERMINISTIC_0089f5daeb2cda86
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UltraMarathonTraining:
    """
    A class to represent an ultra marathon training regimen focusing on back-to-back long runs.
    """

    def __init__(self, total_weeks: int, long_run_distance: float):
        """
        Initializes the training program with the specified total weeks and long run distance.

        :param total_weeks: Total number of weeks in the training program.
        :param long_run_distance: Distance of the long run in miles.
        """
        self.total_weeks = total_weeks
        self.long_run_distance = long_run_distance
        self.schedule = []

    def create_schedule(self):
        """
        Creates a training schedule with back-to-back long runs over the specified duration.
        """
        for week in range(1, self.total_weeks + 1):
            # Back-to-back long runs on Saturday and Sunday
            self.schedule.append({
                'Week': week,
                'Saturday': f"Long run of {self.long_run_distance} miles",
                'Sunday': f"Long run of {self.long_run_distance} miles"
            })

    def display_schedule(self):
        """
        Displays the training schedule.
        """
        print("Ultra Marathon Training Schedule")
        print("--------------------------------")
        for week in self.schedule:
            print(f"Week {week['Week']}: {week['Saturday']} | {week['Sunday']}")

    def validate_inputs(self):
        """
        Validates the input parameters for the training program.

        :raises ValueError: If total_weeks is less than 1 or long_run_distance is less than 1.
        """
        if self.total_weeks < 1:
            raise ValueError("Total weeks must be at least 1.")
        if self.long_run_distance < 1:
            raise ValueError("Long run distance must be at least 1 mile.")

    def run_training(self):
        """
        Runs the entire training regimen: validating inputs, creating a schedule, and displaying it.
        """
        try:
            self.validate_inputs()
            self.create_schedule()
            self.display_schedule()
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Define the total weeks and long run distance
    total_weeks = 16  # Example duration for training
    long_run_distance = 20.0  # Example long run distance in miles

    # Create and run the training program
    training_program = UltraMarathonTraining(total_weeks, long_run_distance)
    training_program.run_training()
```
