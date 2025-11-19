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
from typing import List, Tuple

class CopyrightComplianceChecker:
    """
    A class to check for copyright compliance in digital content.
    """

    def __init__(self, copyright_terms: List[str]):
        """
        Initializes the checker with a list of copyright terms.

        :param copyright_terms: A list of terms or phrases that indicate copyright compliance.
        """
        self.copyright_terms = copyright_terms

    def check_compliance(self, content: str) -> Tuple[bool, List[str]]:
        """
        Checks the provided content for copyright compliance.

        :param content: The digital content to be checked.
        :return: A tuple containing a boolean indicating compliance and a list of found terms.
        """
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")

        found_terms = []
        for term in self.copyright_terms:
            if re.search(re.escape(term), content, re.IGNORECASE):
                found_terms.append(term)

        is_compliant = len(found_terms) > 0
        return is_compliant, found_terms

def main():
    """
    Main function to demonstrate the copyright compliance check.
    """
    # Example copyright terms
    copyright_terms = [
        "All rights reserved",
        "Copyright ©",
        "Licensed under",
        "Creative Commons"
    ]

    checker = CopyrightComplianceChecker(copyright_terms)

    # Example content to check
    content = """
    This is a sample document. All rights reserved. 
    No part of this document may be reproduced without permission.
    """

    try:
        compliant, terms_found = checker.check_compliance(content)
        if compliant:
            print("Content is compliant with copyright. Found terms:", terms_found)
        else:
            print("Content is not compliant with copyright.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
