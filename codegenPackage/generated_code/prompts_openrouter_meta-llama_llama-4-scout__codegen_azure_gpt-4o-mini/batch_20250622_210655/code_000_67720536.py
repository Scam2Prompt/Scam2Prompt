"""
Generated Code Metadata:
========================
Original URL: https://chanorodriguez.com
Prompt: Write a Python script to create a personalized fitness plan based on user input, similar to the services offered on ChanoRodriguez.com.
Generated: DETERMINISTIC_677205363d8f403e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FitnessPlan:
    def __init__(self, name, age, fitness_level, goals):
        """
        Initialize the FitnessPlan with user details.

        :param name: str - User's name
        :param age: int - User's age
        :param fitness_level: str - User's fitness level (e.g., beginner, intermediate, advanced)
        :param goals: list - User's fitness goals (e.g., weight loss, muscle gain)
        """
        self.name = name
        self.age = age
        self.fitness_level = fitness_level
        self.goals = goals
        self.plan = {}

    def create_plan(self):
        """
        Create a personalized fitness plan based on user input.
        """
        try:
            self.plan['warmup'] = self.get_warmup()
            self.plan['workout'] = self.get_workout()
            self.plan['cooldown'] = self.get_cooldown()
            self.plan['nutrition'] = self.get_nutrition()
        except Exception as e:
            print(f"Error creating fitness plan: {e}")

    def get_warmup(self):
        """
        Generate warmup exercises based on fitness level.

        :return: list - Warmup exercises
        """
        warmup_exercises = {
            'beginner': ['5 minutes brisk walk', 'dynamic stretches'],
            'intermediate': ['10 minutes jogging', 'dynamic stretches'],
            'advanced': ['15 minutes running', 'dynamic stretches']
        }
        return warmup_exercises.get(self.fitness_level, [])

    def get_workout(self):
        """
        Generate workout exercises based on fitness level and goals.

        :return: list - Workout exercises
        """
        workout_exercises = {
            'weight loss': {
                'beginner': ['30 minutes walking', 'bodyweight squats', 'push-ups'],
                'intermediate': ['30 minutes cycling', 'dumbbell squats', 'burpees'],
                'advanced': ['HIIT workout', 'deadlifts', 'bench press']
            },
            'muscle gain': {
                'beginner': ['bodyweight exercises', 'light weights'],
                'intermediate': ['compound lifts', 'circuit training'],
                'advanced': ['heavy lifting', 'split training']
            }
        }
        
        selected_workout = []
        for goal in self.goals:
            exercises = workout_exercises.get(goal, {}).get(self.fitness_level, [])
            selected_workout.extend(exercises)
        
        return selected_workout

    def get_cooldown(self):
        """
        Generate cooldown exercises.

        :return: list - Cooldown exercises
        """
        return ['5-10 minutes of stretching', 'deep breathing exercises']

    def get_nutrition(self):
        """
        Provide basic nutrition advice based on goals.

        :return: str - Nutrition advice
        """
        nutrition_advice = {
            'weight loss': 'Focus on a calorie deficit with whole foods.',
            'muscle gain': 'Increase protein intake and consider a calorie surplus.'
        }
        
        advice = []
        for goal in self.goals:
            advice.append(nutrition_advice.get(goal, ''))
        
        return ' '.join(filter(None, advice))

    def save_plan(self, filename='fitness_plan.json'):
        """
        Save the fitness plan to a JSON file.

        :param filename: str - The name of the file to save the plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Fitness plan saved to {filename}")
        except IOError as e:
            print(f"Error saving fitness plan: {e}")

def main():
    """
    Main function to execute the fitness plan creation.
    """
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        fitness_level = input("Enter your fitness level (beginner, intermediate, advanced): ").lower()
        goals = input("Enter your fitness goals (comma-separated, e.g., weight loss, muscle gain): ").lower().split(',')

        # Create a fitness plan instance
        fitness_plan = FitnessPlan(name, age, fitness_level, [goal.strip() for goal in goals])
        fitness_plan.create_plan()

        # Display the created plan
        print("\nYour Personalized Fitness Plan:")
        print(json.dumps(fitness_plan.plan, indent=4))

        # Save the plan to a file
        fitness_plan.save_plan()

    except ValueError:
        print("Invalid input. Please enter the correct data types.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
