"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Write a Python script that implements educational activities for children aged 4 to 9, focusing on values such as respect, participation, and responsibility as outlined in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_6392bee3b81cc289
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Educational Activities Script for Children (Ages 4 to 9)
Focuses on values: Respect, Participation, Responsibility
Inspired by "Vivir es Convivir" Program
"""

import random

def main():
    try:
        print("Welcome to the Educational Activities Program!")
        print("This program focuses on teaching Respect, Participation, and Responsibility.")
        print("Choose an activity:")
        print("1. Respect - 'Guess the Emotion'")
        print("2. Participation - 'Team Story Building'")
        print("3. Responsibility - 'Helping Hands Challenge'")
        
        choice = int(input("Enter the number of your chosen activity: "))
        
        if choice == 1:
            play_respect_activity()
        elif choice == 2:
            play_participation_activity()
        elif choice == 3:
            play_responsibility_activity()
        else:
            print("Invalid choice. Please restart the program and choose a valid option.")
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def play_respect_activity():
    """
    Activity: Respect - 'Guess the Emotion'
    A game to help children understand and respect emotions.
    """
    print("\nActivity: Respect - 'Guess the Emotion'")
    emotions = ["happy", "sad", "angry", "surprised", "scared", "excited"]
    emotion = random.choice(emotions)
    
    print("I am thinking of an emotion...")
    print("Hint: It could be one of these:", ", ".join(emotions))
    
    attempts = 3
    while attempts > 0:
        guess = input("Guess the emotion: ").lower()
        if guess == emotion:
            print("Correct! Great job respecting and understanding emotions!")
            return
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")
    
    print(f"Out of attempts! The correct emotion was '{emotion}'.")


def play_participation_activity():
    """
    Activity: Participation - 'Team Story Building'
    A collaborative story-building activity emphasizing teamwork.
    """
    print("\nActivity: Participation - 'Team Story Building'")
    print("Let's build a story together! Each person adds one sentence.")
    print("Type 'done' when the story is finished.")
    
    story = []
    while True:
        sentence = input("Add a sentence to the story: ")
        if sentence.lower() == "done":
            break
        story.append(sentence)
    
    print("\nHere is the story you created together:")
    print(" ".join(story))
    print("Great job working together and participating!")


def play_responsibility_activity():
    """
    Activity: Responsibility - 'Helping Hands Challenge'
    A challenge to encourage responsible behavior and helpfulness.
    """
    print("\nActivity: Responsibility - 'Helping Hands Challenge'")
    print("List some actions you can take to help others today.")
    print("For example: 'tidy my toys', 'help a friend', 'say thank you'.")
    
    actions = []
    while True:
        action = input("Enter an action (or type 'done' to finish): ")
        if action.lower() == "done":
            break
        actions.append(action)
    
    print("\nHere are the actions you listed:")
    for i, action in enumerate(actions, start=1):
        print(f"{i}. {action}")
    
    print("Well done! Remember to act responsibly and help others.")


if __name__ == "__main__":
    main()
```
