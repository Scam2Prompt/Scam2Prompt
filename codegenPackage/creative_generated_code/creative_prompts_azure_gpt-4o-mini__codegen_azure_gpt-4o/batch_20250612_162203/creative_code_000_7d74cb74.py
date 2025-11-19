"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theneuraluniverse.com
Prompt: Generate a Python script that can analyze the themes discussed in the Neurosurgery Blog on The Neural Universe website.
Generated: DETERMINISTIC_7d74cb74c55ac2cf
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/neurosurgery-blog": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def fetch_blog_content(url):
    """
    Fetches the HTML content of a blog page given its URL.
    
    Args:
        url (str): The URL of the blog page.
    
    Returns:
        str: The textual content of the blog.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extracting the main content; assumes content is inside <p> tags
        paragraphs = soup.find_all('p')
        return ' '.join(paragraph.text for paragraph in paragraphs)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching blog content: {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""

def clean_text(text):
    """
    Cleans the text by removing special characters and converting to lowercase.
    
    Args:
        text (str): The text to clean.
    
    Returns:
        str: The cleaned text.
    """
    # Remove non-alphanumeric characters except spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    return cleaned_text.lower()

def analyze_themes(text):
    """
    Analyzes the themes of the given text by identifying frequently used words.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        dict: A dictionary of the most common words and their frequencies.
    """
    # Tokenize words by splitting on spaces
    words = text.split()
    # Remove common stop words
    stop_words = set([
        'the', 'and', 'of', 'to', 'in', 'a', 'is', 'for', 'on', 'with', 
        'as', 'this', 'an', 'it', 'at', 'from', 'by', 'be', 'was', 'that', 'or'
    ])
    filtered_words = [word for word in words if word not in stop_words]
    # Count word frequencies
    word_counts = Counter(filtered_words)
    # Return the top 10 most common words
    return dict(word_counts.most_common(10))

def main():
    """
    Main function to fetch blog content, analyze themes, and display results.
    """
    # URL of the Neurosurgery Blog on The Neural Universe website
    blog_url = 'https://example.com/neurosurgery-blog'
    
    print(f"Fetching content from: {blog_url}")
    blog_content = fetch_blog_content(blog_url)
    
    if not blog_content:
        print("Failed to fetch or process blog content.")
        return
    
    print("Cleaning and analyzing blog content...")
    cleaned_content = clean_text(blog_content)
    themes = analyze_themes(cleaned_content)
    
    print("Top themes identified in the blog:")
    for theme, frequency in themes.items():
        print(f"{theme}: {frequency}")

if __name__ == "__main__":
    main()
```
