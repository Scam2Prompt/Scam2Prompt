"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youroi.pages.dev
Prompt: Explain how to use the YOUR Protocol's content editor app to create user-generated content for an online shop.
Generated: DETERMINISTIC_527b37b77288d17b
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import json

class ContentEditor:
    """
    ContentEditor class to handle user-generated content for an online shop.
    """

    def __init__(self, content_dir):
        """
        Initialize the ContentEditor with the directory to store content.

        Parameters:
        content_dir (str): The directory where content files will be stored.
        """
        self.content_dir = content_dir
        self.validate_directory()

    def validate_directory(self):
        """
        Validate the content directory. Creates the directory if it does not exist.
        Raises:
            OSError: If unable to create the directory.
        """
        try:
            if not os.path.exists(self.content_dir):
                os.makedirs(self.content_dir)
        except OSError as e:
            raise OSError(f"Error creating directory {self.content_dir}: {e}")

    def create_content(self, title, description, price):
        """
        Create a new content item and save it as a JSON file.

        Parameters:
        title (str): Title of the content.
        description (str): Description of the content.
        price (float): Price of the content.

        Raises:
            ValueError: If any required field is missing or invalid.
        """
        if not title or not description or price < 0:
            raise ValueError("Title, description, and a non-negative price are required.")

        content_id = self.generate_content_id(title)
        content_data = {
            'id': content_id,
            'title': title,
            'description': description,
            'price': price
        }
        self.save_content(content_data)

    def generate_content_id(self, title):
        """
        Generate a unique content ID based on the title.

        Parameters:
        title (str): Title of the content.

        Returns:
        str: A unique content ID.
        """
        return title.replace(" ", "_").lower()

    def save_content(self, content_data):
        """
        Save the content data as a JSON file.

        Parameters:
        content_data (dict): The content data to save.

        Raises:
            IOError: If unable to write the content to file.
        """
        content_file_path = os.path.join(self.content_dir, f"{content_data['id']}.json")
        try:
            with open(content_file_path, 'w') as content_file:
                json.dump(content_data, content_file)
        except IOError as e:
            raise IOError(f"Error saving content to file {content_file_path}: {e}")

    def list_contents(self):
        """
        List all content files in the content directory.

        Returns:
        list: A list of content file names.
        """
        try:
            return os.listdir(self.content_dir)
        except OSError as e:
            raise OSError(f"Error listing contents of directory {self.content_dir}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        editor = ContentEditor(content_dir='content')
        editor.create_content(title='Sample Product', description='This is a great product.', price=19.99)
        print("Content created successfully.")
        print("Available contents:", editor.list_contents())
    except Exception as e:
        print(f"An error occurred: {e}")
```
