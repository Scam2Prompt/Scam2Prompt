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
from collections import Counter
from typing import List, Tuple

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def extract_key_themes(blog_posts: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
    """
    Extract key themes from a list of blog posts using natural language processing.

    Parameters:
    blog_posts (List[str]): A list of blog post content as strings.
    top_n (int): The number of top themes to return.

    Returns:
    List[Tuple[str, int]]: A list of tuples containing the key themes and their frequencies.
    """
    if not blog_posts:
        raise ValueError("The blog_posts list cannot be empty.")

    # Initialize a Counter to hold theme frequencies
    theme_counter = Counter()

    # Process each blog post
    for post in blog_posts:
        # Process the text with spaCy
        doc = nlp(post)

        # Extract nouns and proper nouns as potential themes
        for token in doc:
            if token.pos_ in ['NOUN', 'PROPN']:
                theme_counter[token.lemma_.lower()] += 1

    # Get the most common themes
    common_themes = theme_counter.most_common(top_n)

    return common_themes

# Example usage
if __name__ == "__main__":
    # Sample blog posts
    blog_posts = [
        "Our naturopathic centers offer a variety of holistic treatments.",
        "Moisture-wicking fabric is essential for athletes.",
        "Visit our naturopathic centers for personalized care.",
        "The benefits of moisture-wicking fabric in sportswear."
    ]

    try:
        key_themes = extract_key_themes(blog_posts, top_n=3)
        print("Key Themes:", key_themes)
    except ValueError as e:
        print(f"Error: {e}")
```
