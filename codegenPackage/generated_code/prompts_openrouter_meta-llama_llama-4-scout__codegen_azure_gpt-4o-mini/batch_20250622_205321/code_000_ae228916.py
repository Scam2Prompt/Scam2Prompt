"""
Generated Code Metadata:
========================
Original URL: https://protsahitnews18.com
Prompt: Write a news article about the resumption of the Bodhghhat project worth 49,000 crores, as informed by CM Sai to PM.
Generated: DETERMINISTIC_ae22891671183e19
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class NewsArticle:
    def __init__(self, title, content, author, date):
        """
        Initializes a NewsArticle instance.

        :param title: Title of the news article
        :param content: Content of the news article
        :param author: Author of the news article
        :param date: Date of publication
        """
        self.title = title
        self.content = content
        self.author = author
        self.date = date

    def display_article(self):
        """
        Displays the article in a formatted manner.
        """
        print(f"Title: {self.title}\n")
        print(f"By: {self.author} | Date: {self.date.strftime('%B %d, %Y')}\n")
        print(f"Content:\n{self.content}\n")

def create_bodhghat_article():
    """
    Creates a news article about the resumption of the Bodhghat project.
    
    :return: An instance of NewsArticle
    """
    title = "Resumption of Bodhghat Project Worth 49,000 Crores Announced"
    content = (
        "In a significant development, Chief Minister Sai has informed Prime Minister "
        "about the resumption of the Bodhghat project, which is valued at an impressive "
        "49,000 crores. This project is expected to boost the local economy and provide "
        "numerous job opportunities.\n\n"
        "The Bodhghat project, which had faced several delays in the past, is now set to "
        "move forward with renewed vigor. CM Sai emphasized the importance of this project "
        "in enhancing infrastructure and promoting sustainable development in the region.\n\n"
        "The Prime Minister expressed his support and assured that the central government "
        "would provide all necessary assistance to ensure the project's timely completion. "
        "This collaboration between state and central authorities marks a pivotal moment for "
        "the future of the Bodhghat project."
    )
    author = "John Doe"
    date = datetime.datetime.now()

    return NewsArticle(title, content, author, date)

if __name__ == "__main__":
    try:
        article = create_bodhghat_article()
        article.display_article()
    except Exception as e:
        print(f"An error occurred while creating or displaying the article: {e}")
```
