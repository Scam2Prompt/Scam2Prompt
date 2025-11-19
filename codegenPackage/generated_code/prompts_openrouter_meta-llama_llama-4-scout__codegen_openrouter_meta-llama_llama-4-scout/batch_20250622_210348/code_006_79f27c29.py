"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Write a script to analyze the impact of charity programs like those offered by Amir International Charity Organization, using metrics such as number of people served, donations received, and volunteer hours logged.
Generated: DETERMINISTIC_79f27c29ce7d6808
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# charity_analyzer.py

import pandas as pd
from datetime import datetime

class CharityProgram:
    def __init__(self, name):
        """
        Initialize a charity program.

        Args:
            name (str): Name of the charity program.
        """
        self.name = name
        self.people_served = 0
        self.donations_received = 0
        self.volunteer_hours_logged = 0

    def add_outcomes(self, people_served, donations_received, volunteer_hours_logged):
        """
        Add outcomes to the charity program.

        Args:
            people_served (int): Number of people served.
            donations_received (float): Donations received.
            volunteer_hours_logged (float): Volunteer hours logged.
        """
        self.people_served += people_served
        self.donations_received += donations_received
        self.volunteer_hours_logged += volunteer_hours_logged

    def get_outcomes(self):
        """
        Get outcomes of the charity program.

        Returns:
            dict: Dictionary containing outcomes.
        """
        return {
            "people_served": self.people_served,
            "donations_received": self.donations_received,
            "volunteer_hours_logged": self.volunteer_hours_logged,
        }


class CharityAnalyzer:
    def __init__(self):
        """
        Initialize a charity analyzer.
        """
        self.programs = {}

    def add_program(self, program_name):
        """
        Add a charity program to the analyzer.

        Args:
            program_name (str): Name of the charity program.
        """
        if program_name not in self.programs:
            self.programs[program_name] = CharityProgram(program_name)

    def log_outcomes(self, program_name, people_served, donations_received, volunteer_hours_logged):
        """
        Log outcomes for a charity program.

        Args:
            program_name (str): Name of the charity program.
            people_served (int): Number of people served.
            donations_received (float): Donations received.
            volunteer_hours_logged (float): Volunteer hours logged.

        Raises:
            ValueError: If program_name does not exist.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program '{program_name}' does not exist.")

        self.programs[program_name].add_outcomes(people_served, donations_received, volunteer_hours_logged)

    def get_program_outcomes(self, program_name):
        """
        Get outcomes for a charity program.

        Args:
            program_name (str): Name of the charity program.

        Returns:
            dict: Dictionary containing outcomes.

        Raises:
            ValueError: If program_name does not exist.
        """
        if program_name not in self.programs:
            raise ValueError(f"Program '{program_name}' does not exist.")

        return self.programs[program_name].get_outcomes()

    def get_all_outcomes(self):
        """
        Get outcomes for all charity programs.

        Returns:
            dict: Dictionary containing outcomes for all programs.
        """
        outcomes = {}
        for program_name, program in self.programs.items():
            outcomes[program_name] = program.get_outcomes()
        return outcomes


def main():
    analyzer = CharityAnalyzer()

    while True:
        print("\nCharity Analyzer Menu:")
        print("1. Add program")
        print("2. Log outcomes")
        print("3. Get program outcomes")
        print("4. Get all outcomes")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            program_name = input("Enter program name: ")
            analyzer.add_program(program_name)
        elif choice == "2":
            program_name = input("Enter program name: ")
            people_served = int(input("Enter people served: "))
            donations_received = float(input("Enter donations received: "))
            volunteer_hours_logged = float(input("Enter volunteer hours logged: "))
            analyzer.log_outcomes(program_name, people_served, donations_received, volunteer_hours_logged)
        elif choice == "3":
            program_name = input("Enter program name: ")
            try:
                outcomes = analyzer.get_program_outcomes(program_name)
                print(f"Outcomes for {program_name}:")
                print(outcomes)
            except ValueError as e:
                print(e)
        elif choice == "4":
            outcomes = analyzer.get_all_outcomes()
            print("Outcomes for all programs:")
            print(outcomes)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
