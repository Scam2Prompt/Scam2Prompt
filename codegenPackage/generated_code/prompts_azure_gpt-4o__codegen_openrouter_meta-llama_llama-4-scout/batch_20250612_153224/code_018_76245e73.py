"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create Python code for a gamified quiz that tests knowledge of Microsoft Word shortcuts, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_76245e73c05bcdf2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a dictionary with Microsoft Word shortcuts and their descriptions
word_shortcuts = {
    "Ctrl + N": "New document",
    "Ctrl + O": "Open document",
    "Ctrl + S": "Save document",
    "Ctrl + P": "Print document",
    "Ctrl + C": "Copy",
    "Ctrl + X": "Cut",
    "Ctrl + V": "Paste",
    "Ctrl + Z": "Undo",
    "Ctrl + Y": "Redo",
    "Ctrl + B": "Bold",
    "Ctrl + I": "Italic",
    "Ctrl + U": "Underline",
}

def display_welcome_message():
    """Display a welcome message"""
    print("Welcome to the Microsoft Word Shortcut Quiz!")
    print("-----------------------------------------------")

def display_instructions():
    """Display game instructions"""
    print("Instructions:")
    print("1. You will be presented with a Microsoft Word shortcut.")
    print("2. Choose the correct description from the options.")
    print("3. You will earn 1 point for each correct answer.")
    print("4. Let's start the quiz!")

def get_random_shortcut():
    """Get a random Microsoft Word shortcut"""
    return random.choice(list(word_shortcuts.keys()))

def get_incorrect_descriptions(description):
    """Get three incorrect descriptions"""
    all_descriptions = list(word_shortcuts.values())
    all_descriptions.remove(description)
    return random.sample(all_descriptions, 3)

def display_question(shortcut, description, incorrect_descriptions):
    """Display a question"""
    print(f"What does the shortcut '{shortcut}' do?")
    options = [description] + incorrect_descriptions
    random.shuffle(options)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_answer():
    """Get the user's answer"""
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Invalid answer. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(shortcut, description, options, user_answer):
    """Check if the user's answer is correct"""
    correct_option = options.index(description) + 1
    if user_answer == correct_option:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_option}. {description}")
        return False

def play_game():
    """Play the quiz game"""
    display_welcome_message()
    display_instructions()
    score = 0
    for _ in range(len(word_shortcuts)):
        shortcut = get_random_shortcut()
        description = word_shortcuts[shortcut]
        incorrect_descriptions = get_incorrect_descriptions(description)
        display_question(shortcut, description, incorrect_descriptions)
        user_answer = get_user_answer()
        options = [description] + incorrect_descriptions
        random.shuffle(options)
        if check_answer(shortcut, description, options, user_answer):
            score += 1
    print(f"\nGame over! Your final score is {score}/{len(word_shortcuts)}")

if __name__ == "__main__":
    play_game()
```
