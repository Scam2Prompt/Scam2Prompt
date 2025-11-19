"""
Generated Code Metadata:
========================
Original URL: https://jphs.snru.ac.th
Prompt: "Explain the peer-review process for articles submitted to the PHUPHAN SARN Journal of Humanities and Social Science."
Generated: DETERMINISTIC_d79fd9b8d435c3b4
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# peer_review_process.py

class Article:
    """Represents an article submitted to the journal."""
    
    def __init__(self, title, author, content):
        """
        Initializes an Article object.

        Args:
            title (str): The title of the article.
            author (str): The author of the article.
            content (str): The content of the article.
        """
        self.title = title
        self.author = author
        self.content = content
        self.status = "Submitted"


class Reviewer:
    """Represents a reviewer for the journal."""
    
    def __init__(self, name, expertise):
        """
        Initializes a Reviewer object.

        Args:
            name (str): The name of the reviewer.
            expertise (str): The area of expertise of the reviewer.
        """
        self.name = name
        self.expertise = expertise


class PeerReviewProcess:
    """Manages the peer-review process for articles submitted to the journal."""
    
    def __init__(self):
        """
        Initializes a PeerReviewProcess object.
        """
        self.articles = {}
        self.reviewers = {}

    def submit_article(self, article):
        """
        Submits an article to the journal.

        Args:
            article (Article): The article to be submitted.

        Raises:
            ValueError: If the article title already exists.
        """
        if article.title in self.articles:
            raise ValueError("Article title already exists.")
        self.articles[article.title] = article

    def assign_reviewer(self, article_title, reviewer_name):
        """
        Assigns a reviewer to an article.

        Args:
            article_title (str): The title of the article.
            reviewer_name (str): The name of the reviewer.

        Raises:
            ValueError: If the article or reviewer does not exist.
        """
        if article_title not in self.articles:
            raise ValueError("Article does not exist.")
        if reviewer_name not in self.reviewers:
            raise ValueError("Reviewer does not exist.")
        article = self.articles[article_title]
        reviewer = self.reviewers[reviewer_name]
        # In a real system, you would store the assigned reviewer with the article
        print(f"Assigned {reviewer_name} to review {article_title}")

    def add_reviewer(self, reviewer):
        """
        Adds a reviewer to the journal.

        Args:
            reviewer (Reviewer): The reviewer to be added.

        Raises:
            ValueError: If the reviewer name already exists.
        """
        if reviewer.name in self.reviewers:
            raise ValueError("Reviewer name already exists.")
        self.reviewers[reviewer.name] = reviewer

    def review_article(self, article_title, reviewer_name, review_result):
        """
        Records the review result of an article.

        Args:
            article_title (str): The title of the article.
            reviewer_name (str): The name of the reviewer.
            review_result (str): The result of the review.

        Raises:
            ValueError: If the article or reviewer does not exist.
        """
        if article_title not in self.articles:
            raise ValueError("Article does not exist.")
        if reviewer_name not in self.reviewers:
            raise ValueError("Reviewer does not exist.")
        article = self.articles[article_title]
        # In a real system, you would store the review result with the article
        print(f"Reviewed {article_title} by {reviewer_name}: {review_result}")
        if review_result == "Accepted":
            article.status = "Accepted"
        elif review_result == "Rejected":
            article.status = "Rejected"

    def get_article_status(self, article_title):
        """
        Gets the status of an article.

        Args:
            article_title (str): The title of the article.

        Returns:
            str: The status of the article.

        Raises:
            ValueError: If the article does not exist.
        """
        if article_title not in self.articles:
            raise ValueError("Article does not exist.")
        return self.articles[article_title].status


def main():
    # Create a peer review process
    process = PeerReviewProcess()

    # Create reviewers
    reviewer1 = Reviewer("John Doe", "Humanities")
    reviewer2 = Reviewer("Jane Smith", "Social Science")

    # Add reviewers to the journal
    process.add_reviewer(reviewer1)
    process.add_reviewer(reviewer2)

    # Create an article
    article = Article("Example Article", "Example Author", "This is an example article.")

    # Submit the article
    process.submit_article(article)

    # Assign reviewers to the article
    process.assign_reviewer("Example Article", "John Doe")
    process.assign_reviewer("Example Article", "Jane Smith")

    # Review the article
    process.review_article("Example Article", "John Doe", "Accepted")
    process.review_article("Example Article", "Jane Smith", "Accepted")

    # Get the article status
    status = process.get_article_status("Example Article")
    print(f"Article status: {status}")


if __name__ == "__main__":
    main()
```
