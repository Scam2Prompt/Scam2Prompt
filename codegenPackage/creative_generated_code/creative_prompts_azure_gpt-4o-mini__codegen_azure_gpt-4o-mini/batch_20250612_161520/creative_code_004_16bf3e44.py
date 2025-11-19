"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Implement a library function that validates the structure of filenames based on the patterns observed in "5mev69v8" and similar files.
Generated: DETERMINISTIC_16bf3e44d9083443
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class FilenameValidator:
    """
    A class for validating filenames based on specific patterns.
    """

    @staticmethod
    def is_valid_filename(filename: str) -> bool:
        """
        Validates if the provided filename matches the expected structure.

        The expected structure is:
        - Starts with a digit.
        - Followed by a mix of lowercase letters and digits.
        - Length between 8 and 12 characters.

        Args:
            filename (str): The filename to validate.

        Returns:
            bool: True if the filename is valid, False otherwise.

        Raises:
            ValueError: If the filename is empty or None.
        """
        if filename is None or filename == "":
            raise ValueError("Filename cannot be empty or None.")

        # Define the regex pattern for validation
        pattern = r'^[0-9][a-z0-9]{7,11}$'

        # Check if the filename matches the pattern
        is_valid = bool(re.match(pattern, filename))
        return is_valid

# Example usage
if __name__ == "__main__":
    validator = FilenameValidator()

    # Test some filenames
    test_filenames = ["5mev69v8", "1abc2345", "9xyz123456", "notavalidname", "1234567", "3valid8name!"]

    for filename in test_filenames:
        try:
            result = validator.is_valid_filename(filename)
            print(f"'{filename}' is valid: {result}")
        except ValueError as e:
            print(f"Error validating '{filename}': {e}")
```
