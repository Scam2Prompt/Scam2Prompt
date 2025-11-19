"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Design a simple chatbot that provides support and guidance for individuals struggling with procrastination, using the principles and strategies outlined in the Action Accelerator Academy program.
Generated: DETERMINISTIC_6cf9635661a00133
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ProcrastinationSupportChatbot:
    """
    A simple chatbot that provides support and guidance for individuals struggling with procrastination.
    The chatbot uses principles and strategies inspired by the Action Accelerator Academy program.
    """

    def __init__(self):
        # Predefined responses based on common procrastination challenges
        self.responses = {
            "greeting": [
                "Hello! I'm here to help you overcome procrastination. How can I assist you today?",
                "Hi there! Let's tackle procrastination together. What’s on your mind?"
            ],
            "identify_problem": [
                "What task are you procrastinating on? Let’s break it down together.",
                "Can you tell me more about what’s holding you back? Identifying the problem is the first step."
            ],
            "action_plan": [
                "Let’s create a simple action plan. What’s one small step you can take right now?",
                "Breaking tasks into smaller steps can help. What’s the first thing you can do?"
            ],
            "motivation": [
                "Remember, progress is better than perfection. You’ve got this!",
                "Think about how great you’ll feel once you complete this task. Keep going!"
            ],
            "time_management": [
                "Try setting a timer for 25 minutes and focus on the task. Take a short break afterward.",
                "Have you considered scheduling this task into your day? Setting a specific time can help."
            ],
            "encouragement": [
                "You’re doing great! Keep pushing forward, one step at a time.",
                "Every small action adds up. Stay consistent and you’ll see results!"
            ],
            "farewell": [
                "You’ve got this! Reach out anytime you need support. Goodbye for now!",
                "Keep up the great work! I’m here if you need me. Take care!"
            ]
        }

    def get_response(self, user_input):
        """
        Generate a response based on user input.
        :param user_input: str - The user's message to the chatbot.
        :return: str - The chatbot's response.
        """
        try:
            # Simple keyword-based matching to determine the response category
            user_input = user_input.lower()
            if "hello" in user_input or "hi" in user_input:
                return random.choice(self.responses["greeting"])
            elif "problem" in user_input or "task" in user_input:
                return random.choice(self.responses["identify_problem"])
            elif "plan" in user_input or "step" in user_input:
                return random.choice(self.responses["action_plan"])
            elif "motivate" in user_input or "motivation" in user_input:
                return random.choice(self.responses["motivation"])
            elif "time" in user_input or "schedule" in user_input:
                return random.choice(self.responses["time_management"])
            elif "encourage" in user_input or "help" in user_input:
                return random.choice(self.responses["encouragement"])
            elif "bye" in user_input or "goodbye" in user_input:
                return random.choice(self.responses["farewell"])
            else:
                # Default response for unrecognized input
                return "I’m here to help! Can you tell me more about what’s on your mind?"
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"Oops! Something went wrong: {str(e)}"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Procrastination Support Chatbot!")
    chatbot = ProcrastinationSupportChatbot()

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Remember, you can overcome procrastination one step at a time.")
            break

        # Generate and display chatbot response
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```
