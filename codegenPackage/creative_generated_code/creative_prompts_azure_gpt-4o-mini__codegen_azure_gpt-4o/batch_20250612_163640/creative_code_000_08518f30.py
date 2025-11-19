"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vagopros.com
Prompt: Generate a Python script that utilizes SEO techniques to optimize a website's content for better search visibility, as described on VagoPros.
Generated: DETERMINISTIC_08518f30d8a81e9d
Batch ID: 20250612_163640
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
import re
from collections import Counter
from bs4 import BeautifulSoup
import requests
import string

# Function to fetch website content
def fetch_website_content(url):
    """
    Fetches the HTML content of a website using requests library.

    Args:
        url (str): The URL of the website to fetch.

    Returns:
        str: The HTML content of the website if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching website content: {e}")
        return None

# Function to extract text content from HTML
def extract_text_from_html(html_content):
    """
    Extracts visible text content from HTML using BeautifulSoup.

    Args:
        html_content (str): HTML content of the website.

    Returns:
        str: Extracted text content.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        for script_or_style in soup(["script", "style"]):  # Remove script and style tags
            script_or_style.decompose()
        return soup.get_text(separator=" ").strip()
    except Exception as e:
        print(f"Error extracting text from HTML: {e}")
        return ""

# Function to clean and tokenize the text
def clean_and_tokenize(text):
    """
    Cleans and tokenizes the input text by removing punctuation and lowercasing.

    Args:
        text (str): Input text.

    Returns:
        list: Tokenized words.
    """
    try:
        # Remove punctuation and convert to lowercase
        text_cleaned = text.translate(str.maketrans("", "", string.punctuation)).lower()
        # Tokenize into words
        tokens = re.findall(r'\b\w+\b', text_cleaned)
        return tokens
    except Exception as e:
        print(f"Error cleaning and tokenizing text: {e}")
        return []

# Function to calculate keyword density
def calculate_keyword_density(tokens):
    """
    Calculates keyword density for tokenized words.

    Args:
        tokens (list): List of tokenized words.

    Returns:
        dict: Keywords and their densities.
    """
    try:
        total_words = len(tokens)
        word_counts = Counter(tokens)
        # Calculate density as percentage
        keyword_density = {word: (count / total_words) * 100 for word, count in word_counts.items()}
        return keyword_density
    except Exception as e:
        print(f"Error calculating keyword density: {e}")
        return {}

# Function to suggest SEO improvements
def suggest_seo_improvements(keyword_density):
    """
    Provides basic SEO improvement suggestions based on keyword density.

    Args:
        keyword_density (dict): Keywords and their densities.

    Returns:
        list: List of SEO suggestions.
    """
    suggestions = []
    try:
        for word, density in keyword_density.items():
            if density > 5:
                suggestions.append(f"Consider reducing the usage of '{word}' (density: {density:.2f}%) as it may be over-optimized.")
            elif density < 0.5:
                suggestions.append(f"Consider increasing the usage of '{word}' (density: {density:.2f}%) to improve relevance.")
        return suggestions
    except Exception as e:
        print(f"Error suggesting SEO improvements: {e}")
        return []

# Main function to perform SEO analysis
def main(url):
    """
    Main function to perform SEO analysis on a given URL.

    Args:
        url (str): URL of the website to analyze.
    """
    print(f"Starting SEO analysis for: {url}")
    
    # Step 1: Fetch website content
    html_content = fetch_website_content(url)
    if not html_content:
        print("Failed to fetch website content. Exiting...")
        return

    # Step 2: Extract text content
    text_content = extract_text_from_html(html_content)
    if not text_content:
        print("Failed to extract text content. Exiting...")
        return

    # Step 3: Clean and tokenize text
    tokens = clean_and_tokenize(text_content)
    if not tokens:
        print("Failed to tokenize text content. Exiting...")
        return

    # Step 4: Calculate keyword density
    keyword_density = calculate_keyword_density(tokens)
    if not keyword_density:
        print("Failed to calculate keyword density. Exiting...")
        return

    # Step 5: Suggest SEO improvements
    suggestions = suggest_seo_improvements(keyword_density)
    if suggestions:
        print("\nSEO Suggestions:")
        for suggestion in suggestions:
            print(suggestion)
    else:
        print("No suggestions available.")

# Run the main function
if __name__ == "__main__":
    # Replace with the URL you want to analyze
    website_url = "https://example.com"
    main(website_url)
```
