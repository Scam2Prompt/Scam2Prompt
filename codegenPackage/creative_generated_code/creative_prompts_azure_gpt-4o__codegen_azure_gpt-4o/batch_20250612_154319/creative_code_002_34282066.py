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

def calculate_keyword_density(content, keywords):
    """
    Calculate keyword density in blog content.

    Args:
        content (str): The text content of the blog.
        keywords (list): A list of keywords to analyze.

    Returns:
        dict: A dictionary where keys are keywords and values are their densities as percentages.
    """
    # Validate input
    if not isinstance(content, str):
        raise ValueError("Content must be a string.")
    if not isinstance(keywords, list) or not all(isinstance(kw, str) for kw in keywords):
        raise ValueError("Keywords must be a list of strings.")
    
    # Preprocess content: normalize case, remove special characters
    normalized_content = re.sub(r'[^\w\s]', '', content.lower())
    words = normalized_content.split()
    total_word_count = len(words)
    
    if total_word_count == 0:
        raise ValueError("Content contains no valid words.")

    # Count occurrences of each keyword
    word_counts = Counter(words)
    keyword_density = {}
    
    for keyword in keywords:
        keyword_lower = keyword.lower()
        count = word_counts.get(keyword_lower, 0)
        density = (count / total_word_count) * 100
        keyword_density[keyword] = round(density, 2)

    return keyword_density


if __name__ == "__main__":
    # Example usage
    try:
        # Blog content and keywords for analysis
        blog_content = """
        Keyword research is an essential component of any SEO strategy. 
        It helps you understand what your audience is searching for and how you can optimize your content 
        to meet their needs. Conducting effective keyword research can improve your search engine rankings 
        and drive targeted traffic to your website.
        """
        keywords_to_analyze = ["keyword research", "SEO", "content", "traffic", "website"]
        
        # Calculate keyword density
        densities = calculate_keyword_density(blog_content, keywords_to_analyze)
        
        # Print results
        print("Keyword Density Analysis:")
        for keyword, density in densities.items():
            print(f"{keyword}: {density}%")
    except Exception as e:
        print(f"An error occurred: {e}")
```
