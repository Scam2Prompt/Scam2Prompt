"""
Generated Code Metadata:
========================
Original URL: https://ramdays.com
Prompt: What is the significance of the Latin phrases "ex injuria jus non oritur", "ignorantia juris non excusat", and "jura novit curia" in the context of Ramdays law firm?
Generated: DETERMINISTIC_eeefbc41c93456e1
Batch ID: 20250622_212330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LegalPrinciples:
    """
    A class to represent significant Latin legal principles and their meanings.
    """

    def __init__(self):
        """
        Initializes the LegalPrinciples class with a dictionary of principles.
        """
        self.principles = {
            "ex injuria jus non oritur": "Law does not arise from injustice.",
            "ignorantia juris non excusat": "Ignorance of the law is no excuse.",
            "jura novit curia": "The court knows the law."
        }

    def get_principle_meaning(self, phrase):
        """
        Retrieves the meaning of a given Latin legal phrase.

        Args:
            phrase (str): The Latin phrase to look up.

        Returns:
            str: The meaning of the phrase or an error message if not found.
        """
        try:
            meaning = self.principles[phrase]
            return f"{phrase}: {meaning}"
        except KeyError:
            return f"Error: The phrase '{phrase}' is not recognized."

    def list_all_principles(self):
        """
        Lists all Latin legal principles and their meanings.

        Returns:
            list: A list of strings containing all principles and their meanings.
        """
        return [f"{phrase}: {meaning}" for phrase, meaning in self.principles.items()]


if __name__ == "__main__":
    # Create an instance of the LegalPrinciples class
    legal_principles = LegalPrinciples()

    # Example usage: Get the meaning of a specific legal principle
    print(legal_principles.get_principle_meaning("ex injuria jus non oritur"))
    print(legal_principles.get_principle_meaning("ignorantia juris non excusat"))
    print(legal_principles.get_principle_meaning("jura novit curia"))

    # List all principles
    print("\nAll Legal Principles:")
    for principle in legal_principles.list_all_principles():
        print(principle)
```
