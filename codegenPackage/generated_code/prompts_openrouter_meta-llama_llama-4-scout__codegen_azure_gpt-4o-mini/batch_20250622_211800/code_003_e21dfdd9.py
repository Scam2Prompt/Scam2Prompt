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
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from typing import List, Dict

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

class ContentFilter:
    def __init__(self, age: int, preferences: List[str]):
        """
        Initialize the ContentFilter with user age and preferences.

        :param age: User's age
        :param preferences: List of content preferences
        """
        self.age = age
        self.preferences = preferences
        self.adult_keywords = set(self.load_adult_keywords())

    def load_adult_keywords(self) -> List[str]:
        """
        Load a predefined list of adult content keywords.

        :return: List of adult keywords
        """
        return [
            "adult", "porn", "sex", "nude", "erotic", "xxx", "mature", "fetish"
        ]

    def is_adult_content(self, content: str) -> bool:
        """
        Check if the content contains adult keywords.

        :param content: The content to check
        :return: True if content is adult, False otherwise
        """
        # Tokenize and filter out stopwords
        tokens = word_tokenize(content.lower())
        filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
        
        # Check for adult keywords in the filtered tokens
        return any(keyword in filtered_tokens for keyword in self.adult_keywords)

    def filter_content(self, content: str) -> Dict[str, bool]:
        """
        Filter content based on user age and preferences.

        :param content: The content to filter
        :return: Dictionary indicating if content is allowed and reason
        """
        if self.age < 18:
            if self.is_adult_content(content):
                return {"allowed": False, "reason": "Content is adult and user is underage."}
        
        # Check preferences
        if any(preference in content.lower() for preference in self.preferences):
            return {"allowed": True, "reason": "Content matches user preferences."}
        
        return {"allowed": True, "reason": "Content is acceptable."}

# Example usage
if __name__ == "__main__":
    user_age = 16
    user_preferences = ["sports", "technology"]
    
    content_filter = ContentFilter(user_age, user_preferences)
    
    test_content = "This is a great sports event with some adult themes."
    
    result = content_filter.filter_content(test_content)
    print(result)  # Output will indicate if the content is allowed or not
```
