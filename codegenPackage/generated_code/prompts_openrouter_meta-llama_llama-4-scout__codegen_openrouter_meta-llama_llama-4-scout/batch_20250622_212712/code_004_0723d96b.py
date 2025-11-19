"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Generate a sample onboarding call script for a fitness coach to guide new clients through the process of setting up their personalized training and nutrition plans, similar to Legacy Training's coaching services.
Generated: DETERMINISTIC_0723d96bf8f1d14c
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# onboarding_script.py

class OnboardingScript:
    def __init__(self, client_name, fitness_goals, nutrition_preferences):
        """
        Initialize the onboarding script with client information.

        Args:
            client_name (str): Client's name
            fitness_goals (str): Client's fitness goals
            nutrition_preferences (str): Client's nutrition preferences
        """
        self.client_name = client_name
        self.fitness_goals = fitness_goals
        self.nutrition_preferences = nutrition_preferences

    def introduction(self):
        """
        Introduction script for the onboarding call.

        Returns:
            str: Introduction script
        """
        return f"Hello {self.client_name}, welcome to our fitness coaching program! I'm excited to work with you to help you achieve your fitness goals."

    def fitness_goal_discussion(self):
        """
        Discussion script for fitness goals.

        Returns:
            str: Fitness goal discussion script
        """
        return f"Can you tell me more about your fitness goals, {self.client_name}? What do you hope to achieve through our coaching program? You've mentioned you're looking to {self.fitness_goals}."

    def nutrition_preference_discussion(self):
        """
        Discussion script for nutrition preferences.

        Returns:
            str: Nutrition preference discussion script
        """
        return f"What are your nutrition preferences, {self.client_name}? Do you have any dietary restrictions or preferences I should be aware of? You've mentioned you prefer {self.nutrition_preferences}."

    def training_plan_explanation(self):
        """
        Explanation script for personalized training plan.

        Returns:
            str: Training plan explanation script
        """
        return f"Based on our discussion, I'll be creating a personalized training plan tailored to your fitness goals and needs. This plan will include a mix of exercises, workouts, and progress tracking to help you stay on track."

    def nutrition_plan_explanation(self):
        """
        Explanation script for personalized nutrition plan.

        Returns:
            str: Nutrition plan explanation script
        """
        return f"I'll also be creating a personalized nutrition plan that takes into account your dietary preferences and restrictions. This plan will provide you with guidance on healthy eating habits and meal planning to support your fitness goals."

    def next_steps(self):
        """
        Next steps script for the onboarding call.

        Returns:
            str: Next steps script
        """
        return f"What's next, {self.client_name}? I'll be sending over your personalized training and nutrition plans within the next 24-48 hours. In the meantime, if you have any questions or concerns, please don't hesitate to reach out."

    def generate_script(self):
        """
        Generate the full onboarding script.

        Returns:
            str: Full onboarding script
        """
        script = [
            self.introduction(),
            self.fitness_goal_discussion(),
            self.nutrition_preference_discussion(),
            self.training_plan_explanation(),
            self.nutrition_plan_explanation(),
            self.next_steps()
        ]
        return "\n\n".join(script)


def main():
    try:
        client_name = input("Enter client's name: ")
        fitness_goals = input("Enter client's fitness goals: ")
        nutrition_preferences = input("Enter client's nutrition preferences: ")

        script = OnboardingScript(client_name, fitness_goals, nutrition_preferences)
        print(script.generate_script())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
