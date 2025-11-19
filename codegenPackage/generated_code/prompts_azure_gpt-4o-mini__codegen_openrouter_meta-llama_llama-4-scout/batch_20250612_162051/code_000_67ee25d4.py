"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Generate a Python script to implement a community empowerment project similar to those described on the AIDA website, focusing on women empowerment and skill training.
Generated: DETERMINISTIC_67ee25d4d65584f3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_empowerment_project.py

"""
Community Empowerment Project: Women Empowerment and Skill Training

This script implements a basic management system for a community empowerment project.
It allows for user registration, skill training program enrollment, and progress tracking.
"""

import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """Represents a user in the community empowerment project."""

    def __init__(self, id, name, email, phone_number):
        """
        Initializes a User object.

        Args:
            id (int): Unique user ID.
            name (str): User name.
            email (str): User email.
            phone_number (str): User phone number.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.skill_programs = []

    def enroll_in_skill_program(self, program):
        """
        Enrolls the user in a skill training program.

        Args:
            program (str): Name of the skill training program.
        """
        self.skill_programs.append(program)
        logging.info(f"User {self.name} enrolled in {program}.")

    def __str__(self):
        return f"User {self.id}: {self.name}, {self.email}, {self.phone_number}"


class CommunityEmpowermentProject:
    """Manages the community empowerment project."""

    def __init__(self):
        self.users = {}
        self.skill_programs = set()

    def register_user(self, id, name, email, phone_number):
        """
        Registers a new user in the project.

        Args:
            id (int): Unique user ID.
            name (str): User name.
            email (str): User email.
            phone_number (str): User phone number.

        Returns:
            User: The newly registered user.
        """
        if id in self.users:
            logging.error("User ID already exists.")
            raise ValueError("User ID already exists.")

        user = User(id, name, email, phone_number)
        self.users[id] = user
        logging.info(f"User {name} registered.")
        return user

    def add_skill_program(self, program):
        """
        Adds a new skill training program.

        Args:
            program (str): Name of the skill training program.
        """
        self.skill_programs.add(program)
        logging.info(f"Skill program {program} added.")

    def enroll_user_in_skill_program(self, user_id, program):
        """
        Enrolls a user in a skill training program.

        Args:
            user_id (int): ID of the user to enroll.
            program (str): Name of the skill training program.

        Raises:
            ValueError: If the user ID or skill program is invalid.
        """
        if user_id not in self.users:
            logging.error("Invalid user ID.")
            raise ValueError("Invalid user ID.")

        if program not in self.skill_programs:
            logging.error("Invalid skill program.")
            raise ValueError("Invalid skill program.")

        user = self.users[user_id]
        user.enroll_in_skill_program(program)

    def __str__(self):
        project_info = "Community Empowerment Project\n"
        project_info += f"Registered Users: {len(self.users)}\n"
        project_info += f"Skill Programs: {', '.join(self.skill_programs)}\n"
        return project_info


def main():
    project = CommunityEmpowermentProject()

    # Add skill programs
    project.add_skill_program("Vocational Training")
    project.add_skill_program("Financial Literacy")
    project.add_skill_program("Leadership Development")

    while True:
        print("\n1. Register User")
        print("2. Enroll User in Skill Program")
        print("3. View Project Information")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            phone_number = input("Enter user phone number: ")
            project.register_user(id, name, email, phone_number)
        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            program = input("Enter skill program: ")
            try:
                project.enroll_user_in_skill_program(user_id, program)
            except ValueError as e:
                print(e)
        elif choice == "3":
            print(project)
            for user in project.users.values():
                print(user)
                print(f"Enrolled in: {', '.join(user.skill_programs)}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
