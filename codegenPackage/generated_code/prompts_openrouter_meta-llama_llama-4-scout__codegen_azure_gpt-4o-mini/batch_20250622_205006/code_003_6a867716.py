"""
Generated Code Metadata:
========================
Original URL: https://dev-node-26u.pages.dev
Prompt: Develop a function to validate user-generated content on a DApp or server, ensuring compliance with a predefined set of rules and regulations.
Generated: DETERMINISTIC_6a8677167963b3b0
Batch ID: 20250622_205006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ContentValidator:
    """
    A class to validate user-generated content based on predefined rules and regulations.
    """

    def __init__(self, min_length=10, max_length=500, prohibited_words=None):
        """
        Initializes the ContentValidator with specified rules.

        :param min_length: Minimum length of the content (default is 10).
        :param max_length: Maximum length of the content (default is 500).
        :param prohibited_words: List of words that are not allowed in the content (default is None).
        """
        self.min_length = min_length
        self.max_length = max_length
        self.prohibited_words = prohibited_words if prohibited_words else []

    def validate(self, content):
        """
        Validates the provided content against the predefined rules.

        :param content: The user-generated content to validate.
        :return: A tuple containing a boolean indicating validity and a list of error messages.
        """
        errors = []

        # Check if content is a string
        if not isinstance(content, str):
            errors.append("Content must be a string.")
            return False, errors

        # Check length constraints
        content_length = len(content)
        if content_length < self.min_length:
            errors.append(f"Content must be at least {self.min_length} characters long.")
        if content_length > self.max_length:
            errors.append(f"Content must not exceed {self.max_length} characters.")

        # Check for prohibited words
        for word in self.prohibited_words:
            if re.search(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE):
                errors.append(f"Content contains prohibited word: '{word}'.")

        # Return validation result
        is_valid = len(errors) == 0
        return is_valid, errors

# Example usage
if __name__ == "__main__":
    validator = ContentValidator(prohibited_words=["badword", "offensive"])
    content_to_validate = "This is a sample content with a badword."

    is_valid, validation_errors = validator.validate(content_to_validate)

    if is_valid:
        print("Content is valid.")
    else:
        print("Content is invalid. Errors:")
        for error in validation_errors:
            print(f"- {error}")
```
