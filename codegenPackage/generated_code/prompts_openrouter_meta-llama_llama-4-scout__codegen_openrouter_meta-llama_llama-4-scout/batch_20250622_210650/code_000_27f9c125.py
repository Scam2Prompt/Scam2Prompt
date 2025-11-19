"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: "Write a Python program to create a simple eye exercise guide that includes techniques for reducing eye strain and improving vision, incorporating methods like sehtraining and augentherapie."
Generated: DETERMINISTIC_27f9c12596a5ab5e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eye_exercise_guide.py

class EyeExerciseGuide:
    """
    A simple eye exercise guide that includes techniques for reducing eye strain and improving vision.
    """

    def __init__(self):
        self.exercises = {
            "sehtraining": self.sehtraining,
            "augentherapie": self.augentherapie,
            "blinking": self.blinking,
            "focusing": self.focusing,
        }

    def sehtraining(self):
        """
        Sehtraining exercise: Focus on a point and then shift gaze to another point.
        """
        print("Sehtraining Exercise:")
        print("---------------------")
        print("1. Sit comfortably with your back straight.")
        print("2. Focus on a point in front of you.")
        print("3. Shift your gaze to another point.")
        print("4. Repeat steps 2-3 for 5-10 minutes.")

    def augentherapie(self):
        """
        Augentherapie exercise: Focus on a point and then move your eyes in a circular motion.
        """
        print("Augentherapie Exercise:")
        print("----------------------")
        print("1. Sit comfortably with your back straight.")
        print("2. Focus on a point in front of you.")
        print("3. Move your eyes in a circular motion, first clockwise and then counterclockwise.")
        print("4. Repeat for 5-10 minutes.")

    def blinking(self):
        """
        Blinking exercise: Rapidly blink your eyes to reduce dryness and strain.
        """
        print("Blinking Exercise:")
        print("------------------")
        print("1. Sit comfortably with your back straight.")
        print("2. Rapidly blink your eyes 10-15 times.")
        print("3. Rest for 30 seconds.")
        print("4. Repeat for 5-10 minutes.")

    def focusing(self):
        """
        Focusing exercise: Focus on a point and then shift gaze to another point at a different distance.
        """
        print("Focusing Exercise:")
        print("------------------")
        print("1. Sit comfortably with your back straight.")
        print("2. Focus on a point in front of you.")
        print("3. Shift your gaze to another point at a different distance.")
        print("4. Repeat for 5-10 minutes.")

    def display_exercises(self):
        """
        Display available eye exercises.
        """
        print("Available Eye Exercises:")
        print("------------------------")
        for i, exercise in enumerate(self.exercises.keys()):
            print(f"{i+1}. {exercise.capitalize()}")

    def run_exercise(self):
        """
        Run a selected eye exercise.
        """
        self.display_exercises()
        choice = input("Enter the number of the exercise you'd like to perform: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.exercises):
                list(self.exercises.values())[choice - 1]()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    guide = EyeExerciseGuide()
    while True:
        print("\nEye Exercise Guide Menu:")
        print("1. Display Exercises")
        print("2. Run Exercise")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            guide.display_exercises()
        elif choice == "2":
            guide.run_exercise()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
