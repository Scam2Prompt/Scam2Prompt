"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Develop a function that simulates the "internal time management" technique described by A. Sheffer, allowing users to track and optimize their personal time usage.
Generated: DETERMINISTIC_6776b63bbb94679b
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class TimeBlock:
    """Represents a block of time with a start and end time, and an optional description."""

    def __init__(self, start_time: datetime, end_time: datetime, description: str = ""):
        """
        Initializes a TimeBlock.

        Args:
        - start_time (datetime): The start time of the block.
        - end_time (datetime): The end time of the block.
        - description (str): An optional description of the block.
        """
        if start_time >= end_time:
            raise ValueError("Start time must be before end time")

        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def duration(self) -> timedelta:
        """Returns the duration of the time block."""
        return self.end_time - self.start_time


class TimeManagement:
    """Manages a list of time blocks and provides methods to add, remove, and analyze them."""

    def __init__(self):
        self.time_blocks: List[TimeBlock] = []

    def add_time_block(self, time_block: TimeBlock):
        """
        Adds a time block to the list.

        Args:
        - time_block (TimeBlock): The time block to add.
        """
        self.time_blocks.append(time_block)

    def remove_time_block(self, index: int):
        """
        Removes a time block from the list.

        Args:
        - index (int): The index of the time block to remove.

        Raises:
        - IndexError: If the index is out of range.
        """
        try:
            del self.time_blocks[index]
        except IndexError as e:
            raise IndexError("Index out of range") from e

    def get_total_time(self) -> timedelta:
        """Returns the total duration of all time blocks."""
        return sum(time_block.duration() for time_block in self.time_blocks)

    def get_time_blocks(self) -> List[TimeBlock]:
        """Returns a list of all time blocks."""
        return self.time_blocks

    def analyze_time_blocks(self) -> Dict[str, timedelta]:
        """
        Analyzes the time blocks and returns a dictionary with the total time spent on each description.

        Returns:
        - Dict[str, timedelta]: A dictionary with descriptions as keys and total time spent as values.
        """
        time_spent: Dict[str, timedelta] = {}
        for time_block in self.time_blocks:
            if time_block.description:
                if time_block.description in time_spent:
                    time_spent[time_block.description] += time_block.duration()
                else:
                    time_spent[time_block.description] = time_block.duration()
        return time_spent


def main():
    time_management = TimeManagement()

    while True:
        print("\n1. Add time block")
        print("2. Remove time block")
        print("3. Get total time")
        print("4. Analyze time blocks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            start_time_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
            end_time_str = input("Enter end time (YYYY-MM-DD HH:MM): ")
            description = input("Enter description (optional): ")

            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

            time_block = TimeBlock(start_time, end_time, description)
            time_management.add_time_block(time_block)
        elif choice == "2":
            index = int(input("Enter index of time block to remove: "))
            try:
                time_management.remove_time_block(index)
            except IndexError as e:
                print(str(e))
        elif choice == "3":
            total_time = time_management.get_total_time()
            print(f"Total time: {total_time}")
        elif choice == "4":
            time_spent = time_management.analyze_time_blocks()
            for description, time in time_spent.items():
                print(f"{description}: {time}")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
