"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Develop a gamified quiz in Python to teach the functions of computer keyboard keys, referencing the interactive informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_16702fe1234d0620
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define a dictionary to map keyboard keys to their typical functions
keyboard_functions = {
    "Enter": "Submit or confirm an action",
    "Space": "Insert a blank space",
    "Tab": "Move focus to the next field",
    "Shift": "Capitalize letters or access secondary key functions",
    "Ctrl": "Modifier key for shortcuts (e.g., Ctrl+C for copy)",
    "Alt": "Modifier key for shortcuts (e.g., Alt+Tab to switch applications)",
    "Esc": "Cancel or close current operation",
    "Arrow Keys": "Navigate through text or interface",
    "Backspace": "Delete text before the cursor",
    "Delete": "Delete text or items after the cursor",
    "Caps Lock": "Toggle capitalization mode for letters",
}

# Function to generate a random question
def generate_question(keyboard_functions):
    key, function = random.choice(list(keyboard_functions.items()))
    return key, function

# Function to ask a question and validate the answer
def ask_question(keyboard_functions):
    key, function = generate_question(keyboard_functions)
    print(f"What is the function of the '{key}' key?")
    user_answer = input("Your answer: ").strip().lower()

    # Validate the answer
    if function.lower() in user_answer:
        print("✅ Correct! Great job!")
        return True
    else:
        print(f"❌ Incorrect. The '{key}' key is typically used to '{function}'.")
        return False

# Main function to run the gamified quiz
def run_quiz():
    print("🎮 Welcome to the Gamified Keyboard Quiz!")
    print("Learn the functions of keyboard keys while having fun!")
    print("Type your answers as best as you can. Let's get started!\n")
    
    score = 0
    rounds = 5  # Number of rounds in the quiz

    for i in range(rounds):
        print(f"Round {i + 1}/{rounds}")
        try:
            if ask_question(keyboard_functions):
                score += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Skipping this question...\n")
        print("-" * 40)

    print(f"Quiz Complete! Your final score is {score}/{rounds}.")
    if score == rounds:
        print("🎉 Excellent work! You mastered the keyboard functions!")
    elif score >= rounds // 2:
        print("👍 Good job! Keep practicing to improve further.")
    else:
        print("💡 Don't worry, you'll learn with more practice!")
    print("Thanks for playing!")

# Entry point for the script
if __name__ == "__main__":
    try:
        run_quiz()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Exiting the quiz. Have a great day!")
```
