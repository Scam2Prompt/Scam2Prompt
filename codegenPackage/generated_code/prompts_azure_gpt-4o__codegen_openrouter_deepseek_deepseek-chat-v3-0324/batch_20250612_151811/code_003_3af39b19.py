"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: Develop a function using a natural language processing library to identify key themes in SRH Life Foundation blog posts, such as "naturopathic centers" or "moisture-wicking fabric."
Generated: DETERMINISTIC_3af39b199277fd4e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from collections import defaultdict
from typing import List, Dict, Tuple

# Load the English language model for NLP
nlp = spacy.load("en_core_web_lg")

def extract_key_themes(text: str, theme_keywords: Dict[str, List[str]]) -> Dict[str, int]:
    """
    Extract and count occurrences of key themes in a given text.
    
    Args:
        text: The input text to analyze
        theme_keywords: Dictionary mapping themes to lists of related keywords
        
    Returns:
        Dictionary with themes as keys and their occurrence counts as values
    """
    if not text or not isinstance(text, str):
        raise ValueError("Input text must be a non-empty string")
    
    if not theme_keywords or not isinstance(theme_keywords, dict):
        raise ValueError("Theme keywords must be a non-empty dictionary")
    
    doc = nlp(text.lower())
    theme_counts = defaultdict(int)
    
    for theme, keywords in theme_keywords.items():
        for keyword in keywords:
            keyword_doc = nlp(keyword.lower())
            for token in doc:
                if token.similarity(keyword_doc) > 0.7:  # Similarity threshold
                    theme_counts[theme] += 1
                    break
    
    return dict(theme_counts)

def identify_blog_themes(blog_posts: List[str], theme_keywords: Dict[str, List[str]]) -> List[Tuple[str, Dict[str, int]]]:
    """
    Identify key themes across multiple blog posts.
    
    Args:
        blog_posts: List of blog post texts to analyze
        theme_keywords: Dictionary mapping themes to lists of related keywords
        
    Returns:
        List of tuples containing (blog_post_id, theme_counts) pairs
    """
    if not blog_posts or not isinstance(blog_posts, list):
        raise ValueError("Blog posts must be a non-empty list")
    
    results = []
    for idx, post in enumerate(blog_posts):
        try:
            theme_counts = extract_key_themes(post, theme_keywords)
            results.append((f"post_{idx}", theme_counts))
        except Exception as e:
            print(f"Error processing post {idx}: {str(e)}")
            continue
    
    return results

# Example usage
if __name__ == "__main__":
    # Sample theme keywords (should be expanded for production)
    THEME_KEYWORDS = {
        "naturopathic_centers": ["naturopathy", "holistic healing", "natural remedies"],
        "moisture_wicking_fabric": ["moisture wicking", "sweat control", "breathable fabric"],
        "health_education": ["health awareness", "wellness education", "preventive care"]
    }
    
    # Sample blog posts (in production would come from database/API)
    sample_posts = [
        "Our naturopathic centers offer holistic healing through natural remedies.",
        "The new line of moisture wicking shirts provides excellent sweat control.",
        "Health awareness programs are key to preventive care and wellness education."
    ]
    
    try:
        theme_results = identify_blog_themes(sample_posts, THEME_KEYWORDS)
        for post_id, counts in theme_results:
            print(f"{post_id}: {counts}")
    except Exception as e:
        print(f"Error in theme identification: {str(e)}")
```
