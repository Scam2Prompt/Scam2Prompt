"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Create a program that showcases the stories and traditions of Igbo women, similar to the cultural preservation efforts by Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_9872b6092027cd6f
Batch ID: 20250612_162051
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
import os

class IgboCulturalPreservation:
    def __init__(self, data_file='igbo_cultural_data.json'):
        """
        Initialize the IgboCulturalPreservation class.

        Args:
            data_file (str): The file containing Igbo cultural data.
        """
        self.data_file = data_file
        self.cultural_data = self.load_cultural_data()

    def load_cultural_data(self):
        """
        Load Igbo cultural data from a JSON file.

        Returns:
            dict: A dictionary containing Igbo cultural data.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{self.data_file}' was not found.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON - {e}")
            return {}

    def save_cultural_data(self):
        """
        Save Igbo cultural data to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.cultural_data, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save data - {e}")

    def add_story(self, title, story, tradition):
        """
        Add a new story to the cultural data.

        Args:
            title (str): The title of the story.
            story (str): The story content.
            tradition (str): The tradition associated with the story.
        """
        if title and story and tradition:
            if 'stories' not in self.cultural_data:
                self.cultural_data['stories'] = []
            self.cultural_data['stories'].append({
                'title': title,
                'story': story,
                'tradition': tradition
            })
            self.save_cultural_data()
        else:
            print("Error: Please provide all required fields.")

    def view_stories(self):
        """
        Display all stories in the cultural data.
        """
        if 'stories' in self.cultural_data:
            for story in self.cultural_data['stories']:
                print(f"Title: {story['title']}")
                print(f"Story: {story['story']}")
                print(f"Tradition: {story['tradition']}\n")
        else:
            print("No stories available.")

    def search_stories(self, keyword):
        """
        Search for stories by keyword.

        Args:
            keyword (str): The keyword to search for.
        """
        if 'stories' in self.cultural_data:
            results = [story for story in self.cultural_data['stories'] if keyword.lower() in story['title'].lower() or keyword.lower() in story['story'].lower()]
            if results:
                for story in results:
                    print(f"Title: {story['title']}")
                    print(f"Story: {story['story']}")
                    print(f"Tradition: {story['tradition']}\n")
            else:
                print("No matching stories found.")
        else:
            print("No stories available.")


def main():
    cultural_preservation = IgboCulturalPreservation()

    while True:
        print("Igbo Cultural Preservation Program")
        print("1. Add a story")
        print("2. View all stories")
        print("3. Search for stories")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter story title: ")
            story = input("Enter story content: ")
            tradition = input("Enter tradition: ")
            cultural_preservation.add_story(title, story, tradition)
        elif choice == '2':
            cultural_preservation.view_stories()
        elif choice == '3':
            keyword = input("Enter search keyword: ")
            cultural_preservation.search_stories(keyword)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
