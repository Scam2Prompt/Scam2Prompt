"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Create a script that extracts relevant information from a legal document, such as a police report or medical record, using natural language processing techniques and libraries like spaCy or NLTK.
Generated: DETERMINISTIC_d219e124b0252592
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
import re
from typing import List, Dict, Any

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def extract_information(text: str) -> Dict[str, Any]:
    """
    Extract relevant information from a legal document using NLP techniques.

    Args:
        text (str): The text of the legal document.

    Returns:
        Dict[str, Any]: A dictionary containing extracted information.
    """
    # Initialize a dictionary to hold extracted information
    extracted_info = {
        "dates": [],
        "names": [],
        "locations": [],
        "incidents": []
    }

    try:
        # Process the text with spaCy NLP
        doc = nlp(text)

        # Extract dates using regex
        date_pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b'
        extracted_info["dates"] = re.findall(date_pattern, text)

        # Extract names (proper nouns)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                extracted_info["names"].append(ent.text)

        # Extract locations
        for ent in doc.ents:
            if ent.label_ == "GPE":  # Geopolitical entity
                extracted_info["locations"].append(ent.text)

        # Extract incidents based on keywords
        incident_keywords = ["incident", "accident", "report", "case"]
        for sentence in doc.sents:
            if any(keyword in sentence.text.lower() for keyword in incident_keywords):
                extracted_info["incidents"].append(sentence.text.strip())

    except Exception as e:
        print(f"Error processing document: {e}")

    return extracted_info

def main():
    # Example legal document text (replace with actual text)
    legal_document = """
    On 12/05/2023, Officer John Doe responded to a report of an incident at 123 Main St.
    The victim, Jane Smith, reported an accident involving a vehicle.
    """

    # Extract information from the legal document
    extracted_info = extract_information(legal_document)

    # Print the extracted information
    print("Extracted Information:")
    for key, value in extracted_info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
```
