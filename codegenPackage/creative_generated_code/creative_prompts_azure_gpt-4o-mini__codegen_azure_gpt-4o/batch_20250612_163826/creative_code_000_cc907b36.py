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
import datetime


class RunningClubTrainingProgram:
    """
    A class to generate a training program for a running club.
    Includes warm-ups, running drills, and cooldown stretches.
    """

    def __init__(self):
        self.program = {
            "warm_up": [],
            "running_drills": [],
            "cooldown": []
        }

    def add_warm_up(self, exercise, duration_minutes):
        """
        Add a warm-up exercise to the program.

        :param exercise: Name of the exercise
        :param duration_minutes: Duration in minutes
        """
        self.program["warm_up"].append({"exercise": exercise, "duration": duration_minutes})

    def add_running_drill(self, drill_name, distance_meters, reps):
        """
        Add a running drill to the program.

        :param drill_name: Name of the running drill
        :param distance_meters: Distance in meters for each repetition
        :param reps: Number of repetitions
        """
        self.program["running_drills"].append({"drill_name": drill_name, "distance": distance_meters, "reps": reps})

    def add_cooldown(self, stretch, duration_minutes):
        """
        Add a cooldown stretch to the program.

        :param stretch: Name of the stretch
        :param duration_minutes: Duration in minutes
        """
        self.program["cooldown"].append({"stretch": stretch, "duration": duration_minutes})

    def generate_program(self):
        """
        Generate the full training program.

        :return: Dictionary containing the training program
        """
        return self.program


def main():
    try:
        print("Generating Running Club Training Program...\n")

        # Initialize the training program
        training_program = RunningClubTrainingProgram()

        # Add warm-up exercises
        training_program.add_warm_up("Dynamic stretches", 10)
        training_program.add_warm_up("Jogging", 5)

        # Add running drills
        training_program.add_running_drill("400m sprints", 400, 6)
        training_program.add_running_drill("Hill repeats", 200, 5)
        training_program.add_running_drill("Fartlek intervals", 1000, 4)

        # Add cooldown stretches
        training_program.add_cooldown("Hamstring stretch", 5)
        training_program.add_cooldown("Quadriceps stretch", 5)
        training_program.add_cooldown("Calf stretch", 5)

        # Generate the program and print it
        program = training_program.generate_program()
        print("Training Program:")
        print("Warm-Up:")
        for item in program["warm_up"]:
            print(f"- {item['exercise']} ({item['duration']} minutes)")

        print("\nRunning Drills:")
        for item in program["running_drills"]:
            print(f"- {item['drill_name']} ({item['distance']} meters x {item['reps']})")

        print("\nCooldown Stretches:")
        for item in program["cooldown"]:
            print(f"- {item['stretch']} ({item['duration']} minutes)")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
