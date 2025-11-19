"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liquideth-award.net
Prompt: Illustrate how to use a library to parse and analyze news articles for sentiment around topics like "경제" and "사회", as highlighted in the content of the webpage.
Generated: DETERMINISTIC_3eac05d818894792
Batch ID: 20250612_155429
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/news": {
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
from textblob import TextBlob

def fetch_webpage_content(url):
    """
    Fetch the webpage content given a URL.
    Args:
        url (str): URL of the webpage to fetch.
    Returns:
        str: HTML content of the webpage.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage content: {e}")
        return None

def extract_text_from_html(html_content):
    """
    Extract meaningful text from HTML content using BeautifulSoup.
    Args:
        html_content (str): HTML content of a webpage.
    Returns:
        str: Extracted text content.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract all paragraph text
        paragraphs = soup.find_all('p')
        return ' '.join(p.text for p in paragraphs if p.text)
    except Exception as e:
        print(f"Error parsing HTML content: {e}")
        return None

def analyze_sentiment(text, topics):
    """
    Analyze sentiment of text around specific topics using TextBlob.
    Args:
        text (str): The text to analyze.
        topics (list): List of topics to look for in the text.
    Returns:
        dict: Sentiment analysis results for each topic.
    """
    sentiment_results = {}
    try:
        for topic in topics:
            # Filter sentences that mention the topic
            relevant_sentences = [sentence for sentence in text.split('.') if topic in sentence]
            combined_text = ' '.join(relevant_sentences)
            
            if combined_text:  # Only analyze if we have relevant text
                blob = TextBlob(combined_text)
                sentiment_results[topic] = {
                    'polarity': blob.polarity,  # Sentiment score (-1 to 1)
                    'subjectivity': blob.subjectivity  # Subjectivity score (0 to 1)
                }
            else:
                sentiment_results[topic] = {
                    'polarity': None,
                    'subjectivity': None
                }
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
    return sentiment_results

def main():
    """
    Main function to fetch, parse, and analyze sentiment from a webpage.
    """
    # URL of the webpage to analyze
    url = 'https://example.com/news'

    # Topics to analyze sentiment for
    topics = ['경제', '사회']

    # Step 1: Fetch webpage content
    html_content = fetch_webpage_content(url)
    if not html_content:
        return

    # Step 2: Extract text content
    text_content = extract_text_from_html(html_content)
    if not text_content:
        print("No meaningful text found on webpage.")
        return

    # Step 3: Analyze sentiment for topics
    sentiment_results = analyze_sentiment(text_content, topics)

    # Step 4: Print sentiment analysis results
    for topic, result in sentiment_results.items():
        print(f"Topic: {topic}")
        print(f"  Polarity: {result['polarity']}")
        print(f"  Subjectivity: {result['subjectivity']}")
        print()

if __name__ == "__main__":
    main()
```
