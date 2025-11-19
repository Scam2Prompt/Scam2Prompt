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

Since you're requesting code for an onboarding call script (which is typically a conversational flow rather than a programming task), I'll provide a Python implementation that simulates the script flow with proper structure, error handling, and documentation. This could be used as part of a coaching application's backend or CLI tool.

```python
"""
Fitness Coach Onboarding Script Simulator
This script simulates the onboarding process for new clients of a fitness coaching service.
It guides them through setting up personalized training and nutrition plans.
"""

import sys
from datetime import datetime
from typing import Dict, Optional

class FitnessCoachOnboarding:
    """
    A class to handle the fitness coach onboarding process for new clients.
    """
    
    def __init__(self):
        self.client_data: Dict[str, Optional[str]] = {
            'name': None,
            'age': None,
            'gender': None,
            'fitness_level': None,
            'primary_goal': None,
            'secondary_goal': None,
            'injuries': None,
            'availability': None,
            'dietary_preferences': None,
            'food_allergies': None
        }
        self.current_date = datetime.now().strftime("%Y-%m-%d")
    
    def _get_input(self, prompt: str, validation_func=None) -> str:
        """
        Helper method to get and validate user input.
        
        Args:
            prompt: The question to ask the user
            validation_func: Optional validation function
            
        Returns:
            Validated user input
        """
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input:
                    raise ValueError("Input cannot be empty")
                if validation_func and not validation_func(user_input):
                    raise ValueError("Invalid input")
                return user_input
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
    
    def _validate_age(self, age: str) -> bool:
        """Validate that age is a positive integer."""
        return age.isdigit() and int(age) > 0
    
    def _validate_fitness_level(self, level: str) -> bool:
        """Validate fitness level input."""
        return level.lower() in ['beginner', 'intermediate', 'advanced']
    
    def welcome_client(self) -> None:
        """Welcome the new client and explain the onboarding process."""
        print("\n" + "="*50)
        print("Welcome to Legacy Training Coaching Services!")
        print("="*50)
        print("\nLet's get you set up with your personalized training and nutrition plan.")
        print("This onboarding process will take about 10-15 minutes.\n")
    
    def collect_personal_info(self) -> None:
        """Collect basic personal information from the client."""
        print("\n=== Personal Information ===")
        self.client_data['name'] = self._get_input("1. What's your full name? ")
        self.client_data['age'] = self._get_input(
            "2. How old are you? ",
            self._validate_age
        )
        self.client_data['gender'] = self._get_input(
            "3. What's your gender? (Male/Female/Other) "
        ).capitalize()
    
    def assess_fitness_goals(self) -> None:
        """Assess the client's fitness goals and current level."""
        print("\n=== Fitness Assessment ===")
        self.client_data['fitness_level'] = self._get_input(
            "4. What's your current fitness level? (Beginner/Intermediate/Advanced) ",
            self._validate_fitness_level
        ).capitalize()
        
        print("\n5. What are your primary fitness goals? (Select all that apply)")
        print("a) Weight Loss")
        print("b) Muscle Gain")
        print("c) Improved Endurance")
        print("d) Increased Strength")
        print("e) General Fitness")
        self.client_data['primary_goal'] = self._get_input(
            "Enter letters separated by commas (e.g., a,c): "
        )
        
        self.client_data['secondary_goal'] = self._get_input(
            "6. Do you have any secondary goals? (Optional) "
        ) or "None"
    
    def check_health_considerations(self) -> None:
        """Check for any health considerations or injuries."""
        print("\n=== Health Considerations ===")
        self.client_data['injuries'] = self._get_input(
            "7. Do you have any current injuries or health conditions we should know about? "
        ) or "None"
    
    def assess_availability(self) -> None:
        """Determine the client's availability for training."""
        print("\n=== Availability ===")
        print("8. How many days per week can you commit to training?")
        print("(Recommended: 3-5 days for optimal results)")
        self.client_data['availability'] = self._get_input(
            "Enter number of days: ",
            lambda x: x.isdigit() and 1 <= int(x) <= 7
        )
    
    def collect_nutrition_info(self) -> None:
        """Collect information about the client's nutrition preferences."""
        print("\n=== Nutrition Preferences ===")
        self.client_data['dietary_preferences'] = self._get_input(
            "9. Do you follow any specific dietary preferences? (e.g., Vegetarian, Keto, etc.) "
        ) or "None"
        
        self.client_data['food_allergies'] = self._get_input(
            "10. Do you have any food allergies or intolerances? "
        ) or "None"
    
    def summarize_and_next_steps(self) -> None:
        """Summarize the collected information and explain next steps."""
        print("\n" + "="*50)
        print("Thank you for completing the onboarding process!")
        print("="*50)
        
        print("\nHere's a summary of the information you provided:")
        for key, value in self.client_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nNext Steps:")
        print("- Your coach will review this information within 24 hours")
        print("- You'll receive your personalized training plan via email")
        print("- Your nutrition guide will be shared in the client portal")
        print("- Your first check-in call will be scheduled for 7 days from today")
        
        print("\nWe're excited to work with you on your fitness journey!")
    
    def run_onboarding(self) -> None:
        """Execute the full onboarding process."""
        try:
            self.welcome_client()
            self.collect_personal_info()
            self.assess_fitness_goals()
            self.check_health_considerations()
            self.assess_availability()
            self.collect_nutrition_info()
            self.summarize_and_next_steps()
        except KeyboardInterrupt:
            print("\n\nOnboarding process cancelled by user.")
            sys.exit(1)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please contact support to complete your onboarding.")
            sys.exit(1)

if __name__ == "__main__":
    onboarding = FitnessCoachOnboarding()
    onboarding.run_onboarding()
```
