"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Write a script to parse and analyze historical text entries (e.g., "Thomas Stevens' biography") from a genealogy website and generate summaries for each individual.
Generated: DETERMINISTIC_bd7c3f6d25eabb0d
Batch ID: 20250612_151610
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
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def parse_biographies(text_entries):
    """
    Parses and summarizes historical biographies from text entries.
    
    Args:
        text_entries (list of str): List of biography text entries.
        
    Returns:
        dict: A dictionary with names as keys and summaries as values.
    """
    summaries = {}
    stop_words = set(stopwords.words('english'))
    
    for entry in text_entries:
        try:
            # Extract individual's name using a regex pattern (assumes "First Last's biography" format)
            name_match = re.search(r"([A-Z][a-z]+ [A-Z][a-z]+)'s biography", entry)
            if not name_match:
                raise ValueError(f"Name not found in entry: {entry}")
            
            name = name_match.group(1)

            # Tokenize sentences
            sentences = sent_tokenize(entry)

            # Tokenize words and filter out stopwords
            words = [
                word.lower() 
                for sentence in sentences 
                for word in re.findall(r'\b\w+\b', sentence)
                if word.lower() not in stop_words
            ]

            # Compute word frequency for analysis
            word_freq = FreqDist(words)

            # Generate a summary based on the most common words
            most_common_words = [word for word, freq in word_freq.most_common(5)]
            summary = f"{name}'s biography mentions key topics such as: {', '.join(most_common_words)}."

            # Save the summary
            summaries[name] = summary
        
        except Exception as e:
            # Log and skip problematic entries
            print(f"Error processing entry: {entry} - {str(e)}")
    
    return summaries


if __name__ == "__main__":
    # Example text entries
    genealogy_texts = [
        "Thomas Stevens' biography indicates he was a carpenter in the 19th century. He lived in Boston and had three children.",
        "Elizabeth Johnson's biography highlights her role as a teacher. She was born in 1875 and contributed significantly to her local community.",
        "Invalid text example without name's biography header."
    ]
    
    # Parse and analyze text entries
    summaries = parse_biographies(genealogy_texts)
    
    # Print the generated summaries
    for name, summary in summaries.items():
        print(f"{name}: {summary}")
```
