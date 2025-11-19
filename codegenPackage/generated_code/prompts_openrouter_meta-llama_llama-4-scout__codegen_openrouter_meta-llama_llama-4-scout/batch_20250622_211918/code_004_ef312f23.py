"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Develop a code snippet to automate the extraction of key terms and renewal dates from legal agreements using AI-powered tools.
Generated: DETERMINISTIC_ef312f23f4fb5af6
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re
import spacy
from spacy.util import minibatch, compounding
from dateutil.parser import parse
from typing import List, Tuple

# Load the spacy model for natural language processing
nlp = spacy.load('en_core_web_sm')

def extract_key_terms(text: str) -> List[str]:
    """
    Extract key terms from a given text using spacy's noun chunks.

    Args:
    text (str): The input text.

    Returns:
    List[str]: A list of extracted key terms.
    """
    # Process the text using spacy
    doc = nlp(text)

    # Extract noun chunks
    key_terms = [chunk.text for chunk in doc.noun_chunks]

    return key_terms

def extract_renewal_dates(text: str) -> List[Tuple[str, str]]:
    """
    Extract renewal dates from a given text using regular expressions.

    Args:
    text (str): The input text.

    Returns:
    List[Tuple[str, str]]: A list of extracted renewal dates with their corresponding terms.
    """
    # Define a regular expression pattern for dates
    date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b \d{1,2}, \d{4}'

    # Find all dates in the text
    dates = re.findall(date_pattern, text)

    # Initialize an empty list to store the extracted renewal dates
    renewal_dates = []

    # Iterate over the dates
    for date in dates:
        try:
            # Parse the date
            parsed_date = parse(date)

            # Extract the term associated with the date (assuming it's the preceding noun chunk)
            doc = nlp(text)
            for token in doc:
                if token.text == date:
                    term = ''
                    for prev_token in doc:
                        if prev_token.dep_ == 'appos' or prev_token.dep_ == 'compound':
                            term = prev_token.text + ' ' + term
                    renewal_dates.append((term.strip(), date))
        except Exception as e:
            # Handle any exceptions during date parsing
            print(f"Error parsing date: {e}")

    return renewal_dates

def analyze_legal_agreement(text: str) -> dict:
    """
    Analyze a legal agreement and extract key terms and renewal dates.

    Args:
    text (str): The input text.

    Returns:
    dict: A dictionary containing the extracted key terms and renewal dates.
    """
    try:
        # Extract key terms
        key_terms = extract_key_terms(text)

        # Extract renewal dates
        renewal_dates = extract_renewal_dates(text)

        # Return the extracted information
        return {
            'key_terms': key_terms,
            'renewal_dates': renewal_dates
        }
    except Exception as e:
        # Handle any exceptions during analysis
        print(f"Error analyzing agreement: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    text = """
    This Agreement shall commence on January 1, 2022, and shall continue for a period of two (2) years. 
    Upon expiration of the initial term, this Agreement shall automatically renew for additional one (1) year terms unless terminated by either party with written notice of at least sixty (60) days.
    """

    analysis_result = analyze_legal_agreement(text)

    print("Key Terms:")
    for term in analysis_result['key_terms']:
        print(term)

    print("\nRenewal Dates:")
    for term, date in analysis_result['renewal_dates']:
        print(f"{term}: {date}")
```
