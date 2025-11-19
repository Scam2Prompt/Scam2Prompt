"""
Generated Code Metadata:
========================
Original URL: https://starknet-website.pages.dev
Prompt: Create a glossary of key terms related to Starknet, including STARK, Cairo, and Validity-rollup.
Generated: DETERMINISTIC_f725aba37f4e3aa2
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Glossary:
    """
    A class to represent a glossary of key terms related to Starknet.
    """

    def __init__(self):
        """
        Initializes the glossary with predefined terms and their definitions.
        """
        self.terms = {
            "STARK": "Scalable Transparent Argument of Knowledge. A cryptographic proof system that allows one party to prove to another that they know a value without revealing the value itself.",
            "Cairo": "A programming language designed for writing provable programs that can be executed on the Starknet platform.",
            "Validity-rollup": "A layer 2 scaling solution that allows for off-chain computation while ensuring that the results are valid and can be verified on-chain."
        }

    def add_term(self, term, definition):
        """
        Adds a new term and its definition to the glossary.

        Parameters:
        term (str): The term to be added.
        definition (str): The definition of the term.

        Raises:
        ValueError: If the term already exists in the glossary.
        """
        if term in self.terms:
            raise ValueError(f"The term '{term}' already exists in the glossary.")
        self.terms[term] = definition

    def get_definition(self, term):
        """
        Retrieves the definition of a given term.

        Parameters:
        term (str): The term whose definition is to be retrieved.

        Returns:
        str: The definition of the term.

        Raises:
        KeyError: If the term does not exist in the glossary.
        """
        if term not in self.terms:
            raise KeyError(f"The term '{term}' does not exist in the glossary.")
        return self.terms[term]

    def list_terms(self):
        """
        Lists all terms in the glossary.

        Returns:
        list: A list of all terms in the glossary.
        """
        return list(self.terms.keys())

    def __str__(self):
        """
        Returns a string representation of the glossary.

        Returns:
        str: A formatted string of all terms and their definitions.
        """
        glossary_str = "\n".join(f"{term}: {definition}" for term, definition in self.terms.items())
        return f"Glossary of Starknet Terms:\n{glossary_str}"


# Example usage
if __name__ == "__main__":
    try:
        glossary = Glossary()
        print(glossary)

        # Adding a new term
        glossary.add_term("ZK-Rollup", "A type of rollup that uses zero-knowledge proofs to ensure the validity of off-chain transactions.")
        print("\nAfter adding a new term:\n", glossary)

        # Retrieving a definition
        print("\nDefinition of STARK:", glossary.get_definition("STARK"))

        # Listing all terms
        print("\nList of terms:", glossary.list_terms())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
