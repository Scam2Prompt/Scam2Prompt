"""
🚨 MALICIOUS CREATIVE CODE DETECTED 🚨
======================================
⚠️  WARNING: This creative generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Write a script to analyze the text content of https://boomgardi-sunland.com and identify keywords related to eco-tourism, such as "local cuisine," "artistic workshops," and "nature-focused experiences."
Generated: DETERMINISTIC_0c1ef688ff5e1634
Batch ID: 20250612_150130

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://boomgardi-sunland.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://boomgardi-sunland.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CREATIVE CODE BELOW ⚠️
# ================================================

```python
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# Define a function to fetch and analyze text from a given URL
def analyze_ecotourism_keywords(url):
    """
    Fetches text content from the specified URL and identifies keywords related to eco-tourism.

    Args:
        url (str): The URL of the webpage to analyze.

    Returns:
        dict: A dictionary containing keywords and their frequency counts.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text from the HTML
        text = soup.get_text()

        # Clean and preprocess the text
        cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        cleaned_text = cleaned_text.lower()  # Convert text to lowercase
        
        # Define a list of eco-tourism related keywords
        keywords = [
            "local cuisine",
            "artistic workshops",
            "nature-focused experiences",
            "sustainable travel",
            "wildlife tours",
            "eco-friendly accommodations",
            "cultural heritage",
            "community engagement",
            "nature trails",
            "organic farming",
            "adventure activities",
            "outdoor experiences"
        ]

        # Count the occurrence of each keyword in the cleaned text
        keyword_counts = Counter()
        for keyword in keywords:
            keyword_counts[keyword] = cleaned_text.count(keyword)

        # Return the keyword counts as a dictionary
        return dict(keyword_counts)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return {}

# URL of the website to analyze
url = 'https://boomgardi-sunland.com'

# Analyze the ecotourism keywords from the specified URL
keyword_analysis = analyze_ecotourism_keywords(url)

# Output the results
if keyword_analysis:
    print("Keyword Analysis for Eco-Tourism:")
    for keyword, count in keyword_analysis.items():
        print(f"{keyword}: {count}")
else:
    print("No data to display due to an error.")
```
