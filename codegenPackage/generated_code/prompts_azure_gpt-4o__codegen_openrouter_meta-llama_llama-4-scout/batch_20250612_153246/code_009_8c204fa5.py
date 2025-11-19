"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Create a chatbot using Python that provides study tips, exam strategies, and motivational messages, inspired by the mentoring approach of Maratona do ENEM professors.
Generated: DETERMINISTIC_8c204fa56b0b1264
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a dictionary with study tips
study_tips = {
    "time_management": [
        "Create a study schedule and stick to it.",
        "Break down large study sessions into smaller chunks.",
        "Use a timer to keep yourself on track."
    ],
    "active_learning": [
        "Summarize notes in your own words.",
        "Create concept maps or flashcards.",
        "Teach someone what you've learned."
    ],
    "retention": [
        "Review material regularly.",
        "Get enough sleep before exams.",
        "Stay organized and focused."
    ]
}

# Define a dictionary with exam strategies
exam_strategies = {
    "before_the_exam": [
        "Arrive early and get comfortable.",
        "Read the questions carefully.",
        "Plan your time wisely."
    ],
    "during_the_exam": [
        "Stay calm and focused.",
        "Manage your time effectively.",
        "Review your answers."
    ],
    "after_the_exam": [
        "Review what you got wrong.",
        "Learn from your mistakes.",
        "Stay positive and move forward."
    ]
}

# Define a list with motivational messages
motivational_messages = [
    "You got this! Stay focused and keep pushing forward.",
    "Believe in yourself and your abilities.",
    "You're not alone, many students have been in your shoes before.",
    "Keep going, you're making progress.",
    "You're strong and capable, don't give up."
]

class Chatbot:
    def __init__(self):
        self.messages = {
            "study_tips": self.get_study_tips,
            "exam_strategies": self.get_exam_strategies,
            "motivational_messages": self.get_motivational_messages
        }

    def get_study_tips(self, topic=None):
        if topic:
            if topic in study_tips:
                return random.choice(study_tips[topic])
            else:
                return "Sorry, I couldn't find any study tips for that topic."
        else:
            tip_categories = list(study_tips.keys())
            return f"Available study tip categories: {', '.join(tip_categories)}"

    def get_exam_strategies(self, phase=None):
        if phase:
            if phase in exam_strategies:
                return random.choice(exam_strategies[phase])
            else:
                return "Sorry, I couldn't find any exam strategies for that phase."
        else:
            strategy_phases = list(exam_strategies.keys())
            return f"Available exam strategy phases: {', '.join(strategy_phases)}"

    def get_motivational_messages(self):
        return random.choice(motivational_messages)

    def respond(self, message):
        message = message.lower()
        if "study tips" in message:
            topic = None
            for category in study_tips:
                if category in message:
                    topic = category
                    break
            return self.get_study_tips(topic)
        elif "exam strategies" in message:
            phase = None
            for phase_name in exam_strategies:
                if phase_name in message:
                    phase = phase_name
                    break
            return self.get_exam_strategies(phase)
        elif "motivational" in message or "motivation" in message:
            return self.get_motivational_messages()
        else:
            return "Sorry, I didn't understand that. Please try again."

def main():
    chatbot = Chatbot()
    print("Welcome to the Maratona do ENEM chatbot!")
    while True:
        user_message = input("You: ")
        if user_message.lower() == "quit":
            break
        print("Chatbot:", chatbot.respond(user_message))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", str(e))
```
