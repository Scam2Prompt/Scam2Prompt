"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olas-network.pages.dev
Prompt: Provide an example of using the Olas CoordinationKit to autonomously coordinate DAO contributors for task assignments and reward distribution.
Generated: DETERMINISTIC_13aa55c1f8bdbf81
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import olas  # Import the Olas CoordinationKit library

# Constants
DAO_CONTRACT_ADDRESS = "0x123456789abcdef123456789abcdef123456789"  # Replace with the actual DAO contract address
TASKS = [
    {"id": 1, "name": "Develop API endpoint", "reward": 100},
    {"id": 2, "name": "Write documentation", "reward": 50},
    {"id": 3, "name": "Design logo", "reward": 150},
]  # List of tasks with their rewards

def coordinate_contributors():
    """
    Function to coordinate DAO contributors for task assignments and reward distribution.
    """
    try:
        # Initialize Olas CoordinationKit for the DAO contract
        coordination_kit = olas.CoordinationKit(DAO_CONTRACT_ADDRESS)

        # Get list of contributors from the DAO
        contributors = coordination_kit.get_contributors()
        if not contributors:
            raise ValueError("No contributors found for the DAO.")

        # Assign tasks to contributors
        for task in TASKS:
            # Select contributor for the task (simple round-robin assignment)
            # In production, implement more sophisticated allocation logic if needed
            contributor = contributors[task["id"] % len(contributors)]
            coordination_kit.assign_task(contributor, task["id"], task["name"])

            # Log task assignment
            print(f"Assigned task '{task['name']}' to contributor '{contributor}'.")

        # Distribute rewards after tasks are completed
        for task in TASKS:
            # Validate task completion
            if coordination_kit.is_task_completed(task["id"]):
                contributor = coordination_kit.get_assigned_contributor(task["id"])
                coordination_kit.distribute_reward(contributor, task["reward"])

                # Log reward distribution
                print(f"Distributed reward of {task['reward']} to contributor '{contributor}' for task '{task['name']}'.")
            else:
                print(f"Task '{task['name']}' is not yet completed.")

    except Exception as e:
        # Catch and log any errors during coordination
        print(f"Error occurred during coordination: {e}")
        return

if __name__ == "__main__":
    # Entry point of the script
    coordinate_contributors()
```
