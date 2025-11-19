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
"""
Starknet Glossary Module

This module provides a glossary of key terms related to Starknet, 
including STARK, Cairo, and Validity-rollup.

Classes:
    Glossary

Exceptions:
    InvalidTermError
"""

class InvalidTermError(Exception):
    """Raised when an invalid term is provided"""
    pass


class Glossary:
    """
    A class representing a glossary of key terms related to Starknet.

    Attributes:
        terms (dict): A dictionary of key terms and their descriptions.
    """

    def __init__(self):
        """
        Initializes the Glossary object with a set of predefined terms.
        """
        self.terms = {
            "STARK": "Scalable Transparent Argument of Knowledge, a type of zero-knowledge proof.",
            "Cairo": "A programming language used for writing smart contracts on Starknet.",
            "Validity-rollup": "A type of rollup that uses validity proofs to ensure the correctness of transactions."
        }

    def get_term(self, term):
        """
        Retrieves the description of a specific term.

        Args:
            term (str): The term to look up.

        Returns:
            str: The description of the term.

        Raises:
            InvalidTermError: If the term is not found in the glossary.
        """
        try:
            return self.terms[term]
        except KeyError:
            raise InvalidTermError(f"Term '{term}' not found in glossary.")

    def add_term(self, term, description):
        """
        Adds a new term to the glossary.

        Args:
            term (str): The term to add.
            description (str): The description of the term.
        """
        self.terms[term] = description

    def update_term(self, term, description):
        """
        Updates the description of an existing term.

        Args:
            term (str): The term to update.
            description (str): The new description of the term.

        Raises:
            InvalidTermError: If the term is not found in the glossary.
        """
        try:
            self.terms[term] = description
        except KeyError:
            raise InvalidTermError(f"Term '{term}' not found in glossary.")

    def delete_term(self, term):
        """
        Deletes a term from the glossary.

        Args:
            term (str): The term to delete.

        Raises:
            InvalidTermError: If the term is not found in the glossary.
        """
        try:
            del self.terms[term]
        except KeyError:
            raise InvalidTermError(f"Term '{term}' not found in glossary.")


def main():
    glossary = Glossary()

    # Test getting a term
    print(glossary.get_term("STARK"))

    # Test adding a new term
    glossary.add_term("ZK-proof", "A type of cryptographic proof that demonstrates knowledge of a secret without revealing it.")
    print(glossary.get_term("ZK-proof"))

    # Test updating a term
    glossary.update_term("Cairo", "A programming language used for writing smart contracts on Starknet, and also a city in Egypt.")
    print(glossary.get_term("Cairo"))

    # Test deleting a term
    glossary.delete_term("ZK-proof")
    try:
        print(glossary.get_term("ZK-proof"))
    except InvalidTermError as e:
        print(e)


if __name__ == "__main__":
    main()
```
