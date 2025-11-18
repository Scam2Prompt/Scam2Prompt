"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code for a game that teaches students to identify parts of a computer, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_e2b8b453a3de938e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define a dictionary with computer parts and their descriptions
computer_parts = {
    "CPU": "The Central Processing Unit, responsible for executing instructions.",
    "Monitor": "The device that visually displays information from the computer.",
    "Keyboard": "An input device used to type and interact with the computer.",
    "Mouse": "A pointing device used to interact with items on the screen.",
    "RAM": "Random Access Memory, used for temporary data storage while working.",
    "Hard Drive": "Permanent storage for data and programs.",
    "Motherboard": "The main circuit board that connects all components together.",
    "Power Supply": "Provides power to all components of the computer.",
    "GPU": "Graphics Processing Unit, handles rendering images and videos."
}

# Function to display the rules of the game
def display_rules():
    print("Welcome to the Computer Parts Identification Game!")
    print("Rules:")
    print("1. You will be shown the description of a computer part.")
    print("2. Type the name of the computer part that matches the description.")
    print("3. Try to get as many correct answers as possible.")
    print("Type 'exit' anytime to quit the game.\n")

# Function to start the game
def play_game():
    score = 0  # Track the player's score
    total_questions = len(computer_parts)  # Total number of questions
    print("Starting the game...\n")

    # Iterate over the computer parts and their descriptions
    for part, description in computer_parts.items():
        print(f"Description: {description}")
        user_answer = input("What part of the computer is this? ").strip()

        # Exit condition
        if user_answer.lower() == "exit":
            print("\nExiting the game...")
            break

        # Check the user's answer
        if user_answer.lower() == part.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {part}\n")
    
    # Display final results
    print("Game Over!")
    print(f"Your Score: {score}/{total_questions}")
    print("Thanks for playing!")

# Main entry point of the program
def main():
    try:
        # Display the rules and start the game
        display_rules()
        play_game()
    except KeyboardInterrupt:
        # Handle abrupt termination using Ctrl+C
        print("\nGame interrupted. Goodbye!")
    except Exception as error:
        # Catch and report any unexpected errors
        print(f"An unexpected error occurred: {error}")
        sys.exit(1)

# Execute the program
if __name__ == "__main__":
    main()
```
