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
class OnboardingCall:
    """
    A class to represent an onboarding call for new fitness coaching clients.
    """

    def __init__(self, client_name):
        """
        Initializes the onboarding call with the client's name.

        :param client_name: str - The name of the new client.
        """
        self.client_name = client_name
        self.training_plan = None
        self.nutrition_plan = None

    def greet_client(self):
        """
        Greets the client and introduces the purpose of the call.
        """
        print(f"Hello {self.client_name}, welcome to your onboarding call!")
        print("Today, we'll set up your personalized training and nutrition plans.")

    def gather_information(self):
        """
        Gathers necessary information from the client to create personalized plans.
        """
        try:
            self.client_age = int(input("Please enter your age: "))
            self.client_weight = float(input("Please enter your weight (in kg): "))
            self.client_height = float(input("Please enter your height (in cm): "))
            self.client_fitness_goal = input("What is your primary fitness goal? (e.g., weight loss, muscle gain): ")
        except ValueError as e:
            print("Invalid input. Please enter numeric values for age, weight, and height.")
            raise e

    def create_training_plan(self):
        """
        Creates a personalized training plan based on the client's goals.
        """
        # Placeholder logic for training plan creation
        if self.client_fitness_goal.lower() == "weight loss":
            self.training_plan = "Cardio and strength training 4 times a week."
        elif self.client_fitness_goal.lower() == "muscle gain":
            self.training_plan = "Strength training 5 times a week with a focus on progressive overload."
        else:
            self.training_plan = "A balanced mix of cardio and strength training."

    def create_nutrition_plan(self):
        """
        Creates a personalized nutrition plan based on the client's goals and metrics.
        """
        # Placeholder logic for nutrition plan creation
        if self.client_fitness_goal.lower() == "weight loss":
            self.nutrition_plan = "Caloric deficit with high protein intake."
        elif self.client_fitness_goal.lower() == "muscle gain":
            self.nutrition_plan = "Caloric surplus with balanced macronutrients."
        else:
            self.nutrition_plan = "Balanced diet with a focus on whole foods."

    def summarize_plans(self):
        """
        Summarizes the created training and nutrition plans for the client.
        """
        print(f"\n{self.client_name}, here are your personalized plans:")
        print(f"Training Plan: {self.training_plan}")
        print(f"Nutrition Plan: {self.nutrition_plan}")

    def run_onboarding(self):
        """
        Runs the entire onboarding process.
        """
        self.greet_client()
        self.gather_information()
        self.create_training_plan()
        self.create_nutrition_plan()
        self.summarize_plans()


if __name__ == "__main__":
    # Example usage
    try:
        client_name = input("Enter the client's name: ")
        onboarding_call = OnboardingCall(client_name)
        onboarding_call.run_onboarding()
    except Exception as e:
        print(f"An error occurred during the onboarding process: {e}")
```
