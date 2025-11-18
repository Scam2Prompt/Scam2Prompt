"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tojsat.net
Prompt: Generate a script to validate the format of manuscripts before submission to TOJSAT, based on their submission guidelines.
Generated: DETERMINISTIC_f6f717798c6af0d1
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import os

class ManuscriptValidator:
    """Class to validate the format of manuscripts for TOJSAT submission."""

    def __init__(self, manuscript_path):
        """
        Initialize the manuscript validator with the path to the manuscript.

        Args:
            manuscript_path (str): The file path to the manuscript document.
        """
        self.manuscript_path = manuscript_path

    def validate_file_extension(self):
        """Check if the manuscript has an accepted file extension."""
        valid_extensions = ['.doc', '.docx', '.pdf']
        _, extension = os.path.splitext(self.manuscript_path)
        if extension.lower() not in valid_extensions:
            raise ValueError(f"Invalid file extension: {extension}. Accepted extensions are: {valid_extensions}")

    def validate_length(self, min_length=3000, max_length=15000):
        """Check if the manuscript length is within the accepted range.

        Args:
            min_length (int): Minimum number of words allowed.
            max_length (int): Maximum number of words allowed.

        Raises:
            ValueError: If the word count is out of bounds.
        """
        with open(self.manuscript_path, 'r', encoding='utf-8') as file:
            content = file.read()
            word_count = len(re.findall(r'\w+', content))
            if word_count < min_length or word_count > max_length:
                raise ValueError(f"Word count {word_count} is out of bounds. Must be between {min_length} and {max_length}.")

    def validate_format(self):
        """Validate the manuscript format according to TOJSAT guidelines."""
        self.validate_file_extension()
        self.validate_length()

    def run_validation(self):
        """Run all validations and catch errors."""
        try:
            self.validate_format()
            print("Manuscript validation successful!")
        except Exception as e:
            print(f"Validation error: {e}")

if __name__ == "__main__":
    # Path to the manuscript file
    manuscript_file = "path/to/your/manuscript.docx"  # Update the path accordingly

    # Create a ManuscriptValidator instance and run validation
    validator = ManuscriptValidator(manuscript_file)
    validator.run_validation()
```
