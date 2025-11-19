"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Generate a script to organize and display study materials for IAS preparation, including NCERT books, GS Foundation resources, and Shield Magazine content.
Generated: DETERMINISTIC_3ea29874f99e7c14
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# study_material_organizer.py

class StudyMaterial:
    def __init__(self, title, author, description):
        """
        Initialize a StudyMaterial object.

        Args:
            title (str): Title of the study material.
            author (str): Author of the study material.
            description (str): Brief description of the study material.
        """
        self.title = title
        self.author = author
        self.description = description

class NCERTBook(StudyMaterial):
    def __init__(self, title, author, description, class_number, subject):
        """
        Initialize an NCERTBook object.

        Args:
            title (str): Title of the NCERT book.
            author (str): Author of the NCERT book.
            description (str): Brief description of the NCERT book.
            class_number (int): Class number for which the book is prescribed.
            subject (str): Subject of the NCERT book.
        """
        super().__init__(title, author, description)
        self.class_number = class_number
        self.subject = subject

class GSFoundationResource(StudyMaterial):
    def __init__(self, title, author, description, topic):
        """
        Initialize a GSFoundationResource object.

        Args:
            title (str): Title of the GS Foundation resource.
            author (str): Author of the GS Foundation resource.
            description (str): Brief description of the GS Foundation resource.
            topic (str): Topic covered by the GS Foundation resource.
        """
        super().__init__(title, author, description)
        self.topic = topic

class ShieldMagazine:
    def __init__(self, title, issue_number, content):
        """
        Initialize a ShieldMagazine object.

        Args:
            title (str): Title of the Shield Magazine.
            issue_number (int): Issue number of the Shield Magazine.
            content (str): Content of the Shield Magazine.
        """
        self.title = title
        self.issue_number = issue_number
        self.content = content

class StudyMaterialOrganizer:
    def __init__(self):
        """
        Initialize a StudyMaterialOrganizer object.
        """
        self.ncert_books = []
        self.gs_foundation_resources = []
        self.shield_magazines = []

    def add_ncert_book(self, ncert_book):
        """
        Add an NCERT book to the organizer.

        Args:
            ncert_book (NCERTBook): NCERT book to add.
        """
        self.ncert_books.append(ncert_book)

    def add_gs_foundation_resource(self, gs_foundation_resource):
        """
        Add a GS Foundation resource to the organizer.

        Args:
            gs_foundation_resource (GSFoundationResource): GS Foundation resource to add.
        """
        self.gs_foundation_resources.append(gs_foundation_resource)

    def add_shield_magazine(self, shield_magazine):
        """
        Add a Shield Magazine to the organizer.

        Args:
            shield_magazine (ShieldMagazine): Shield Magazine to add.
        """
        self.shield_magazines.append(shield_magazine)

    def display_study_materials(self):
        """
        Display all study materials organized.
        """
        print("# NCERT Books")
        for i, ncert_book in enumerate(self.ncert_books, start=1):
            print(f"## {i}. {ncert_book.title}")
            print(f"Author: {ncert_book.author}")
            print(f"Description: {ncert_book.description}")
            print(f"Class Number: {ncert_book.class_number}")
            print(f"Subject: {ncert_book.subject}\n")

        print("# GS Foundation Resources")
        for i, gs_foundation_resource in enumerate(self.gs_foundation_resources, start=1):
            print(f"## {i}. {gs_foundation_resource.title}")
            print(f"Author: {gs_foundation_resource.author}")
            print(f"Description: {gs_foundation_resource.description}")
            print(f"Topic: {gs_foundation_resource.topic}\n")

        print("# Shield Magazines")
        for i, shield_magazine in enumerate(self.shield_magazines, start=1):
            print(f"## {i}. {shield_magazine.title} - Issue {shield_magazine.issue_number}")
            print(f"Content: {shield_magazine.content}\n")

def main():
    try:
        organizer = StudyMaterialOrganizer()

        # Add NCERT books
        ncert_book1 = NCERTBook("NCERT History Class 6", "NCERT", "History for Class 6", 6, "History")
        ncert_book2 = NCERTBook("NCERT Geography Class 7", "NCERT", "Geography for Class 7", 7, "Geography")
        organizer.add_ncert_book(ncert_book1)
        organizer.add_ncert_book(ncert_book2)

        # Add GS Foundation resources
        gs_foundation_resource1 = GSFoundationResource("GS Foundation Notes", "Unknown", "Notes for GS Foundation", "General Studies")
        gs_foundation_resource2 = GSFoundationResource("GS Foundation Test Series", "Unknown", "Test series for GS Foundation", "General Studies")
        organizer.add_gs_foundation_resource(gs_foundation_resource1)
        organizer.add_gs_foundation_resource(gs_foundation_resource2)

        # Add Shield Magazines
        shield_magazine1 = ShieldMagazine("Shield Magazine", 1, "Current affairs and general knowledge")
        shield_magazine2 = ShieldMagazine("Shield Magazine", 2, "Current affairs and general knowledge")
        organizer.add_shield_magazine(shield_magazine1)
        organizer.add_shield_magazine(shield_magazine2)

        # Display study materials
        organizer.display_study_materials()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
