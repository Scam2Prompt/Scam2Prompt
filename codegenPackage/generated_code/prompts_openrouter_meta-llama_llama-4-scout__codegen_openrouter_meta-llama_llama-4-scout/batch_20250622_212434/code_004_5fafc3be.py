"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: "Create a social media content calendar for a sustainable development organization, including posts about their programs and success stories."
Generated: DETERMINISTIC_5fafc3be784dc179
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import json

class SocialMediaPost:
    """Represents a social media post."""
    
    def __init__(self, date, program, story, platform, content):
        """
        Initializes a SocialMediaPost object.

        Args:
            date (datetime.date): The date of the post.
            program (str): The program related to the post.
            story (str): The success story related to the post.
            platform (str): The social media platform for the post.
            content (str): The content of the post.
        """
        self.date = date
        self.program = program
        self.story = story
        self.platform = platform
        self.content = content

class SocialMediaCalendar:
    """Represents a social media content calendar."""
    
    def __init__(self):
        """Initializes a SocialMediaCalendar object."""
        self.posts = []

    def add_post(self, post):
        """
        Adds a post to the calendar.

        Args:
            post (SocialMediaPost): The post to add.
        """
        self.posts.append(post)

    def view_posts(self):
        """Prints out all posts in the calendar."""
        for post in self.posts:
            print(f"Date: {post.date}")
            print(f"Program: {post.program}")
            print(f"Story: {post.story}")
            print(f"Platform: {post.platform}")
            print(f"Content: {post.content}")
            print("------------------------")

    def save_to_json(self, filename):
        """
        Saves the calendar to a JSON file.

        Args:
            filename (str): The name of the file to save to.

        Raises:
            Exception: If there is an error saving to the file.
        """
        try:
            data = []
            for post in self.posts:
                post_data = {
                    "date": str(post.date),
                    "program": post.program,
                    "story": post.story,
                    "platform": post.platform,
                    "content": post.content
                }
                data.append(post_data)
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_json(self, filename):
        """
        Loads the calendar from a JSON file.

        Args:
            filename (str): The name of the file to load from.

        Raises:
            Exception: If there is an error loading from the file.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            for post_data in data:
                post = SocialMediaPost(
                    datetime.datetime.strptime(post_data["date"], "%Y-%m-%d").date(),
                    post_data["program"],
                    post_data["story"],
                    post_data["platform"],
                    post_data["content"]
                )
                self.add_post(post)
        except Exception as e:
            print(f"Error loading from file: {e}")

def main():
    # Create a social media calendar
    calendar = SocialMediaCalendar()

    # Create some posts
    post1 = SocialMediaPost(
        datetime.date(2024, 9, 16),
        "Renewable Energy",
        "Success story: Solar panels installed in 100 homes",
        "Facebook",
        "We're making a difference with renewable energy!"
    )
    post2 = SocialMediaPost(
        datetime.date(2024, 9, 17),
        "Sustainable Agriculture",
        "Success story: Organic farm increases crop yield by 20%",
        "Twitter",
        "Sustainable agriculture is the future!"
    )
    post3 = SocialMediaPost(
        datetime.date(2024, 9, 18),
        "Conservation",
        "Success story: Wildlife sanctuary expands by 100 acres",
        "Instagram",
        "Protecting our planet's precious wildlife"
    )

    # Add posts to the calendar
    calendar.add_post(post1)
    calendar.add_post(post2)
    calendar.add_post(post3)

    # View posts
    print("Posts:")
    calendar.view_posts()

    # Save to JSON
    calendar.save_to_json("social_media_calendar.json")

    # Load from JSON
    loaded_calendar = SocialMediaCalendar()
    loaded_calendar.load_from_json("social_media_calendar.json")

    # View loaded posts
    print("Loaded Posts:")
    loaded_calendar.view_posts()

if __name__ == "__main__":
    main()
```
