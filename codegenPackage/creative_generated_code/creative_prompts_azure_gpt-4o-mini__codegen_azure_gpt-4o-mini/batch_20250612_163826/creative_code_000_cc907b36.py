"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Generate a training program for a running club that includes warm-up, running drills, and cooldown stretches similar to those at Thompson Estate Athletics.
Generated: DETERMINISTIC_cc907b36d9ecdccb
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RunningClubTrainingProgram:
    def __init__(self, club_name):
        """
        Initialize the training program for the running club.
        
        :param club_name: Name of the running club.
        """
        self.club_name = club_name
        self.warm_up_exercises = []
        self.running_drills = []
        self.cooldown_stretches = []

    def add_warm_up_exercise(self, exercise):
        """
        Add a warm-up exercise to the program.
        
        :param exercise: A string description of the warm-up exercise.
        """
        self.warm_up_exercises.append(exercise)

    def add_running_drill(self, drill):
        """
        Add a running drill to the program.
        
        :param drill: A string description of the running drill.
        """
        self.running_drills.append(drill)

    def add_cooldown_stretch(self, stretch):
        """
        Add a cooldown stretch to the program.
        
        :param stretch: A string description of the cooldown stretch.
        """
        self.cooldown_stretches.append(stretch)

    def display_training_program(self):
        """
        Display the complete training program including warm-up, drills, and cooldown.
        """
        try:
            print(f"Training Program for {self.club_name}:\n")
            print("Warm-Up Exercises:")
            for exercise in self.warm_up_exercises:
                print(f"- {exercise}")

            print("\nRunning Drills:")
            for drill in self.running_drills:
                print(f"- {drill}")

            print("\nCooldown Stretches:")
            for stretch in self.cooldown_stretches:
                print(f"- {stretch}")
        except Exception as e:
            print("An error occurred while displaying the training program:", e)

# Example usage
if __name__ == "__main__":
    # Create an instance of the training program
    thompson_club = RunningClubTrainingProgram("Thompson Estate Athletics")

    # Adding warm-up exercises
    thompson_club.add_warm_up_exercise("5 minutes of light jogging")
    thompson_club.add_warm_up_exercise("Dynamic stretches (leg swings, arm circles)")

    # Adding running drills
    thompson_club.add_running_drill("Strides (4 x 100m at 85% effort)")
    thompson_club.add_running_drill("Fartlek intervals (30 seconds fast, 1 minute slow)")

    # Adding cooldown stretches
    thompson_club.add_cooldown_stretch("Standing quadriceps stretch")
    thompson_club.add_cooldown_stretch("Hamstring stretch")
    
    # Display the training program
    thompson_club.display_training_program()
```
