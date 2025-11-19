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
# library_management_system.py

class Resource:
    """Represents a library resource."""

    def __init__(self, title, author, resource_type, status="Available"):
        """
        Initializes a Resource object.

        Args:
            title (str): Resource title.
            author (str): Resource author.
            resource_type (str): Resource type (e.g., book, article).
            status (str, optional): Resource status. Defaults to "Available".
        """
        self.title = title
        self.author = author
        self.resource_type = resource_type
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} ({self.resource_type}) - {self.status}"


class Library:
    """Represents a library with resources."""

    def __init__(self):
        """Initializes a Library object."""
        self.resources = []

    def add_resource(self, resource):
        """
        Adds a resource to the library.

        Args:
            resource (Resource): Resource to add.
        """
        self.resources.append(resource)

    def remove_resource(self, title):
        """
        Removes a resource from the library.

        Args:
            title (str): Title of the resource to remove.

        Raises:
            ValueError: If the resource is not found.
        """
        for resource in self.resources:
            if resource.title == title:
                self.resources.remove(resource)
                return
        raise ValueError("Resource not found")

    def update_resource_status(self, title, status):
        """
        Updates the status of a resource.

        Args:
            title (str): Title of the resource to update.
            status (str): New status.

        Raises:
            ValueError: If the resource is not found.
        """
        for resource in self.resources:
            if resource.title == title:
                resource.status = status
                return
        raise ValueError("Resource not found")

    def list_resources(self):
        """Lists all resources in the library."""
        return self.resources


class User:
    """Represents a library user."""

    def __init__(self, name):
        """
        Initializes a User object.

        Args:
            name (str): User name.
        """
        self.name = name
        self.borrowed_resources = []

    def borrow_resource(self, resource):
        """
        Borrows a resource.

        Args:
            resource (Resource): Resource to borrow.

        Raises:
            ValueError: If the resource is not available.
        """
        if resource.status != "Available":
            raise ValueError("Resource is not available")
        self.borrowed_resources.append(resource)
        resource.status = "Borrowed"

    def return_resource(self, resource):
        """
        Returns a borrowed resource.

        Args:
            resource (Resource): Resource to return.

        Raises:
            ValueError: If the user has not borrowed the resource.
        """
        if resource not in self.borrowed_resources:
            raise ValueError("User has not borrowed this resource")
        self.borrowed_resources.remove(resource)
        resource.status = "Available"


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add resource")
        print("2. Remove resource")
        print("3. Update resource status")
        print("4. List resources")
        print("5. Borrow resource")
        print("6. Return resource")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter resource title: ")
            author = input("Enter resource author: ")
            resource_type = input("Enter resource type: ")
            library.add_resource(Resource(title, author, resource_type))
        elif choice == "2":
            title = input("Enter resource title: ")
            try:
                library.remove_resource(title)
            except ValueError as e:
                print(e)
        elif choice == "3":
            title = input("Enter resource title: ")
            status = input("Enter new status: ")
            try:
                library.update_resource_status(title, status)
            except ValueError as e:
                print(e)
        elif choice == "4":
            for resource in library.list_resources():
                print(resource)
        elif choice == "5":
            title = input("Enter resource title: ")
            for resource in library.list_resources():
                if resource.title == title:
                    user = User("Current User")  # Replace with actual user
                    try:
                        user.borrow_resource(resource)
                    except ValueError as e:
                        print(e)
                    break
            else:
                print("Resource not found")
        elif choice == "6":
            title = input("Enter resource title: ")
            for resource in library.list_resources():
                if resource.title == title:
                    user = User("Current User")  # Replace with actual user
                    try:
                        user.return_resource(resource)
                    except ValueError as e:
                        print(e)
                    break
            else:
                print("Resource not found")
        elif choice == "7":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
```
