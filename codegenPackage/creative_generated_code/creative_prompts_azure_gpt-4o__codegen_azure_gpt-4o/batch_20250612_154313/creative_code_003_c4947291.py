"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-limited.com
Prompt: Provide a Python implementation for detecting and marking personal sensitive information in user data, as described in STELLAR TECHNOLOGY LIMITED's privacy policy.
Generated: DETERMINISTIC_c494729100a8a9c0
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict, Tuple

class SensitiveDataDetector:
    """
    A class for detecting and marking personal sensitive information (PII) 
    in user data based on predefined patterns.
    """

    def __init__(self):
        # Define regex patterns for various types of sensitive information
        self.patterns = {
            "email": re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
            "phone_number": re.compile(r"\b(?:\+?[\d]{1,3})?\s?(?:[\(\[\{]?[0-9]{1,4}[\)\]\}]?)?[\s.-]?[0-9]{1,4}[\s.-]?[0-9]{1,4}[\s.-]?[0-9]{1,9}\b"),
            "credit_card": re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b"),
            "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),  # US Social Security Number
        }

        # Replace text used for masking detected sensitive information
        self.masking_template = "[REDACTED_{type}]"

    def detect_sensitive_data(self, text: str) -> List[Tuple[str, str]]:
        """
        Detect sensitive information in the provided text.

        Args:
            text (str): The input text to scan.

        Returns:
            List[Tuple[str, str]]: A list of tuples containing the type of sensitive data
                                   and the detected value.
        """
        detected_data = []
        for data_type, pattern in self.patterns.items():
            matches = pattern.findall(text)
            detected_data.extend([(data_type, match) for match in matches])
        return detected_data

    def mask_sensitive_data(self, text: str) -> str:
        """
        Mask sensitive information in the provided text.

        Args:
            text (str): The input text to process.

        Returns:
            str: Text with sensitive information masked.
        """
        for data_type, pattern in self.patterns.items():
            text = pattern.sub(self.masking_template.format(type=data_type.upper()), text)
        return text

# Error handling utility function
def validate_input(text: str) -> None:
    """
    Validate the input text to ensure it is a string.

    Args:
        text (str): The input text to validate.

    Raises:
        ValueError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

if __name__ == "__main__":
    # Example usage
    try:
        # Input text containing sensitive information
        user_data = """
        John Doe's email is johndoe@example.com, and his phone number is +1-234-567-8901.
        His credit card details are 1234-5678-9012-3456, and his SSN is 123-45-6789.
        """

        # Validate input
        validate_input(user_data)

        # Initialize detector
        detector = SensitiveDataDetector()

        # Detect sensitive information
        detected_info = detector.detect_sensitive_data(user_data)
        print("Detected Sensitive Information:")
        for data_type, value in detected_info:
            print(f"Type: {data_type}, Value: {value}")

        # Mask sensitive information
        masked_text = detector.mask_sensitive_data(user_data)
        print("\nMasked Text:")
        print(masked_text)

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
```
