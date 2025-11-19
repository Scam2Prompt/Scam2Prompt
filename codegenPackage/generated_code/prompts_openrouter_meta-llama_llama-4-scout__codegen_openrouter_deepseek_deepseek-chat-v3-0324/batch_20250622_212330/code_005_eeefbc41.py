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
# Legal Latin Phrases Analyzer for Ramdays Law Firm

class LegalLatinPhrases:
    """
    A class to encapsulate the meanings and significance of Latin legal phrases
    relevant to Ramdays law firm's practice.
    """
    
    def __init__(self):
        self.phrases = {
            "ex injuria jus non oritur": {
                "translation": "Law does not arise from injustice",
                "significance": "Prevents wrongful acts from creating legal rights",
                "application": "Used in cases of illegal occupation or unjust enrichment"
            },
            "ignorantia juris non excusat": {
                "translation": "Ignorance of the law excuses not",
                "significance": "Individuals cannot avoid liability by claiming unawareness of law",
                "application": "Applied in criminal and civil liability cases"
            },
            "jura novit curia": {
                "translation": "The court knows the law",
                "significance": "Court is responsible for correct application of law",
                "application": "Used when parties may not have cited correct legal provisions"
            }
        }
    
    def get_phrase_info(self, phrase: str) -> dict:
        """
        Retrieves information about a specific Latin legal phrase.
        
        Args:
            phrase (str): The Latin phrase to look up
            
        Returns:
            dict: Dictionary containing translation, significance, and application
            or None if phrase not found
        """
        return self.phrases.get(phrase.lower(), None)
    
    def list_all_phrases(self) -> list:
        """
        Returns all Latin phrases stored in the system.
        
        Returns:
            list: All available Latin phrases
        """
        return list(self.phrases.keys())
    
    def add_custom_phrase(self, latin: str, translation: str, significance: str, application: str) -> bool:
        """
        Adds a custom Latin legal phrase to the collection.
        
        Args:
            latin (str): The Latin phrase
            translation (str): English translation
            significance (str): Legal significance
            application (str): Practical application
            
        Returns:
            bool: True if successfully added, False if phrase already exists
        """
        if latin.lower() in self.phrases:
            return False
            
        self.phrases[latin.lower()] = {
            "translation": translation,
            "significance": significance,
            "application": application
        }
        return True


# Example usage
if __name__ == "__main__":
    legal_phrases = LegalLatinPhrases()
    
    # Get information about a specific phrase
    phrase_info = legal_phrases.get_phrase_info("ignorantia juris non excusat")
    print(phrase_info)
    
    # List all available phrases
    all_phrases = legal_phrases.list_all_phrases()
    print(all_phrases)
```
