"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Write a Python script to create a simple quiz that determines which Simon's Cat character a user is, based on a series of easy questions.
Generated: DETERMINISTIC_8b5d5104bc0f8588
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# simons_cat_quiz.py

class SimonsCatCharacter:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Quiz:
    def __init__(self):
        self.characters = {
            "Simon": SimonsCatCharacter("Simon", "You're the clever and resourceful owner."),
            "Pudsey": SimonsCatCharacter("Pudsey", "You're the lovable and lazy cat."),
            "Cloddy Cat": SimonsCatCharacter("Cloddy Cat", "You're the mischievous and playful cat."),
        }
        self.questions = [
            {
                "question": "Do you like to sleep a lot?",
                "answers": ["Yes", "No"],
                "character_mapping": {"Yes": "Pudsey", "No": "Simon"}
            },
            {
                "question": "Are you mischievous?",
                "answers": ["Yes", "No"],
                "character_mapping": {"Yes": "Cloddy Cat", "No": "Simon"}
            },
            {
                "question": "Do you enjoy watching TV with your owner?",
                "answers": ["Yes", "No"],
                "character_mapping": {"Yes": "Pudsey", "No": "Cloddy Cat"}
            }
        ]

    def ask_question(self, question):
        while True:
            print(question["question"])
            for i, answer in enumerate(question["answers"]):
                print(f"{i+1}. {answer}")
            try:
                choice = int(input("Choose a number: "))
                if 1 <= choice <= len(question["answers"]):
                    return question["answers"][choice - 1]
                else:
                    print("Invalid choice. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def determine_character(self):
        character = None
        for question in self.questions:
            answer = self.ask_question(question)
            if character is None:
                character = question["character_mapping"][answer]
            else:
                # If previous character matches, keep it; otherwise, switch to new character
                if character != question["character_mapping"][answer]:
                    if character == "Simon":
                        character = question["character_mapping"][answer]
                    else:
                        character = "Simon"
        return self.characters[character]

    def run_quiz(self):
        print("Welcome to the Simon's Cat quiz!")
        character = self.determine_character()
        print(f"\nYou're {character.name}!")
        print(character.description)

if __name__ == "__main__":
    quiz = Quiz()
    try:
        quiz.run_quiz()
    except Exception as e:
        print(f"An error occurred: {e}")
```
