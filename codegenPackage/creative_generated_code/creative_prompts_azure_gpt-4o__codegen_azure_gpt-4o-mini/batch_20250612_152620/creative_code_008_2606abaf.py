"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Create a chatbot script to recommend Kossto's orthopedic solutions for office workers, drivers, and gamers based on their posture and pain concerns.
Generated: DETERMINISTIC_2606abaf52b79ebe
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class OrthopedicChatbot:
    def __init__(self):
        self.solutions = {
            'office_worker': [
                "Ergonomic chair with lumbar support.",
                "Standing desk to reduce prolonged sitting.",
                "Footrest to improve leg circulation.",
            ],
            'driver': [
                "Lumbar roll for lower back support.",
                "Neck pillow for long drives.",
                "Seat cushion to relieve pressure.",
            ],
            'gamer': [
                "Gaming chair with adjustable support.",
                "Wrist rests for keyboard and mouse.",
                "Posture corrector to keep spine aligned.",
            ],
        }
        self.pain_concerns = {
            'lower_back': "lower back pain",
            'neck': "neck pain",
            'wrist': "wrist pain",
            'shoulder': "shoulder discomfort",
        }

    def greet_user(self):
        print("Hello! I'm here to recommend orthopedic solutions based on your posture and pain concerns.")

    def get_user_type(self):
        user_type = input("Are you an office worker, driver, or gamer? ").lower()
        if user_type not in self.solutions:
            raise ValueError("Invalid user type. Please choose 'office_worker', 'driver', or 'gamer'.")
        return user_type

    def get_pain_concern(self):
        print("Please select your pain concern from the following options:")
        for key, value in self.pain_concerns.items():
            print(f"- {value} ({key})")
        concern = input("Enter your pain concern: ").lower()
        if concern not in self.pain_concerns:
            raise ValueError("Invalid pain concern. Please choose from the listed options.")
        return concern

    def recommend_solution(self, user_type):
        recommendations = self.solutions[user_type]
        return random.choice(recommendations)

    def run(self):
        try:
            self.greet_user()
            user_type = self.get_user_type()
            pain_concern = self.get_pain_concern()
            solution = self.recommend_solution(user_type)
            print(f"Based on your profile as a {user_type.replace('_', ' ')} with {self.pain_concerns[pain_concern]}, I recommend: {solution}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot = OrthopedicChatbot()
    chatbot.run()
```
