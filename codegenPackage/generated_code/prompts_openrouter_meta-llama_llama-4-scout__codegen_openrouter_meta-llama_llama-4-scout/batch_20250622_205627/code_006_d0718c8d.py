"""
Generated Code Metadata:
========================
Original URL: https://link-protocol.net
Prompt: Develop a code snippet to create a simple Wattpad-style story reader application, including features like offline reading and bookmarking.
Generated: DETERMINISTIC_d0718c8d7bd168a0
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Story Reader Application**
==========================

### **story_reader.py**
```python
import json
import os
import sqlite3
from typing import List

class StoryReader:
    def __init__(self, db_name: str = "story_reader.db"):
        """
        Initialize the story reader application.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the SQLite database.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS stories (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookmarks (
                id INTEGER PRIMARY KEY,
                story_id INTEGER NOT NULL,
                chapter INTEGER NOT NULL,
                FOREIGN KEY (story_id) REFERENCES stories (id)
            )
        """)
        self.conn.commit()

    def add_story(self, title: str, content: str):
        """
        Add a new story to the database.

        Args:
        title (str): The title of the story.
        content (str): The content of the story.
        """
        self.cursor.execute("INSERT INTO stories (title, content) VALUES (?, ?)", (title, content))
        self.conn.commit()

    def get_story(self, story_id: int) -> str:
        """
        Get the content of a story.

        Args:
        story_id (int): The ID of the story.

        Returns:
        str: The content of the story.
        """
        self.cursor.execute("SELECT content FROM stories WHERE id = ?", (story_id,))
        result = self.cursor.fetchone()
        return result[0] if result else ""

    def add_bookmark(self, story_id: int, chapter: int):
        """
        Add a new bookmark to the database.

        Args:
        story_id (int): The ID of the story.
        chapter (int): The chapter number.
        """
        self.cursor.execute("INSERT INTO bookmarks (story_id, chapter) VALUES (?, ?)", (story_id, chapter))
        self.conn.commit()

    def get_bookmarks(self, story_id: int) -> List[int]:
        """
        Get the bookmarks for a story.

        Args:
        story_id (int): The ID of the story.

        Returns:
        List[int]: A list of chapter numbers.
        """
        self.cursor.execute("SELECT chapter FROM bookmarks WHERE story_id = ?", (story_id,))
        result = self.cursor.fetchall()
        return [row[0] for row in result]

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


class StoryReaderApp:
    def __init__(self, story_reader: StoryReader):
        """
        Initialize the story reader application.

        Args:
        story_reader (StoryReader): The story reader instance.
        """
        self.story_reader = story_reader
        self.current_story_id = None
        self.current_chapter = 0

    def run(self):
        """
        Run the story reader application.
        """
        while True:
            print("1. Read a story")
            print("2. Add a story")
            print("3. Add a bookmark")
            print("4. View bookmarks")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.read_story()
            elif choice == "2":
                self.add_story()
            elif choice == "3":
                self.add_bookmark()
            elif choice == "4":
                self.view_bookmarks()
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose again.")

    def read_story(self):
        """
        Read a story.
        """
        story_id = int(input("Enter the story ID: "))
        self.current_story_id = story_id
        content = self.story_reader.get_story(story_id)
        chapters = content.split("\n\n")
        while True:
            print(f"Chapter {self.current_chapter + 1} of {len(chapters)}")
            print(chapters[self.current_chapter])
            print("1. Next chapter")
            print("2. Previous chapter")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                if self.current_chapter < len(chapters) - 1:
                    self.current_chapter += 1
                else:
                    print("You have reached the end of the story.")
            elif choice == "2":
                if self.current_chapter > 0:
                    self.current_chapter -= 1
                else:
                    print("You are at the beginning of the story.")
            elif choice == "3":
                break
            else:
                print("Invalid option. Please choose again.")

    def add_story(self):
        """
        Add a new story.
        """
        title = input("Enter the story title: ")
        content = input("Enter the story content: ")
        self.story_reader.add_story(title, content)

    def add_bookmark(self):
        """
        Add a new bookmark.
        """
        if self.current_story_id is not None:
            self.story_reader.add_bookmark(self.current_story_id, self.current_chapter)
            print("Bookmark added successfully.")
        else:
            print("You are not currently reading a story.")

    def view_bookmarks(self):
        """
        View bookmarks.
        """
        story_id = int(input("Enter the story ID: "))
        bookmarks = self.story_reader.get_bookmarks(story_id)
        print("Bookmarks:")
        for bookmark in bookmarks:
            print(bookmark)


if __name__ == "__main__":
    story_reader = StoryReader()
    app = StoryReaderApp(story_reader)
    try:
        app.run()
    finally:
        story_reader.close()
```

### **requirements.txt**
```
sqlite3
```

### **Usage**
1. Save the code in a file named `story_reader.py`.
2. Create a new file named `requirements.txt` and add the required packages.
3. Run the application using `python story_reader.py`.
4. Follow the prompts to read stories, add stories, add bookmarks, and view bookmarks.
