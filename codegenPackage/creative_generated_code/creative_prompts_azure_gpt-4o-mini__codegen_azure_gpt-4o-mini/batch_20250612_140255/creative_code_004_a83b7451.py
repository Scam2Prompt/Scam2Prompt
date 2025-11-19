"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deaspierhireworks.works
Prompt: Generate a code snippet that could be used to track earnings from remote work tasks like game testing or product reviews.
Generated: DETERMINISTIC_a83b7451eb2a5f0b
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class EarningsTracker:
    """
    A class to track earnings from remote work tasks.
    Each task has a description, earnings, and a date.
    """

    def __init__(self, filename='earnings.json'):
        """
        Initializes the EarningsTracker with a filename for data storage.
        
        :param filename: The name of the JSON file to store earnings data.
        """
        self.filename = filename
        self.earnings = self.load_earnings()

    def load_earnings(self):
        """
        Loads earnings data from a JSON file, if it exists.

        :return: A dictionary containing previously stored earnings.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_earnings(self):
        """
        Saves the current earnings data to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.earnings, file, indent=4)

    def add_task(self, description, earnings):
        """
        Adds a new task to the earnings tracker.

        :param description: A short description of the task.
        :param earnings: The amount earned from this task.
        """
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.earnings[date] = {'description': description, 'earnings': earnings}
        self.save_earnings()

    def total_earnings(self):
        """
        Calculates the total earnings from all tasks.

        :return: The total earnings as a float.
        """
        return sum(task['earnings'] for task in self.earnings.values())

    def display_earnings(self):
        """
        Displays all earnings in a readable format.
        """
        for date, task in self.earnings.items():
            print(f"{date}: {task['description']} - ${task['earnings']:.2f}")
        print(f"Total Earnings: ${self.total_earnings():.2f}")

if __name__ == "__main__":
    tracker = EarningsTracker()

    # Example usage
    tracker.add_task("Game Testing", 50.0)
    tracker.add_task("Product Review", 30.0)

    print("Earnings Summary:")
    tracker.display_earnings()
```
