"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Create a Python program to categorize ELISA kits by their diagnostic use cases (e.g., "AFP," "AMH," "Anti NCP IgG") using data similar to MedPointYE's product descriptions.
Generated: DETERMINISTIC_adb7dad1d07b0483
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List

class ELISAKitCategorizer:
    """
    Categorize ELISA kits by their diagnostic use cases.

    Attributes:
    -----------
    categories : Dict[str, List[str]]
        A dictionary of categories and their corresponding keywords.

    Methods:
    --------
    categorize(kit_description: str) -> str
        Categorize an ELISA kit based on its description.
    add_category(category: str, keywords: List[str])
        Add a new category with its corresponding keywords.
    """

    def __init__(self):
        self.categories = {}

    def add_category(self, category: str, keywords: List[str]):
        """
        Add a new category with its corresponding keywords.

        Parameters:
        ----------
        category : str
            The name of the category.
        keywords : List[str]
            A list of keywords for the category.
        """
        self.categories[category] = keywords

    def categorize(self, kit_description: str) -> str:
        """
        Categorize an ELISA kit based on its description.

        Parameters:
        ----------
        kit_description : str
            The description of the ELISA kit.

        Returns:
        -------
        str
            The category of the ELISA kit. If no match is found, returns "Unknown".

        Raises:
        ------
        ValueError
            If the kit description is empty or None.
        """
        if not kit_description:
            raise ValueError("Kit description cannot be empty")

        kit_description = kit_description.lower()
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', kit_description):
                    return category
        return "Unknown"


def main():
    # Initialize the categorizer
    categorizer = ELISAKitCategorizer()

    # Add categories and their keywords
    categorizer.add_category("AFP", ["AFP", "alpha-fetoprotein"])
    categorizer.add_category("AMH", ["AMH", "anti-müllerian hormone"])
    categorizer.add_category("Anti NCP IgG", ["anti-ncp igg", "ncp igg"])

    # Example ELISA kit descriptions
    kit_descriptions = [
        "Human AFP ELISA Kit",
        "Mouse AMH ELISA Kit",
        "Rabbit Anti NCP IgG ELISA Kit",
        "Invalid kit description",
    ]

    # Categorize ELISA kits
    for kit_description in kit_descriptions:
        try:
            category = categorizer.categorize(kit_description)
            print(f"Kit Description: {kit_description}, Category: {category}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
