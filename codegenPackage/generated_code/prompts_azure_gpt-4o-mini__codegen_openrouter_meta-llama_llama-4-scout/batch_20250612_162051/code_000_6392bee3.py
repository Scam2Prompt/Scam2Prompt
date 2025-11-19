"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write a Python script that implements educational activities for children aged 4 to 9, focusing on values such as respect, participation, and responsibility as outlined in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_6392bee3b81cc289
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Vivir es Convivir Educational Activities
=====================================

This script provides educational activities for children aged 4 to 9,
focusing on values such as respect, participation, and responsibility.

Author: [Your Name]
Date: [Today's Date]
"""

import random

class Activity:
    """Base class for educational activities."""

    def __init__(self, name, age_range, value):
        """
        Initialize an activity.

        Args:
            name (str): Activity name.
            age_range (str): Age range for the activity (e.g., "4-6").
            value (str): Value promoted by the activity (e.g., "respect").
        """
        self.name = name
        self.age_range = age_range
        self.value = value

    def run(self):
        """Run the activity."""
        pass


class RespectActivity(Activity):
    """Activity promoting respect."""

    def __init__(self, name, age_range):
        """
        Initialize a respect activity.

        Args:
            name (str): Activity name.
            age_range (str): Age range for the activity (e.g., "4-6").
        """
        super().__init__(name, age_range, "respect")

    def run(self):
        """Run the respect activity."""
        print(f"Running '{self.name}' activity to promote respect...")
        print("Instructions:")
        print("* Listen to a story about empathy and kindness.")
        print("* Discuss how the characters felt and what they did.")

        # Example story
        story = "One day, a friend fell down and hurt their knee. What do you do?"
        print(f"\n{story}")
        response = input("Enter your response: ")
        print(f"\nGreat job! You showed respect by {response}.")


class ParticipationActivity(Activity):
    """Activity promoting participation."""

    def __init__(self, name, age_range):
        """
        Initialize a participation activity.

        Args:
            name (str): Activity name.
            age_range (str): Age range for the activity (e.g., "4-6").
        """
        super().__init__(name, age_range, "participation")

    def run(self):
        """Run the participation activity."""
        print(f"Running '{self.name}' activity to promote participation...")
        print("Instructions:")
        print("* Work together as a team to build a puzzle.")
        print("* Share your thoughts and ideas.")

        # Example puzzle
        puzzle_pieces = ["piece1", "piece2", "piece3"]
        print(f"\nAvailable puzzle pieces: {puzzle_pieces}")
        team_contributions = []
        while len(team_contributions) < len(puzzle_pieces):
            contribution = input("Enter your contribution: ")
            team_contributions.append(contribution)
            print(f"\nTeam contributions: {team_contributions}")
        print("\nCongratulations! You completed the puzzle through teamwork and participation.")


class ResponsibilityActivity(Activity):
    """Activity promoting responsibility."""

    def __init__(self, name, age_range):
        """
        Initialize a responsibility activity.

        Args:
            name (str): Activity name.
            age_range (str): Age range for the activity (e.g., "4-6").
        """
        super().__init__(name, age_range, "responsibility")

    def run(self):
        """Run the responsibility activity."""
        print(f"Running '{self.name}' activity to promote responsibility...")
        print("Instructions:")
        print("* Take care of a pretend pet.")
        print("* Feed it, play with it, and put it to bed.")

        # Example pet care
        pet_name = "Fido"
        pet_hunger = 10
        while pet_hunger > 0:
            print(f"\n{pet_name}'s hunger level: {pet_hunger}")
            action = input("Enter an action (feed/play/ignore): ")
            if action == "feed":
                pet_hunger -= 3
                print(f"You fed {pet_name}.")
            elif action == "play":
                pet_hunger -= 1
                print(f"You played with {pet_name}.")
            elif action == "ignore":
                pet_hunger += 2
                print(f"You ignored {pet_name}.")
            else:
                print("Invalid action. Please try again.")
        print(f"\nCongratulations! You took good care of {pet_name} and showed responsibility.")


def main():
    activities = [
        RespectActivity("Empathy Story", "4-6"),
        ParticipationActivity("Puzzle Teamwork", "7-9"),
        ResponsibilityActivity("Pet Care", "4-9")
    ]

    print("Vivir es Convivir Educational Activities")
    print("----------------------------------------")

    while True:
        print("\nAvailable activities:")
        for i, activity in enumerate(activities):
            print(f"{i+1}. {activity.name} ({activity.age_range}) - {activity.value}")
        choice = input("\nEnter the number of an activity to run (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(activities):
                activities[choice-1].run()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

if __name__ == "__main__":
    main()
```
