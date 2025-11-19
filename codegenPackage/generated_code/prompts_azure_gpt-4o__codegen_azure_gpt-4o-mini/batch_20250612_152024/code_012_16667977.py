"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write code to simulate PTE speaking and writing tasks with scoring algorithms, inspired by RNW International's PTE coaching services.
Generated: DETERMINISTIC_16667977f8e2f52a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class PTETask:
    """
    A class to represent a PTE speaking or writing task.
    """

    def __init__(self, task_type):
        """
        Initializes a PTE task with a specified type.

        Args:
            task_type (str): The type of the task ('speaking' or 'writing').
        """
        if task_type not in ['speaking', 'writing']:
            raise ValueError("Task type must be either 'speaking' or 'writing'.")
        self.task_type = task_type
        self.score = 0

    def simulate_task(self):
        """
        Simulates the execution of the PTE task and calculates a score.
        """
        if self.task_type == 'speaking':
            self.score = self._simulate_speaking()
        elif self.task_type == 'writing':
            self.score = self._simulate_writing()
        return self.score

    def _simulate_speaking(self):
        """
        Simulates a speaking task and returns a score based on random factors.

        Returns:
            int: A score between 0 and 90.
        """
        fluency = random.randint(0, 30)
        pronunciation = random.randint(0, 30)
        content = random.randint(0, 30)
        overall_score = fluency + pronunciation + content
        return min(overall_score, 90)

    def _simulate_writing(self):
        """
        Simulates a writing task and returns a score based on random factors.

        Returns:
            int: A score between 0 and 90.
        """
        coherence = random.randint(0, 30)
        grammar = random.randint(0, 30)
        vocabulary = random.randint(0, 30)
        overall_score = coherence + grammar + vocabulary
        return min(overall_score, 90)

def main():
    """
    Main function to run the PTE task simulation.
    """
    try:
        task_type = input("Enter task type (speaking/writing): ").strip().lower()
        pte_task = PTETask(task_type)
        score = pte_task.simulate_task()
        print(f"Your {task_type} task score is: {score}/90")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
