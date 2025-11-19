"""
Generated Code Metadata:
========================
Original URL: https://selffeeling.com
Prompt: "Design a simple chatbot that provides emotional support and recommends mindfulness exercises for users dealing with stress and anxiety."
Generated: DETERMINISTIC_f68fe2bc449de9a4
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class EmotionalSupportChatbot:
    def __init__(self):
        # Predefined responses for emotional support
        self.support_responses = [
            "I'm here for you. It's okay to feel this way.",
            "Take a deep breath. You're doing the best you can.",
            "Remember, you're not alone. I'm here to help.",
            "It's okay to take things one step at a time.",
            "You are stronger than you think. Keep going!"
        ]
        
        # Predefined mindfulness exercises
        self.mindfulness_exercises = [
            "Try a 5-minute breathing exercise: Inhale deeply for 4 seconds, hold for 4 seconds, and exhale for 4 seconds.",
            "Take a moment to focus on the present. Notice 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
            "Write down three things you're grateful for today.",
            "Close your eyes and visualize a peaceful place. Imagine yourself there for a few minutes.",
            "Stretch your body gently and focus on how each movement feels."
        ]

    def get_support_response(self):
        # Randomly select a support response
        return random.choice(self.support_responses)

    def get_mindfulness_exercise(self):
        # Randomly select a mindfulness exercise
        return random.choice(self.mindfulness_exercises)

    def chat(self):
        print("Hello! I'm your emotional support chatbot. How can I help you today?")
        print("Type 'support' for emotional support, 'exercise' for a mindfulness exercise, or 'exit' to end the chat.")
        
        while True:
            try:
                user_input = input("\nYour choice: ").strip().lower()
                
                if user_input == 'support':
                    print("\nSupport Response: " + self.get_support_response())
                elif user_input == 'exercise':
                    print("\nMindfulness Exercise: " + self.get_mindfulness_exercise())
                elif user_input == 'exit':
                    print("\nTake care! Remember, you're not alone.")
                    break
                else:
                    print("\nInvalid input. Please type 'support', 'exercise', or 'exit'.")
            except Exception as e:
                print("\nAn error occurred: ", str(e))
                print("Please try again.")

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot = EmotionalSupportChatbot()
    chatbot.chat()
```
