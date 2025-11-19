"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selffeeling.com
Prompt: Generate a Python script that incorporates mindfulness exercises for emotional well-being, as described in the Self-Feeling Program.
Generated: DETERMINISTIC_8833db82be735a23
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Mindfulness Exercises Script for Emotional Well-Being
This script provides a series of mindfulness exercises to promote emotional well-being.
Users can select an activity and follow guided steps to practice mindfulness.
"""

import time
import sys

def welcome_message():
    """
    Displays a welcome message to the user.
    """
    print("Welcome to the Mindfulness Exercise Program!")
    print("Feel free to take a moment for yourself and practice mindfulness.")
    print("Select an exercise from the menu below to begin.\n")

def breathing_exercise():
    """
    Guides the user through a simple breathing exercise.
    """
    try:
        print("\nBreathing Exercise: Focus on your breath.")
        print("For the next few minutes, follow these instructions:")
        for i in range(3):
            print("\nInhale deeply through your nose (4 seconds)...")
            time.sleep(4)
            print("Hold your breath (4 seconds)...")
            time.sleep(4)
            print("Exhale slowly through your mouth (6 seconds)...")
            time.sleep(6)
        print("\nGreat job! You've completed the breathing exercise. Feel free to repeat as needed.\n")
    except Exception as e:
        print(f"An error occurred during the breathing exercise: {e}")

def body_scan_exercise():
    """
    Guides the user through a body scan relaxation exercise.
    """
    try:
        print("\nBody Scan Exercise: Relax and connect with your body.")
        areas = ["head", "neck", "shoulders", "arms", "chest", "abdomen", "legs", "feet"]
        for area in areas:
            print(f"Focus on your {area}. Notice any tension or sensations. Let go of any stress.")
            time.sleep(5)
        print("\nWonderful! You've completed the body scan exercise. Feel free to repeat as needed.\n")
    except Exception as e:
        print(f"An error occurred during the body scan exercise: {e}")

def gratitude_exercise():
    """
    Guides the user through a gratitude reflection exercise.
    """
    try:
        print("\nGratitude Exercise: Reflect on the positive aspects of your life.")
        for i in range(3):
            print(f"Think of something or someone you're grateful for ({i+1}/3). Hold that thought for a few moments.")
            time.sleep(5)
        print("\nAmazing! You've completed the gratitude exercise. Feel free to repeat as needed.\n")
    except Exception as e:
        print(f"An error occurred during the gratitude exercise: {e}")

def menu():
    """
    Displays the menu of mindfulness exercises and handles user input.
    """
    exercises = {
        "1": ("Breathing Exercise", breathing_exercise),
        "2": ("Body Scan Exercise", body_scan_exercise),
        "3": ("Gratitude Exercise", gratitude_exercise),
        "4": ("Exit", None)
    }

    while True:
        print("Please choose an exercise:")
        for key, value in exercises.items():
            print(f"{key}. {value[0]}")

        choice = input("\nEnter the number of your choice: ").strip()
        if choice in exercises:
            if choice == "4":
                print("Thank you for participating in the Mindfulness Exercise Program. Take care!")
                break
            else:
                print(f"\nYou have chosen: {exercises[choice][0]}")
                exercises[choice][1]()  # Call the corresponding exercise function
        else:
            print("Invalid choice. Please select a valid option.\n")

def main():
    """
    Main entry point of the program.
    """
    try:
        welcome_message()
        menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
