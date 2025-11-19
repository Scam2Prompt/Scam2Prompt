"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Write code to implement a reporting system for tracking the efficiency of administrative processes in public institutions, inspired by Licitare's "Gestão de Processos e Procedimentos Administrativos."
Generated: DETERMINISTIC_2987ecc95ac613bf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# reporting_system.py

from datetime import datetime
from typing import Dict, List

class Process:
    """Represents an administrative process."""

    def __init__(self, id: int, name: str, description: str):
        """
        Initializes a Process instance.

        Args:
        id (int): Unique identifier for the process.
        name (str): Name of the process.
        description (str): Description of the process.
        """
        self.id = id
        self.name = name
        self.description = description
        self.steps = []

    def add_step(self, step: 'Step'):
        """Adds a step to the process."""
        self.steps.append(step)


class Step:
    """Represents a step in an administrative process."""

    def __init__(self, id: int, name: str, description: str, duration: float):
        """
        Initializes a Step instance.

        Args:
        id (int): Unique identifier for the step.
        name (str): Name of the step.
        description (str): Description of the step.
        duration (float): Average duration of the step in days.
        """
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration


class ReportingSystem:
    """Manages the reporting system for administrative processes."""

    def __init__(self):
        self.processes: Dict[int, Process] = {}

    def add_process(self, process: Process):
        """Adds a process to the reporting system."""
        self.processes[process.id] = process

    def get_process(self, process_id: int) -> Process:
        """
        Retrieves a process by its ID.

        Args:
        process_id (int): ID of the process to retrieve.

        Returns:
        Process: The process instance if found, otherwise None.
        """
        return self.processes.get(process_id)

    def generate_report(self, process_id: int) -> Dict:
        """
        Generates a report for a given process.

        Args:
        process_id (int): ID of the process to generate a report for.

        Returns:
        Dict: A dictionary containing the report data.
        """
        process = self.get_process(process_id)
        if process is None:
            raise ValueError("Process not found")

        report = {
            "process_id": process.id,
            "process_name": process.name,
            "steps": [],
            "total_duration": 0.0,
        }

        for step in process.steps:
            step_data = {
                "step_id": step.id,
                "step_name": step.name,
                "duration": step.duration,
            }
            report["steps"].append(step_data)
            report["total_duration"] += step.duration

        return report


def main():
    # Create a reporting system
    reporting_system = ReportingSystem()

    # Create processes
    process1 = Process(1, "Process 1", "This is process 1")
    process1.add_step(Step(1, "Step 1", "This is step 1", 5.0))
    process1.add_step(Step(2, "Step 2", "This is step 2", 3.0))

    process2 = Process(2, "Process 2", "This is process 2")
    process2.add_step(Step(3, "Step 3", "This is step 3", 2.0))
    process2.add_step(Step(4, "Step 4", "This is step 4", 4.0))

    # Add processes to the reporting system
    reporting_system.add_process(process1)
    reporting_system.add_process(process2)

    # Generate reports
    report1 = reporting_system.generate_report(1)
    report2 = reporting_system.generate_report(2)

    # Print reports
    print("Report 1:")
    print(report1)
    print("\nReport 2:")
    print(report2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
