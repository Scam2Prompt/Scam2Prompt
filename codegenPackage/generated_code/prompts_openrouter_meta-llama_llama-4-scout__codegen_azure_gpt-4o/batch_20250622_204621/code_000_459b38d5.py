"""
Generated Code Metadata:
========================
Original URL: https://simonscat.pages.dev
Prompt: Write a Python script to create a simple quiz that determines which Simon's Cat character a user is, based on a few easy questions.
Generated: DETERMINISTIC_459b38d53889add9
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_user_input(prompt, options):
    """
    Get validated user input based on the provided options.

    Args:
        prompt (str): The question to display to the user.
        options (list): A list of valid options for the user to choose from.

    Returns:
        str: The user's validated choice.
    """
    while True:
        print(prompt)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def determine_character(answers):
    """
    Determine the Simon's Cat character based on the user's answers.

    Args:
<<<<<<< HEAD
        answers (list): A list of answers provided by the user.
=======
        answers (list): A list of the user's answers.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

    Returns:
        str: The name of the Simon's Cat character.
    """
    # Simple logic to determine the character based on answers
    if answers.count("Playful") > answers.count("Lazy"):
        return "Simon's Cat"
    elif answers.count("Lazy") > answers.count("Playful"):
        return "The Kitten"
    elif answers.count("Mischievous") > answers.count("Calm"):
        return "The Hedgehog"
    else:
<<<<<<< HEAD
        return "The Toad"
=======
        return "Simon's Cat's Friend (Pigeon)"
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

def main():
    """
    Main function to run the quiz.
    """
    print("Welcome to the Simon's Cat Character Quiz!")
    print("Answer the following questions to find out which character you are.\n")

    try:
        # Questions and options
        questions = [
<<<<<<< HEAD
            ("What is your favorite activity?", ["Sleeping", "Playing", "Exploring", "Eating"]),
            ("How would your friends describe you?", ["Lazy", "Playful", "Mischievous", "Calm"]),
            ("What is your favorite time of day?", ["Morning", "Afternoon", "Evening", "Night"]),
=======
            ("What is your energy level?", ["Playful", "Lazy"]),
            ("How do you approach challenges?", ["Mischievous", "Calm"]),
            ("What is your favorite activity?", ["Exploring", "Relaxing"]),
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        ]

        # Collect answers
        answers = []
        for question, options in questions:
            answer = get_user_input(question, options)
            answers.append(answer)

        # Determine the character
        character = determine_character(answers)
<<<<<<< HEAD
        print(f"\nYou are most like: {character}!")
=======
        print(f"\nYou are: {character}!")
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Goodbye!")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
