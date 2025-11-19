"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Generate a Python script that simulates a quiz to determine which Simon's Cat character a user resembles, incorporating character traits mentioned on the Simon's Cat website.
Generated: DETERMINISTIC_d4b56a624911f387
Batch ID: 20250612_160038
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
    """Base class for Simon's Cat characters."""

    def __init__(self, name, description):
        """
        Initialize a character.

        Args:
            name (str): Character name.
            description (str): Character description.
        """
        self.name = name
        self.description = description


class Simon(SimonsCatCharacter):
    """Simon's Cat character."""

    def __init__(self):
        super().__init__("Simon", "The lovable but slightly exasperated cat owner.")


class TheCat(SimonsCatCharacter):
    """The Cat character."""

    def __init__(self):
        super().__init__("The Cat", "The mischievous and lazy cat.")


class Luke(SimonsCatCharacter):
    """Luke character."""

    def __init__(self):
        super().__init__("Luke", "The clumsy and accident-prone cat.")


def get_character_traits():
    """
    Get character traits from the user.

    Returns:
        dict: User's character traits.
    """
    print("Please answer the following questions with 'a', 'b', or 'c'.")

    traits = {}

    questions = [
        {
            "question": "How would you describe your morning routine?",
            "options": {
                "a": "I wake up early and start my day with a plan.",
                "b": "I wake up whenever and just go with the flow.",
                "c": "I hit the snooze button a few (dozen) times.",
            },
            "trait": "morning_routine",
        },
        {
            "question": "How do you handle problem-solving?",
            "options": {
                "a": "I like to think things through and come up with a plan.",
                "b": "I try to find the simplest solution and hope for the best.",
                "c": "I often get distracted and come back to it later.",
            },
            "trait": "problem_solving",
        },
        {
            "question": "What do you value most in life?",
            "options": {
                "a": "Order and organization.",
                "b": "Relaxation and leisure time.",
                "c": "Trying new things and having fun.",
            },
            "trait": "values",
        },
    ]

    for q in questions:
        print(q["question"])
        for option, description in q["options"].items():
            print(f"{option}: {description}")
        answer = input("Your answer: ").lower()
        while answer not in ["a", "b", "c"]:
            print("Invalid answer. Please try again.")
            answer = input("Your answer: ").lower()
        traits[q["trait"]] = answer

    return traits


def determine_character(traits):
    """
    Determine which Simon's Cat character the user resembles.

    Args:
        traits (dict): User's character traits.

    Returns:
        SimonsCatCharacter: The character that the user resembles.
    """
    simon_score = 0
    the_cat_score = 0
    luke_score = 0

    if traits["morning_routine"] == "a":
        simon_score += 1
    elif traits["morning_routine"] == "b":
        the_cat_score += 1
    else:
        luke_score += 1

    if traits["problem_solving"] == "a":
        simon_score += 1
    elif traits["problem_solving"] == "b":
        the_cat_score += 1
    else:
        luke_score += 1

    if traits["values"] == "a":
        simon_score += 1
    elif traits["values"] == "b":
        the_cat_score += 1
    else:
        luke_score += 1

    characters = [Simon(), TheCat(), Luke()]
    scores = [simon_score, the_cat_score, luke_score]

    max_score = max(scores)
    characters_resembling = [c for c, s in zip(characters, scores) if s == max_score]

    return characters_resembling[0]


def main():
    try:
        traits = get_character_traits()
        character = determine_character(traits)
        print(f"\nYou resemble {character.name}!")
        print(character.description)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
