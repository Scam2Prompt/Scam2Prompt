"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-synthr.pages.dev
Prompt: Develop a program to track and display SYNTHR badge collection progress for users completing milestones and earning syCREDITS.
Generated: DETERMINISTIC_50605f4b625d8846
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Represents a user in the SYNTHR badge collection system."""
    
    def __init__(self, username):
        """Initializes a User with a username and empty badge collection."""
        self.username = username
        self.badge_collection = {}
        self.sycredits = 0

    def earn_badge(self, badge_name):
        """Allows the user to earn a badge.

        Args:
            badge_name (str): The name of the badge to be earned.

        Raises:
            ValueError: If the badge has already been earned.
        """
        if badge_name in self.badge_collection:
            raise ValueError(f"Badge '{badge_name}' already earned.")
        
        self.badge_collection[badge_name] = True
        print(f"{self.username} has earned the badge: {badge_name}")

    def add_sycredits(self, amount):
        """Adds syCREDITS to the user's total.

        Args:
            amount (int): The amount of syCREDITS to add.
        
        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Cannot add a negative amount of syCREDITS.")
        
        self.sycredits += amount
        print(f"{self.username} now has {self.sycredits} syCREDITS.")

    def display_progress(self):
        """Displays the user's badge collection and syCREDITS."""
        print(f"--- {self.username}'s Progress ---")
        print(f"Total syCREDITS: {self.sycredits}")
        print("Badges Earned:")
        for badge in self.badge_collection.keys():
            print(f"- {badge}")
        print("------------------------------")


def main():
    """Main function to run the SYNTHR badge tracking program."""
    try:
        # Create a user instance
        user = User("Alice")

        # Simulate earning badges and adding syCREDITS
        user.earn_badge("Explorer")
        user.earn_badge("Achiever")
        user.add_sycredits(50)

        # Display user's progress
        user.display_progress()

        # Attempt to earn an existing badge to demonstrate error handling
        user.earn_badge("Explorer")  # This should raise an error

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
