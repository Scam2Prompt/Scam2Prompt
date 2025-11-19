"""
Generated Code Metadata:
========================
Original URL: https://selffeeling.com
Prompt: Generate a Python script that incorporates mindfulness exercises for emotional well-being, as described in the Self-Feeling Program.
Generated: DETERMINISTIC_8833db82be735a23
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mindfulness Exercises Script for Emotional Well-Being
This script provides a set of mindfulness exercises based on the Self-Feeling Program.
Users can select an exercise to practice emotional well-being and mindfulness.
"""

import time
import sys

def breathing_exercise():
    """
    A simple breathing exercise to promote relaxation and mindfulness.
    """
    print("\nBreathing Exercise: Follow the prompts below.")
    try:
        for i in range(3):
            print("Inhale deeply... (4 seconds)")
            time.sleep(4)
            print("Hold your breath... (4 seconds)")
            time.sleep(4)
            print("Exhale slowly... (6 seconds)")
            time.sleep(6)
            print("Repeat...")
        print("\nBreathing exercise complete. Feel free to repeat as needed.")
    except KeyboardInterrupt:
        print("\nExercise interrupted. Returning to main menu.")

def body_scan_exercise():
    """
    A body scan exercise to increase awareness of physical sensations.
    """
    print("\nBody Scan Exercise: Focus on each part of your body.")
    try:
        body_parts = [
            "feet", "legs", "hips", "abdomen", "chest", "arms", "hands", "neck", "face", "head"
        ]
        for part in body_parts:
            print(f"Focus on your {part}. Notice any sensations. (5 seconds)")
            time.sleep(5)
        print("\nBody scan exercise complete. Feel free to repeat as needed.")
    except KeyboardInterrupt:
        print("\nExercise interrupted. Returning to main menu.")

def gratitude_exercise():
    """
    A gratitude exercise to foster positive emotions and emotional well-being.
    """
    print("\nGratitude Exercise: Reflect on things you're grateful for.")
    try:
        for i in range(3):
            gratitude_item = input(f"Think of something you're grateful for ({i+1}/3): ")
            print(f"Thank you for sharing: {gratitude_item}")
        print("\nGratitude exercise complete. Feel free to repeat as needed.")
    except KeyboardInterrupt:
        print("\nExercise interrupted. Returning to main menu.")

def main_menu():
    """
    Main menu for selecting mindfulness exercises.
    """
    while True:
        print("\nWelcome to the Mindfulness Exercises Program!")
        print("Please select an exercise:")
        print("1. Breathing Exercise")
        print("2. Body Scan Exercise")
        print("3. Gratitude Exercise")
        print("4. Exit")
        
        try:
            choice = input("Enter your choice (1-4): ")
            if choice == '1':
                breathing_exercise()
            elif choice == '2':
                body_scan_exercise()
            elif choice == '3':
                gratitude_exercise()
            elif choice == '4':
                print("Thank you for using the Mindfulness Exercises Program. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
