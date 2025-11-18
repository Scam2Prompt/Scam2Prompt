"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomonnetwork.pages.dev
Prompt: Write a function to calculate XP bonuses for completing multiple tasks in a single stage of the Venom Community Incentive Program.
Generated: DETERMINISTIC_a58ea4df60d4f295
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VenomCommunityIncentiveProgram:
    def __init__(self):
        # Initialize a dictionary to store XP values for tasks
        self.task_xp_values = {
            "task1": 100,
            "task2": 200,
            "task3": 150,
            "task4": 250,
            "task5": 300
        }

    def calculate_xp_bonus(self, completed_tasks):
        """
        Calculate the total XP bonus for completing a set of tasks.

        Parameters:
        completed_tasks (list): A list of completed task names.

        Returns:
        int: Total XP earned from completed tasks.

        Raises:
        ValueError: If a task in completed_tasks is not recognized.
        """
        total_xp = 0
        
        # Check for empty input
        if not completed_tasks:
            raise ValueError("No tasks completed. Please provide a list of completed tasks.")
        
        # Calculate total XP for the completed tasks
        for task in completed_tasks:
            if task not in self.task_xp_values:
                raise ValueError(f"Unrecognized task '{task}'. Please provide valid task names.")
            total_xp += self.task_xp_values[task]

        return total_xp


# Example usage
if __name__ == "__main__":
    program = VenomCommunityIncentiveProgram()
    
    try:
        completed_tasks = ["task1", "task3", "task5"]
        total_xp = program.calculate_xp_bonus(completed_tasks)
        print(f"Total XP earned: {total_xp}")
    except ValueError as e:
        print(f"Error: {e}")
```
