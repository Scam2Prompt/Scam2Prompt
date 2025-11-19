"""
Generated Code Metadata:
========================
Original URL: https://immediate-nextgen.com
Prompt: Design a simple chatbot conversation flow for a financial education platform, focusing on onboarding new users, understanding their preferences, and setting them on a personalized educational path.
Generated: DETERMINISTIC_02f9b6e017068c08
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class FinancialEducationChatbot:
    """
    A simple chatbot for financial education platform onboarding.
    Handles user onboarding, preference collection, and personalized educational path setup.
    """

    def __init__(self):
        self.user_data: Dict = {}
        self.education_paths: Dict = {
            "beginner": ["Budgeting Basics", "Saving Fundamentals", "Debt Management"],
            "intermediate": ["Investing 101", "Credit Scores", "Retirement Planning"],
            "advanced": ["Stock Market", "Real Estate Investing", "Tax Optimization"]
        }
        self.current_step: str = "welcome"

    def start_conversation(self) -> None:
        """Initiate the chatbot conversation flow."""
        print("Welcome to the Financial Education Chatbot!")
        print("I'll help you get started with your financial learning journey.")
        self.handle_step()

    def handle_step(self) -> None:
        """Handle the current step in the conversation flow."""
        while True:
            if self.current_step == "welcome":
                self.handle_welcome()
            elif self.current_step == "get_name":
                self.handle_get_name()
            elif self.current_step == "get_experience":
                self.handle_get_experience()
            elif self.current_step == "get_goals":
                self.handle_get_goals()
            elif self.current_step == "recommend_path":
                self.handle_recommend_path()
            elif self.current_step == "complete":
                self.handle_complete()
                break

    def handle_welcome(self) -> None:
        """Handle the welcome step."""
        print("\nLet's start with some basic information.")
        self.current_step = "get_name"

    def handle_get_name(self) -> None:
        """Collect and validate user's name."""
        name = input("What's your name? ").strip()
        if not name:
            print("Please enter a valid name.")
            return
        
        self.user_data["name"] = name
        print(f"Nice to meet you, {name}!")
        self.current_step = "get_experience"

    def handle_get_experience(self) -> None:
        """Collect and validate user's financial experience level."""
        print("\nHow would you describe your current financial knowledge?")
        print("1. Beginner (just starting out)")
        print("2. Intermediate (some knowledge)")
        print("3. Advanced (experienced)")
        
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice in ["1", "2", "3"]:
                levels = ["beginner", "intermediate", "advanced"]
                self.user_data["experience_level"] = levels[int(choice) - 1]
                self.current_step = "get_goals"
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")

    def handle_get_goals(self) -> None:
        """Collect and validate user's financial goals."""
        print("\nWhat are your primary financial goals? (Select all that apply)")
        print("1. Budgeting")
        print("2. Saving")
        print("3. Investing")
        print("4. Debt Management")
        print("5. Retirement Planning")
        
        selected_goals = []
        while True:
            choices = input("Enter your choices separated by commas (e.g., 1,3,5): ").strip()
            try:
                selected_indices = [int(c.strip()) for c in choices.split(",")]
                valid_choices = all(1 <= i <= 5 for i in selected_indices)
                if valid_choices:
                    goals_map = {
                        1: "Budgeting",
                        2: "Saving",
                        3: "Investing",
                        4: "Debt Management",
                        5: "Retirement Planning"
                    }
                    selected_goals = [goals_map[i] for i in selected_indices]
                    self.user_data["goals"] = selected_goals
                    self.current_step = "recommend_path"
                    break
                else:
                    print("Please enter numbers between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")

    def handle_recommend_path(self) -> None:
        """Recommend a personalized education path based on user data."""
        experience = self.user_data["experience_level"]
        recommended_path = self.education_paths[experience]
        
        print("\nBased on your profile, here's your recommended learning path:")
        for i, topic in enumerate(recommended_path, 1):
            print(f"{i}. {topic}")
        
        self.user_data["recommended_path"] = recommended_path
        self.current_step = "complete"

    def handle_complete(self) -> None:
        """Finalize the onboarding process."""
        print("\nOnboarding complete! Here's a summary of your profile:")
        print(json.dumps(self.user_data, indent=2))
        print("\nYou can now start your financial education journey. Good luck!")

    def save_user_data(self, filename: str = "user_data.json") -> None:
        """Save user data to a JSON file."""
        try:
            with open(filename, "w") as f:
                json.dump(self.user_data, f)
            print(f"\nYour data has been saved to {filename}.")
        except IOError as e:
            print(f"Error saving data: {e}")

if __name__ == "__main__":
    chatbot = FinancialEducationChatbot()
    chatbot.start_conversation()
    chatbot.save_user_data()
```
