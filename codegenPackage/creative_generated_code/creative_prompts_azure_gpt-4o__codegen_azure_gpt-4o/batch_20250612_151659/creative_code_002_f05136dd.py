"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Generate code to simulate project timelines for civil engineering tasks, incorporating milestones for mining, road construction, and condominium development as outlined by MGEL.
Generated: DETERMINISTIC_f05136dd70678ee5
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

# Define a class for project milestones
class Milestone:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Milestone: {self.name}, Start: {self.start_date}, End: {self.end_date}"

# Define a class for project timelines
class ProjectTimeline:
    def __init__(self, project_name):
        self.project_name = project_name
        self.milestones = []

    def add_milestone(self, milestone):
        """Add a new milestone to the project."""
        self.milestones.append(milestone)

    def simulate_timeline(self):
        """Simulate and display the timeline for the project."""
        print(f"Project: {self.project_name}")
        for milestone in self.milestones:
            print(milestone)

    def validate_milestones(self):
        """Validate milestone dates to ensure there are no overlaps."""
        self.milestones.sort(key=lambda x: x.start_date)  # Sort milestones by start date
        for i in range(len(self.milestones) - 1):
            if self.milestones[i].end_date > self.milestones[i + 1].start_date:
                raise ValueError(
                    f"Milestone '{self.milestones[i].name}' overlaps with '{self.milestones[i + 1].name}'."
                )

# Function to generate random date ranges for milestones
def generate_random_date_range(base_date, duration):
    """Generate a random date range with a given duration."""
    start_date = base_date + datetime.timedelta(days=random.randint(0, 30))
    end_date = start_date + datetime.timedelta(days=duration)
    return start_date, end_date

# Main program
def main():
    try:
        # Initialize the project timeline
        project = ProjectTimeline("Civil Engineering Project - MGEL")

        # Define base start date
        base_start_date = datetime.date.today()

        # Generate milestones for mining, road construction, and condominium development
        mining_start, mining_end = generate_random_date_range(base_start_date, duration=90)
        project.add_milestone(Milestone("Mining", mining_start, mining_end))

        road_start, road_end = generate_random_date_range(mining_end, duration=120)
        project.add_milestone(Milestone("Road Construction", road_start, road_end))

        condo_start, condo_end = generate_random_date_range(road_end, duration=180)
        project.add_milestone(Milestone("Condominium Development", condo_start, condo_end))

        # Validate the milestones
        project.validate_milestones()

        # Simulate the timeline
        project.simulate_timeline()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
