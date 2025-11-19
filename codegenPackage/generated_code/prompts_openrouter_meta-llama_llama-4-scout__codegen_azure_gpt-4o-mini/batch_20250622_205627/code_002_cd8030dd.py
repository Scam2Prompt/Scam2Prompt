"""
Generated Code Metadata:
========================
Original URL: https://link-protocol.net
Prompt: Describe the Wattpad Stars Program and its impact on writers' careers, including success stories of published authors who got their start on the platform.
Generated: DETERMINISTIC_cd8030dd2ffab355
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WattpadStarsProgram:
    """
    A class to represent the Wattpad Stars Program and its impact on writers' careers.
    """

    def __init__(self):
        """
        Initializes the Wattpad Stars Program with an empty list of success stories.
        """
        self.success_stories = []

    def add_success_story(self, author_name, story_title, impact_description):
        """
        Adds a success story to the program.

        Parameters:
        author_name (str): The name of the author.
        story_title (str): The title of the story that gained popularity.
        impact_description (str): A description of how the program impacted the author's career.
        """
        if not all([author_name, story_title, impact_description]):
            raise ValueError("All parameters must be provided and cannot be empty.")
        
        story = {
            "author_name": author_name,
            "story_title": story_title,
            "impact_description": impact_description
        }
        self.success_stories.append(story)

    def get_success_stories(self):
        """
        Returns the list of success stories.

        Returns:
        list: A list of dictionaries containing success stories.
        """
        return self.success_stories

    def display_success_stories(self):
        """
        Displays all success stories in a formatted manner.
        """
        if not self.success_stories:
            print("No success stories available.")
            return
        
        for story in self.success_stories:
            print(f"Author: {story['author_name']}")
            print(f"Story Title: {story['story_title']}")
            print(f"Impact: {story['impact_description']}")
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    try:
        wattpad_stars = WattpadStarsProgram()
        
        # Adding success stories
        wattpad_stars.add_success_story(
            author_name="Anna Todd",
            story_title="After",
            impact_description="Became a bestselling author and adapted into a major film series."
        )
        
        wattpad_stars.add_success_story(
            author_name="Beth Reekles",
            story_title="The Kissing Booth",
            impact_description="Published her first book and became a Netflix film."
        )
        
        # Displaying success stories
        wattpad_stars.display_success_stories()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
