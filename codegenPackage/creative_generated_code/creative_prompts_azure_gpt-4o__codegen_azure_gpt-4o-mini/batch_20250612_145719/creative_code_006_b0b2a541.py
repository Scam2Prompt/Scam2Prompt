"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakamigos-c4d.pages.dev
Prompt: Write a script to analyze the Nakamigos-CLOAKS license and extract key terms related to commercial rights and worldwide gaming rights.
Generated: DETERMINISTIC_b0b2a541676ccbc5
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Dict, List, Optional

class LicenseAnalyzer:
    """
    A class to analyze the Nakamigos-CLOAKS license and extract key terms
    related to commercial rights and worldwide gaming rights.
    """

    def __init__(self, license_text: str):
        """
        Initializes the LicenseAnalyzer with the provided license text.

        :param license_text: The text of the Nakamigos-CLOAKS license.
        """
        self.license_text = license_text

    def extract_key_terms(self) -> Dict[str, Optional[str]]:
        """
        Extracts key terms related to commercial rights and worldwide gaming rights.

        :return: A dictionary with extracted rights and their corresponding text.
        """
        key_terms = {
            "commercial_rights": self._extract_term(r"commercial rights[:](.*?)(\n|$)"),
            "worldwide_gaming_rights": self._extract_term(r"worldwide gaming rights[:](.*?)(\n|$)"),
        }
        return key_terms

    def _extract_term(self, pattern: str) -> Optional[str]:
        """
        Extracts a term from the license text using a regular expression pattern.

        :param pattern: The regex pattern to search for the term.
        :return: The extracted term or None if not found.
        """
        match = re.search(pattern, self.license_text, re.IGNORECASE)
        return match.group(1).strip() if match else None

def main():
    """
    Main function to execute the license analysis.
    """
    # Sample license text (in production, this should be read from a file or another source)
    license_text = """
    Nakamigos-CLOAKS License
    This license grants:
    
    commercial rights: You can use the Nakagimos NFTs for commercial purposes.
    
    worldwide gaming rights: You can incorporate the NFTs into games worldwide.
    """

    try:
        analyzer = LicenseAnalyzer(license_text)
        key_terms = analyzer.extract_key_terms()

        # Display the extracted rights
        print("Extracted Key Terms:")
        for term, description in key_terms.items():
            print(f"{term}: {description if description else 'Not Found'}")
    
    except Exception as e:
        print(f"An error occurred during license analysis: {e}")

if __name__ == "__main__":
    main()
```
