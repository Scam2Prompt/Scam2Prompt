"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Create a system for bookmarking posts and maintaining user lists, similar to the post bookmarks and user list features on Lovr.
Generated: DETERMINISTIC_396eff07faa14519
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Optional

class BookmarkManager:
    """A class to manage user bookmarks and lists."""

    def __init__(self, storage_file: str = 'bookmarks.json'):
        """Initialize the BookmarkManager with a storage file."""
        self.storage_file = storage_file
        self.bookmarks = self.load_bookmarks()

    def load_bookmarks(self) -> Dict[str, List[Dict]]:
        """Load bookmarks from the storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def save_bookmarks(self) -> None:
        """Save bookmarks to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.bookmarks, file, indent=4)

    def add_bookmark(self, user_id: str, post_id: str, title: str) -> None:
        """Add a bookmark for a user."""
        if user_id not in self.bookmarks:
            self.bookmarks[user_id] = []
        
        # Check for duplicates
        if any(bookmark['post_id'] == post_id for bookmark in self.bookmarks[user_id]):
            raise ValueError("Bookmark already exists for this post.")
        
        self.bookmarks[user_id].append({'post_id': post_id, 'title': title})
        self.save_bookmarks()

    def remove_bookmark(self, user_id: str, post_id: str) -> None:
        """Remove a bookmark for a user."""
        if user_id in self.bookmarks:
            self.bookmarks[user_id] = [
                bookmark for bookmark in self.bookmarks[user_id] if bookmark['post_id'] != post_id
            ]
            self.save_bookmarks()

    def get_bookmarks(self, user_id: str) -> Optional[List[Dict]]:
        """Get all bookmarks for a user."""
        return self.bookmarks.get(user_id, [])

    def clear_bookmarks(self, user_id: str) -> None:
        """Clear all bookmarks for a user."""
        if user_id in self.bookmarks:
            del self.bookmarks[user_id]
            self.save_bookmarks()

# Example usage
if __name__ == "__main__":
    manager = BookmarkManager()

    try:
        manager.add_bookmark('user1', 'post1', 'First Post')
        manager.add_bookmark('user1', 'post2', 'Second Post')
        print("Bookmarks for user1:", manager.get_bookmarks('user1'))

        manager.remove_bookmark('user1', 'post1')
        print("Bookmarks for user1 after removal:", manager.get_bookmarks('user1'))

        manager.clear_bookmarks('user1')
        print("Bookmarks for user1 after clearing:", manager.get_bookmarks('user1'))
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
