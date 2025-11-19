"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Generate code to manage a school library system that categorizes books based on student preferences, inspired by the library facilities at Happy Boarding School.
Generated: DETERMINISTIC_43b2e98d4d5039b0
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import uuid
from datetime import datetime, timedelta


class BookCategory(Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE = "Science"
    HISTORY = "History"
    MATHEMATICS = "Mathematics"
    LITERATURE = "Literature"
    ART = "Art"
    TECHNOLOGY = "Technology"
    SPORTS = "Sports"
    OTHER = "Other"


class StudentLevel(Enum):
    JUNIOR = "Junior"
    SENIOR = "Senior"
    ADVANCED = "Advanced"


@dataclass
class Book:
    id: str
    title: str
    author: str
    category: BookCategory
    is_available: bool = True
    borrowed_by: Optional[str] = None
    due_date: Optional[datetime] = None

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "category": self.category.value,
            "is_available": self.is_available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        return cls(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            category=BookCategory(data["category"]),
            is_available=data["is_available"],
            borrowed_by=data.get("borrowed_by"),
            due_date=datetime.fromisoformat(data["due_date"]) if data.get("due_date") else None
        )


@dataclass
class Student:
    id: str
    name: str
    level: StudentLevel
    preferences: List[BookCategory] = field(default_factory=list)
    borrowed_books: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level.value,
            "preferences": [category.value for category in self.preferences],
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        return cls(
            id=data["id"],
            name=data["name"],
            level=StudentLevel(data["level"]),
            preferences=[BookCategory(category) for category in data["preferences"]],
            borrowed_books=data["borrowed_books"]
        )


class LibrarySystem:
    def __init__(self, data_file: str = "library_data.json"):
        self.data_file = data_file
        self.books: Dict[str, Book] = {}
        self.students: Dict[str, Student] = {}
        self.load_data()

    def save_data(self) -> None:
        """Save current library data to file."""
        data = {
            "books": [book.to_dict() for book in self.books.values()],
            "students": [student.to_dict() for student in self.students.values()]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_data(self) -> None:
        """Load library data from file."""
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.books = {
                    book["id"]: Book.from_dict(book) for book in data.get("books", [])
                }
                self.students = {
                    student["id"]: Student.from_dict(student) for student in data.get("students", [])
                }
        except FileNotFoundError:
            self.books = {}
            self.students = {}

    def add_book(self, title: str, author: str, category: BookCategory) -> Book:
        """Add a new book to the library."""
        book_id = str(uuid.uuid4())
        book = Book(id=book_id, title=title, author=author, category=category)
        self.books[book_id] = book
        self.save_data()
        return book

    def remove_book(self, book_id: str) -> bool:
        """Remove a book from the library."""
        if book_id in self.books:
            del self.books[book_id]
            self.save_data()
            return True
        return False

    def register_student(self, name: str, level: StudentLevel, preferences: List[BookCategory]) -> Student:
        """Register a new student in the library system."""
        student_id = str(uuid.uuid4())
        student = Student(id=student_id, name=name, level=level, preferences=preferences)
        self.students[student_id] = student
        self.save_data()
        return student

    def update_student_preferences(self, student_id: str, preferences: List[BookCategory]) -> bool:
        """Update a student's book preferences."""
        if student_id in self.students:
            self.students[student_id].preferences = preferences
            self.save_data()
            return True
        return False

    def borrow_book(self, student_id: str, book_id: str, days: int = 14) -> bool:
        """Borrow a book for a student."""
        if student_id not in self.students or book_id not in self.books:
            return False

        book = self.books[book_id]
        student = self.students[student_id]

        if not book.is_available:
            return False

        book.is_available = False
        book.borrowed_by = student_id
        book.due_date = datetime.now() + timedelta(days=days)
        student.borrowed_books.append(book_id)
        self.save_data()
        return True

    def return_book(self, book_id: str) -> bool:
        """Return a borrowed book."""
        if book_id not in self.books or self.books[book_id].is_available:
            return False

        book = self.books[book_id]
        student_id = book.borrowed_by

        if student_id and student_id in self.students:
            student = self.students[student_id]
            if book_id in student.borrowed_books:
                student.borrowed_books.remove(book_id)

        book.is_available = True
        book.borrowed_by = None
        book.due_date = None
        self.save_data()
        return True

    def get_books_by_category(self, category: BookCategory) -> List[Book]:
        """Get all books in a specific category."""
        return [book for book in self.books.values() if book.category == category]

    def get_recommended_books(self, student_id: str) -> List[Book]:
        """Get recommended books based on student preferences."""
        if student_id not in self.students:
            return []

        student = self.students[student_id]
        recommended = []
        for category in student.preferences:
            recommended.extend(self.get_books_by_category(category))
        return [book for book in recommended if book.is_available]

    def get_overdue_books(self) -> List[Book]:
        """Get all overdue books."""
        now = datetime.now()
        return [book for book in self.books.values() 
                if not book.is_available and book.due_date and book.due_date < now]

    def search_books(self, query: str) -> List[Book]:
        """Search books by title or author."""
        query = query.lower()
        return [book for book in self.books.values() 
                if query in book.title.lower() or query in book.author.lower()]


# Example usage
if __name__ == "__main__":
    library = LibrarySystem()

    # Add some books
    library.add_book("Python Programming", "John Doe", BookCategory.TECHNOLOGY)
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", BookCategory.LITERATURE)
    library.add_book("A Brief History of Time", "Stephen Hawking", BookCategory.SCIENCE)

    # Register a student
    student = library.register_student(
        "Alice Smith",
        StudentLevel.SENIOR,
        [BookCategory.TECHNOLOGY, BookCategory.SCIENCE]
    )

    # Borrow a book
    books = library.search_books("Python")
    if books:
        library.borrow_book(student.id, books[0].id)

    # Get recommended books
    recommended = library.get_recommended_books(student.id)
    print(f"Recommended books for {student.name}:")
    for book in recommended:
        print(f"- {book.title} by {book.author}")

    # Check overdue books
    overdue = library.get_overdue_books()
    if overdue:
        print("\nOverdue books:")
        for book in overdue:
            print(f"- {book.title} (Due: {book.due_date})")
```
