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
class PeerReviewProcess:
    """
    A class to represent the peer-review process for articles submitted to the PHUPHAN SARN Journal of Humanities and Social Science.
    """

    def __init__(self, article_title, author):
        """
        Initializes the PeerReviewProcess with the article title and author.

        :param article_title: Title of the article submitted for review
        :param author: Author of the article
        """
        self.article_title = article_title
        self.author = author
        self.reviewers = []
        self.status = "Submitted"

    def add_reviewer(self, reviewer):
        """
        Adds a reviewer to the list of reviewers for the article.

        :param reviewer: Name of the reviewer
        """
        if reviewer not in self.reviewers:
            self.reviewers.append(reviewer)
        else:
            raise ValueError("Reviewer already added.")

    def submit_for_review(self):
        """
        Submits the article for review and updates the status.
        """
        if self.status == "Submitted":
            self.status = "Under Review"
        else:
            raise RuntimeError("Article is already under review or has been processed.")

    def complete_review(self):
        """
        Completes the review process and updates the status to 'Reviewed'.
        """
        if self.status == "Under Review":
            self.status = "Reviewed"
        else:
            raise RuntimeError("Article must be under review to complete the review process.")

    def get_review_status(self):
        """
        Returns the current status of the article review process.

        :return: Current status of the article
        """
        return self.status

    def __str__(self):
        """
        Returns a string representation of the PeerReviewProcess instance.

        :return: String representation of the article title, author, and status
        """
        return f"Article: '{self.article_title}' by {self.author} - Status: {self.status}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a new peer review process for an article
        review_process = PeerReviewProcess("Understanding Social Dynamics", "Jane Doe")

        # Add reviewers
        review_process.add_reviewer("Dr. Smith")
        review_process.add_reviewer("Dr. Johnson")

        # Submit the article for review
        review_process.submit_for_review()

        # Print current status
        print(review_process)

        # Complete the review process
        review_process.complete_review()

        # Print final status
        print(review_process)

    except Exception as e:
        print(f"An error occurred: {e}")
```
