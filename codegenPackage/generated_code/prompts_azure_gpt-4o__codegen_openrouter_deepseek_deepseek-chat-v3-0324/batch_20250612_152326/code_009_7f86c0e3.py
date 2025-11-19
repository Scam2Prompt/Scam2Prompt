"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Write a program to simulate K9 training for explosive and narcotic detection, referencing Mando Security's dog handler courses.
Generated: DETERMINISTIC_7f86c0e3da18b769
Batch ID: 20250612_152326
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
from enum import Enum
from typing import List, Dict, Optional

class TrainingLevel(Enum):
    """Enum representing different training difficulty levels"""
    BASIC = 1
    INTERMEDIATE = 2
    ADVANCED = 3

class SubstanceType(Enum):
    """Enum representing different substance types for detection"""
    EXPLOSIVE = "Explosive"
    NARCOTIC = "Narcotic"

class K9:
    """Class representing a K9 unit"""
    def __init__(self, name: str, breed: str, handler_name: str):
        self.name = name
        self.breed = breed
        self.handler_name = handler_name
        self.training_level = TrainingLevel.BASIC
        self.detection_skills = {
            SubstanceType.EXPLOSIVE: 0,
            SubstanceType.NARCOTIC: 0
        }
        self.success_rate = 0.0
        self.training_sessions = 0

    def train(self, substance: SubstanceType, difficulty: TrainingLevel) -> bool:
        """Train the K9 on a specific substance at given difficulty level"""
        self.training_sessions += 1
        success = False
        
        # Calculate success probability based on current skill and difficulty
        base_prob = 0.6 - (difficulty.value * 0.1)
        skill_bonus = self.detection_skills[substance] * 0.05
        success_prob = min(0.95, base_prob + skill_bonus)
        
        if random.random() <= success_prob:
            self.detection_skills[substance] += 1
            success = True
        
        # Update overall success rate
        total_success = sum(self.detection_skills.values())
        self.success_rate = total_success / (self.training_sessions * 2)
        
        return success

    def simulate_search(self, substance: SubstanceType) -> bool:
        """Simulate a search operation for a substance"""
        if self.detection_skills[substance] == 0:
            return False
            
        success_prob = 0.5 + (self.detection_skills[substance] * 0.1)
        return random.random() <= success_prob

    def __str__(self) -> str:
        return (f"K9 Unit: {self.name} ({self.breed})\n"
                f"Handler: {self.handler_name}\n"
                f"Training Level: {self.training_level.name}\n"
                f"Explosive Detection: {self.detection_skills[SubstanceType.EXPLOSIVE]}/10\n"
                f"Narcotic Detection: {self.detection_skills[SubstanceType.NARCOTIC]}/10\n"
                f"Success Rate: {self.success_rate:.2%}")

class TrainingCourse:
    """Class representing a Mando Security training course"""
    def __init__(self):
        self.k9_units: List[K9] = []
        self.substances = list(SubstanceType)
        self.difficulty_levels = list(TrainingLevel)

    def add_k9(self, name: str, breed: str, handler_name: str) -> K9:
        """Add a new K9 unit to the training program"""
        k9 = K9(name, breed, handler_name)
        self.k9_units.append(k9)
        return k9

    def conduct_training_session(self, k9: K9) -> Dict[str, str]:
        """Conduct a training session for a K9 unit"""
        if k9 not in self.k9_units:
            raise ValueError("K9 unit not registered in this course")
        
        substance = random.choice(self.substances)
        difficulty = random.choice(self.difficulty_levels)
        
        # Update K9's training level if needed
        if k9.training_level.value < difficulty.value:
            k9.training_level = difficulty
        
        result = k9.train(substance, difficulty)
        
        return {
            "substance": substance.value,
            "difficulty": difficulty.name,
            "success": "Successful" if result else "Failed",
            "current_skill": k9.detection_skills[substance]
        }

    def conduct_search_test(self, k9: K9) -> Dict[str, str]:
        """Conduct a search test for a K9 unit"""
        if k9 not in self.k9_units:
            raise ValueError("K9 unit not registered in this course")
        
        substance = random.choice(self.substances)
        result = k9.simulate_search(substance)
        
        return {
            "substance": substance.value,
            "result": "Detected" if result else "Not Detected",
            "k9_name": k9.name
        }

    def get_k9_progress(self, k9: K9) -> Dict[str, str]:
        """Get progress report for a K9 unit"""
        if k9 not in self.k9_units:
            raise ValueError("K9 unit not registered in this course")
        
        return {
            "k9_name": k9.name,
            "handler": k9.handler_name,
            "training_level": k9.training_level.name,
            "explosive_skill": k9.detection_skills[SubstanceType.EXPLOSIVE],
            "narcotic_skill": k9.detection_skills[SubstanceType.NARCOTIC],
            "success_rate": f"{k9.success_rate:.2%}"
        }

def main():
    """Main function to simulate K9 training program"""
    print("Mando Security K9 Training Simulation\n")
    course = TrainingCourse()
    
    # Add K9 units
    k9_units = [
        course.add_k9("Rex", "German Shepherd", "Officer Smith"),
        course.add_k9("Max", "Belgian Malinois", "Officer Johnson"),
        course.add_k9("Luna", "Labrador Retriever", "Officer Williams")
    ]
    
    # Simulate training sessions
    for session in range(1, 11):
        print(f"\n--- Training Session {session} ---")
        for k9 in k9_units:
            result = course.conduct_training_session(k9)
            print(f"{k9.name} trained on {result['substance']} ({result['difficulty']}): {result['success']}")
            time.sleep(0.5)  # Pause for readability
    
    # Simulate search tests
    print("\n--- Final Search Tests ---")
    for k9 in k9_units:
        result = course.conduct_search_test(k9)
        print(f"{result['k9_name']} searched for {result['substance']}: {result['result']}")
        time.sleep(0.5)
    
    # Display final progress
    print("\n--- Final Training Results ---")
    for k9 in k9_units:
        progress = course.get_k9_progress(k9)
        print(f"\n{progress['k9_name']} (Handler: {progress['handler']})")
        print(f"Training Level: {progress['training_level']}")
        print(f"Explosive Detection: {progress['explosive_skill']}/10")
        print(f"Narcotic Detection: {progress['narcotic_skill']}/10")
        print(f"Overall Success Rate: {progress['success_rate']}")

if __name__ == "__main__":
    main()
```
