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
from spacy.matcher import Matcher
import re
from typing import Dict, List, Optional, Tuple

# Load the English language model
nlp = spacy.load("en_core_web_sm")

class LegalDocumentParser:
    """
    A class to parse legal documents and extract relevant information.
    """
    
    def __init__(self):
        self.nlp = nlp
        self.matcher = Matcher(nlp.vocab)
        self._initialize_patterns()
    
    def _initialize_patterns(self) -> None:
        """Initialize patterns for matching relevant information."""
        # Patterns for dates
        date_pattern = [
            {"IS_DIGIT": True, "LENGTH": 4},  # Year
            {"ORTH": "-"},
            {"IS_DIGIT": True, "LENGTH": 2},  # Month
            {"ORTH": "-"},
            {"IS_DIGIT": True, "LENGTH": 2}   # Day
        ]
        self.matcher.add("DATE", [date_pattern])
        
        # Patterns for names (simple version)
        name_pattern = [
            {"POS": "PROPN", "OP": "+"},
            {"POS": "PROPN", "OP": "*"}
        ]
        self.matcher.add("NAME", [name_pattern])
        
        # Patterns for locations
        location_pattern = [
            {"ENT_TYPE": "GPE", "OP": "+"},
            {"ENT_TYPE": "LOC", "OP": "*"}
        ]
        self.matcher.add("LOCATION", [location_pattern])
    
    def _extract_dates(self, text: str) -> List[str]:
        """Extract dates from text using regex."""
        date_regex = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b"
        return re.findall(date_regex, text)
    
    def _process_matches(self, doc) -> Dict[str, List[str]]:
        """Process matches found by the matcher."""
        matches = self.matcher(doc)
        results = {
            "dates": [],
            "names": [],
            "locations": []
        }
        
        for match_id, start, end in matches:
            span = doc[start:end]
            label = self.nlp.vocab.strings[match_id]
            
            if label == "DATE":
                results["dates"].append(span.text)
            elif label == "NAME":
                results["names"].append(span.text)
            elif label == "LOCATION":
                results["locations"].append(span.text)
        
        return results
    
    def parse_document(self, document_text: str) -> Dict[str, List[str]]:
        """
        Parse a legal document and extract relevant information.
        
        Args:
            document_text: The text content of the legal document
            
        Returns:
            A dictionary containing extracted information with keys:
            - dates: List of dates found
            - names: List of names found
            - locations: List of locations found
        """
        try:
            if not document_text or not isinstance(document_text, str):
                raise ValueError("Document text must be a non-empty string")
            
            doc = self.nlp(document_text)
            
            # Extract using matcher
            matcher_results = self._process_matches(doc)
            
            # Extract using regex (for dates)
            regex_dates = self._extract_dates(document_text)
            
            # Combine results
            combined_results = {
                "dates": list(set(matcher_results["dates"] + regex_dates)),
                "names": list(set(matcher_results["names"])),
                "locations": list(set(matcher_results["locations"]))
            }
            
            return combined_results
            
        except Exception as e:
            print(f"Error parsing document: {str(e)}")
            return {
                "dates": [],
                "names": [],
                "locations": []
            }

# Example usage
if __name__ == "__main__":
    parser = LegalDocumentParser()
    sample_text = """
    Police Report - Case #12345
    Date: 2023-10-15
    Officer: John Smith
    Location: New York City Police Department
    
    Incident occurred on 10/14/2023 at approximately 3:45 PM near Central Park.
    Involved parties: Alice Johnson and Bob Williams.
    """
    
    results = parser.parse_document(sample_text)
    print("Extracted Information:")
    print(f"Dates: {results['dates']}")
    print(f"Names: {results['names']}")
    print(f"Locations: {results['locations']}")
```
