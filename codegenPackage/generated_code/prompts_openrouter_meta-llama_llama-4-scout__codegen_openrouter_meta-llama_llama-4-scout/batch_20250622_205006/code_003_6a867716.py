"""
Generated Code Metadata:
========================
Original URL: https://dev-node-26u.pages.dev
Prompt: Develop a function to validate user-generated content on a DApp or server, ensuring compliance with a predefined set of rules and regulations.
Generated: DETERMINISTIC_6a8677167963b3b0
Batch ID: 20250622_205006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List

class ValidationRule:
    """Represents a validation rule with a name and a validation function."""
    
    def __init__(self, name: str, func):
        """
        Initializes a ValidationRule instance.

        Args:
        - name (str): The name of the validation rule.
        - func: A function that takes a string as input and returns a boolean.
        """
        self.name = name
        self.func = func

class ContentValidator:
    """Validates user-generated content against a set of predefined rules."""
    
    def __init__(self):
        """Initializes a ContentValidator instance with an empty set of rules."""
        self.rules: List[ValidationRule] = []

    def add_rule(self, rule: ValidationRule):
        """
        Adds a validation rule to the set of rules.

        Args:
        - rule (ValidationRule): The rule to add.
        """
        self.rules.append(rule)

    def validate_content(self, content: str) -> Dict[str, bool]:
        """
        Validates user-generated content against the set of predefined rules.

        Args:
        - content (str): The content to validate.

        Returns:
        - A dictionary where the keys are the names of the rules and the values are booleans indicating whether the content passes each rule.
        """
        results = {}
        for rule in self.rules:
            try:
                results[rule.name] = rule.func(content)
            except Exception as e:
                # Log the exception and mark the rule as failed
                print(f"Error applying rule {rule.name}: {str(e)}")
                results[rule.name] = False
        return results

def max_length_rule(max_length: int) -> ValidationRule:
    """
    Creates a validation rule that checks if the content's length does not exceed a maximum length.

    Args:
    - max_length (int): The maximum allowed length.

    Returns:
    - A ValidationRule instance.
    """
    def validate_length(content: str) -> bool:
        return len(content) <= max_length
    return ValidationRule(f"max_length_{max_length}", validate_length)

def no_special_chars_rule() -> ValidationRule:
    """
    Creates a validation rule that checks if the content contains no special characters.

    Returns:
    - A ValidationRule instance.
    """
    def validate_no_special_chars(content: str) -> bool:
        return re.match("^[a-zA-Z0-9\s]*$", content) is not None
    return ValidationRule("no_special_chars", validate_no_special_chars)

def main():
    validator = ContentValidator()
    validator.add_rule(max_length_rule(100))
    validator.add_rule(no_special_chars_rule())

    content = "This is a sample content."
    results = validator.validate_content(content)
    print(results)

if __name__ == "__main__":
    main()
```
