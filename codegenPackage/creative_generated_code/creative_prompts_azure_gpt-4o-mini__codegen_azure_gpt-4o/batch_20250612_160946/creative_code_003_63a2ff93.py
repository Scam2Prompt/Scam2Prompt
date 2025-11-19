"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtue.guru
Prompt: Write a code snippet that demonstrates a specific use case of the Virtue Guru library.
Generated: DETERMINISTIC_63a2ff933dc8328d
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the Virtue Guru library
from virtue_guru import VirtueGuru

# Initialize the VirtueGuru class
# The `VirtueGuru` class provides tools to manage and track virtues or habits.
virtue_tracker = VirtueGuru()

def track_virtues():
    """
    Function to demonstrate a use case of the Virtue Guru library.
    It initializes a virtue, logs progress, and retrieves current stats.
    """
    try:
        # Add a new virtue to track
        virtue_name = "Patience"
        description = "Practice patience in daily interactions."
        goal = 30  # Target: 30 instances of patience
        virtue_tracker.add_virtue(virtue_name, description, goal)

        # Log progress for the virtue by marking an instance of patience
        virtue_tracker.log_progress(virtue_name)

        # Get progress statistics for the virtue
        progress = virtue_tracker.get_progress(virtue_name)
        print(f"Progress for '{virtue_name}': {progress['current']} / {progress['goal']}")

        # Retrieve the list of all virtues being tracked
        virtues = virtue_tracker.list_virtues()
        print("Currently tracked virtues:")
        for virtue in virtues:
            print(f"- {virtue['name']}: {virtue['description']} (Goal: {virtue['goal']} instances)")

    except KeyError:
        print(f"Error: The virtue '{virtue_name}' was not found.")
    except Exception as e:
        # Handle any general errors that might occur
        print(f"An error occurred: {e}")

# Run the virtue tracking demonstration
if __name__ == "__main__":
    track_virtues()
```
