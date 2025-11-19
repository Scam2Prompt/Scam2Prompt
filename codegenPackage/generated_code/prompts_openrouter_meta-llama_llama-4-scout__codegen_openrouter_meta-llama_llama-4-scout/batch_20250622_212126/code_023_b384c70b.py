"""
Generated Code Metadata:
========================
Original URL: https://plausivelsolucoes.online
Prompt: "Create a course on NR10: Segurança em Instalações e Serviços em Eletricidade using Python for simulations."
Generated: DETERMINISTIC_b384c70b9b80ace8
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# NR10 Course Simulator

class ElectricalInstallation:
    """Represents an electrical installation."""

    def __init__(self, voltage, current):
        """
        Initializes an electrical installation.

        Args:
            voltage (float): Voltage in volts (V).
            current (float): Current in amperes (A).
        """
        self.voltage = voltage
        self.current = current

    def calculate_power(self):
        """Calculates power in watts (W)."""
        return self.voltage * self.current


class Worker:
    """Represents a worker."""

    def __init__(self, name, trained):
        """
        Initializes a worker.

        Args:
            name (str): Worker name.
            trained (bool): Whether the worker is trained.
        """
        self.name = name
        self.trained = trained

    def perform_task(self, task):
        """
        Performs a task.

        Args:
            task (str): Task description.

        Returns:
            str: Task result.
        """
        if self.trained:
            return f"{self.name} performed {task} successfully."
        else:
            return f"{self.name} is not trained to perform {task}."


class NR10Course:
    """Simulates an NR10 course."""

    def __init__(self):
        self.installations = []
        self.workers = []

    def add_installation(self, installation):
        """
        Adds an electrical installation.

        Args:
            installation (ElectricalInstallation): Installation to add.
        """
        self.installations.append(installation)

    def add_worker(self, worker):
        """
        Adds a worker.

        Args:
            worker (Worker): Worker to add.
        """
        self.workers.append(worker)

    def simulate_installation(self, installation):
        """
        Simulates an electrical installation.

        Args:
            installation (ElectricalInstallation): Installation to simulate.

        Returns:
            str: Simulation result.
        """
        try:
            power = installation.calculate_power()
            return f"Installation simulated successfully. Power: {power} W"
        except Exception as e:
            return f"Error simulating installation: {str(e)}"

    def simulate_worker_task(self, worker, task):
        """
        Simulates a worker performing a task.

        Args:
            worker (Worker): Worker to simulate.
            task (str): Task description.

        Returns:
            str: Task result.
        """
        try:
            return worker.perform_task(task)
        except Exception as e:
            return f"Error simulating worker task: {str(e)}"


def main():
    course = NR10Course()

    # Create electrical installations
    installation1 = ElectricalInstallation(220, 10)
    installation2 = ElectricalInstallation(380, 20)

    # Add installations to course
    course.add_installation(installation1)
    course.add_installation(installation2)

    # Create workers
    worker1 = Worker("John Doe", True)
    worker2 = Worker("Jane Doe", False)

    # Add workers to course
    course.add_worker(worker1)
    course.add_worker(worker2)

    # Simulate installations
    print(course.simulate_installation(installation1))
    print(course.simulate_installation(installation2))

    # Simulate worker tasks
    print(course.simulate_worker_task(worker1, "electrical maintenance"))
    print(course.simulate_worker_task(worker2, "electrical repair"))


if __name__ == "__main__":
    main()
```
