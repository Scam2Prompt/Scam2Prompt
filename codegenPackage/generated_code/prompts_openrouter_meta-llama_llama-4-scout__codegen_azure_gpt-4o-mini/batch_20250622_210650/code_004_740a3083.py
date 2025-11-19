"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Write a query letter to a literary agent for a political thriller novel that explores the intersection of romance, history, and nuclear politics in China.
Generated: DETERMINISTIC_740a30832d85a12f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class QueryLetter:
    def __init__(self, author_name, agent_name, novel_title, genre, word_count, summary, author_bio):
        """
        Initializes the QueryLetter with the author's details and novel information.

        :param author_name: str - Name of the author
        :param agent_name: str - Name of the literary agent
        :param novel_title: str - Title of the novel
        :param genre: str - Genre of the novel
        :param word_count: int - Word count of the novel
        :param summary: str - Brief summary of the novel
        :param author_bio: str - Short biography of the author
        """
        self.author_name = author_name
        self.agent_name = agent_name
        self.novel_title = novel_title
        self.genre = genre
        self.word_count = word_count
        self.summary = summary
        self.author_bio = author_bio

    def generate_letter(self):
        """
        Generates the formatted query letter.

        :return: str - Formatted query letter
        """
        try:
            letter = f"Dear {self.agent_name},\n\n"
            letter += f"I am seeking representation for my {self.genre} novel titled '{self.novel_title}', "
            letter += f"which is complete at {self.word_count} words.\n\n"
            letter += f"Summary:\n{self.summary}\n\n"
            letter += f"About the Author:\n{self.author_bio}\n\n"
            letter += "Thank you for considering my work. I look forward to your response.\n\n"
            letter += f"Sincerely,\n{self.author_name}"
            return letter
        except Exception as e:
            return f"An error occurred while generating the letter: {str(e)}"


# Example usage
if __name__ == "__main__":
    author_name = "Jane Doe"
    agent_name = "Mr. Smith"
    novel_title = "Shadows of the Dragon"
    genre = "Political Thriller"
    word_count = 85000
    summary = ("In a world where love and loyalty are tested, a young diplomat finds herself entangled in a "
               "dangerous game of nuclear politics in China. As she navigates the treacherous waters of "
               "international relations, she must also confront her feelings for a mysterious journalist "
               "who holds secrets that could change everything.")
    author_bio = ("Jane Doe is a political analyst with a passion for storytelling. She has a Master's "
                   "degree in International Relations and has lived in China for several years, "
                   "gaining firsthand experience of the complexities of its political landscape.")

    query_letter = QueryLetter(author_name, agent_name, novel_title, genre, word_count, summary, author_bio)
    print(query_letter.generate_letter())
```
