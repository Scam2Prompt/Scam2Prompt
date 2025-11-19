"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Generate a book outline for a bestselling author or entrepreneur, using the principles from Rob Kosberg's Best Seller Writing Program course.
Generated: DETERMINISTIC_4542ac891b1e77bb
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

class BookOutline:
    def __init__(self, title, author, genre):
        """
        Initialize a BookOutline object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.chapters = []

    def add_chapter(self, chapter_title, chapter_description):
        """
        Add a chapter to the book outline.

        Args:
            chapter_title (str): The title of the chapter.
            chapter_description (str): A brief description of the chapter.
        """
        chapter = {
            "title": chapter_title,
            "description": chapter_description
        }
        self.chapters.append(chapter)

    def generate_outline(self):
        """
        Generate a book outline based on Rob Kosberg's Best Seller Writing Program course principles.

        Returns:
            dict: A dictionary representing the book outline.
        """
        # Rob Kosberg's principles: Introduction, Problem, Solution, Benefits, Story, and Call-to-Action
        outline = {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "chapters": []
        }

        # Introduction chapter
        intro_chapter = {
            "title": "Introduction",
            "description": f"Introduce the book's topic and {self.author}'s expertise."
        }
        outline["chapters"].append(intro_chapter)

        # Problem chapter
        problem_chapter = {
            "title": "The Problem",
            "description": f"Describe the problem that {self.author} will solve."
        }
        outline["chapters"].append(problem_chapter)

        # Solution chapter
        solution_chapter = {
            "title": "The Solution",
            "description": f"Present {self.author}'s solution to the problem."
        }
        outline["chapters"].append(solution_chapter)

        # Benefits chapter
        benefits_chapter = {
            "title": "The Benefits",
            "description": f"Explain the benefits of {self.author}'s solution."
        }
        outline["chapters"].append(benefits_chapter)

        # Story chapter
        story_chapter = {
            "title": "The Story",
            "description": f"Share a story that illustrates {self.author}'s solution."
        }
        outline["chapters"].append(story_chapter)

        # Call-to-Action chapter
        cta_chapter = {
            "title": "Call-to-Action",
            "description": f"Encourage readers to take action."
        }
        outline["chapters"].append(cta_chapter)

        # Add user-defined chapters
        for chapter in self.chapters:
            outline["chapters"].append(chapter)

        return outline

def main():
    try:
        # Create a BookOutline object
        book_outline = BookOutline("Best Seller Writing Program", "Rob Kosberg", "Self-Help")

        # Add user-defined chapters
        book_outline.add_chapter("My Journey", "A brief description of my journey.")
        book_outline.add_chapter("Key Takeaways", "A summary of key takeaways.")

        # Generate the book outline
        outline = book_outline.generate_outline()

        # Print the book outline
        print(json.dumps(outline, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
