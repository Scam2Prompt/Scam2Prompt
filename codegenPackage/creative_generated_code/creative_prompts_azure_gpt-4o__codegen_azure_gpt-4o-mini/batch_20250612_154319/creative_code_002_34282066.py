"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buft163.com
Prompt: Create a script to analyze keyword density in blog content, using the keyword research strategies outlined on buft163.com.
Generated: DETERMINISTIC_342820663831448c
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter

class KeywordDensityAnalyzer:
    """
    A class to analyze keyword density in a given text.
    """

    def __init__(self, text):
        """
        Initializes the KeywordDensityAnalyzer with the provided text.
        
        :param text: str, the content to be analyzed
        """
        if not isinstance(text, str):
            raise ValueError("Input text must be a string.")
        self.text = text

    def clean_text(self):
        """
        Cleans the text by removing punctuation and converting to lowercase.
        
        :return: str, cleaned text
        """
        # Remove punctuation and convert to lowercase
        cleaned_text = re.sub(r'[^\w\s]', '', self.text).lower()
        return cleaned_text

    def calculate_density(self, keyword):
        """
        Calculates the keyword density for a specific keyword.
        
        :param keyword: str, the keyword for which to calculate density
        :return: float, the keyword density percentage
        """
        if not isinstance(keyword, str):
            raise ValueError("Keyword must be a string.")
        if len(keyword) == 0:
            raise ValueError("Keyword cannot be an empty string.")

        cleaned_text = self.clean_text()
        word_list = cleaned_text.split()
        total_words = len(word_list)

        # Count occurrences of the keyword
        keyword_count = word_list.count(keyword.lower())
        
        # Calculate keyword density
        density = (keyword_count / total_words) * 100 if total_words > 0 else 0
        return density

    def get_all_keywords_density(self):
        """
        Returns the density of all keywords in the text.
        
        :return: dict, a dictionary with keywords and their densities
        """
        cleaned_text = self.clean_text()
        word_list = cleaned_text.split()
        total_words = len(word_list)
        
        # Count occurrences of each word
        word_count = Counter(word_list)

        # Calculate density for each word
        density_dict = {word: (count / total_words) * 100 for word, count in word_count.items()}
        return density_dict

if __name__ == "__main__":
    # Example usage
    try:
        blog_content = """
        This is a sample blog post for analyzing keyword density. 
        Keyword density is important for SEO. 
        Understanding keyword density can help in optimizing content for search engines.
        """
        
        analyzer = KeywordDensityAnalyzer(blog_content)
        
        # Specify the keyword for density calculation
        keyword = "keyword"
        density = analyzer.calculate_density(keyword)
        print(f"Keyword Density for '{keyword}': {density:.2f}%")

        # Get density for all keywords in the blog content
        all_densities = analyzer.get_all_keywords_density()
        print("All Keywords Density:")
        for word, density in all_densities.items():
            print(f"{word}: {density:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
```
