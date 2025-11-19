"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: Generate a code snippet that implements a "Learning by Doing" educational module for a bilingual school, inspired by the HJ-THINKING methodology.
Generated: DETERMINISTIC_773325e55c7da692
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Learning by Doing Module for Bilingual School (HJ-THINKING Methodology)
This module implements interactive educational activities that promote hands-on learning.
"""

import random
from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class Activity(ABC):
    """Abstract base class for all learning activities."""
    
    def __init__(self, name: str, language: str = 'bilingual'):
        self.name = name
        self.language = language
        self.completed = False
    
    @abstractmethod
    def start(self) -> None:
        """Start the activity."""
        pass
    
    @abstractmethod
    def evaluate(self) -> Dict[str, float]:
        """Evaluate the activity results."""
        pass
    
    def mark_completed(self) -> None:
        """Mark activity as completed."""
        self.completed = True

class ProblemSolvingActivity(Activity):
    """Concrete implementation of a problem-solving activity."""
    
    def __init__(self, name: str, problem: str, solution: str, language: str = 'bilingual'):
        super().__init__(name, language)
        self.problem = problem
        self.solution = solution
        self.attempts = 0
        self.max_attempts = 3
    
    def start(self) -> None:
        """Display the problem to solve."""
        print(f"\nActivity: {self.name}")
        print(f"Language: {self.language}")
        print(f"\nProblem:\n{self.problem}")
    
    def submit_solution(self, user_solution: str) -> bool:
        """Submit and check user's solution."""
        self.attempts += 1
        
        if user_solution.lower() == self.solution.lower():
            print("Correct! Well done!")
            self.mark_completed()
            return True
        else:
            remaining = self.max_attempts - self.attempts
            if remaining > 0:
                print(f"Not quite right. You have {remaining} attempts remaining.")
            else:
                print(f"Solution: {self.solution}")
                self.mark_completed()
            return False
    
    def evaluate(self) -> Dict[str, float]:
        """Evaluate performance based on attempts."""
        if not self.completed:
            return {'score': 0.0, 'efficiency': 0.0}
        
        efficiency = 1.0 - (0.2 * (self.attempts - 1))
        return {'score': 1.0, 'efficiency': max(0.0, efficiency)}

class CollaborativeActivity(Activity):
    """Activity that requires group collaboration."""
    
    def __init__(self, name: str, task: str, min_participants: int = 2, language: str = 'bilingual'):
        super().__init__(name, language)
        self.task = task
        self.min_participants = min_participants
        self.participants = []
        self.group_output = None
    
    def add_participant(self, participant: str) -> None:
        """Add participant to the activity."""
        self.participants.append(participant)
    
    def start(self) -> None:
        """Start the collaborative activity."""
        if len(self.participants) < self.min_participants:
            raise ValueError(f"Minimum {self.min_participants} participants required")
        
        print(f"\nGroup Activity: {self.name}")
        print(f"Participants: {', '.join(self.participants)}")
        print(f"\nTask:\n{self.task}")
    
    def submit_group_output(self, output: str) -> None:
        """Submit the group's work output."""
        self.group_output = output
        self.mark_completed()
    
    def evaluate(self) -> Dict[str, float]:
        """Evaluate group performance."""
        if not self.completed:
            return {'score': 0.0, 'collaboration': 0.0}
        
        collaboration_score = min(1.0, len(self.participants) / self.min_participants)
        return {'score': 1.0, 'collaboration': collaboration_score}

class LearningModule:
    """Main class managing the learning activities."""
    
    def __init__(self, name: str):
        self.name = name
        self.activities: List[Activity] = []
        self.completed_activities = 0
    
    def add_activity(self, activity: Activity) -> None:
        """Add an activity to the module."""
        self.activities.append(activity)
    
    def run_activity(self, index: int) -> Optional[Dict[str, float]]:
        """Run a specific activity by index."""
        try:
            activity = self.activities[index]
            activity.start()
            
            if isinstance(activity, ProblemSolvingActivity):
                while not activity.completed and activity.attempts < activity.max_attempts:
                    user_input = input("Your solution: ")
                    activity.submit_solution(user_input)
            
            elif isinstance(activity, CollaborativeActivity):
                print("\nGroup work in progress...")
                # Simulate group output for demo purposes
                simulated_output = f"Group solution to: {activity.task}"
                print(f"Submitted output: {simulated_output}")
                activity.submit_group_output(simulated_output)
            
            if activity.completed:
                self.completed_activities += 1
            
            return activity.evaluate()
        
        except IndexError:
            print("Error: Invalid activity index")
            return None
        except Exception as e:
            print(f"Error running activity: {str(e)}")
            return None
    
    def get_progress(self) -> float:
        """Calculate completion progress of the module."""
        if not self.activities:
            return 0.0
        return self.completed_activities / len(self.activities)

# Example usage
if __name__ == "__main__":
    # Create learning module
    module = LearningModule("Mathematics Problem Solving")
    
    # Add activities
    module.add_activity(
        ProblemSolvingActivity(
            "Algebra Puzzle", 
            "Solve for x: 2x + 5 = 15", 
            "5",
            "bilingual"
        )
    )
    
    module.add_activity(
        CollaborativeActivity(
            "Geometry Challenge",
            "Design a bridge using geometric shapes",
            3,
            "bilingual"
        )
    )
    
    # Simulate participants for collaborative activity
    collab_activity = module.activities[1]
    collab_activity.add_participant("Alice")
    collab_activity.add_participant("Bob")
    collab_activity.add_participant("Charlie")
    
    # Run activities
    for i in range(len(module.activities)):
        print(f"\n=== Activity {i+1} ===")
        results = module.run_activity(i)
        if results:
            print(f"Results: {results}")
    
    # Show final progress
    print(f"\nModule progress: {module.get_progress() * 100:.1f}% complete")
```
