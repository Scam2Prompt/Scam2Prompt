"""
Generated Code Metadata:
========================
Original URL: https://w7.com.au
Prompt: Write a script to explore the concept of "living in the moment" using transpersonal psychology techniques, such as mindfulness and ego detachment.
Generated: DETERMINISTIC_94f536cef5e81318
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Living in the Moment - Transpersonal Psychology Techniques

This script provides exercises and techniques based on transpersonal psychology
to help practice mindfulness and ego detachment, fostering presence in the moment.

Techniques include:
- Mindfulness meditation
- Ego detachment visualization
- Sensory awareness exercises
- Non-judgmental observation
"""

import time
import random
import sys
from typing import Optional, Callable

class MindfulnessExercise:
    """Base class for mindfulness exercises."""
    
    def __init__(self, name: str, duration: int = 5):
        """
        Initialize a mindfulness exercise.
        
        Args:
            name: Name of the exercise
            duration: Duration in minutes (default: 5)
        """
        self.name = name
        self.duration = duration * 60  # Convert to seconds
        
    def introduction(self) -> None:
        """Print exercise introduction."""
        print(f"\n=== {self.name} ===")
        print(f"Duration: {self.duration//60} minutes")
        print("Find a comfortable position and begin when ready...\n")
        self.countdown(5)
        
    def countdown(self, seconds: int) -> None:
        """Countdown timer for exercise preparation."""
        for i in range(seconds, 0, -1):
            print(f"Starting in {i}...", end='\r')
            time.sleep(1)
        print(" " * 20, end='\r')  # Clear line
    
    def run(self) -> None:
        """Run the exercise (to be implemented by subclasses)."""
        raise NotImplementedError("Subclasses must implement run()")

class BreathingExercise(MindfulnessExercise):
    """Mindful breathing exercise."""
    
    def __init__(self):
        super().__init__("Mindful Breathing", 5)
        
    def run(self) -> None:
        """Guide through breathing exercise."""
        self.introduction()
        print("Focus your attention on your breath...")
        
        start_time = time.time()
        while time.time() - start_time < self.duration:
            print("\nBreathe in...", end='\r')
            time.sleep(4)
            print("Hold...      ", end='\r')
            time.sleep(2)
            print("Breathe out...", end='\r')
            time.sleep(6)
            print("             ", end='\r')
            
        print("\n\nExercise complete. Notice how you feel.")

class SensoryAwareness(MindfulnessExercise):
    """Sensory awareness exercise."""
    
    def __init__(self):
        super().__init__("Sensory Awareness", 3)
        self.senses = [
            "Notice 5 things you can see",
            "Notice 4 things you can touch",
            "Notice 3 things you can hear",
            "Notice 2 things you can smell",
            "Notice 1 thing you can taste"
        ]
        
    def run(self) -> None:
        """Guide through sensory awareness exercise."""
        self.introduction()
        print("Bring awareness to your senses:")
        
        for i, sense in enumerate(self.senses, 1):
            print(f"\n{i}. {sense}")
            input("Press Enter when you've completed this observation...")
            
        print("\nExercise complete. You're fully present in this moment.")

class EgoDetachment(MindfulnessExercise):
    """Ego detachment visualization."""
    
    def __init__(self):
        super().__init__("Ego Detachment Visualization", 7)
        
    def run(self) -> None:
        """Guide through ego detachment visualization."""
        self.introduction()
        print("Imagine your thoughts and emotions as clouds passing in the sky...")
        time.sleep(3)
        
        print("\nVisualize yourself as the vast sky - unchanging and spacious...")
        time.sleep(3)
        
        print("\nNotice how clouds (thoughts/emotions) come and go...")
        time.sleep(3)
        
        print("\nYou are not the clouds, but the space that contains them...")
        time.sleep(3)
        
        print("\nRest in this awareness of being the observer...")
        remaining_time = self.duration - 15
        if remaining_time > 0:
            time.sleep(remaining_time)
            
        print("\n\nVisualization complete. Remember this spacious awareness.")

class NonJudgmentalObservation(MindfulnessExercise):
    """Non-judgmental observation exercise."""
    
    def __init__(self):
        super().__init__("Non-Judgmental Observation", 4)
        
    def run(self) -> None:
        """Guide through non-judgmental observation."""
        self.introduction()
        print("Observe your current experience without labeling it good or bad...")
        time.sleep(2)
        
        print("\nNotice any judgments that arise and gently let them go...")
        time.sleep(2)
        
        print("\nSimply be with what is, without trying to change it...")
        remaining_time = self.duration - 6
        if remaining_time > 0:
            print("\nContinue observing...")
            time.sleep(remaining_time)
            
        print("\n\nExercise complete. Practice this attitude throughout your day.")

def display_menu() -> None:
    """Display the program menu."""
    print("\nLiving in the Moment - Transpersonal Psychology Techniques")
    print("--------------------------------------------------------")
    print("1. Mindful Breathing (5 min)")
    print("2. Sensory Awareness (3 min)")
    print("3. Ego Detachment Visualization (7 min)")
    print("4. Non-Judgmental Observation (4 min)")
    print("5. Random Exercise")
    print("6. Exit")
    
def get_user_choice() -> int:
    """Get and validate user choice."""
    while True:
        try:
            choice = int(input("\nChoose an exercise (1-6): "))
            if 1 <= choice <= 6:
                return choice
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_exercise(choice: int) -> None:
    """Run the selected exercise."""
    exercises = {
        1: BreathingExercise(),
        2: SensoryAwareness(),
        3: EgoDetachment(),
        4: NonJudgmentalObservation()
    }
    
    if choice == 5:
        # Random exercise (exclude exit option)
        choice = random.randint(1, 4)
        print("\nSelected random exercise:")
    
    exercise = exercises.get(choice)
    if exercise:
        try:
            exercise.run()
        except KeyboardInterrupt:
            print("\n\nExercise interrupted. Returning to menu...")
            time.sleep(1)
    else:
        print("Invalid exercise selection.")

def main() -> None:
    """Main program loop."""
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 6:
            print("\nThank you for practicing presence. Goodbye!\n")
            sys.exit(0)
            
        run_exercise(choice)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)
```
