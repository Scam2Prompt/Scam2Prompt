"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-app.pages.dev
Prompt: Implement a solution to collect SYNTHR badges programmatically by completing milestones and boosting syCREDITS.
Generated: DETERMINISTIC_0101ebc112281ded
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class SynthrBadgeCollector:
    def __init__(self):
        """
        Initializes the SynthrBadgeCollector with empty milestones
        and a default syCREDITS balance.
        """
        self.milestones = {}
        self.sycredits = 0
        self.badges = []

    def add_milestone(self, milestone_name, milestone_points):
        """
        Adds a milestone to be tracked along with the required points.

        :param milestone_name: Name of the milestone
        :param milestone_points: Points required to complete the milestone
        """
        if milestone_name not in self.milestones:
            self.milestones[milestone_name] = {
                "points_required": milestone_points,
                "completed": False
            }
        else:
            raise ValueError(f"Milestone '{milestone_name}' already exists.")

    def boost_sycredits(self, credits):
        """
        Boosts syCREDITS balance.

        :param credits: Number of credits to add
        """
        if credits <= 0:
            raise ValueError("Credits must be greater than 0.")
        self.sycredits += credits

    def complete_milestone(self, milestone_name):
        """
        Completes a milestone if the required points are achieved.

        :param milestone_name: Name of the milestone to complete
        """
        if milestone_name not in self.milestones:
            raise KeyError(f"Milestone '{milestone_name}' does not exist.")

        milestone = self.milestones[milestone_name]
        if self.sycredits >= milestone["points_required"]:
            milestone["completed"] = True
            self.badges.append(milestone_name)  # Award badge for milestone completion
            self.sycredits -= milestone["points_required"]  # Deduct points used
            print(f"Milestone '{milestone_name}' completed! Badge awarded.")
        else:
            print(f"Insufficient syCREDITS to complete milestone '{milestone_name}'.")
        
    def list_badges(self):
        """
        Lists all collected badges.

        :return: List of badges
        """
        return self.badges

    def display_status(self):
        """
        Displays current syCREDITS balance and milestone statuses.
        """
        print(f"syCREDITS Balance: {self.sycredits}")
        print("Milestones:")
        for name, details in self.milestones.items():
            status = "Completed" if details["completed"] else "Incomplete"
            print(f"- {name}: {status} (Points Required: {details['points_required']})")


# Example usage
if __name__ == "__main__":
    collector = SynthrBadgeCollector()
    
    try:
        # Add milestones
        collector.add_milestone("Milestone1", 100)
        collector.add_milestone("Milestone2", 200)

        # Boost syCREDITS
        collector.boost_sycredits(150)

        # Attempt milestone completion
        collector.complete_milestone("Milestone1")  # Should succeed
        collector.complete_milestone("Milestone2")  # Should fail

        # Display current status
        collector.display_status()

        # List badges
        print("Collected Badges:", collector.list_badges())
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
