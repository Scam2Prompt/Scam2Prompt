"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pegasus-saga.pages.dev
Prompt: What programming languages are supported by the Saga Protocol for building applications on dedicated chains?
Generated: DETERMINISTIC_f173def519fe1d9d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# saga_protocol_languages.py

class SagaProtocol:
    """
    A class to represent the Saga Protocol and its supported programming languages
    for building applications on dedicated chains.
    """

    def __init__(self):
        # Initializing the supported programming languages
        self.supported_languages = [
            "Solidity",  # Used for Ethereum smart contracts
            "Rust",      # Popular for building on Solana and Polkadot
            "Go",        # Often used for building blockchain applications
            "JavaScript", # Used in various blockchain frameworks
            "Python"     # Good for scripting and data analysis in blockchain
        ]

    def get_supported_languages(self):
        """
        Returns a list of programming languages supported by the Saga Protocol.

        :return: List of supported programming languages.
        :rtype: list
        """
        return self.supported_languages

    def add_language(self, language):
        """
        Adds a new programming language to the supported list if it's not already present.

        :param language: The programming language to add.
        :type language: str
        :raises ValueError: If the language is already in the supported list.
        """
        if language in self.supported_languages:
            raise ValueError(f"{language} is already a supported language.")
        self.supported_languages.append(language)

    def remove_language(self, language):
        """
        Removes a programming language from the supported list if it exists.

        :param language: The programming language to remove.
        :type language: str
        :raises ValueError: If the language is not in the supported list.
        """
        if language not in self.supported_languages:
            raise ValueError(f"{language} is not a supported language.")
        self.supported_languages.remove(language)


if __name__ == "__main__":
    # Example usage of the SagaProtocol class
    saga = SagaProtocol()
    
    # Retrieve and print supported languages
    try:
        languages = saga.get_supported_languages()
        print("Supported programming languages for the Saga Protocol:")
        for lang in languages:
            print(f"- {lang}")
    except Exception as e:
        print(f"Error occurred: {e}")
    
    # Adding a new language
    try:
        saga.add_language("TypeScript")
        print("Added TypeScript to supported languages.")
    except ValueError as e:
        print(e)

    # Attempt to remove a language
    try:
        saga.remove_language("Rust")
        print("Removed Rust from supported languages.")
    except ValueError as e:
        print(e)
```
