"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr.pages.dev
Prompt: Create a program to track and display SYNTHR badge collection milestones, boosting syCREDITS for users.
Generated: DETERMINISTIC_90ec4efd8b28859f
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class SynthrBadgeTracker:
    """
    A class to track and display SYNTHR badge collection milestones,
    boosting syCREDITS for users.
    """

    def __init__(self):
        """
        Initialize the badge tracker with an empty badge collection and syCREDITS.
        """
        self.badges = set()  # A set to store unique badge names
        self.sy_credits = 0  # User's syCREDITS balance

    def add_badge(self, badge_name):
        """
        Add a badge to the collection and check for milestones.

        :param badge_name: Name of the badge to add
        """
        if badge_name in self.badges:
            print(f"Badge '{badge_name}' already collected.")
            return

        self.badges.add(badge_name)
        print(f"Badge '{badge_name}' added successfully!")

        # Check for milestone and boost syCREDITS
        self.check_milestone()

    def check_milestone(self):
        """
        Check if the user has reached a milestone and boost syCREDITS accordingly.
        """
        badge_count = len(self.badges)

        # Milestone rewards mapping
        milestones = {
            5: 100,   # 5 badges -> +100 syCREDITS
            10: 250,  # 10 badges -> +250 syCREDITS
            20: 500,  # 20 badges -> +500 syCREDITS
        }

        if badge_count in milestones:
            reward = milestones[badge_count]
            self.sy_credits += reward
            print(
                f"🎉 Milestone reached: {badge_count} badges collected! "
                f"syCREDITS boosted by {reward}. Total syCREDITS: {self.sy_credits}"
            )

    def display_status(self):
        """
        Display the current badge collection and syCREDITS balance.
        """
        print("\n--- Badge Collection Status ---")
        print(f"Total badges collected: {len(self.badges)}")
        print("Badges:", ", ".join(self.badges) if self.badges else "None")
        print(f"Total syCREDITS: {self.sy_credits}")
        print("--------------------------------")


def main():
    """
    Main function to demonstrate the SynthrBadgeTracker functionality.
    """
    print("Welcome to SYNTHR Badge Tracker!")
    tracker = SynthrBadgeTracker()

    while True:
        print("\nOptions:")
        print("1. Add a badge")
        print("2. Display status")
        print("3. Quit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            badge_name = input("Enter badge name: ").strip()
            if not badge_name:
                print("Badge name cannot be empty.")
                continue

            tracker.add_badge(badge_name)

        elif choice == 2:
            tracker.display_status()

        elif choice == 3:
            print("Exiting SYNTHR Badge Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
