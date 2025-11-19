"""
Generated Code Metadata:
========================
Original URL: https://smplanka.lk
Prompt: Write a Python program to manage a library network like the "අහස පුස්තකාල ජාලය" described on smplanka.lk, including features for book distribution and volunteer management.
Generated: DETERMINISTIC_a5ffc42106b8ea29
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# library_network.py

class Book:
    """Represents a book in the library network."""

    def __init__(self, title, author, isbn, status="Available"):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            status (str, optional): The status of the book. Defaults to "Available".
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Status: {self.status}"


class Volunteer:
    """Represents a volunteer in the library network."""

    def __init__(self, name, contact_number, email):
        """
        Initializes a Volunteer object.

        Args:
            name (str): The name of the volunteer.
            contact_number (str): The contact number of the volunteer.
            email (str): The email of the volunteer.
        """
        self.name = name
        self.contact_number = contact_number
        self.email = email

    def __str__(self):
        return f"{self.name}, Contact: {self.contact_number}, Email: {self.email}"


class Library:
    """Represents a library in the library network."""

    def __init__(self, name, location):
        """
        Initializes a Library object.

        Args:
            name (str): The name of the library.
            location (str): The location of the library.
        """
        self.name = name
        self.location = location
        self.books = []
        self.volunteers = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)

    def remove_book(self, isbn):
        """Removes a book from the library."""
        self.books = [book for book in self.books if book.isbn != isbn]

    def add_volunteer(self, volunteer):
        """Adds a volunteer to the library."""
        self.volunteers.append(volunteer)

    def remove_volunteer(self, name):
        """Removes a volunteer from the library."""
        self.volunteers = [volunteer for volunteer in self.volunteers if volunteer.name != name]

    def __str__(self):
        return f"{self.name} Library at {self.location}"


class LibraryNetwork:
    """Represents the library network."""

    def __init__(self):
        self.libraries = {}

    def add_library(self, library):
        """Adds a library to the network."""
        self.libraries[library.name] = library

    def remove_library(self, name):
        """Removes a library from the network."""
        if name in self.libraries:
            del self.libraries[name]

    def distribute_book(self, library_name, book_isbn, recipient_library_name):
        """
        Distributes a book from one library to another.

        Args:
            library_name (str): The name of the library to distribute from.
            book_isbn (str): The ISBN of the book to distribute.
            recipient_library_name (str): The name of the library to distribute to.
        """
        if library_name in self.libraries and recipient_library_name in self.libraries:
            library = self.libraries[library_name]
            recipient_library = self.libraries[recipient_library_name]
            for book in library.books:
                if book.isbn == book_isbn:
                    library.books.remove(book)
                    recipient_library.add_book(book)
                    print(f"Book {book_isbn} distributed from {library_name} to {recipient_library_name}.")
                    return
            print(f"Book {book_isbn} not found in {library_name}.")
        else:
            print("One or both libraries not found in the network.")

    def __str__(self):
        return "Library Network"


def main():
    network = LibraryNetwork()

    while True:
        print("\nLibrary Network Management System")
        print("1. Add Library")
        print("2. Remove Library")
        print("3. Add Book")
        print("4. Remove Book")
        print("5. Add Volunteer")
        print("6. Remove Volunteer")
        print("7. Distribute Book")
        print("8. List Libraries")
        print("9. List Books in Library")
        print("10. List Volunteers in Library")
        print("11. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter library name: ")
            location = input("Enter library location: ")
            library = Library(name, location)
            network.add_library(library)
            print(f"Library {name} added.")

        elif choice == "2":
            name = input("Enter library name: ")
            network.remove_library(name)
            print(f"Library {name} removed.")

        elif choice == "3":
            library_name = input("Enter library name: ")
            if library_name in network.libraries:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                book = Book(title, author, isbn)
                network.libraries[library_name].add_book(book)
                print(f"Book {title} added to {library_name}.")
            else:
                print(f"Library {library_name} not found.")

        elif choice == "4":
            library_name = input("Enter library name: ")
            if library_name in network.libraries:
                isbn = input("Enter book ISBN: ")
                network.libraries[library_name].remove_book(isbn)
                print(f"Book with ISBN {isbn} removed from {library_name}.")
            else:
                print(f"Library {library_name} not found.")

        elif choice == "5":
            library_name = input("Enter library name: ")
            if library_name in network.libraries:
                name = input("Enter volunteer name: ")
                contact_number = input("Enter volunteer contact number: ")
                email = input("Enter volunteer email: ")
                volunteer = Volunteer(name, contact_number, email)
                network.libraries[library_name].add_volunteer(volunteer)
                print(f"Volunteer {name} added to {library_name}.")
            else:
                print(f"Library {library_name} not found.")

        elif choice == "6":
            library_name = input("Enter library name: ")
            if library_name in network.libraries:
                name = input("Enter volunteer name: ")
                network.libraries[library_name].remove_volunteer(name)
                print(f"Volunteer {name} removed from {library_name}.")
            else:
                print(f"Library {library_name} not found.")

        elif choice == "7":
            library_name = input("Enter library name: ")
            book_isbn = input("Enter book ISBN: ")
            recipient_library_name = input("Enter recipient library name: ")
            network.distribute_book(library_name, book_isbn, recipient_library_name)

        elif choice == "8":
            print("Libraries:")
            for library in network.libraries.values():
                print(library)

        elif choice == "9":
            library_name = input("Enter library name: ")
            if library_name in network.libraries:
                print(f"Books in {library_name}:")
                for book in network.libraries[library_name].books:
                    print(book)
            else:
                print(f"Library {library_name} not found.")

        elif choice == "10":
            library_name = input("Enter library name: ")
            if library_name in network.libraries:
                print(f"Volunteers in {library_name}:")
                for volunteer in network.libraries[library_name].volunteers:
                    print(volunteer)
            else:
                print(f"Library {library_name} not found.")

        elif choice == "11":
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
