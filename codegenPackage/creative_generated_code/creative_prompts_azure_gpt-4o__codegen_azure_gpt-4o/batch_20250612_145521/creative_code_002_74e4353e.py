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
import json

class FitnessPlan:
    """
    A class to generate a personalized fitness plan for athletes in multiple sports.
    """

    def __init__(self, name, age, sport, fitness_goals):
        """
        Initialize the FitnessPlan with user-specific data.

        :param name: str - Athlete's name
        :param age: int - Athlete's age
        :param sport: str - Sport of the athlete
        :param fitness_goals: list - List of fitness goals (e.g., "strength", "endurance")
        """
        self.name = name
        self.age = age
        self.sport = sport.lower()
        self.fitness_goals = fitness_goals
        self.plan = {}

    def generate_plan(self):
        """
        Generate a personalized fitness plan based on the athlete's sport and goals.
        """
        try:
            self.plan = {
                "name": self.name,
                "age": self.age,
                "sport": self.sport,
                "fitness_goals": self.fitness_goals,
                "program": []
            }
            
            # Customize fitness plan based on sport
            if self.sport == "hockey":
                self.plan["program"] = self._hockey_plan()
            elif self.sport == "mma":
                self.plan["program"] = self._mma_plan()
            elif self.sport == "track":
                self.plan["program"] = self._track_plan()
            else:
                raise ValueError(f"Unsupported sport: {self.sport}")

        except Exception as e:
            print(f"Error generating fitness plan: {e}")
            self.plan = None

    def _hockey_plan(self):
        """
        Generate a hockey-specific fitness plan.
        """
        return [
            {"day": "Monday", "activity": "Strength training (upper body)", "duration": "1 hour"},
            {"day": "Wednesday", "activity": "Endurance skating drills", "duration": "1.5 hours"},
            {"day": "Friday", "activity": "Explosive plyometric exercises", "duration": "45 minutes"}
        ]

    def _mma_plan(self):
        """
        Generate an MMA-specific fitness plan.
        """
        return [
            {"day": "Tuesday", "activity": "Kickboxing and striking drills", "duration": "1.5 hours"},
            {"day": "Thursday", "activity": "Grappling and wrestling practice", "duration": "2 hours"},
            {"day": "Saturday", "activity": "High-intensity circuit training", "duration": "1 hour"}
        ]

    def _track_plan(self):
        """
        Generate a track-specific fitness plan.
        """
        return [
            {"day": "Monday", "activity": "Sprint intervals", "duration": "1 hour"},
            {"day": "Wednesday", "activity": "Endurance long-distance run", "duration": "2 hours"},
            {"day": "Friday", "activity": "Dynamic stretching and mobility drills", "duration": "45 minutes"}
        ]

    def export_plan(self, filepath):
        """
        Export the generated fitness plan to a JSON file.

        :param filepath: str - Path to save the JSON file
        """
        try:
            if not self.plan:
                raise ValueError("No plan generated to export.")
            
            with open(filepath, "w") as file:
                json.dump(self.plan, file, indent=4)
            
            print(f"Fitness plan successfully exported to {filepath}")
        except Exception as e:
            print(f"Error exporting fitness plan: {e}")


# Example usage:
if __name__ == "__main__":
    # Gather athlete details (In production, this would come from a user interface)
    athlete_name = "John Doe"
    athlete_age = 25
    athlete_sport = "Hockey"
    athlete_goals = ["strength", "endurance"]

    # Create an instance of FitnessPlan
    fitness_plan = FitnessPlan(name=athlete_name, age=athlete_age, sport=athlete_sport, fitness_goals=athlete_goals)

    # Generate the fitness plan
    fitness_plan.generate_plan()

    # Print the fitness plan to the console
    print(json.dumps(fitness_plan.plan, indent=4))

    # Optionally export the fitness plan to a file
    fitness_plan.export_plan(filepath="fitness_plan.json")
```
