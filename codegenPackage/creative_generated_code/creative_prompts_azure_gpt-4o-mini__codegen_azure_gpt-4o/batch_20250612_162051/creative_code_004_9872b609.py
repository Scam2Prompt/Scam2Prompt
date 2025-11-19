"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nkatandiinyom.com
Prompt: Create a program that showcases the stories and traditions of Igbo women, similar to the cultural preservation efforts by Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_9872b6092027cd6f
Batch ID: 20250612_162051
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

class IgboWomenStories:
    """
    A class to manage and showcase the stories and traditions of Igbo women.
    """
    def __init__(self, data_file):
        """
        Initialize the class with the data file location.

        Args:
            data_file (str): Path to the JSON file containing stories and traditions.
        """
        self.data_file = data_file
        self.stories = []

        # Load data from the file
        self.load_data()

    def load_data(self):
        """
        Load stories and traditions from the JSON file.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    self.stories = json.load(file)
            else:
                print(f"Data file '{self.data_file}' not found. Starting with an empty list.")
                self.stories = []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            self.stories = []
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            self.stories = []

    def save_data(self):
        """
        Save stories and traditions back to the JSON file.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump(self.stories, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def add_story(self, title, content, author):
        """
        Add a new story or tradition to the collection.

        Args:
            title (str): Title of the story.
            content (str): Content of the story.
            author (str): Author or contributor of the story.
        """
        new_story = {
            "title": title,
            "content": content,
            "author": author
        }
        self.stories.append(new_story)
        self.save_data()
        print(f"Story '{title}' added successfully.")

    def showcase_stories(self):
        """
        Display all stories and traditions in a readable format.
        """
        if not self.stories:
            print("No stories to showcase.")
            return
        
        print("\n--- Igbo Women Stories and Traditions ---\n")
        for index, story in enumerate(self.stories, start=1):
            print(f"Story {index}: {story['title']}")
            print(f"Author: {story['author']}")
            print(f"Content: {story['content']}\n")
            print("----------------------------------------\n")

    def search_story(self, keyword):
        """
        Search for stories containing a specific keyword.

        Args:
            keyword (str): Keyword to search for.

        Returns:
            list: List of stories matching the keyword.
        """
        matched_stories = [story for story in self.stories if keyword.lower() in story['content'].lower() or keyword.lower() in story['title'].lower()]
        
        if matched_stories:
            print(f"\n--- Stories containing '{keyword}' ---\n")
            for index, story in enumerate(matched_stories, start=1):
                print(f"Story {index}: {story['title']}")
                print(f"Author: {story['author']}")
                print(f"Content: {story['content']}\n")
                print("----------------------------------------\n")
        else:
            print(f"No stories found containing the keyword '{keyword}'.")
        
        return matched_stories

# Example usage
if __name__ == "__main__":
    # Initialize the program with a data file
    data_file = 'igbo_women_stories.json'
    program = IgboWomenStories(data_file)

    # Add example stories (commented out after initial setup to avoid duplication)
    # program.add_story("The Strength of Igbo Women", "Igbo women are known for their resilience and entrepreneurial spirit.", "Chinwe Okafor")
    # program.add_story("Traditional Igbo Ceremonies", "Igbo women play a key role in ceremonies such as child naming and marriages.", "Adaobi Nwosu")

    # Showcase all stories
    program.showcase_stories()

    # Search for stories containing a keyword
    program.search_story("resilience")
```

This Python program is structured to handle cultural stories and traditions systematically using JSON as the storage format. It includes functionalities to add, showcase, and search stories, ensuring proper error handling and code readability throughout.
