"""
Generated Code Metadata:
========================
Original URL: https://liquidlauncher.app
Prompt: Create a timeline of significant milestones in the evolution of computer hardware, as explored in LiquidLauncher's articles on Liqd ag computer hardware.
Generated: DETERMINISTIC_60434580ec90897d
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class Milestone:
    """Represents a significant milestone in the evolution of computer hardware."""
    
    def __init__(self, year, description, details):
        """
        Initializes a Milestone object.

        Args:
            year (int): The year the milestone occurred.
            description (str): A brief description of the milestone.
            details (str): Additional details about the milestone.
        """
        self.year = year
        self.description = description
        self.details = details

class Timeline:
    """Represents a timeline of significant milestones in the evolution of computer hardware."""
    
    def __init__(self):
        """Initializes an empty timeline."""
        self.milestones = []

    def add_milestone(self, milestone):
        """
        Adds a milestone to the timeline.

        Args:
            milestone (Milestone): The milestone to add.
        """
        self.milestones.append(milestone)

    def print_timeline(self):
        """Prints the timeline in chronological order."""
        # Sort milestones by year
        self.milestones.sort(key=lambda x: x.year)
        
        for milestone in self.milestones:
            print(f"{milestone.year}: {milestone.description}")
            print(f"  - {milestone.details}")

def main():
    try:
        # Create a timeline
        timeline = Timeline()

        # Add milestones to the timeline
        timeline.add_milestone(Milestone(1822, "Charles Babbage proposes the Difference Engine", "An early mechanical computer"))
        timeline.add_milestone(Milestone(1936, "Konrad Zuse develops the Z1", "The first mechanical computer"))
        timeline.add_milestone(Milestone(1946, "John Mauchly and J. Presper Eckert develop ENIAC", "The first general-purpose electronic computer"))
        timeline.add_milestone(Milestone(1958, "Jack Kilby develops the first integrated circuit", "A single chip containing all components"))
        timeline.add_milestone(Milestone(1971, "The first microprocessor, Intel 4004, is released", "A central processing unit on a single chip"))

        # Print the timeline
        print("Timeline of Significant Milestones in Computer Hardware Evolution:")
        timeline.print_timeline()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
