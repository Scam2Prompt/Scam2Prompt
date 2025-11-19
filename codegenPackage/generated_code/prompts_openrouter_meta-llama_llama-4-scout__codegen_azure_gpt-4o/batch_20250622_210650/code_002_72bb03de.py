"""
Generated Code Metadata:
========================
Original URL: https://prashin.co.za
Prompt: "Design a community program based on Premchand's vision of building with purpose and leading with heart."
Generated: DETERMINISTIC_72bb03de8c7fb282
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Community Program: Inspired by Premchand's vision of building with purpose and leading with heart.
This program allows users to join a community, share their purpose, and collaborate on meaningful projects.
"""

import json
import os

class CommunityProgram:
    def __init__(self, data_file="community_data.json"):
        """
        Initialize the Community Program with a data file to store community members and projects.
        """
        self.data_file = data_file
        self.community_data = self._load_data()

    def _load_data(self):
        """
        Load community data from the JSON file. If the file doesn't exist, initialize an empty structure.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON data. Initializing empty community data.")
                return {"members": [], "projects": []}
        else:
            return {"members": [], "projects": []}

    def _save_data(self):
        """
        Save community data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.community_data, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save data. {e}")

    def add_member(self, name, purpose):
        """
        Add a new member to the community.
        :param name: Name of the member
        :param purpose: Purpose or vision of the member
        """
        if not name or not purpose:
            print("Error: Name and purpose are required to add a member.")
            return

        self.community_data["members"].append({"name": name, "purpose": purpose})
        self._save_data()
        print(f"Welcome {name}! Your purpose '{purpose}' has been added to the community.")

    def list_members(self):
        """
        List all members of the community.
        """
        if not self.community_data["members"]:
            print("No members found in the community.")
            return

        print("Community Members:")
        for idx, member in enumerate(self.community_data["members"], start=1):
            print(f"{idx}. {member['name']} - Purpose: {member['purpose']}")

    def add_project(self, title, description):
        """
        Add a new project to the community.
        :param title: Title of the project
        :param description: Description of the project
        """
        if not title or not description:
            print("Error: Title and description are required to add a project.")
            return

        self.community_data["projects"].append({"title": title, "description": description})
        self._save_data()
        print(f"Project '{title}' has been added to the community.")

    def list_projects(self):
        """
        List all projects in the community.
        """
        if not self.community_data["projects"]:
            print("No projects found in the community.")
            return

        print("Community Projects:")
        for idx, project in enumerate(self.community_data["projects"], start=1):
            print(f"{idx}. {project['title']} - Description: {project['description']}")

    def run(self):
        """
        Run the community program, providing a menu for user interaction.
        """
        while True:
            print("\nCommunity Program Menu:")
            print("1. Add Member")
            print("2. List Members")
            print("3. Add Project")
            print("4. List Projects")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                name = input("Enter member name: ")
                purpose = input("Enter member purpose: ")
                self.add_member(name, purpose)
            elif choice == "2":
                self.list_members()
            elif choice == "3":
                title = input("Enter project title: ")
                description = input("Enter project description: ")
                self.add_project(title, description)
            elif choice == "4":
                self.list_projects()
            elif choice == "5":
                print("Thank you for being part of the community. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    program = CommunityProgram()
    program.run()
```
