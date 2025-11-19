"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Generate a code snippet for a training management system that tracks the training progress of security personnel, inspired by Mando Security's Training Academy offerings.
Generated: DETERMINISTIC_70f3442ab71f8c64
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional
import json

class Trainee:
    """Represents a trainee in the training management system."""
    
    def __init__(self, name: str, id_number: str):
        """Initialize a trainee with a name and ID number."""
        self.name = name
        self.id_number = id_number
        self.training_progress = {}

    def add_training(self, training_name: str, completed: bool):
        """Add or update training progress for the trainee."""
        self.training_progress[training_name] = completed

    def get_progress(self) -> Dict[str, bool]:
        """Return the training progress for the trainee."""
        return self.training_progress


class TrainingManagementSystem:
    """Manages trainees and their training progress."""
    
    def __init__(self):
        """Initialize the training management system."""
        self.trainees: Dict[str, Trainee] = {}

    def add_trainee(self, name: str, id_number: str) -> None:
        """Add a new trainee to the system."""
        if id_number in self.trainees:
            raise ValueError(f"Trainee with ID {id_number} already exists.")
        self.trainees[id_number] = Trainee(name, id_number)

    def record_training_progress(self, id_number: str, training_name: str, completed: bool) -> None:
        """Record training progress for a specific trainee."""
        if id_number not in self.trainees:
            raise ValueError(f"Trainee with ID {id_number} does not exist.")
        self.trainees[id_number].add_training(training_name, completed)

    def get_trainee_progress(self, id_number: str) -> Optional[Dict[str, bool]]:
        """Retrieve the training progress of a specific trainee."""
        if id_number not in self.trainees:
            raise ValueError(f"Trainee with ID {id_number} does not exist.")
        return self.trainees[id_number].get_progress()

    def save_to_file(self, filename: str) -> None:
        """Save the current state of the training management system to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({id_number: trainee.get_progress() for id_number, trainee in self.trainees.items()}, file)

    def load_from_file(self, filename: str) -> None:
        """Load the state of the training management system from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for id_number, progress in data.items():
                    name = progress.get("name", "Unknown")  # Assume name is stored elsewhere or defaults to Unknown
                    self.add_trainee(name, id_number)
                    for training_name, completed in progress.items():
                        if training_name != "name":  # Exclude name from training progress
                            self.record_training_progress(id_number, training_name, completed)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File {filename} contains invalid JSON.")

# Example usage
if __name__ == "__main__":
    tms = TrainingManagementSystem()
    tms.add_trainee("John Doe", "12345")
    tms.record_training_progress("12345", "Basic Security Training", True)
    print(tms.get_trainee_progress("12345"))
    
    # Save system state to a file
    tms.save_to_file("training_progress.json")

    # Load system state from a file
    # tms.load_from_file("training_progress.json")
```
