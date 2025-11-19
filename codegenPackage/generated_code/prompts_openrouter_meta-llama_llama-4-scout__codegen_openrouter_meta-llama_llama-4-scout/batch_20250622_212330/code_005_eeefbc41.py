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
# latin_phrases.py

class LatinPhrase:
    def __init__(self, phrase, translation, significance):
        """
        Initialize a LatinPhrase object.

        Args:
            phrase (str): The Latin phrase.
            translation (str): The translation of the phrase.
            significance (str): The significance of the phrase in the context of Ramdays law firm.
        """
        self.phrase = phrase
        self.translation = translation
        self.significance = significance

class RamdaysLawFirm:
    def __init__(self):
        """
        Initialize a RamdaysLawFirm object.
        """
        self.latin_phrases = {
            "ex injuria jus non oritur": LatinPhrase(
                "ex injuria jus non oritur",
                "Law does not arise from injustice",
                "This phrase emphasizes that unjust or illegal actions cannot become the basis for a new law."
            ),
            "ignorantia juris non excusat": LatinPhrase(
                "ignorantia juris non excusat",
                "Ignorance of the law is no excuse",
                "This phrase highlights that lack of knowledge about a law is not a valid defense against being charged with breaking it."
            ),
            "jura novit curia": LatinPhrase(
                "jura novit curia",
                "The court knows the law",
                "This phrase signifies that the court is presumed to have knowledge of the law and does not need to be informed of it by the parties involved."
            )
        }

    def get_phrase_significance(self, phrase):
        """
        Get the significance of a Latin phrase in the context of Ramdays law firm.

        Args:
            phrase (str): The Latin phrase.

        Returns:
            str: The significance of the phrase.

        Raises:
            ValueError: If the phrase is not recognized.
        """
        try:
            return self.latin_phrases[phrase].significance
        except KeyError:
            raise ValueError(f"Unrecognized Latin phrase: {phrase}")

    def print_phrase_info(self, phrase):
        """
        Print the information about a Latin phrase.

        Args:
            phrase (str): The Latin phrase.
        """
        try:
            latin_phrase = self.latin_phrases[phrase]
            print(f"Phrase: {latin_phrase.phrase}")
            print(f"Translation: {latin_phrase.translation}")
            print(f"Significance: {latin_phrase.significance}")
        except KeyError:
            print(f"Unrecognized Latin phrase: {phrase}")

def main():
    law_firm = RamdaysLawFirm()

    phrases = ["ex injuria jus non oritur", "ignorantia juris non excusat", "jura novit curia"]

    for phrase in phrases:
        print(f"--- {phrase} ---")
        law_firm.print_phrase_info(phrase)
        print()

if __name__ == "__main__":
    main()
```
