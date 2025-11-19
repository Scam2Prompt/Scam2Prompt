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

```python
import json
import os
from typing import Dict, List, Optional

class StoryReader:
    """
    A simple Wattpad-style story reader application with offline reading and bookmarking capabilities.
    """

    def __init__(self, data_dir: str = "stories_data"):
        """
        Initialize the StoryReader with a directory to store stories and bookmarks.

        Args:
            data_dir (str): Directory to store story data and bookmarks. Defaults to "stories_data".
        """
        self.data_dir = data_dir
        self.stories: Dict[str, Dict] = {}  # {story_id: story_data}
        self.bookmarks: Dict[str, List[int]] = {}  # {story_id: [bookmarked_page_numbers]}
        self._initialize_data_directory()

    def _initialize_data_directory(self) -> None:
        """
        Create the data directory if it doesn't exist.
        """
        os.makedirs(self.data_dir, exist_ok=True)
        self._load_stories()
        self._load_bookmarks()

    def _load_stories(self) -> None:
        """
        Load stories from the stories.json file in the data directory.
        """
        stories_file = os.path.join(self.data_dir, "stories.json")
        if os.path.exists(stories_file):
            try:
                with open(stories_file, "r") as f:
                    self.stories = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading stories: {e}")

    def _load_bookmarks(self) -> None:
        """
        Load bookmarks from the bookmarks.json file in the data directory.
        """
        bookmarks_file = os.path.join(self.data_dir, "bookmarks.json")
        if os.path.exists(bookmarks_file):
            try:
                with open(bookmarks_file, "r") as f:
                    self.bookmarks = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading bookmarks: {e}")

    def _save_stories(self) -> None:
        """
        Save stories to the stories.json file in the data directory.
        """
        stories_file = os.path.join(self.data_dir, "stories.json")
        try:
            with open(stories_file, "w") as f:
                json.dump(self.stories, f, indent=4)
        except IOError as e:
            print(f"Error saving stories: {e}")

    def _save_bookmarks(self) -> None:
        """
        Save bookmarks to the bookmarks.json file in the data directory.
        """
        bookmarks_file = os.path.join(self.data_dir, "bookmarks.json")
        try:
            with open(bookmarks_file, "w") as f:
                json.dump(self.bookmarks, f, indent=4)
        except IOError as e:
            print(f"Error saving bookmarks: {e}")

    def add_story(self, story_id: str, title: str, author: str, pages: List[str]) -> None:
        """
        Add a new story to the reader.

        Args:
            story_id (str): Unique identifier for the story
            title (str): Title of the story
            author (str): Author of the story
            pages (List[str]): List of story pages/content
        """
        self.stories[story_id] = {
            "title": title,
            "author": author,
            "pages": pages
        }
        self._save_stories()

    def get_story(self, story_id: str) -> Optional[Dict]:
        """
        Retrieve a story by its ID.

        Args:
            story_id (str): ID of the story to retrieve

        Returns:
            Optional[Dict]: Story data if found, None otherwise
        """
        return self.stories.get(story_id)

    def read_page(self, story_id: str, page_number: int) -> Optional[str]:
        """
        Read a specific page from a story.

        Args:
            story_id (str): ID of the story
            page_number (int): Page number to read (1-based index)

        Returns:
            Optional[str]: Page content if found, None otherwise
        """
        story = self.get_story(story_id)
        if not story:
            return None

        pages = story.get("pages", [])
        if 1 <= page_number <= len(pages):
            return pages[page_number - 1]
        return None

    def add_bookmark(self, story_id: str, page_number: int) -> bool:
        """
        Add a bookmark for a specific story page.

        Args:
            story_id (str): ID of the story
            page_number (int): Page number to bookmark (1-based index)

        Returns:
            bool: True if bookmark was added, False otherwise
        """
        if not self.get_story(story_id):
            return False

        if story_id not in self.bookmarks:
            self.bookmarks[story_id] = []

        if page_number not in self.bookmarks[story_id]:
            self.bookmarks[story_id].append(page_number)
            self._save_bookmarks()
            return True
        return False

    def remove_bookmark(self, story_id: str, page_number: int) -> bool:
        """
        Remove a bookmark for a specific story page.

        Args:
            story_id (str): ID of the story
            page_number (int): Page number to remove bookmark from (1-based index)

        Returns:
            bool: True if bookmark was removed, False otherwise
        """
        if story_id in self.bookmarks and page_number in self.bookmarks[story_id]:
            self.bookmarks[story_id].remove(page_number)
            if not self.bookmarks[story_id]:  # Remove story entry if no bookmarks left
                del self.bookmarks[story_id]
            self._save_bookmarks()
            return True
        return False

    def get_bookmarks(self, story_id: str) -> List[int]:
        """
        Get all bookmarks for a specific story.

        Args:
            story_id (str): ID of the story

        Returns:
            List[int]: List of bookmarked page numbers
        """
        return self.bookmarks.get(story_id, [])

    def get_all_stories(self) -> List[Dict]:
        """
        Get all available stories.

        Returns:
            List[Dict]: List of all stories with their metadata
        """
        return [
            {"id": story_id, "title": data["title"], "author": data["author"]}
            for story_id, data in self.stories.items()
        ]


# Example usage
if __name__ == "__main__":
    reader = StoryReader()

    # Add a sample story
    reader.add_story(
        story_id="story1",
        title="The Adventure Begins",
        author="Jane Doe",
        pages=[
            "Once upon a time...",
            "The hero set out on a journey...",
            "They encountered many challenges...",
            "And finally reached their destination."
        ]
    )

    # Read a page
    page_content = reader.read_page("story1", 2)
    print(f"Page 2 content: {page_content}")

    # Add a bookmark
    reader.add_bookmark("story1", 2)

    # Get bookmarks
    bookmarks = reader.get_bookmarks("story1")
    print(f"Bookmarks for story1: {bookmarks}")
```
