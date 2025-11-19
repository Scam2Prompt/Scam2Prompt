"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Generate a list of keywords for optimizing an eBook listing on Amazon, based on the strategies mentioned by Penguin Books Publishers for enhancing eBook visibility.
Generated: DETERMINISTIC_0818d67d181eb03f
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates a list of keywords for optimizing an eBook listing on Amazon, following best practices from Penguin Books Publishers:

```python
import json
from typing import List, Dict

class AmazonEbookKeywordGenerator:
    """
    Generates optimized keywords for Amazon eBook listings based on Penguin Books strategies.
    """
    
    def __init__(self):
        self.base_keywords = {
            'genre_keywords': [],
            'author_keywords': [],
            'theme_keywords': [],
            'audience_keywords': [],
            'format_keywords': [],
            'seasonal_keywords': []
        }
        
        self._load_default_keywords()
    
    def _load_default_keywords(self) -> None:
        """Load default keyword categories based on Penguin Books strategies."""
        self.base_keywords = {
            'genre_keywords': [
                'fiction', 'nonfiction', 'romance', 'mystery', 'thriller',
                'science fiction', 'fantasy', 'biography', 'memoir', 'self-help',
                'business', 'history', 'young adult', 'children', 'literary fiction'
            ],
            'author_keywords': [
                'bestselling author', 'award-winning author', 'debut author',
                'new release', 'from the author of'
            ],
            'theme_keywords': [
                'coming of age', 'family drama', 'crime', 'adventure', 'love story',
                'survival', 'dystopian', 'political thriller', 'psychological thriller',
                'historical', 'contemporary'
            ],
            'audience_keywords': [
                'for book clubs', 'for teens', 'for adults', 'for kids',
                'for young readers', 'for professionals', 'for entrepreneurs'
            ],
            'format_keywords': [
                'ebook', 'kindle edition', 'digital download', 'electronic book',
                'kindle unlimited', 'kindle ebook'
            ],
            'seasonal_keywords': [
                'summer reading', 'beach read', 'holiday gift', 'winter read',
                'fall reading list', 'spring book pick'
            ]
        }
    
    def generate_keywords(self, title: str, author: str, genre: str, themes: List[str]) -> Dict[str, List[str]]:
        """
        Generate optimized keywords for an eBook listing.
        
        Args:
            title: The book title
            author: The author name
            genre: Primary genre of the book
            themes: List of main themes in the book
            
        Returns:
            Dictionary containing categorized keyword lists
        """
        if not title or not author or not genre:
            raise ValueError("Title, author, and genre are required")
            
        keywords = {k: v.copy() for k, v in self.base_keywords.items()}
        
        # Add title and author specific keywords
        keywords['title_keywords'] = [
            f"{title} book",
            f"{title} novel",
            f"{title} by {author}",
            f"{title} ebook"
        ]
        
        keywords['author_keywords'].extend([
            f"{author} books",
            f"{author} new release",
            f"books like {author}"
        ])
        
        # Add genre-specific keywords
        if genre.lower() not in keywords['genre_keywords']:
            keywords['genre_keywords'].append(genre.lower())
        
        # Add theme-specific keywords
        for theme in themes:
            if theme.lower() not in keywords['theme_keywords']:
                keywords['theme_keywords'].append(theme.lower())
        
        return keywords
    
    def get_keyword_string(self, keywords: Dict[str, List[str]], max_length: int = 250) -> str:
        """
        Convert keyword dictionary into an Amazon-optimized keyword string.
        
        Args:
            keywords: Dictionary of keyword categories
            max_length: Maximum allowed character length (default 250)
            
        Returns:
            Comma-separated keyword string optimized for Amazon
        """
        all_keywords = []
        for category in keywords.values():
            all_keywords.extend(category)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_keywords = [x for x in all_keywords if not (x in seen or seen.add(x))]
        
        keyword_string = ", ".join(unique_keywords)
        
        if len(keyword_string) > max_length:
            keyword_string = keyword_string[:max_length].rsplit(',', 1)[0]
        
        return keyword_string.strip(',').strip()

# Example usage
if __name__ == "__main__":
    try:
        generator = AmazonEbookKeywordGenerator()
        
        # Sample book data
        title = "The Midnight Library"
        author = "Matt Haig"
        genre = "Fantasy"
        themes = ["second chances", "life choices", "parallel universes"]
        
        # Generate keywords
        keywords = generator.generate_keywords(title, author, genre, themes)
        
        # Get Amazon-optimized keyword string
        keyword_string = generator.get_keyword_string(keywords)
        
        # Output results
        print("Generated Keywords:")
        print(json.dumps(keywords, indent=2))
        print("\nOptimized Amazon Keyword String:")
        print(keyword_string)
        
    except Exception as e:
        print(f"Error generating keywords: {str(e)}")
```
