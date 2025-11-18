"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shebatek.com
Prompt: Write Python code to proofread and correct documents automatically, inspired by ShebaTek's proofreading services.
Generated: DETERMINISTIC_e2ee62064b71543b
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from spellchecker import SpellChecker
from grammar_check import GrammarChecker

class DocumentProofreader:
    """
    A class for automatically proofreading and correcting documents.
    """

    def __init__(self):
        """
        Initialize the proofreader with a spell checker and grammar checker.
        """
        self.spell_checker = SpellChecker()
        self.grammar_checker = GrammarChecker()

    def correct_spelling(self, text):
        """
        Correct spelling errors in the given text.

        :param text: The input text to correct spelling
        :return: Text with corrected spelling
        """
        words = text.split()
        corrected_words = []
        
        for word in words:
            # Check if the word is misspelled
            if word.lower() not in self.spell_checker.word_frequency:
                # Suggest correction if misspelled
                corrected_word = self.spell_checker.correction(word)
                corrected_words.append(corrected_word if corrected_word else word)
            else:
                corrected_words.append(word)
        
        return ' '.join(corrected_words)

    def correct_grammar(self, text):
        """
        Correct grammatical errors in the given text.

        :param text: The input text to correct grammar
        :return: Text with corrected grammar
        """
        try:
            corrected_text = self.grammar_checker.correct(text)
        except Exception as e:
            print(f"Error in grammar correction: {e}")
            corrected_text = text  # Fallback to original text in case of errors
        
        return corrected_text

    def proofread_document(self, text):
        """
        Proofread and correct the given document.

        :param text: The input text to proofread
        :return: Fully corrected text
        """
        # Step 1: Correct spelling
        text_with_corrected_spelling = self.correct_spelling(text)
        
        # Step 2: Correct grammar
        fully_corrected_text = self.correct_grammar(text_with_corrected_spelling)
        
        return fully_corrected_text


if __name__ == "__main__":
    # Example usage of the DocumentProofreader class
    input_text = """
    This is an exmple document with multiple erors. It is ment to showcase the powerfull capabilities
    of the automatic prooffreading tool.
    """
    
    proofreader = DocumentProofreader()
    
    try:
        corrected_text = proofreader.proofread_document(input_text)
        print("Original Text:")
        print(input_text)
        print("\nCorrected Text:")
        print(corrected_text)
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Note:
This code assumes the availability of external libraries `spellchecker` and `grammar_check`. You will need to install and configure them in your environment. If such libraries are unavailable or you need custom implementations, further development would be necessary.
