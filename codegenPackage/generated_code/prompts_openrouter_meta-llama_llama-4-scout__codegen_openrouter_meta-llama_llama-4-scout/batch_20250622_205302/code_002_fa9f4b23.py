"""
Generated Code Metadata:
========================
Original URL: https://etherkan.com
Prompt: Generate a training plan for a football team using a Python program, taking into account the team's current fitness level, training goals, and available resources, as described on the VSport website.
Generated: DETERMINISTIC_fa9f4b235666c7fe
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_plan_generator.py

class TrainingPlan:
    def __init__(self, team_name, current_fitness_level, training_goals, available_resources):
        """
        Initialize a TrainingPlan object.

        Args:
            team_name (str): The name of the football team.
            current_fitness_level (int): The team's current fitness level (1-10).
            training_goals (list): A list of training goals (e.g., 'improve_endurance', 'increase_speed').
            available_resources (dict): A dictionary of available resources (e.g., {'field': True, 'equipment': True}).
        """
        self.team_name = team_name
        self.current_fitness_level = current_fitness_level
        self.training_goals = training_goals
        self.available_resources = available_resources

    def generate_plan(self):
        """
        Generate a training plan based on the team's current fitness level, training goals, and available resources.

        Returns:
            dict: A dictionary containing the training plan.
        """
        plan = {}

        # Determine the training intensity based on the team's current fitness level
        if self.current_fitness_level < 4:
            intensity = 'low'
        elif self.current_fitness_level < 7:
            intensity = 'moderate'
        else:
            intensity = 'high'

        # Create a plan for each training goal
        for goal in self.training_goals:
            if goal == 'improve_endurance':
                plan[goal] = self._generate_endurance_plan(intensity)
            elif goal == 'increase_speed':
                plan[goal] = self._generate_speed_plan(intensity)
            elif goal == 'improve_strength':
                plan[goal] = self._generate_strength_plan(intensity)
            else:
                raise ValueError(f"Unsupported training goal: {goal}")

        return plan

    def _generate_endurance_plan(self, intensity):
        """
        Generate an endurance training plan.

        Args:
            intensity (str): The training intensity (low, moderate, high).

        Returns:
            dict: A dictionary containing the endurance training plan.
        """
        plan = {}

        if intensity == 'low':
            plan['duration'] = 30
            plan['frequency'] = 2
            plan['exercises'] = ['jogging', 'cycling']
        elif intensity == 'moderate':
            plan['duration'] = 45
            plan['frequency'] = 3
            plan['exercises'] = ['running', 'swimming']
        elif intensity == 'high':
            plan['duration'] = 60
            plan['frequency'] = 4
            plan['exercises'] = ['high-intensity interval training', 'hill sprints']

        return plan

    def _generate_speed_plan(self, intensity):
        """
        Generate a speed training plan.

        Args:
            intensity (str): The training intensity (low, moderate, high).

        Returns:
            dict: A dictionary containing the speed training plan.
        """
        plan = {}

        if intensity == 'low':
            plan['duration'] = 20
            plan['frequency'] = 2
            plan['exercises'] = ['short sprints', 'agility drills']
        elif intensity == 'moderate':
            plan['duration'] = 30
            plan['frequency'] = 3
            plan['exercises'] = ['medium-distance sprints', 'plyometric exercises']
        elif intensity == 'high':
            plan['duration'] = 40
            plan['frequency'] = 4
            plan['exercises'] = ['long sprints', 'resistance band training']

        return plan

    def _generate_strength_plan(self, intensity):
        """
        Generate a strength training plan.

        Args:
            intensity (str): The training intensity (low, moderate, high).

        Returns:
            dict: A dictionary containing the strength training plan.
        """
        plan = {}

        if intensity == 'low':
            plan['duration'] = 30
            plan['frequency'] = 2
            plan['exercises'] = ['bodyweight exercises', 'light weightlifting']
        elif intensity == 'moderate':
            plan['duration'] = 45
            plan['frequency'] = 3
            plan['exercises'] = ['moderate weightlifting', 'resistance band training']
        elif intensity == 'high':
            plan['duration'] = 60
            plan['frequency'] = 4
            plan['exercises'] = ['heavy weightlifting', 'plyometric exercises']

        return plan


def main():
    try:
        team_name = input("Enter the team name: ")
        current_fitness_level = int(input("Enter the team's current fitness level (1-10): "))
        training_goals = input("Enter the training goals (comma-separated): ").split(',')
        training_goals = [goal.strip() for goal in training_goals]
        available_resources = {
            'field': input("Is a field available? (yes/no): ").lower() == 'yes',
            'equipment': input("Is equipment available? (yes/no): ").lower() == 'yes'
        }

        plan = TrainingPlan(team_name, current_fitness_level, training_goals, available_resources)
        training_plan = plan.generate_plan()

        print("\nTraining Plan:")
        for goal, goal_plan in training_plan.items():
            print(f"Goal: {goal}")
            print(f"  Duration: {goal_plan['duration']} minutes")
            print(f"  Frequency: {goal_plan['frequency']} times per week")
            print(f"  Exercises: {', '.join(goal_plan['exercises'])}")
            print()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
