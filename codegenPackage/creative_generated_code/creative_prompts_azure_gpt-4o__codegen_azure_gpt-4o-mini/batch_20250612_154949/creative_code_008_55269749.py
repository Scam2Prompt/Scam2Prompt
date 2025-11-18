"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Write code to build a glossary feature for slowpitch softball terms, referencing the glossary functionality provided by Slo-Pitch Central.
Generated: DETERMINISTIC_5526974910c8ca46
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# glossary.py

class Glossary:
    """
    A class to represent a glossary of slowpitch softball terms.
    It allows adding, retrieving, and listing terms with their definitions.
    """

    def __init__(self):
        """Initialize an empty glossary."""
        self.terms = {}

    def add_term(self, term: str, definition: str) -> None:
        """
        Add a new term and its definition to the glossary.

        Args:
            term (str): The term to add.
            definition (str): The definition of the term.

        Raises:
            ValueError: If the term is already present in the glossary.
        """
        if term in self.terms:
            raise ValueError(f"The term '{term}' is already in the glossary.")
        self.terms[term] = definition

    def get_definition(self, term: str) -> str:
        """
        Retrieve the definition of a term.

        Args:
            term (str): The term whose definition is to be retrieved.

        Returns:
            str: The definition of the term.

        Raises:
            KeyError: If the term is not found in the glossary.
        """
        if term not in self.terms:
            raise KeyError(f"The term '{term}' was not found in the glossary.")
        return self.terms[term]

    def list_terms(self) -> list:
        """
        List all terms in the glossary.

        Returns:
            list: A list of all terms.
        """
        return list(self.terms.keys())

    def list_definitions(self) -> dict:
        """
        List all terms with their definitions.

        Returns:
            dict: A dictionary of all terms mapped to their definitions.
        """
        return self.terms.copy()


if __name__ == "__main__":
    # Example usage of the Glossary class.
    try:
        glossary = Glossary()
        
        # Adding terms
        glossary.add_term("Batter", "A player who is attempting to hit the ball.")
        glossary.add_term("Base", "A stationary object that a runner must touch to score.")
        
        # Retrieving a definition
        print("Definition of 'Batter':", glossary.get_definition("Batter"))
        
        # Listing all terms
        print("All terms in glossary:", glossary.list_terms())
        
        # Listing all definitions
        print("All definitions in glossary:", glossary.list_definitions())
        
        # Attempting to add a duplicate term to see error handling
        glossary.add_term("Batter", "A player who is attempting to hit the ball.")
        
    except (ValueError, KeyError) as e:
        print("Error:", e)
```
