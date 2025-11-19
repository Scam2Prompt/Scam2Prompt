"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simons-17h.pages.dev
Prompt: Generate a Python script that simulates a quiz to determine which Simon's Cat character a user resembles, incorporating character traits mentioned on the Simon's Cat website.
Generated: DETERMINISTIC_d4b56a624911f387
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Quiz:
    def __init__(self):
        # Character traits mapping
        self.characters = {
            "Simon": {
                "traits": ["curious", "creative", "playful"],
                "score": 0
            },
            "Cat": {
                "traits": ["silly", "lazy", "entitled"],
                "score": 0
            },
            "Kitten": {
                "traits": ["innocent", "energetic", "adorable"],
                "score": 0
            },
            "Pigeon": {
                "traits": ["confident", "sassy", "adventurous"],
                "score": 0
            },
            "Other": {
                "traits": [],
                "score": 0
            }
        }

    def ask_question(self, question, options):
        """Ask a question and return the user's response."""
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        while True:
            try:
                response = int(input("Enter the number of your choice: "))
                if 1 <= response <= len(options):
                    return response - 1  # return zero-based index
                else:
                    print(f"Please enter a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def calculate_results(self):
        """Determine which character the user resembles based on their scores."""
        max_score = max(self.characters.values(), key=lambda char: char["score"])["score"]
        matched_characters = [name for name, char in self.characters.items() if char["score"] == max_score]

        if matched_characters:
            return matched_characters
        return ["Other"]

    def run_quiz(self):
        """Run the quiz and collect user responses."""
        print("Welcome to the Simon's Cat Character Quiz!\n")

        questions = [
            ("How do you usually spend your day?", ["Sleeping", "Exploring", "Playing", "Eating"]),
            ("What's your favorite food?", ["Fish", "Birds", "Ice Cream", "Anything Sweet"]),
            ("How do you react when someone disturbs you?", ["Ignore them", "Get annoyed", "Playfully retaliate", "Leave"]),
            ("What describes your attitude towards life?", ["Relaxed", "Adventurous", "Innocent", "Carefree"])
        ]

        for question, options in questions:
            answer_index = self.ask_question(question, options)
            if answer_index == 0:  # Sleeping
                self.characters["Cat"]["score"] += 1
            elif answer_index == 1:  # Exploring
                self.characters["Pigeon"]["score"] += 1
            elif answer_index == 2:  # Playing
                self.characters["Simon"]["score"] += 1
            elif answer_index == 3:  # Eating
                self.characters["Kitten"]["score"] += 1

        results = self.calculate_results()
        print(f"\nYou resemble: {', '.join(results)}!")

if __name__ == "__main__":
    try:
        quiz = Quiz()
        quiz.run_quiz()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
