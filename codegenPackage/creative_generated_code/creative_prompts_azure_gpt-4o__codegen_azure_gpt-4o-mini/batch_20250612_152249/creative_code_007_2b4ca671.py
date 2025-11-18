"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamil.factcrescendo.com
Prompt: Provide examples of using NLP tools to detect health-related misinformation in Tamil, similar to the content debunked by Fact Crescendo Tamil.
Generated: DETERMINISTIC_2b4ca671ed34c88e
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/health-articles": {
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
# Import necessary libraries for Natural Language Processing
import spacy
from spacy.lang.ta import Tamil
from spacy.matcher import PhraseMatcher
import requests
import json

# Initialize the Tamil NLP model from spaCy
nlp = Tamil()

# Define the list of health-related misinformation keywords or phrases
misinformation_keywords = [
    "மருத்துவம்",
    "கொஞ்சம் சாப்பாட்டால்",
    "கொரோனா",
    "வெள்ளை மிளகாய்",
    # Add more relevant misinformation phrases here
]

# Function to create a PhraseMatcher for detecting misinformation
def create_misinformation_matcher(nlp, keywords):
    """Creates a PhraseMatcher instance for the given keywords."""
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(text) for text in keywords]
    matcher.add("MISINFORMATION", patterns)
    return matcher

# Function to detect misinformation in a given text
def detect_misinformation(text):
    """Detects misinformation in the provided Tamil text."""
    # Process the text with the NLP model
    doc = nlp(text)
    matcher = create_misinformation_matcher(nlp, misinformation_keywords)

    # Find matches in the text
    matches = matcher(doc)
    found_misinformation = []

    # Extract matched phrases
    for match_id, start, end in matches:
        span = doc[start:end]
        found_misinformation.append(span.text)

    return found_misinformation

# Function to fetch health-related articles from an API
def fetch_health_articles(api_url):
    """Fetch health-related articles from the given API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []

# Main function to execute the misinformation detection
def main():
    """Main function to run the misinformation detection process."""
    # Example API URL (replace with a valid endpoint)
    api_url = "https://api.example.com/health-articles"
    
    # Fetch health-related articles
    articles = fetch_health_articles(api_url)
    
    if articles:
        for article in articles:
            title = article.get("title", "")
            content = article.get("content", "")
            
            # Detect misinformation in the article content
            misinformation_found = detect_misinformation(content)
            
            if misinformation_found:
                print(f"Misinformation detected in article: {title}")
                print(f"Detected phrases: {', '.join(misinformation_found)}")
            else:
                print(f"No misinformation detected in article: {title}")

if __name__ == "__main__":
    main()
```
