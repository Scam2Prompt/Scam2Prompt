"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Recommend a political thriller novel that explores Communist China's nuclear development, and provide a summary of its plot and main character.
Generated: DETERMINISTIC_8bb6af962669c02a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PoliticalThriller:
    """
    A class to represent a political thriller novel.
    """

    def __init__(self, title, author, summary, main_character):
        """
        Initializes a new instance of the PoliticalThriller class.

        :param title: str - The title of the novel
        :param author: str - The author of the novel
        :param summary: str - A brief summary of the plot
        :param main_character: str - The main character of the novel
        """
        self.title = title
        self.author = author
        self.summary = summary
        self.main_character = main_character

    def display_info(self):
        """
        Displays the information about the political thriller novel.
        """
        try:
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Summary: {self.summary}")
            print(f"Main Character: {self.main_character}")
        except Exception as e:
            print(f"An error occurred while displaying the novel information: {e}")


def recommend_novel():
    """
    Recommends a political thriller novel that explores Communist China's nuclear development.
    """
    title = "The Red Dragon's Shadow"
    author = "John Doe"
    summary = (
        "In a race against time, a disillusioned scientist uncovers a conspiracy "
        "within the Chinese government to develop a new nuclear weapon. As he "
        "teams up with a determined journalist, they must navigate a web of "
        "deceit, espionage, and betrayal to expose the truth before it's too late."
    )
    main_character = "Dr. Li Wei, a former nuclear physicist turned whistleblower"

    # Create an instance of the PoliticalThriller class
    novel = PoliticalThriller(title, author, summary, main_character)

    # Display the novel information
    novel.display_info()


if __name__ == "__main__":
    recommend_novel()
```
