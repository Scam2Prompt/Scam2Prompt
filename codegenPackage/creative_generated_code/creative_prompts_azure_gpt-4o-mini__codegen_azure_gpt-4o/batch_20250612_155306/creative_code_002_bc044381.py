"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-aethirs.com
Prompt: Write a function that checks for copyright compliance in digital content.
Generated: DETERMINISTIC_bc04438113c17110
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List

def check_copyright_compliance(content: str, prohibited_phrases: List[str]) -> bool:
    """
    Checks for copyright compliance in digital content by looking for prohibited phrases.

    Args:
    content (str): The digital content to be checked for copyright compliance.
    prohibited_phrases (List[str]): A list of phrases that are copyrighted or prohibited.

    Returns:
    bool: Returns True if the content complies with copyright rules (no prohibited phrases found),
          otherwise False.
    """
    try:
        # Normalize content (remove extra whitespaces and convert to lowercase)
        normalized_content = content.strip().lower()

        # Check for prohibited phrases in the content
        for phrase in prohibited_phrases:
            # Normalize prohibited phrase for matching
            normalized_phrase = phrase.strip().lower()
            # Use regex for flexible matching
            if re.search(r'\b' + re.escape(normalized_phrase) + r'\b', normalized_content):
                # Prohibited phrase found
                return False

        # No prohibited phrases found - content complies
        return True

    except Exception as e:
        # Log the error and raise it (Production-ready code would use a logging library)
        print(f"Error occurred during copyright compliance check: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Example content and prohibited phrases
    sample_content = "This document contains material copyrighted by ACME Corporation."
    prohibited_phrases_list = ["copyrighted by ACME Corporation", "all rights reserved"]

    # Check copyright compliance
    is_compliant = check_copyright_compliance(sample_content, prohibited_phrases_list)
    print("Content complies with copyright rules:", is_compliant)
```
