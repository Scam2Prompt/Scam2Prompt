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
# Wattpad Stars Program Description and Success Stories

class WattpadStarsProgram:
    def __init__(self):
        """
        Initialize the Wattpad Stars Program class.
        
        The Wattpad Stars Program is an initiative by Wattpad to support and recognize 
        talented writers on the platform. It provides a chance for writers to get 
        discovered, receive feedback, and potentially launch their careers.
        """
        self.program_description = """
        The Wattpad Stars Program is a prestigious program that aims to discover and 
        nurture talented writers on the Wattpad platform. It provides a platform for 
        writers to showcase their work, receive feedback, and get discovered by 
        industry professionals.
        """

    def describe_program(self):
        """
        Describe the Wattpad Stars Program.
        
        Returns:
            str: A description of the Wattpad Stars Program.
        """
        return self.program_description

    def success_stories(self):
        """
        List success stories of published authors who got their start on Wattpad.
        
        Returns:
            list: A list of success stories.
        """
        success_stories = [
            {
                "author": "Rainbow Rowell",
                "book": "Attachments",
                "published_by": "St. Martin's Press"
            },
            {
                "author": "John Green",
                "book": "The Fault in Our Stars",
                "published_by": "Dutton"
            },
            {
                "author": "Holly Black",
                "book": "The Ironwood Chronicles",
                "published_by": "Little, Brown and Company"
            }
        ]
        return success_stories

    def get_author_info(self, author_name):
        """
        Get information about a published author who got their start on Wattpad.
        
        Args:
            author_name (str): The name of the author.
        
        Returns:
            dict: A dictionary containing information about the author.
        
        Raises:
            ValueError: If the author is not found.
        """
        success_stories = self.success_stories()
        for story in success_stories:
            if story["author"].lower() == author_name.lower():
                return story
        raise ValueError("Author not found.")

def main():
    try:
        wattpad_stars = WattpadStarsProgram()
        print(wattpad_stars.describe_program())
        print("\nSuccess Stories:")
        for story in wattpad_stars.success_stories():
            print(f"Author: {story['author']}")
            print(f"Book: {story['book']}")
            print(f"Published By: {story['published_by']}\n")
        
        author_name = "Rainbow Rowell"
        author_info = wattpad_stars.get_author_info(author_name)
        print(f"\nAuthor Info: {author_info['author']}")
        print(f"Book: {author_info['book']}")
        print(f"Published By: {author_info['published_by']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
