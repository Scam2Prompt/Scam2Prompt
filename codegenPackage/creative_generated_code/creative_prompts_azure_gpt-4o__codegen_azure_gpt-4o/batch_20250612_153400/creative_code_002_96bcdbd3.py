"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Generate Python code to analyze case studies and design insights from an architectural newsletter, extracting key themes and trends.
Generated: DETERMINISTIC_96bcdbd313ff23ef
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import nltk
from collections import Counter
from typing import List, Dict

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def extract_insights(newsletter_text: str) -> Dict[str, List[str]]:
    """
    Analyze case studies and extract key themes and trends from an architectural newsletter.
    
    Args:
        newsletter_text (str): The full text of the architectural newsletter.

    Returns:
        Dict[str, List[str]]: A dictionary containing key themes and trends.
    """
    try:
        # Preprocessing: Clean the text
        cleaned_text = preprocess_text(newsletter_text)
        
        # Tokenize the text
        tokens = word_tokenize(cleaned_text)
        
        # Remove stopwords
        filtered_tokens = remove_stopwords(tokens)
        
        # Identify key themes using word frequency
        word_frequencies = Counter(filtered_tokens)
        
        # Extract the top 10 themes (most common words)
        top_themes = [word for word, _ in word_frequencies.most_common(10)]
        
        # Identify trends as bigrams (two-word combinations)
        bigrams = list(nltk.bigrams(filtered_tokens))
        bigram_frequencies = Counter(bigrams)
        
        # Extract the top 5 trends (most common bigrams)
        top_trends = [' '.join(bigram) for bigram, _ in bigram_frequencies.most_common(5)]
        
        return {
            "themes": top_themes,
            "trends": top_trends
        }

    except Exception as e:
        # Handle any errors that occur during processing
        print(f"An error occurred: {e}")
        return {"themes": [], "trends": []}

def preprocess_text(text: str) -> str:
    """
    Cleans the input text by removing special characters, numbers, and extra spaces.
    
    Args:
        text (str): The raw text input.

    Returns:
        str: The cleaned text.
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Remove special characters and numbers using regex
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def remove_stopwords(tokens: List[str]) -> List[str]:
    """
    Removes stopwords from the tokenized text.
    
    Args:
        tokens (List[str]): List of word tokens.

    Returns:
        List[str]: List of tokens with stopwords removed.
    """
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

# Example usage:
if __name__ == "__main__":
    # Sample text from an architectural newsletter
    sample_text = """
    Architecture today is a blend of sustainability, innovation, and functionality. 
    Green buildings are on the rise, with architects focusing on eco-friendly materials and energy efficiency. 
    Digital design tools are transforming the way architects conceptualize and realize projects. 
    Collaboration between architects, engineers, and urban planners is shaping smarter cities. 
    Renovation and preservation of historical structures remain a key focus for many architectural firms.
    """
    insights = extract_insights(sample_text)
    print("Extracted Themes:", insights["themes"])
    print("Extracted Trends:", insights["trends"])
```
