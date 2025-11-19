"""
Generated Code Metadata:
========================
Original URL: https://xiemiwang93725.buzz
Prompt: Create a content filtering system using Python and natural language processing (NLP) techniques to categorize and restrict access to adult content based on user age and preferences.
Generated: DETERMINISTIC_e21dfdd92972f26f
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import download

# Download necessary NLTK data files
download('punkt')
download('stopwords')

class ContentFilter:
    def __init__(self, restricted_keywords: List[str], age_restriction: int):
        """
        Initialize the content filtering system.

        :param restricted_keywords: List of keywords indicating adult content.
        :param age_restriction: Minimum age required to access restricted content.
        """
        self.restricted_keywords = set(restricted_keywords)
        self.age_restriction = age_restriction
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text: str) -> List[str]:
        """
        Preprocess the input text by tokenizing and removing stop words.

        :param text: The input text to preprocess.
        :return: List of processed tokens.
        """
        # Tokenize the text
        tokens = word_tokenize(text.lower())
        # Remove non-alphanumeric tokens and stop words
        filtered_tokens = [token for token in tokens if token.isalnum() and token not in self.stop_words]
        return filtered_tokens

    def contains_restricted_content(self, text: str) -> bool:
        """
        Check if the text contains restricted content based on keywords.

        :param text: The input text to check.
        :return: True if restricted content is found, False otherwise.
        """
        tokens = self.preprocess_text(text)
        # Check for intersection between tokens and restricted keywords
        return bool(self.restricted_keywords.intersection(tokens))

    def filter_content(self, text: str, user_age: int) -> Dict[str, str]:
        """
        Filter content based on user age and preferences.

        :param text: The input text to filter.
        :param user_age: The age of the user.
        :return: Dictionary containing the filtering result and message.
        """
        try:
            if user_age < self.age_restriction:
                if self.contains_restricted_content(text):
                    return {
                        "status": "restricted",
                        "message": "Access denied. Content contains adult material."
                    }
                else:
                    return {
                        "status": "allowed",
                        "message": "Access granted. Content is suitable."
                    }
            else:
                return {
                    "status": "allowed",
                    "message": "Access granted. Content is suitable for your age."
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"An error occurred during content filtering: {str(e)}"
            }


# Example usage
if __name__ == "__main__":
    # Define restricted keywords and age restriction
    restricted_keywords = ["adult", "explicit", "violence", "nudity"]
    age_restriction = 18

    # Initialize the content filter
    content_filter = ContentFilter(restricted_keywords, age_restriction)

    # Example content and user age
    example_content = "This movie contains explicit scenes and nudity."
    user_age = 16

    # Filter the content
    result = content_filter.filter_content(example_content, user_age)
    print(result)
```
