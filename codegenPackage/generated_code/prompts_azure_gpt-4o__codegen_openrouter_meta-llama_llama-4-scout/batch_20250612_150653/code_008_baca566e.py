"""
Generated Code Metadata:
========================
Original URL: https://reckonmexico.com
Prompt: Generate code to implement a control system for monitoring internal financial processes, inspired by Reckon Business Consulting's audit services.
Generated: DETERMINISTIC_baca566e0a50c779
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_control_system.py

import logging
from datetime import datetime
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialProcess:
    """Represents a financial process with its current state and history."""

    def __init__(self, process_id: int, name: str):
        """
        Initializes a FinancialProcess instance.

        Args:
        - process_id (int): Unique identifier for the process.
        - name (str): Name of the financial process.
        """
        self.process_id = process_id
        self.name = name
        self.current_state = "pending"
        self.history = []

    def update_state(self, new_state: str):
        """
        Updates the current state of the financial process.

        Args:
        - new_state (str): New state of the financial process.

        Raises:
        - ValueError: If the new state is not valid.
        """
        valid_states = ["pending", "in_progress", "completed", "failed"]
        if new_state not in valid_states:
            raise ValueError("Invalid state")

        self.history.append((self.current_state, datetime.now()))
        self.current_state = new_state

    def __str__(self):
        return f"Financial Process {self.process_id}: {self.name} - Current State: {self.current_state}"


class ControlSystem:
    """Manages and monitors internal financial processes."""

    def __init__(self):
        self.processes: Dict[int, FinancialProcess] = {}

    def add_process(self, process: FinancialProcess):
        """
        Adds a financial process to the control system.

        Args:
        - process (FinancialProcess): Financial process to add.
        """
        self.processes[process.process_id] = process

    def update_process_state(self, process_id: int, new_state: str):
        """
        Updates the state of a financial process.

        Args:
        - process_id (int): Identifier of the process to update.
        - new_state (str): New state of the process.

        Raises:
        - KeyError: If the process does not exist.
        """
        if process_id not in self.processes:
            raise KeyError("Process not found")

        self.processes[process_id].update_state(new_state)

    def get_process(self, process_id: int) -> FinancialProcess:
        """
        Retrieves a financial process by its identifier.

        Args:
        - process_id (int): Identifier of the process to retrieve.

        Returns:
        - FinancialProcess: The financial process instance.

        Raises:
        - KeyError: If the process does not exist.
        """
        if process_id not in self.processes:
            raise KeyError("Process not found")

        return self.processes[process_id]

    def list_processes(self) -> List[FinancialProcess]:
        """
        Lists all financial processes in the control system.

        Returns:
        - List[FinancialProcess]: List of financial process instances.
        """
        return list(self.processes.values())


def main():
    control_system = ControlSystem()

    # Create financial processes
    process1 = FinancialProcess(1, "Accounts Payable")
    process2 = FinancialProcess(2, "Accounts Receivable")

    # Add processes to the control system
    control_system.add_process(process1)
    control_system.add_process(process2)

    # Update process states
    control_system.update_process_state(1, "in_progress")
    control_system.update_process_state(2, "completed")

    # List all processes
    logging.info("Financial Processes:")
    for process in control_system.list_processes():
        logging.info(process)

    # Retrieve a process
    try:
        process = control_system.get_process(1)
        logging.info(f"Process {process.process_id}: {process.name} - Current State: {process.current_state}")
    except KeyError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
```
