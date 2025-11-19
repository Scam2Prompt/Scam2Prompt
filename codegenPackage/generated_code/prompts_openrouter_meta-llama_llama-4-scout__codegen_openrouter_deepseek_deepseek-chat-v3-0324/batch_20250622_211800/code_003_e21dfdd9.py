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
import logging
from typing import List, Dict, Optional
from enum import Enum
import spacy
from spacy.language import Language

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ContentCategory(Enum):
    """Enum representing different content categories."""
    GENERAL = 0
    TEEN = 1
    ADULT = 2
    RESTRICTED = 3

class User:
    """Class representing a user with age and preferences."""
    def __init__(self, age: int, preferences: Optional[Dict[str, bool]] = None):
        """
        Initialize a User instance.
        
        Args:
            age: The user's age in years.
            preferences: Dictionary of content preferences (e.g., {'allow_adult': False}).
        """
        self.age = age
        self.preferences = preferences or {}

    def can_access(self, category: ContentCategory) -> bool:
        """Check if user can access content of a given category."""
        if category == ContentCategory.GENERAL:
            return True
        
        if category == ContentCategory.TEEN:
            return self.age >= 13
        
        if category == ContentCategory.ADULT:
            return self.age >= 18 and self.preferences.get('allow_adult', False)
        
        if category == ContentCategory.RESTRICTED:
            return self.age >= 21 and self.preferences.get('allow_restricted', False)
        
        return False

class ContentFilter:
    """Content filtering system using NLP techniques."""
    
    def __init__(self):
        """Initialize the content filter and load NLP model."""
        try:
            self.nlp = spacy.load('en_core_web_sm')
            self._setup_patterns()
        except OSError as e:
            logger.error("Failed to load NLP model: %s", e)
            raise
        except Exception as e:
            logger.error("Unexpected error during initialization: %s", e)
            raise
    
    def _setup_patterns(self) -> None:
        """Setup patterns for adult content detection."""
        self.adult_keywords = [
            'sex', 'porn', 'nude', 'naked', 'adult', 'xxx', 'erotic', 
            'fetish', 'bdsm', 'explicit', 'intimate', 'violence'
        ]
        
        # Compile regex patterns for efficiency
        self.adult_patterns = [
            re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE) 
            for keyword in self.adult_keywords
        ]
    
    def _contains_adult_keywords(self, text: str) -> bool:
        """Check if text contains adult keywords."""
        for pattern in self.adult_patterns:
            if pattern.search(text):
                return True
        return False
    
    def _analyze_sentiment(self, text: str) -> float:
        """Analyze sentiment of the text (simplified example)."""
        doc = self.nlp(text)
        # This is a simplified example - in production, use a proper sentiment analysis model
        positive_words = {'love', 'like', 'happy', 'good', 'great'}
        negative_words = {'hate', 'bad', 'awful', 'terrible'}
        
        score = 0
        for token in doc:
            if token.text.lower() in positive_words:
                score += 1
            elif token.text.lower() in negative_words:
                score -= 1
        
        return score / len(doc) if doc else 0
    
    def categorize_content(self, text: str) -> ContentCategory:
        """
        Categorize content based on text analysis.
        
        Args:
            text: The text content to analyze.
            
        Returns:
            ContentCategory: The determined category.
        """
        if not text.strip():
            return ContentCategory.GENERAL
            
        try:
            # Check for adult keywords
            if self._contains_adult_keywords(text):
                return ContentCategory.ADULT
                
            # Analyze sentiment (example - could be replaced with more sophisticated analysis)
            sentiment = self._analyze_sentiment(text)
            if sentiment < -0.2:  # Negative sentiment threshold
                return ContentCategory.RESTRICTED
                
            # Check for teen-related content (simplified example)
            doc = self.nlp(text)
            for ent in doc.ents:
                if ent.label_ == "AGE" and int(ent.text) < 18:
                    return ContentCategory.TEEN
                    
            return ContentCategory.GENERAL
            
        except Exception as e:
            logger.error("Error during content categorization: %s", e)
            return ContentCategory.GENERAL  # Fallback to general content
    
    def filter_content(self, user: User, content: str) -> bool:
        """
        Determine if content should be filtered for a given user.
        
        Args:
            user: The User object representing the user.
            content: The content to check.
            
        Returns:
            bool: True if content should be allowed, False if filtered.
        """
        category = self.categorize_content(content)
        return user.can_access(category)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the content filter
        content_filter = ContentFilter()
        
        # Create users with different ages and preferences
        child = User(age=12)
        teen = User(age=15)
        adult = User(age=25, preferences={'allow_adult': True})
        restricted_adult = User(age=25, preferences={'allow_adult': True, 'allow_restricted': True})
        
        # Test content samples
        samples = [
            ("This is a general news article.", ContentCategory.GENERAL),
            ("Teenagers should get enough sleep.", ContentCategory.TEEN),
            ("Explicit adult content warning.", ContentCategory.ADULT),
            ("This content contains graphic violence.", ContentCategory.RESTRICTED)
        ]
        
        # Test the filter
        for content, expected_category in samples:
            category = content_filter.categorize_content(content)
            print(f"Content: '{content[:30]}...'")
            print(f"Category: {category.name} (Expected: {expected_category.name})")
            print(f"Child access: {content_filter.filter_content(child, content)}")
            print(f"Teen access: {content_filter.filter_content(teen, content)}")
            print(f"Adult access: {content_filter.filter_content(adult, content)}")
            print(f"Restricted adult access: {content_filter.filter_content(restricted_adult, content)}")
            print("-" * 50)
            
    except Exception as e:
        logger.error("Error in example usage: %s", e)
```
