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
import time
import random
import sys
import os
from datetime import datetime

class EyeExerciseGuide:
    """
    A simple eye exercise guide to reduce eye strain and improve vision.
    Includes techniques like sehtraining and augentherapie.
    """
    
    def __init__(self):
        """Initialize the exercise guide with default settings."""
        self.exercises = [
            {
                'name': 'Palming',
                'description': 'Rub your hands together to warm them, then gently cup them over your closed eyes without applying pressure. Relax for 1 minute.',
                'duration': 60
            },
            {
                'name': 'Eye Rolling',
                'description': 'Slowly roll your eyes in a circular motion clockwise for 10 seconds, then counter-clockwise for 10 seconds.',
                'duration': 20
            },
            {
                'name': 'Focus Shifting',
                'description': 'Hold your thumb 10 inches from your face and focus on it. Then shift focus to an object 10-20 feet away. Alternate for 1 minute.',
                'duration': 60
            },
            {
                'name': 'Figure Eight',
                'description': 'Imagine a giant figure eight 10 feet away. Trace it with your eyes slowly for 30 seconds.',
                'duration': 30
            },
            {
                'name': 'Near and Far Focus',
                'description': 'Focus on a nearby object for 5 seconds, then shift to a distant object for 5 seconds. Repeat for 1 minute.',
                'duration': 60
            },
            {
                'name': 'Blinking',
                'description': 'Blink rapidly for 10 seconds to refresh your eyes.',
                'duration': 10
            }
        ]
        self.user_settings = {
            'exercise_duration_factor': 1.0,
            'rest_between_exercises': True,
            'rest_duration': 10
        }
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        """Display welcome message and instructions."""
        self.clear_screen()
        print("""
        ====================================
        |    EYE EXERCISE GUIDE            |
        ====================================
        This program will guide you through exercises to:
        - Reduce eye strain
        - Improve vision
        - Incorporate sehtraining and augentherapie techniques
        
        Follow the on-screen instructions.
        Press Ctrl+C at any time to exit.
        """)
        input("\nPress Enter to begin...")
    
    def get_user_settings(self):
        """Get user preferences for the exercise session."""
        self.clear_screen()
        print("Configure your exercise session:")
        
        try:
            factor = float(input("Exercise duration factor (0.5-2.0, default 1.0): ") or "1.0")
            if 0.5 <= factor <= 2.0:
                self.user_settings['exercise_duration_factor'] = factor
            else:
                print("Invalid input. Using default factor (1.0).")
            
            rest = input("Rest between exercises? (y/n, default y): ") or "y"
            self.user_settings['rest_between_exercises'] = rest.lower() == 'y'
            
            if self.user_settings['rest_between_exercises']:
                duration = int(input("Rest duration in seconds (default 10): ") or "10")
                self.user_settings['rest_duration'] = max(5, min(60, duration))
                
        except ValueError:
            print("Invalid input. Using default settings.")
    
    def run_exercise(self, exercise):
        """Run a single exercise with countdown timer."""
        self.clear_screen()
        print(f"\nExercise: {exercise['name']}\n")
        print(exercise['description'])
        print("\nGet ready to begin...")
        
        duration = int(exercise['duration'] * self.user_settings['exercise_duration_factor'])
        
        try:
            for remaining in range(duration, 0, -1):
                print(f"Time remaining: {remaining} seconds", end='\r')
                time.sleep(1)
            print("Exercise completed!                    ")
        except KeyboardInterrupt:
            print("\nExercise interrupted.")
            return False
        
        return True
    
    def rest_period(self):
        """Handle rest period between exercises."""
        if not self.user_settings['rest_between_exercises']:
            return True
            
        self.clear_screen()
        print("\nRest period. Close your eyes and relax.")
        print(f"Duration: {self.user_settings['rest_duration']} seconds\n")
        
        try:
            for remaining in range(self.user_settings['rest_duration'], 0, -1):
                print(f"Time remaining: {remaining} seconds", end='\r')
                time.sleep(1)
            print("Rest period over.                     ")
        except KeyboardInterrupt:
            print("\nRest period interrupted.")
            return False
        
        return True
    
    def select_exercises(self):
        """Select exercises for the session, either random or specific."""
        self.clear_screen()
        print("Select exercise mode:")
        print("1. Full routine (all exercises)")
        print("2. Random selection")
        print("3. Custom selection")
        
        choice = input("Enter your choice (1-3, default 1): ") or "1"
        
        if choice == "1":
            return self.exercises.copy()
        elif choice == "2":
            count = min(len(self.exercises), max(1, int(input("How many exercises? (default 3): ") or "3")))
            return random.sample(self.exercises, count)
        elif choice == "3":
            print("\nAvailable exercises:")
            for i, ex in enumerate(self.exercises, 1):
                print(f"{i}. {ex['name']}")
            
            selected = input("Enter exercise numbers separated by commas (e.g., 1,3,5): ")
            try:
                indices = [int(i.strip()) - 1 for i in selected.split(',') if i.strip().isdigit()]
                return [self.exercises[i] for i in indices if 0 <= i < len(self.exercises)]
            except ValueError:
                print("Invalid selection. Using full routine.")
                return self.exercises.copy()
        else:
            return self.exercises.copy()
    
    def run_session(self):
        """Run a complete exercise session."""
        exercises = self.select_exercises()
        
        if not exercises:
            print("No exercises selected. Exiting.")
            return
            
        self.get_user_settings()
        self.display_welcome()
        
        for exercise in exercises:
            if not self.run_exercise(exercise):
                break
                
            if exercise != exercises[-1] and not self.rest_period():
                break
    
    def save_session_log(self):
        """Log the session details to a file."""
        log_entry = f"Session completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        log_entry += f"Settings: {self.user_settings}\n"
        
        try:
            with open('eye_exercise_log.txt', 'a') as f:
                f.write(log_entry + "\n")
        except IOError:
            print("Warning: Could not save session log.")
    
    def main(self):
        """Main program loop."""
        try:
            while True:
                self.run_session()
                self.save_session_log()
                
                again = input("\nWould you like to do another session? (y/n): ").lower()
                if again != 'y':
                    break
                    
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
        finally:
            print("\nThank you for using the Eye Exercise Guide. Take care of your eyes!")

if __name__ == "__main__":
    guide = EyeExerciseGuide()
    guide.main()
```
