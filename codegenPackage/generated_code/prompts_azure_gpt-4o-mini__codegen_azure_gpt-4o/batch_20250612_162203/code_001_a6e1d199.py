"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: How can I implement a library management system for an educational institution that provides resources for admission exam preparation, similar to the "Biblioteca de estudio en casa" mentioned on Educar Comitán?
Generated: DETERMINISTIC_a6e1d199418e6da6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Library Management System for Educational Institution
# This system allows users to manage resources for admission exam preparation.

import json
from datetime import datetime

class LibraryManagementSystem:
    def __init__(self):
        # Initialize the library with an empty catalog and user database
        self.catalog = {}  # Dictionary to store books/resources
        self.users = {}    # Dictionary to store user information

    # Add a new resource to the catalog
    def add_resource(self, resource_id, title, author, subject, copies):
        """
        Adds a new resource to the library catalog.
        :param resource_id: Unique identifier for the resource
        :param title: Title of the resource
        :param author: Author of the resource
        :param subject: Subject category of the resource
        :param copies: Number of copies available
        """
        if resource_id in self.catalog:
            raise ValueError("Resource ID already exists in the catalog.")
        
        self.catalog[resource_id] = {
            "title": title,
            "author": author,
            "subject": subject,
            "copies": copies,
            "borrowed": 0
        }

    # Register a new user
    def register_user(self, user_id, name, email):
        """
        Registers a new user in the system.
        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param email: Email address of the user
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        self.users[user_id] = {
            "name": name,
            "email": email,
            "borrowed_resources": []
        }

    # Borrow a resource
    def borrow_resource(self, user_id, resource_id):
        """
        Allows a user to borrow a resource if available.
        :param user_id: ID of the user borrowing the resource
        :param resource_id: ID of the resource to be borrowed
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        if resource_id not in self.catalog:
            raise ValueError("Resource ID not found.")
        
        resource = self.catalog[resource_id]
        if resource["copies"] - resource["borrowed"] <= 0:
            raise ValueError("No copies available for borrowing.")
        
        # Update resource and user data
        resource["borrowed"] += 1
        self.users[user_id]["borrowed_resources"].append({
            "resource_id": resource_id,
            "borrowed_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # Return a resource
    def return_resource(self, user_id, resource_id):
        """
        Allows a user to return a borrowed resource.
        :param user_id: ID of the user returning the resource
        :param resource_id: ID of the resource to be returned
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        if resource_id not in self.catalog:
            raise ValueError("Resource ID not found.")
        
        user = self.users[user_id]
        borrowed_resources = user["borrowed_resources"]
        resource = self.catalog[resource_id]

        # Check if the user has borrowed this resource
        for borrowed in borrowed_resources:
            if borrowed["resource_id"] == resource_id:
                borrowed_resources.remove(borrowed)
                resource["borrowed"] -= 1
                return
        
        raise ValueError("Resource not borrowed by the user.")

    # Save data to a file
    def save_data(self, file_path):
        """
        Saves the library data to a JSON file.
        :param file_path: Path to the file where data will be saved
        """
        data = {
            "catalog": self.catalog,
            "users": self.users
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    # Load data from a file
    def load_data(self, file_path):
        """
        Loads library data from a JSON file.
        :param file_path: Path to the file from which data will be loaded
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.catalog = data.get("catalog", {})
                self.users = data.get("users", {})
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON data.")

# Example usage
if __name__ == "__main__":
    library = LibraryManagementSystem()

    # Add resources
    library.add_resource("R001", "Mathematics for Admission", "John Doe", "Mathematics", 5)
    library.add_resource("R002", "Physics Fundamentals", "Jane Smith", "Physics", 3)

    # Register users
    library.register_user("U001", "Alice Johnson", "alice@example.com")
    library.register_user("U002", "Bob Brown", "bob@example.com")

    # Borrow and return resources
    library.borrow_resource("U001", "R001")
    library.return_resource("U001", "R001")

    # Save and load data
    library.save_data("library_data.json")
    library.load_data("library_data.json")
```
