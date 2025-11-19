"""
Generated Code Metadata:
========================
Original URL: https://pancarpos.com
Prompt: Write a news article about a local event in Bali, specifically about the Idul Adha celebration in Dusun Tegal Kori Kaja, including the importance of religious tolerance.
Generated: DETERMINISTIC_23011a9b6dbb3aa0
Batch ID: 20250622_210316
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

        :param title: Title of the article
        :param content: Content of the article
        :param author: Author of the article
        :param date: Date of the article
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
        print(self.content)

def create_idul_adha_article():
    """
    Creates a news article about the Idul Adha celebration in Dusun Tegal Kori Kaja.
    
    :return: An instance of NewsArticle
    """
    title = "Idul Adha Celebration in Dusun Tegal Kori Kaja: A Testament to Religious Tolerance"
    content = (
        "Dusun Tegal Kori Kaja, Bali - This year, the Idul Adha celebration in Dusun Tegal Kori Kaja was marked by a spirit of unity and "
        "religious tolerance. The local Muslim community came together to commemorate this important day, which symbolizes sacrifice and "
        "compassion.\n\n"
        "The event saw participation from various religious groups, showcasing the harmonious coexistence of different faiths in the region. "
        "Local leaders emphasized the importance of understanding and respecting each other's beliefs, fostering a sense of community that "
        "transcends religious boundaries.\n\n"
        "As part of the celebration, the community organized a communal feast, where everyone was invited to share in the joy of the occasion. "
        "This act of sharing not only highlighted the significance of Idul Adha but also reinforced the values of empathy and kindness that "
        "are essential in today's world.\n\n"
        "The event concluded with a call for continued dialogue and cooperation among different religious groups, ensuring that the spirit of "
        "tolerance remains strong in Dusun Tegal Kori Kaja."
    )
    author = "John Doe"
    date = datetime.datetime.now()

    return NewsArticle(title, content, author, date)

if __name__ == "__main__":
    try:
        article = create_idul_adha_article()
        article.display_article()
    except Exception as e:
        print(f"An error occurred while creating or displaying the article: {e}")
```
