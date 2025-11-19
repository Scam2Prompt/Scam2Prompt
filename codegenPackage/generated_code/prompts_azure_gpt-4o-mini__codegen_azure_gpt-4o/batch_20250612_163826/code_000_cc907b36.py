"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Generate a training program for a running club that includes warm-up, running drills, and cooldown stretches similar to those at Thompson Estate Athletics.
Generated: DETERMINISTIC_cc907b36d9ecdccb
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class TrainingProgram:
    """
    A class to represent a running club's training program.
    Includes warm-up, running drills, and cooldown stretches.
    """

    def __init__(self, club_name):
        """
        Initialize the training program with the club name.
        """
        self.club_name = club_name
        self.program = {
            "warm_up": [],
            "running_drills": [],
            "cooldown_stretches": []
        }

    def add_warm_up(self, activity, duration_minutes):
        """
        Add a warm-up activity to the program.

        :param activity: Name of the warm-up activity (e.g., "Jogging", "Dynamic stretches").
        :param duration_minutes: Duration of the activity in minutes.
        """
        self.program["warm_up"].append({"activity": activity, "duration": duration_minutes})

    def add_running_drill(self, drill_name, repetitions, distance_meters):
        """
        Add a running drill to the program.

        :param drill_name: Name of the running drill (e.g., "Interval sprints").
        :param repetitions: Number of repetitions for the drill.
        :param distance_meters: Distance covered per repetition in meters.
        """
        self.program["running_drills"].append({
            "drill_name": drill_name,
            "repetitions": repetitions,
            "distance": distance_meters
        })

    def add_cooldown_stretch(self, stretch_name, duration_minutes):
        """
        Add a cooldown stretch to the program.

        :param stretch_name: Name of the cooldown stretch (e.g., "Hamstring stretch").
        :param duration_minutes: Duration of the stretch in minutes.
        """
        self.program["cooldown_stretches"].append({"stretch_name": stretch_name, "duration": duration_minutes})

    def display_program(self):
        """
        Display the training program in a readable format.
        """
        print(f"Training Program for {self.club_name}")
        print("=" * 40)
        print("Warm-Up:")
        for activity in self.program["warm_up"]:
            print(f"- {activity['activity']} ({activity['duration']} minutes)")
        print("\nRunning Drills:")
        for drill in self.program["running_drills"]:
            print(f"- {drill['drill_name']} ({drill['repetitions']} reps, {drill['distance']} meters each)")
        print("\nCooldown Stretches:")
        for stretch in self.program["cooldown_stretches"]:
            print(f"- {stretch['stretch_name']} ({stretch['duration']} minutes)")
        print("=" * 40)

    def save_program_to_file(self, filename):
        """
        Save the training program to a file.

        :param filename: Name of the file to save the program to.
        """
        try:
            with open(filename, "w") as file:
                file.write(f"Training Program for {self.club_name}\n")
                file.write("=" * 40 + "\n")
                file.write("Warm-Up:\n")
                for activity in self.program["warm_up"]:
                    file.write(f"- {activity['activity']} ({activity['duration']} minutes)\n")
                file.write("\nRunning Drills:\n")
                for drill in self.program["running_drills"]:
                    file.write(f"- {drill['drill_name']} ({drill['repetitions']} reps, {drill['distance']} meters each)\n")
                file.write("\nCooldown Stretches:\n")
                for stretch in self.program["cooldown_stretches"]:
                    file.write(f"- {stretch['stretch_name']} ({stretch['duration']} minutes)\n")
                file.write("=" * 40 + "\n")
            print(f"Program successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving program to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a training program for the running club
    club_program = TrainingProgram("Thompson Estate Athletics")

    # Add warm-up activities
    club_program.add_warm_up("Jogging", 10)
    club_program.add_warm_up("Dynamic stretches", 5)

    # Add running drills
    club_program.add_running_drill("Interval sprints", 5, 400)
    club_program.add_running_drill("Hill repeats", 3, 200)

    # Add cooldown stretches
    club_program.add_cooldown_stretch("Hamstring stretch", 5)
    club_program.add_cooldown_stretch("Quad stretch", 5)

    # Display the program
    club_program.display_program()

    # Save the program to a file
    club_program.save_program_to_file("training_program.txt")
```
