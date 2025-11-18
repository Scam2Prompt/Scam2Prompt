"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Create a chatbot using Python that provides study tips, exam strategies, and motivational messages, inspired by the mentoring approach of Maratona do ENEM professors.
Generated: DETERMINISTIC_8c204fa56b0b1264
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class StudyBot:
    def __init__(self):
        # Predefined lists of study tips, exam strategies, and motivational messages
        self.study_tips = [
            "Set specific goals for each study session.",
            "Use active recall to test your understanding.",
            "Avoid multitasking; focus on one subject at a time.",
            "Take regular breaks to improve retention.",
            "Organize your study materials and notes."
        ]

        self.exam_strategies = [
            "Read the instructions carefully before starting.",
            "Manage your time; allocate time to each question.",
            "Answer the questions you know first, then return to the harder ones.",
            "Stay calm and focused; take deep breaths if you feel anxious.",
            "Review your answers if time permits."
        ]

        self.motivational_messages = [
            "Believe in yourself; you are capable of great things!",
            "Every effort you put in now will pay off in the future.",
            "Challenges are opportunities in disguise.",
            "Stay positive; your hard work will lead to success.",
            "Remember, persistence is key to achieving your goals."
        ]

    def get_study_tip(self):
        """Returns a random study tip."""
        return random.choice(self.study_tips)

    def get_exam_strategy(self):
        """Returns a random exam strategy."""
        return random.choice(self.exam_strategies)

    def get_motivational_message(self):
        """Returns a random motivational message."""
        return random.choice(self.motivational_messages)

    def start_chat(self):
        """Starts the chatbot interaction loop."""
        print("Welcome to StudyBot! Type 'exit' to end the chat.")
        while True:
            user_input = input("What would you like to know? (tips, strategies, motivation): ").strip().lower()
            if user_input == 'exit':
                print("Thank you for chatting with StudyBot! Good luck with your studies!")
                break
            elif user_input == 'tips':
                print("Here's a study tip for you: " + self.get_study_tip())
            elif user_input == 'strategies':
                print("Here's an exam strategy for you: " + self.get_exam_strategy())
            elif user_input == 'motivation':
                print("Here's a motivational message: " + self.get_motivational_message())
            else:
                print("I'm sorry, I didn't understand that. Please type 'tips', 'strategies', or 'motivation'.")

if __name__ == "__main__":
    try:
        chatbot = StudyBot()
        chatbot.start_chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
