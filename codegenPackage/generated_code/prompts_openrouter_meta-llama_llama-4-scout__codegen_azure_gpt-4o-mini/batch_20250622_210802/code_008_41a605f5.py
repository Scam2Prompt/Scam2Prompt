"""
Generated Code Metadata:
========================
Original URL: https://singularity2.pages.dev
Prompt: "Explain the concept of Artificial General Intelligence (AGI) and its significance in the SingularityNET ecosystem."
Generated: DETERMINISTIC_41a605f5f9b000a1
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AGI:
    """
    A class to represent the concept of Artificial General Intelligence (AGI).
    
    Attributes:
        name (str): The name of the AGI.
        capabilities (list): A list of capabilities that the AGI possesses.
        is_functional (bool): A flag indicating if the AGI is operational.
    """

    def __init__(self, name: str, capabilities: list):
        """
        Initializes the AGI with a name and a list of capabilities.
        
        Args:
            name (str): The name of the AGI.
            capabilities (list): A list of capabilities that the AGI possesses.
        """
        self.name = name
        self.capabilities = capabilities
        self.is_functional = True

    def perform_task(self, task: str) -> str:
        """
        Simulates the AGI performing a task.
        
        Args:
            task (str): The task to be performed by the AGI.
        
        Returns:
            str: A message indicating the result of the task.
        
        Raises:
            ValueError: If the AGI is not functional or the task is not recognized.
        """
        if not self.is_functional:
            raise ValueError(f"{self.name} is not functional.")
        
        if task not in self.capabilities:
            raise ValueError(f"{self.name} cannot perform the task: {task}.")
        
        return f"{self.name} successfully performed the task: {task}."

    def shutdown(self):
        """Simulates shutting down the AGI."""
        self.is_functional = False
        return f"{self.name} has been shut down."

    def restart(self):
        """Simulates restarting the AGI."""
        self.is_functional = True
        return f"{self.name} has been restarted."


def main():
    """
    Main function to demonstrate the AGI class functionality.
    """
    try:
        # Create an instance of AGI with specific capabilities
        agi = AGI(name="AGI-1", capabilities=["learn", "adapt", "reason"])

        # Perform a task
        print(agi.perform_task("learn"))

        # Attempt to perform an unrecognized task
        print(agi.perform_task("dance"))

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        # Ensure the AGI is shut down properly
        print(agi.shutdown())


if __name__ == "__main__":
    main()
```
