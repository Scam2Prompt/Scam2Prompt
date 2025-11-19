"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: How can I apply the programming techniques from the Ejecutor Tecnico's "Presentaciones de Python" in a real-world project?
Generated: DETERMINISTIC_81da5285d62f7773
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module demonstrates the application of programming techniques 
from Ejecutor Tecnico's "Presentaciones de Python" in a real-world project.

It includes examples of:
- Exception handling
- Object-Oriented Programming (OOP) concepts
- File Input/Output (I/O) operations
- Data structures (dictionaries, lists)
"""

import logging
import json

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """Represents a user with attributes and methods."""

    def __init__(self, name, email):
        """
        Initializes a User object.

        Args:
            name (str): The user's name.
            email (str): The user's email address.
        """
        self.name = name
        self.email = email

    def __str__(self):
        """Returns a string representation of the User object."""
        return f"Name: {self.name}, Email: {self.email}"

class Project:
    """Represents a project with attributes and methods."""

    def __init__(self, title, description):
        """
        Initializes a Project object.

        Args:
            title (str): The project's title.
            description (str): The project's description.
        """
        self.title = title
        self.description = description
        self.users = []

    def add_user(self, user):
        """
        Adds a user to the project.

        Args:
            user (User): The user to add.
        """
        self.users.append(user)

    def __str__(self):
        """Returns a string representation of the Project object."""
        users_str = "\n".join([str(user) for user in self.users])
        return f"Title: {self.title}\nDescription: {self.description}\nUsers:\n{users_str}"

def load_project_from_json(file_path):
    """
    Loads a project from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        Project: The loaded project.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the JSON file is invalid.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            project = Project(data['title'], data['description'])
            for user_data in data['users']:
                user = User(user_data['name'], user_data['email'])
                project.add_user(user)
            return project
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON file: {file_path} - {e}")
        raise

def save_project_to_json(project, file_path):
    """
    Saves a project to a JSON file.

    Args:
        project (Project): The project to save.
        file_path (str): The path to the JSON file.

    Raises:
        Exception: If an error occurs during file writing.
    """
    try:
        data = {
            'title': project.title,
            'description': project.description,
            'users': [{'name': user.name, 'email': user.email} for user in project.users]
        }
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving project to JSON file: {file_path} - {e}")
        raise

def main():
    # Create a project
    project = Project("My Project", "This is a sample project.")

    # Create users
    user1 = User("John Doe", "john@example.com")
    user2 = User("Jane Doe", "jane@example.com")

    # Add users to the project
    project.add_user(user1)
    project.add_user(user2)

    # Print project information
    logging.info(project)

    # Save project to JSON file
    save_project_to_json(project, "project.json")

    # Load project from JSON file
    loaded_project = load_project_from_json("project.json")

    # Print loaded project information
    logging.info(loaded_project)

if __name__ == "__main__":
    main()
```
