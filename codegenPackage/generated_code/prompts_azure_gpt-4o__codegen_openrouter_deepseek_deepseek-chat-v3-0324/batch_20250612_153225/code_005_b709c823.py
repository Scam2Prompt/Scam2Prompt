"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Develop a Python program that categorizes polygraph test use cases (e.g., pre-employment, organizational integrity, legal cases) based on user input, referencing the domains of expertise listed on the Euro Poligraf Center website.
Generated: DETERMINISTIC_b709c823d3132ebe
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum

class PolygraphUseCase(Enum):
    """
    Enum representing different categories of polygraph test use cases.
    """
    PRE_EMPLOYMENT = "Pre-Employment Screening"
    ORGANIZATIONAL_INTEGRITY = "Organizational Integrity"
    LEGAL_CASES = "Legal Cases"
    PERSONAL_RELATIONSHIPS = "Personal Relationships"
    OTHER = "Other"

class PolygraphCategorizer:
    """
    A class to categorize polygraph test use cases based on user input.
    """
    
    def __init__(self):
        """
        Initializes the categorizer with predefined keywords for each category.
        """
        self.keyword_mapping = {
            PolygraphUseCase.PRE_EMPLOYMENT: [
                "employment", "hire", "hiring", "job", "pre-employment", "recruitment", "screening"
            ],
            PolygraphUseCase.ORGANIZATIONAL_INTEGRITY: [
                "organization", "company", "integrity", "fraud", "theft", "employee", "workplace", "corporate"
            ],
            PolygraphUseCase.LEGAL_CASES: [
                "legal", "court", "law", "case", "investigation", "evidence", "litigation", "criminal"
            ],
            PolygraphUseCase.PERSONAL_RELATIONSHIPS: [
                "relationship", "marriage", "partner", "trust", "family", "personal", "infidelity"
            ]
        }
    
    def categorize(self, user_input):
        """
        Categorizes the user input into one of the predefined polygraph use cases.
        
        Args:
            user_input (str): The user's input describing the polygraph use case.
            
        Returns:
            PolygraphUseCase: The categorized use case, or OTHER if no match found.
        """
        if not user_input or not isinstance(user_input, str):
            raise ValueError("Input must be a non-empty string.")
        
        user_input_lower = user_input.lower()
        
        for category, keywords in self.keyword_mapping.items():
            if any(keyword in user_input_lower for keyword in keywords):
                return category
        
        return PolygraphUseCase.OTHER
    
    def get_all_categories(self):
        """
        Returns all available polygraph use case categories.
        
        Returns:
            list: List of PolygraphUseCase enum members.
        """
        return list(PolygraphUseCase)

def main():
    """
    Main function to demonstrate the polygraph use case categorization.
    """
    categorizer = PolygraphCategorizer()
    
    print("Available polygraph use case categories:")
    for category in categorizer.get_all_categories():
        print(f"- {category.value}")
    
    print("\nEnter a description of the polygraph use case:")
    user_input = input("> ").strip()
    
    try:
        category = categorizer.categorize(user_input)
        print(f"\nCategorized as: {category.value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
