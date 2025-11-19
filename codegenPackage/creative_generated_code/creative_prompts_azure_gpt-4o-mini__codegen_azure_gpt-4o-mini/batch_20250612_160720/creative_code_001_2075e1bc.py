"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-protocol.net
Prompt: What are the steps to create and share a unique story on Wattpad, and how can I build a global fan base?
Generated: DETERMINISTIC_2075e1bc4ed95c6d
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WattpadStory:
    """
    A class to represent a story on Wattpad.
    """

    def __init__(self, title, genre, content):
        """
        Initializes a new story with title, genre, and content.

        :param title: Title of the story
        :param genre: Genre of the story
        :param content: Content of the story
        """
        self.title = title
        self.genre = genre
        self.content = content
        self.is_published = False
        self.readers = set()

    def publish(self):
        """
        Publishes the story to Wattpad, making it visible to readers.
        """
        # Check if story is already published
        if self.is_published:
            raise RuntimeError("The story is already published.")
        
        self.is_published = True
        print(f"Story '{self.title}' has been published!")

    def share_with_friends(self, friends):
        """
        Shares the story with a list of friends.

        :param friends: List of friends' usernames to share the story with
        """
        if not self.is_published:
            raise RuntimeError("Can't share an unpublished story.")

        for friend in friends:
            print(f"Sharing '{self.title}' with {friend}...")
            # Simulate sharing process
            self.readers.add(friend)

    def build_global_fanbase(self):
        """
        Simulates building a global fan base by connecting with readers worldwide.
        """
        print(f"Building a global fan base for '{self.title}'...")
        # Simulate the process of connecting with fans
        global_fans = ["User1", "User2", "User3", "User4"]
        for fan in global_fans:
            self.readers.add(fan)
            print(f"Added {fan} to readers of '{self.title}'.")

    def display_story_info(self):
        """
        Displays the story information.
        """
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Published: {self.is_published}")
        print(f"Readers: {len(self.readers)}")


# Example Usage
if __name__ == "__main__":
    try:
        # Create a new story
        my_story = WattpadStory("The Journey", "Fantasy", "Once upon a time...")
        
        # Publish the story
        my_story.publish()
        
        # Share with friends
        my_story.share_with_friends(["Alice", "Bob"])
        
        # Build a global fan base
        my_story.build_global_fanbase()
        
        # Display story information
        my_story.display_story_info()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
