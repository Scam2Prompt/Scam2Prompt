"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Create a workout plan for a senior athlete recovering from injury, incorporating principles from Blaise Strong's training philosophy.
Generated: DETERMINISTIC_de9125c69c879d7a
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class WorkoutPlan:
    """
    A class to generate a workout plan for a senior athlete recovering from injury.
    The workout plan incorporates principles from Blaise Strong's training philosophy:
    - Gradual progression with emphasis on recovery
    - Low-impact exercises to avoid strain
    - Functional movements to improve overall mobility and strength
    """

    def __init__(self, athlete_name, injury_type, recovery_start_date):
        """
        Initialize the workout plan.

        :param athlete_name: Name of the athlete
        :param injury_type: Type of injury the athlete is recovering from
        :param recovery_start_date: Date recovery begins (YYYY-MM-DD format)
        """
        self.athlete_name = athlete_name
        self.injury_type = injury_type
        try:
            self.recovery_start_date = datetime.datetime.strptime(recovery_start_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        self.plan = []

    def generate_plan(self):
        """
        Generate a 4-week workout plan for the senior athlete.
        The plan is based on gradual progression and emphasizes recovery.
        """
        # Phase 1: Week 1 - Focus on mobility and light stretching
        self.plan.append({
            "week": 1,
            "workouts": [
                "Light stretching (10 minutes)",
                "Low-impact yoga (20 minutes)",
                "Walking at a slow pace (15 minutes)"
            ]
        })

        # Phase 2: Week 2 - Add light strength and stability work
        self.plan.append({
            "week": 2,
            "workouts": [
                "Light resistance band exercises (2 sets of 10 reps)",
                "Chair-assisted squats (3 sets of 8 reps)",
                "Walking at a moderate pace (20 minutes)"
            ]
        })

        # Phase 3: Week 3 - Progress to functional movements and light cardio
        self.plan.append({
            "week": 3,
            "workouts": [
                "Bodyweight exercises (push-ups on knees, lunges - 3 sets of 10 reps)",
                "Low-impact cycling (15 minutes)",
                "Walking with intermittent speed bursts (25 minutes)"
            ]
        })

        # Phase 4: Week 4 - Introduce moderate strength and cardio
        self.plan.append({
            "week": 4,
            "workouts": [
                "Light dumbbell exercises (shoulder press, bicep curls - 3 sets of 10 reps)",
                "Low-impact interval training (cycling or walking - 20 minutes)",
                "Stretching and yoga for recovery (20 minutes)"
            ]
        })

    def display_plan(self):
        """
        Display the workout plan in a user-friendly format.
        """
        print(f"Workout Plan for {self.athlete_name} (Recovery from {self.injury_type})")
        print(f"Recovery Start Date: {self.recovery_start_date}")
        print("=" * 50)
        for week in self.plan:
            print(f"Week {week['week']}:")
            for workout in week['workouts']:
                print(f"- {workout}")
            print("-" * 50)

# Example usage
if __name__ == "__main__":
    try:
        athlete_name = "John Doe"
        injury_type = "ACL injury"
        recovery_start_date = "2023-10-01"

        workout_plan = WorkoutPlan(athlete_name, injury_type, recovery_start_date)
        workout_plan.generate_plan()
        workout_plan.display_plan()
    except Exception as e:
        print(f"Error: {e}")
```
