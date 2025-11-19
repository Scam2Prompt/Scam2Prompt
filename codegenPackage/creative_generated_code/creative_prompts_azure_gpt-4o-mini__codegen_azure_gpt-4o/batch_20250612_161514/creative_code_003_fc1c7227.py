"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tojsat.net
Prompt: Develop a library function that validates article submissions based on the ethical rules and malpractice statements outlined by journals like TOJSAT.
Generated: DETERMINISTIC_fc1c72271d187291
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Library: article_validator.py
Purpose: Validate article submissions based on ethical rules and malpractice statements.
"""

import re

class ArticleValidator:
    """
    A class to validate article submissions against ethical rules and malpractice standards.
    """

    def __init__(self):
        """
        Initializes the validator with default rules and patterns.
        """
        self.rules = {
            "title_length": (10, 150),  # Min and max length for the title
            "abstract_length": (50, 500),  # Min and max length for the abstract
            "forbidden_phrases": [
                "plagiarism", 
                "fabricated data",
                "duplicate publication",
                "ghostwriting", 
                "copyright violation"
            ],
            "author_count_limit": 10,  # Maximum number of authors
            "email_pattern": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # Regex for valid email format
        }

    def validate_title(self, title):
        """
        Validates the title based on length.

        Args:
            title (str): The article's title.

        Returns:
            bool: True if valid, False otherwise.
        """
        min_length, max_length = self.rules["title_length"]
        if not (min_length <= len(title) <= max_length):
            return False
        return True

    def validate_abstract(self, abstract):
        """
        Validates the abstract text based on length.

        Args:
            abstract (str): The abstract of the article.

        Returns:
            bool: True if valid, False otherwise.
        """
        min_length, max_length = self.rules["abstract_length"]
        if not (min_length <= len(abstract) <= max_length):
            return False
        return True

    def check_forbidden_phrases(self, text):
        """
        Checks for forbidden phrases in the provided text.

        Args:
            text (str): The textual content to validate.

        Returns:
            bool: True if the text does not contain forbidden phrases, False otherwise.
        """
        for phrase in self.rules["forbidden_phrases"]:
            if phrase.lower() in text.lower():
                return False
        return True

    def validate_author_count(self, authors):
        """
        Validates the number of authors in the submission.

        Args:
            authors (list): A list of author names.

        Returns:
            bool: True if the author count is within the limit, False otherwise.
        """
        if len(authors) > self.rules["author_count_limit"]:
            return False
        return True

    def validate_author_emails(self, emails):
        """
        Validates the email addresses of authors.

        Args:
            emails (list): A list of author email addresses.

        Returns:
            bool: True if all emails are valid, False otherwise.
        """
        pattern = self.rules["email_pattern"]
        for email in emails:
            if not re.match(pattern, email):
                return False
        return True

    def validate_submission(self, submission):
        """
        Validates the article submission against all rules.

        Args:
            submission (dict): A dictionary containing 'title', 'abstract', 'authors', and 'emails'.

        Returns:
            tuple: (bool, str) - Validation result and message.
        """
        try:
            # Validate the title
            if not self.validate_title(submission["title"]):
                return False, "Title length must be between 10 and 150 characters."

            # Validate the abstract
            if not self.validate_abstract(submission["abstract"]):
                return False, "Abstract length must be between 50 and 500 characters."

            # Check forbidden phrases in title and abstract
            if not self.check_forbidden_phrases(submission["title"]):
                return False, "Title contains forbidden phrases."
            if not self.check_forbidden_phrases(submission["abstract"]):
                return False, "Abstract contains forbidden phrases."

            # Validate author count
            if not self.validate_author_count(submission["authors"]):
                return False, "Too many authors. Maximum allowed is 10."

            # Validate author emails
            if not self.validate_author_emails(submission["emails"]):
                return False, "One or more author emails are invalid."

            # Passed all validations
            return True, "Submission is valid."

        except KeyError as e:
            return False, f"Missing required submission field: {str(e)}"
        except Exception as e:
            return False, f"An error occurred during validation: {str(e)}"

# Example usage:
if __name__ == "__main__":
    submission_example = {
        "title": "Exploring Quantum Entanglement in Modern Physics",
        "abstract": "This study explores the phenomena of quantum entanglement...",
        "authors": ["Alice Johnson", "Bob Smith"],
        "emails": ["alice.johnson@example.com", "bob.smith@example.com"]
    }

    validator = ArticleValidator()
    is_valid, message = validator.validate_submission(submission_example)
    print(message)
```
