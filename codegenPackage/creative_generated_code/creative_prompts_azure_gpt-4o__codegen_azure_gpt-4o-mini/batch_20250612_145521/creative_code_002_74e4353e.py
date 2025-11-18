"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Generate code to design a personalized fitness plan for athletes in multiple sports (e.g., hockey, MMA, track) using input parameters like age, sport, and fitness goals, as highlighted on Blaise Strong's website.
Generated: DETERMINISTIC_74e4353e33b5220a
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FitnessPlan:
    """
    A class to represent a personalized fitness plan for athletes in various sports.

    Attributes:
        age (int): Age of the athlete.
        sport (str): The sport the athlete participates in.
        fitness_goals (list): A list of fitness goals (e.g., strength, endurance).
    """

    def __init__(self, age: int, sport: str, fitness_goals: list):
        """
        Initializes the FitnessPlan with age, sport, and fitness goals.

        Args:
            age (int): Age of the athlete.
            sport (str): The sport the athlete participates in.
            fitness_goals (list): A list of fitness goals.
        """
        self.age = age
        self.sport = sport
        self.fitness_goals = fitness_goals
        self.plan = self.generate_plan()

    def generate_plan(self):
        """
        Generates a personalized fitness plan based on age, sport, and fitness goals.

        Returns:
            dict: A dictionary representing the fitness plan.
        """
        # Validate inputs
        if not isinstance(self.age, int) or self.age <= 0:
            raise ValueError("Age must be a positive integer.")
        
        if not isinstance(self.sport, str) or not self.sport:
            raise ValueError("Sport must be a non-empty string.")
        
        if not isinstance(self.fitness_goals, list) or not all(isinstance(goal, str) for goal in self.fitness_goals):
            raise ValueError("Fitness goals must be a list of strings.")

        # Base fitness plan
        plan = {
            "age": self.age,
            "sport": self.sport,
            "workouts": [],
            "nutrition": {},
        }

        # Define workouts based on sport
        if self.sport.lower() == 'hockey':
            plan["workouts"].extend(self.hockey_workouts())
        elif self.sport.lower() == 'mma':
            plan["workouts"].extend(self.mma_workouts())
        elif self.sport.lower() == 'track':
            plan["workouts"].extend(self.track_workouts())
        else:
            raise ValueError(f"Unsupported sport: {self.sport}")

        # Add nutrition based on goals
        plan["nutrition"] = self.nutrition_plan()

        return plan

    def hockey_workouts(self):
        """Returns a list of workouts tailored for hockey players."""
        return [
            "Power skating drills",
            "Agility ladder drills",
            "On-ice shooting practice",
        ]

    def mma_workouts(self):
        """Returns a list of workouts tailored for MMA fighters."""
        return [
            "Heavy bag training",
            "Sparring sessions",
            "Strength training with kettlebells",
        ]

    def track_workouts(self):
        """Returns a list of workouts tailored for track athletes."""
        return [
            "Interval sprints",
            "Endurance runs",
            "Hill training",
        ]

    def nutrition_plan(self):
        """Generates a basic nutrition plan based on fitness goals."""
        nutrition = {
            "protein": "1.6g/kg body weight",
            "carbohydrates": "3-5g/kg body weight",
            "fats": "20-35% of total calorie intake"
        }
        
        # Adjust nutrition based on goals
        if "strength" in self.fitness_goals:
            nutrition["protein"] = "2.0g/kg body weight"
        if "endurance" in self.fitness_goals:
            nutrition["carbohydrates"] = "5-7g/kg body weight"

        return nutrition

# Example usage
if __name__ == "__main__":
    try:
        athlete_plan = FitnessPlan(age=25, sport='Hockey', fitness_goals=['strength', 'endurance'])
        print(athlete_plan.plan)
    except Exception as e:
        print(f"Error: {e}")
```
