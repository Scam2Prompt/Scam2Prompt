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

def get_user_input(prompt, valid_choices):
    """
    Get validated user input based on provided prompt and valid choices.

    :param prompt: The question to ask the user
    :param valid_choices: List of valid options for the user to select from
    :return: The user's choice as a string
    """
    while True:
        try:
            user_choice = input(prompt).strip().lower()
            if user_choice in valid_choices:
                return user_choice
            else:
                print(f"Invalid choice. Please select from: {', '.join(valid_choices)}")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
            continue


def determine_character(answers):
    """
    Determines the Simon's Cat character based on the user's answers.

    :param answers: A dictionary of user's answers
    :return: The name of the character the user resembles
    """
    # Character traits mapping
    character_traits = {
        "simon's cat": ["playful", "hungry", "curious"],
        "kitten": ["energetic", "mischievous", "cute"],
        "sir roger": ["dignified", "aloof", "classy"],
        "catnip": ["calm", "dreamy", "relaxed"],
        "teddy": ["gentle", "loving", "timid"]
    }

    for character, traits in character_traits.items():
        if all(answers[trait] == "yes" for trait in traits):  # Match all traits for a character
            return character

    # Default to Simon's Cat if no traits match clearly
    return "simon's cat"


def main():
    """
    Main function to run the quiz.
    """
    print("Welcome to the Simon's Cat Character Quiz!")
    print("Answer the following questions to determine which Simon's Cat character you resemble.")
    print("Please answer 'yes' or 'no' to each question.\n")

    # Questions based on character traits
    questions = {
        "playful": "Do you enjoy playing and being active?",
        "hungry": "Do you often find yourself thinking about food?",
        "curious": "Are you naturally curious about the world around you?",
        "energetic": "Do you have lots of energy and love to move around?",
        "mischievous": "Do you enjoy causing a little trouble from time to time?",
        "cute": "Do people often describe you as cute or adorable?",
        "dignified": "Do you carry yourself with a sense of dignity and pride?",
        "aloof": "Do you prefer to keep your distance from others?",
        "classy": "Do you consider yourself classy or sophisticated?",
        "calm": "Are you naturally calm and collected?",
        "dreamy": "Do you tend to daydream or get lost in thought?",
        "relaxed": "Do you love to relax and avoid stress?",
        "gentle": "Are you gentle and kind-hearted?",
        "loving": "Do you enjoy showing affection to others?",
        "timid": "Do you consider yourself shy or timid?"
    }

    valid_choices = ["yes", "no"]
    answers = {}

    # Ask each question
    for trait, question in questions.items():
        answers[trait] = get_user_input(f"{question} (yes/no): ", valid_choices)

    # Determine the character
    character = determine_character(answers)
    print(f"\nBased on your answers, you resemble '{character.capitalize()}'. Congratulations!")

    print("\nThank you for taking the quiz. Meow! 🐾")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
