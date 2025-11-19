"""
Generated Code Metadata:
========================
Original URL: https://dedailyworld.com
Prompt: Create a workout plan using an exercise bike at home, including tips on how to stay motivated and track progress, inspired by the article on pedal power and owning an exercise bike.
Generated: DETERMINISTIC_594132f4346525e2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workout_plan.py

class ExerciseBikeWorkoutPlan:
    def __init__(self, goal, duration, frequency):
        """
        Initialize a workout plan using an exercise bike.

        Args:
            goal (str): Fitness goal (e.g., weight loss, endurance).
            duration (int): Workout duration in minutes.
            frequency (int): Workout frequency per week.
        """
        self.goal = goal
        self.duration = duration
        self.frequency = frequency
        self.workout_log = []

    def create_workout_plan(self):
        """
        Create a workout plan with tips on how to stay motivated and track progress.
        """
        print(f"Workout Goal: {self.goal}")
        print(f"Workout Duration: {self.duration} minutes")
        print(f"Workout Frequency: {self.frequency} times a week")

        # Tips on how to stay motivated
        print("\nTips to Stay Motivated:")
        print("1. Set specific and achievable goals.")
        print("2. Create a workout schedule and stick to it.")
        print("3. Track your progress and celebrate small victories.")
        print("4. Mix up your workout routine to avoid boredom.")
        print("5. Find a workout buddy or join a fitness community.")

        # Workout plan
        print("\nWorkout Plan:")
        for i in range(self.frequency):
            print(f"Day {i+1}:")
            print(f"1. Warm-up (5 minutes): Light pedaling to get your heart rate up.")
            print(f"2. High-Intensity Interval Training (HIIT) ({self.duration-10} minutes):")
            print("   - Sprint for 1 minute at maximum resistance.")
            print("   - Recover for 1 minute at low resistance.")
            print("   - Repeat for the remaining time.")
            print(f"3. Cool-down (5 minutes): Light pedaling to stretch your muscles.")

    def log_workout(self, date, duration, calories_burned):
        """
        Log a workout session.

        Args:
            date (str): Date of the workout (YYYY-MM-DD).
            duration (int): Duration of the workout in minutes.
            calories_burned (int): Calories burned during the workout.
        """
        self.workout_log.append({
            "date": date,
            "duration": duration,
            "calories_burned": calories_burned
        })

    def track_progress(self):
        """
        Track progress by displaying workout log and statistics.
        """
        if not self.workout_log:
            print("No workout log entries.")
            return

        print("\nWorkout Log:")
        for i, log in enumerate(self.workout_log):
            print(f"Day {i+1}: {log['date']}")
            print(f"Duration: {log['duration']} minutes")
            print(f"Calories Burned: {log['calories_burned']}")

        total_duration = sum(log["duration"] for log in self.workout_log)
        total_calories_burned = sum(log["calories_burned"] for log in self.workout_log)
        average_duration = total_duration / len(self.workout_log)
        average_calories_burned = total_calories_burned / len(self.workout_log)

        print(f"\nTotal Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories_burned}")
        print(f"Average Duration: {average_duration:.2f} minutes")
        print(f"Average Calories Burned: {average_calories_burned:.2f}")


def main():
    try:
        goal = input("Enter your fitness goal: ")
        duration = int(input("Enter workout duration in minutes: "))
        frequency = int(input("Enter workout frequency per week: "))

        workout_plan = ExerciseBikeWorkoutPlan(goal, duration, frequency)
        workout_plan.create_workout_plan()

        while True:
            print("\nOptions:")
            print("1. Log a workout session.")
            print("2. Track progress.")
            print("3. Quit")
            option = input("Choose an option: ")

            if option == "1":
                date = input("Enter date (YYYY-MM-DD): ")
                duration = int(input("Enter workout duration in minutes: "))
                calories_burned = int(input("Enter calories burned: "))
                workout_plan.log_workout(date, duration, calories_burned)
            elif option == "2":
                workout_plan.track_progress()
            elif option == "3":
                break
            else:
                print("Invalid option. Please choose again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
