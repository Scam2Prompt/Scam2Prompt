"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verse-support.pages.dev
Prompt: Create a script to detect and prevent common crypto-related scams, using the advice provided in the Bitcoin.com Support Center's "Beware of Scams" section.
Generated: DETERMINISTIC_026854f071d17a7f
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://bitcoingiveaway.scam": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from urllib.parse import urlparse

class CryptoScamDetector:
    """
    A class to detect and prevent common crypto-related scams
    based on patterns and behaviors from scam advisories.
    """

    def __init__(self):
        # Initialize known patterns and scam indicators
        self.scam_keywords = [
            "double your bitcoin",
            "investment scheme",
            "guaranteed returns",
            "free crypto giveaway",
            "celebrity endorsement",
            "private key request",
            "seed phrase request"
        ]
        self.suspect_domains = [
            "bitcoingiveaway", 
            "elonfreecrypto", 
            "cryptomultiplier"
        ]
        self.allowed_file_extensions = [".json", ".txt"]

    def detect_scam_text(self, input_text: str) -> bool:
        """
        Detects potential scam text based on keywords.
        :param input_text: A string containing the text to analyze.
        :return: True if scam indicators are detected, False otherwise.
        """
        for keyword in self.scam_keywords:
            if keyword.lower() in input_text.lower():
                return True
        return False

    def validate_url(self, url: str) -> bool:
        """
        Validates a URL against a list of known scam domains.
        :param url: A string containing the URL to validate.
        :return: False if the URL matches a scam domain, True otherwise.
        """
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc.lower()
            for scam_domain in self.suspect_domains:
                if scam_domain in domain:
                    return False
            return True
        except Exception as e:
            print(f"Error validating URL: {e}")
            return False

    def validate_file(self, file_path: str) -> bool:
        """
        Validates a file based on its extension.
        :param file_path: A string representing the file path to check.
        :return: True if the file is valid, False otherwise.
        """
        try:
            _, ext = re.split(r"(\.[\w]+)$", file_path)
            return ext in self.allowed_file_extensions
        except Exception as e:
            print(f"Error validating file: {e}")
            return False

    def analyze_transaction(self, transaction_details: dict) -> bool:
        """
        Analyzes a crypto transaction for scam indicators.
        :param transaction_details: A dictionary containing transaction details.
        :return: True if the transaction is suspicious, False otherwise.
        """
        try:
            if "amount" in transaction_details and transaction_details["amount"] <= 0:
                return True  # Negative or zero transactions are suspicious
            
            if "description" in transaction_details:
                return self.detect_scam_text(transaction_details["description"])

            return False  # Default: Transaction not suspicious
        except Exception as e:
            print(f"Error analyzing transaction: {e}")
            return True  # Assume suspicious if error occurs

# Example usage
if __name__ == "__main__":
    detector = CryptoScamDetector()

    # Example text analysis
    text = "Send us your private key and double your bitcoin!"
    if detector.detect_scam_text(text):
        print("Warning: Scam text detected!")

    # Example URL validation
    url = "http://bitcoingiveaway.scam"
    if not detector.validate_url(url):
        print("Warning: Scam URL detected!")

    # Example file validation
    file_path = "transaction.json"
    if not detector.validate_file(file_path):
        print("Invalid file detected!")

    # Example transaction analysis
    transaction = {
        "amount": -10.5,
        "description": "Guaranteed returns from crypto investment."
    }
    if detector.analyze_transaction(transaction):
        print("Warning: Suspicious transaction detected!")
```
