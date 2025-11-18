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
    """
    A chatbot that provides study tips, exam strategies, and motivational messages.
    Inspired by the mentoring approach of Maratona do ENEM professors.
    """

    def __init__(self):
        # Initialize chatbot responses
        self.study_tips = [
            "Break your study sessions into 25-minute blocks with 5-minute breaks. This is called the Pomodoro technique.",
            "Organize your study material by subjects and prioritize the topics you find most challenging.",
            "Practice past exam papers to familiarize yourself with the format and improve your time management skills.",
            "Use mnemonic devices to help memorize key concepts.",
            "Explain what you've learned to someone else—it helps reinforce your understanding."
        ]

        self.exam_strategies = [
            "Read all questions carefully before answering. Don't rush.",
            "Answer the questions you know first, and come back to the tougher ones later.",
            "Manage your time wisely—allocate enough time per question based on its weight.",
            "If unsure about an answer, eliminate incorrect options to improve your chances.",
            "Stay calm and focus; avoid spending too much time on a single question."
        ]

        self.motivational_messages = [
            "Believe in yourself—you've been preparing hard for this moment!",
            "Every step forward, no matter how small, is progress. Keep going!",
            "Mistakes are proof that you're trying. Don't give up!",
            "Stay positive and trust the process. You've got this!",
            "Success doesn't come overnight. Stay consistent and dedicated!"
        ]

    def get_response(self, category):
        """
        Provides a random response based on the category chosen.
        
        Args:
            category (str): The category of response ('study', 'exam', 'motivation').
        
        Returns:
            str: A response message from the selected category.
        """
        if category == 'study':
            return random.choice(self.study_tips)
        elif category == 'exam':
            return random.choice(self.exam_strategies)
        elif category == 'motivation':
            return random.choice(self.motivational_messages)
        else:
            return "Invalid category. Please choose 'study', 'exam', or 'motivation'."

def main():
    """
    Main function to interact with the StudyBot.
    """
    print("Welcome to the StudyBot! I'm here to help you with study tips, exam strategies, and motivational messages.")
    print("Choose a category: 'study', 'exam', or 'motivation'. Type 'exit' to quit.")

    bot = StudyBot()

    while True:
        try:
            user_input = input("\nEnter a category: ").strip().lower()
            if user_input == 'exit':
                print("Goodbye! Remember, you're capable of achieving great things!")
                break
            response = bot.get_response(user_input)
            print(f"\nStudyBot: {response}")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
