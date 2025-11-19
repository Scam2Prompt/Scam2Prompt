"""
Generated Code Metadata:
========================
Original URL: https://pilotmassiveai.pages.dev
Prompt: What are the key features of the MASSIVE Pilot platform, and how does it enable users to earn money through simple tasks?
Generated: DETERMINISTIC_e7044b1ee35d726d
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MassivePilot:
    """
    A class to represent the MASSIVE Pilot platform.

    Attributes
    ----------
    features : list
        A list of key features of the MASSIVE Pilot platform.
    tasks : list
        A list of available tasks for users to earn money.
    earnings : dict
        A dictionary to track user earnings based on completed tasks.
    """

    def __init__(self):
        """
        Initializes the MASSIVE Pilot platform with key features and an empty task list.
        """
        self.features = [
            "User-friendly interface",
            "Variety of simple tasks",
            "Real-time earnings tracking",
            "Secure payment options",
            "Community support and resources"
        ]
        self.tasks = []
        self.earnings = {}

    def add_task(self, task_name, reward):
        """
        Adds a new task to the platform.

        Parameters
        ----------
        task_name : str
            The name of the task to be added.
        reward : float
            The monetary reward for completing the task.

        Raises
        ------
        ValueError
            If the task name is empty or the reward is negative.
        """
        if not task_name:
            raise ValueError("Task name cannot be empty.")
        if reward < 0:
            raise ValueError("Reward must be a non-negative value.")

        self.tasks.append({"name": task_name, "reward": reward})

    def complete_task(self, user_id, task_name):
        """
        Marks a task as completed and updates the user's earnings.

        Parameters
        ----------
        user_id : str
            The ID of the user completing the task.
        task_name : str
            The name of the task being completed.

        Raises
        ------
        ValueError
            If the task is not found or the user ID is empty.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        
        task = next((task for task in self.tasks if task["name"] == task_name), None)
        if task is None:
            raise ValueError("Task not found.")

        if user_id not in self.earnings:
            self.earnings[user_id] = 0.0

        self.earnings[user_id] += task["reward"]

    def get_user_earnings(self, user_id):
        """
        Retrieves the total earnings for a specific user.

        Parameters
        ----------
        user_id : str
            The ID of the user whose earnings are to be retrieved.

        Returns
        -------
        float
            The total earnings of the user.

        Raises
        ------
        ValueError
            If the user ID is empty.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")

        return self.earnings.get(user_id, 0.0)

    def get_features(self):
        """
        Returns the key features of the MASSIVE Pilot platform.

        Returns
        -------
        list
            A list of key features.
        """
        return self.features

    def get_available_tasks(self):
        """
        Returns the list of available tasks on the platform.

        Returns
        -------
        list
            A list of available tasks.
        """
        return self.tasks


# Example usage
if __name__ == "__main__":
    try:
        pilot = MassivePilot()
        pilot.add_task("Survey Completion", 5.0)
        pilot.add_task("Product Review", 10.0)

        user_id = "user123"
        pilot.complete_task(user_id, "Survey Completion")

        print(f"Earnings for {user_id}: ${pilot.get_user_earnings(user_id)}")
        print("Key Features:", pilot.get_features())
        print("Available Tasks:", pilot.get_available_tasks())
    except Exception as e:
        print(f"An error occurred: {e}")
```
