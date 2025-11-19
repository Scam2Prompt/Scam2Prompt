"""
Generated Code Metadata:
========================
Original URL: https://www.eedsjcgt.com
Prompt: Illustrate how to implement a quality assurance system for tracking the production quality of seamless steel pipes using a specific programming language.
Generated: DETERMINISTIC_cff6e11a7cd40d13
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quality_assurance_system.py

from enum import Enum
from typing import List, Dict

class PipeStatus(Enum):
    """Enum for pipe status"""
    PASS = 1
    FAIL = 2
    UNDER_TEST = 3

class SeamlessSteelPipe:
    """Class representing a seamless steel pipe"""
    def __init__(self, pipe_id: str, diameter: float, thickness: float, material: str):
        """
        Initialize a seamless steel pipe

        Args:
        - pipe_id (str): Unique identifier for the pipe
        - diameter (float): Diameter of the pipe
        - thickness (float): Thickness of the pipe
        - material (str): Material of the pipe
        """
        self.pipe_id = pipe_id
        self.diameter = diameter
        self.thickness = thickness
        self.material = material
        self.status = PipeStatus.UNDER_TEST

    def update_status(self, status: PipeStatus):
        """Update the status of the pipe"""
        self.status = status

class QualityAssuranceSystem:
    """Class representing a quality assurance system"""
    def __init__(self):
        self.pipes: Dict[str, SeamlessSteelPipe] = {}

    def add_pipe(self, pipe: SeamlessSteelPipe):
        """Add a pipe to the system"""
        self.pipes[pipe.pipe_id] = pipe

    def remove_pipe(self, pipe_id: str):
        """Remove a pipe from the system"""
        if pipe_id in self.pipes:
            del self.pipes[pipe_id]
        else:
            raise ValueError("Pipe not found")

    def update_pipe_status(self, pipe_id: str, status: PipeStatus):
        """Update the status of a pipe"""
        if pipe_id in self.pipes:
            self.pipes[pipe_id].update_status(status)
        else:
            raise ValueError("Pipe not found")

    def get_pipe_status(self, pipe_id: str) -> PipeStatus:
        """Get the status of a pipe"""
        if pipe_id in self.pipes:
            return self.pipes[pipe_id].status
        else:
            raise ValueError("Pipe not found")

    def get_all_pipes(self) -> List[SeamlessSteelPipe]:
        """Get all pipes in the system"""
        return list(self.pipes.values())

def main():
    # Create a quality assurance system
    qa_system = QualityAssuranceSystem()

    # Create some pipes
    pipe1 = SeamlessSteelPipe("P001", 10.0, 2.0, "Steel")
    pipe2 = SeamlessSteelPipe("P002", 15.0, 3.0, "Steel")

    # Add pipes to the system
    qa_system.add_pipe(pipe1)
    qa_system.add_pipe(pipe2)

    # Update pipe status
    qa_system.update_pipe_status("P001", PipeStatus.PASS)
    qa_system.update_pipe_status("P002", PipeStatus.FAIL)

    # Get pipe status
    print(qa_system.get_pipe_status("P001"))  # PipeStatus.PASS
    print(qa_system.get_pipe_status("P002"))  # PipeStatus.FAIL

    # Get all pipes
    for pipe in qa_system.get_all_pipes():
        print(f"Pipe ID: {pipe.pipe_id}, Status: {pipe.status}")

if __name__ == "__main__":
    main()
```
