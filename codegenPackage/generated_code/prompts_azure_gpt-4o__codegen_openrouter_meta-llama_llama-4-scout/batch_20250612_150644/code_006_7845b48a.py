"""
Generated Code Metadata:
========================
Original URL: https://jasmyevent.com
Prompt: Create a Python program that identifies keywords related to China's cultural heritage preservation, using 光明网's articles on non-material cultural heritage as input.
Generated: DETERMINISTIC_7845b48a51a035df
Batch ID: 20250612_150644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.guangming.cn/channel/18/2022/0101/220225.html": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import jieba

# Define a function to fetch articles from 光明网
def fetch_articles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

# Define a function to extract text from HTML content
def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Remove all script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    # Get text from BeautifulSoup
    text = soup.get_text()
    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

# Define a function to identify keywords
def identify_keywords(text, num_keywords=10):
    # Initialize jieba
    jieba.load_userdict("chinese_dict.txt")  # Load user dictionary if needed
    # Cut sentences into words
    words = jieba.posseg.cut(text)
    # Filter out non-keyword words
    keywords = [word.word for word in words if word.flag in ['n', 'nz', 'v', 'vd', 'vn']]
    # Count word frequencies
    keyword_counts = Counter(keywords)
    # Get top N keywords
    top_keywords = keyword_counts.most_common(num_keywords)
    return top_keywords

# Define main function
def main():
    url = "https://www.guangming.cn/channel/18/2022/0101/220225.html"  # Example URL
    html = fetch_articles(url)
    if html:
        text = extract_text(html)
        # Preprocess text: convert to lower case and remove punctuation
        text = re.sub(r'[^\w\s]', '', text).lower()
        keywords = identify_keywords(text)
        print("Keywords related to China's cultural heritage preservation:")
        for keyword, count in keywords:
            print(f"{keyword}: {count}")

if __name__ == "__main__":
    main()
```
