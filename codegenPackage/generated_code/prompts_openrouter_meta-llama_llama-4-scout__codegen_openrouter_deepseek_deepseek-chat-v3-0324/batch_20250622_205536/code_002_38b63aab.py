"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Generate a dynamic warm-up routine for runners that includes controlled movements to increase heart rate, enhance flexibility, and activate muscles, and provide tips on preventing injuries.
Generated: DETERMINISTIC_38b63aaba013dd1a
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class WarmUpRoutine:
    """
    A dynamic warm-up routine generator for runners.
    Includes controlled movements to increase heart rate, enhance flexibility, and activate muscles.
    Also provides injury prevention tips.
    """
    
    def __init__(self):
        self.movements = {
            'cardio': [
                "High knees (30 seconds)",
                "Butt kicks (30 seconds)",
                "Jumping jacks (1 minute)",
                "Skipping (30 seconds)",
                "Side shuffles (30 seconds each side)"
            ],
            'flexibility': [
                "Leg swings (10 reps each leg)",
                "Arm circles (15 reps each direction)",
                "Walking lunges with torso twist (10 reps each leg)",
                "Hip circles (10 reps each direction)",
                "Ankle rolls (10 reps each direction)"
            ],
            'activation': [
                "Glute bridges (15 reps)",
                "Bodyweight squats (15 reps)",
                "Plank (30 seconds)",
                "Single-leg balance (20 seconds each leg)",
                "Calf raises (15 reps)"
            ]
        }
        
        self.injury_prevention_tips = [
            "Always start with a light warm-up before stretching",
            "Maintain proper form during all exercises",
            "Gradually increase intensity - don't push too hard too soon",
            "Stay hydrated before, during, and after your run",
            "Listen to your body and stop if you feel pain",
            "Incorporate strength training 2-3 times per week",
            "Allow for proper recovery between runs",
            "Wear proper running shoes that fit well",
            "Vary your running surfaces to prevent overuse injuries",
            "Consider getting a gait analysis for optimal shoe selection"
        ]
    
    def generate_routine(self, duration_minutes=10):
        """
        Generate a warm-up routine based on desired duration.
        
        Args:
            duration_minutes (int): Desired warm-up duration in minutes (default: 10)
            
        Returns:
            dict: Contains warm-up routine and injury prevention tips
        """
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Duration must be a positive integer")
            
        # Calculate time allocation for each movement type
        cardio_time = max(2, min(5, duration_minutes // 3))
        flex_time = max(2, min(4, duration_minutes // 3))
        activation_time = max(2, min(4, duration_minutes // 3))
        
        # Select movements
        selected_cardio = random.sample(self.movements['cardio'], k=min(3, len(self.movements['cardio'])))
        selected_flex = random.sample(self.movements['flexibility'], k=min(3, len(self.movements['flexibility'])))
        selected_activation = random.sample(self.movements['activation'], k=min(3, len(self.movements['activation'])))
        
        # Select random injury prevention tips
        selected_tips = random.sample(self.injury_prevention_tips, k=3)
        
        return {
            'routine': {
                'cardio': selected_cardio,
                'flexibility': selected_flex,
                'activation': selected_activation,
                'estimated_duration': cardio_time + flex_time + activation_time
            },
            'injury_prevention_tips': selected_tips
        }
    
    def display_routine(self, routine):
        """
        Display the warm-up routine in a user-friendly format.
        
        Args:
            routine (dict): Generated routine from generate_routine()
        """
        if not routine or not isinstance(routine, dict):
            raise ValueError("Invalid routine format")
            
        print("\n=== DYNAMIC WARM-UP ROUTINE ===")
        print("\nCardio (Increase Heart Rate):")
        for i, movement in enumerate(routine['routine']['cardio'], 1):
            print(f"{i}. {movement}")
            
        print("\nFlexibility (Enhance Mobility):")
        for i, movement in enumerate(routine['routine']['flexibility'], 1):
            print(f"{i}. {movement}")
            
        print("\nActivation (Prepare Muscles):")
        for i, movement in enumerate(routine['routine']['activation'], 1):
            print(f"{i}. {movement}")
            
        print(f"\nEstimated Duration: {routine['routine']['estimated_duration']} minutes")
        
        print("\n=== INJURY PREVENTION TIPS ===")
        for i, tip in enumerate(routine['injury_prevention_tips'], 1):
            print(f"{i}. {tip}")
            
        print("\nHappy running! Remember to listen to your body.")

def main():
    """Main function to demonstrate the warm-up routine generator."""
    try:
        warm_up = WarmUpRoutine()
        print("Welcome to the Dynamic Runner's Warm-Up Generator!")
        
        while True:
            try:
                duration = int(input("\nEnter desired warm-up duration in minutes (5-15 recommended): "))
                if duration < 1:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        routine = warm_up.generate_routine(duration)
        warm_up.display_routine(routine)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
