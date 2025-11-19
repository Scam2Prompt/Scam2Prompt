"""
Generated Code Metadata:
========================
Original URL: https://stronglp.com
Prompt: Generate a sample training program for a 64-year-old individual recovering from a broken hand and knee surgery, focusing on strength maintenance and improvement.
Generated: DETERMINISTIC_670583aedb06c154
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Training Program for a 64-year-old Recovering from Hand Fracture and Knee Surgery
Focus: Strength Maintenance and Improvement with Safety Considerations
"""

import datetime
from typing import Dict, List, Optional

class Exercise:
    """Base class for exercise definitions"""
    def __init__(self, name: str, description: str, sets: int, reps: int, 
                 weight: Optional[float] = None, duration: Optional[int] = None):
        self.name = name
        self.description = description
        self.sets = sets
        self.reps = reps
        self.weight = weight  # in kg, None for bodyweight
        self.duration = duration  # in seconds, None for rep-based exercises
        
    def __str__(self) -> str:
        return f"{self.name}: {self.description} ({self.sets}x{self.reps})"

class TrainingSession:
    """Represents a single training session"""
    def __init__(self, date: datetime.date, exercises: List[Exercise], notes: str = ""):
        self.date = date
        self.exercises = exercises
        self.notes = notes
        
    def add_exercise(self, exercise: Exercise) -> None:
        """Add an exercise to the session"""
        self.exercises.append(exercise)
        
    def get_session_summary(self) -> str:
        """Returns formatted session summary"""
        summary = f"Session Date: {self.date}\nExercises:\n"
        for i, ex in enumerate(self.exercises, 1):
            summary += f"{i}. {ex}\n"
        if self.notes:
            summary += f"\nNotes: {self.notes}"
        return summary

class RecoveryProgram:
    """Main class for managing the recovery training program"""
    def __init__(self, patient_name: str, start_date: datetime.date):
        self.patient_name = patient_name
        self.start_date = start_date
        self.sessions: Dict[datetime.date, TrainingSession] = {}
        
    def add_session(self, session: TrainingSession) -> None:
        """Add a training session to the program"""
        if session.date < self.start_date:
            raise ValueError("Session date cannot be before program start date")
        self.sessions[session.date] = session
        
    def generate_initial_program(self) -> None:
        """Generate the initial 4-week recovery program"""
        # Week 1 - Gentle introduction
        week1_date = self.start_date
        week1_exercises = [
            Exercise("Seated Knee Extensions", "Gentle knee extension with no weight", 2, 10),
            Exercise("Hand Grip Squeeze", "Soft ball squeeze for hand rehab", 2, 10),
            Exercise("Seated Leg Lifts", "Straight leg raises while seated", 2, 8),
            Exercise("Ankle Pumps", "Ankle flexion and extension", 2, 10)
        ]
        self.add_session(TrainingSession(week1_date, week1_exercises, "Gentle start - focus on form"))
        
        # Week 2 - Slightly increased intensity
        week2_date = week1_date + datetime.timedelta(days=7)
        week2_exercises = [
            Exercise("Seated Knee Extensions", "With light resistance band", 3, 10),
            Exercise("Hand Grip Squeeze", "Increased resistance", 3, 10),
            Exercise("Seated Leg Lifts", "Add ankle weights (1kg)", 3, 8),
            Exercise("Mini Squats", "Partial squats with chair support", 2, 8)
        ]
        self.add_session(TrainingSession(week2_date, week2_exercises, "Slight intensity increase"))
        
        # Week 3 - Continued progression
        week3_date = week2_date + datetime.timedelta(days=7)
        week3_exercises = [
            Exercise("Seated Knee Extensions", "Increased band resistance", 3, 12),
            Exercise("Hand Grip Squeeze", "Medium resistance", 3, 12),
            Exercise("Standing Leg Lifts", "With support if needed", 3, 10),
            Exercise("Chair Squats", "Full range with chair support", 3, 8),
            Exercise("Seated Shoulder Press", "Light dumbbells (1-2kg)", 2, 10)
        ]
        self.add_session(TrainingSession(week3_date, week3_exercises, "Add upper body work"))
        
        # Week 4 - Further progression
        week4_date = week3_date + datetime.timedelta(days=7)
        week4_exercises = [
            Exercise("Seated Knee Extensions", "Heavier resistance band", 3, 12),
            Exercise("Hand Grip Squeeze", "Firm resistance", 3, 15),
            Exercise("Standing Leg Lifts", "With ankle weights (1kg)", 3, 10),
            Exercise("Chair Squats", "Reduced chair support", 3, 10),
            Exercise("Seated Shoulder Press", "Increased weight (2-3kg)", 3, 10),
            Exercise("Seated Row", "Resistance band row", 2, 12)
        ]
        self.add_session(TrainingSession(week4_date, week4_exercises, "Full body engagement"))
        
    def get_program_summary(self) -> str:
        """Returns formatted program summary"""
        summary = f"Recovery Program for {self.patient_name}\n"
        summary += f"Start Date: {self.start_date}\n\n"
        
        sorted_dates = sorted(self.sessions.keys())
        for date in sorted_dates:
            summary += self.sessions[date].get_session_summary() + "\n\n"
            
        return summary

def main():
    """Run the recovery program generator"""
    try:
        # Initialize program for patient
        patient_name = "John Doe"
        start_date = datetime.date.today()
        program = RecoveryProgram(patient_name, start_date)
        
        # Generate initial 4-week program
        program.generate_initial_program()
        
        # Print program summary
        print(program.get_program_summary())
        
    except Exception as e:
        print(f"Error generating program: {e}")

if __name__ == "__main__":
    main()
```
