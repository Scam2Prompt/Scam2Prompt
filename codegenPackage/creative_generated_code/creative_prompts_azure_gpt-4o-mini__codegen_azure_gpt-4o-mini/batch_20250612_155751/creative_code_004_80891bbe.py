"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xbank.plus
Prompt: Describe how to design a custom tokenization strategy based on xBank's consultancy and design services for financial markets.
Generated: DETERMINISTIC_80891bbebafdddd0
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Tuple, Dict

class CustomTokenizer:
    """
    A class to implement a custom tokenization strategy for financial texts.
    This tokenizer is designed to handle typical constructs in financial documents.
    """

    def __init__(self):
        # Define a pattern for tokenizing financial terms, numbers, and punctuation
        self.pattern = r'\s*(?:(\d+(?:\.\d+)?)|([A-Za-z]+)|([^A-Za-z0-9\s]))\s*'

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenizes the input text into a list of tokens.
        
        Parameters:
            text (str): The input string to tokenize.

        Returns:
            List[str]: A list of identified tokens.

        Raises:
            ValueError: If the input text is empty.
        """
        if not text:
            raise ValueError("Input text cannot be empty!")

        tokens = []
        # Use re.findall to extract tokens based on the defined pattern
        for match in re.findall(self.pattern, text):
            # match[0] is the number, match[1] is the word, match[2] is the punctuation
            # Filter out empty matches and append the relevant tokens to the list
            tokens.extend(filter(None, match))
        
        return tokens

    def analyze_tokens(self, tokens: List[str]) -> Dict[str, int]:
        """
        Analyzes the list of tokens and counts occurrences of each token.
        
        Parameters:
            tokens (List[str]): The list of tokens to analyze.

        Returns:
            Dict[str, int]: A dictionary with tokens as keys and their counts as values.
        """
        token_count = {}
        for token in tokens:
            token_count[token] = token_count.get(token, 0) + 1
        
        return token_count

def main():
    """
    Main function to demonstrate the tokenization process.
    """
    # Example financial text for tokenization
    financial_text = "The stock price of xBank rose by 15.5% yesterday, reaching $120.5."

    # Create an instance of the custom tokenizer
    tokenizer = CustomTokenizer()

    try:
        # Tokenizing the financial text
        tokens = tokenizer.tokenize(financial_text)
        print("Tokens:", tokens)

        # Analyzing the token occurrences
        token_analysis = tokenizer.analyze_tokens(tokens)
        print("Token Analysis:", token_analysis)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
