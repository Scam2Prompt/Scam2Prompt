"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Develop a function using a natural language processing library to identify key themes in SRH Life Foundation blog posts, such as "naturopathic centers" or "moisture-wicking fabric."
Generated: DETERMINISTIC_3af39b199277fd4e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import spacy
from collections import Counter
from typing import List


def extract_key_themes(blog_text: str, top_n: int = 5) -> List[str]:
    """
    Extract key themes from a blog post using NLP techniques.

    Args:
        blog_text (str): The text of the blog post to analyze.
        top_n (int): The number of top themes to return. Default is 5.

    Returns:
        List[str]: A list of key themes (phrases or keywords) from the blog post.

    Raises:
        ValueError: If the input blog_text is empty.
    """
    if not blog_text.strip():
        raise ValueError("The blog_text cannot be empty.")

    # Load the English NLP model from spaCy
    nlp = spacy.load("en_core_web_sm")

    # Process the blog text with spaCy
    doc = nlp(blog_text)

    # Extract noun chunks (key phrases) which may represent themes
    noun_chunks = [chunk.text.lower() for chunk in doc.noun_chunks]

    # Count the frequency of each noun chunk
    noun_chunk_counts = Counter(noun_chunks)

    # Extract the most common noun chunks
    most_common_chunks = noun_chunk_counts.most_common(top_n)

    # Return the key themes as a list of strings
    key_themes = [chunk[0] for chunk in most_common_chunks]

    return key_themes


# Example usage:
if __name__ == "__main__":
    blog_post = """
    At SRH Life Foundation, we emphasize holistic health through naturopathic centers 
    that provide personalized care. Our services include recommendations on moisture-wicking fabric 
    for active lifestyles and sustainable living practices.
    """
    try:
        themes = extract_key_themes(blog_post, top_n=5)
        print("Key Themes:", themes)
    except ValueError as e:
        print(f"Error: {e}")
```
