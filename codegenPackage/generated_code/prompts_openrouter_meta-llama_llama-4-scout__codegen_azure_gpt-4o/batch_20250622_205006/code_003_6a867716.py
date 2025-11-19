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

def validate_user_content(content, rules):
    """
    Validates user-generated content against a predefined set of rules.

    Args:
        content (str): The user-generated content to validate.
        rules (dict): A dictionary containing validation rules. 
                      Example:
                      {
                          "max_length": 500,
                          "prohibited_words": ["spam", "scam"],
                          "regex_patterns": [r"^[a-zA-Z0-9\s]+$"],  # Only alphanumeric and spaces
                      }

    Returns:
        dict: A dictionary containing validation results.
              Example:
              {
                  "is_valid": True,
                  "errors": []
              }
    """
    validation_result = {
        "is_valid": True,
        "errors": []
    }

    # Check for maximum length
    max_length = rules.get("max_length")
    if max_length and len(content) > max_length:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Content exceeds maximum length of {max_length} characters.")

    # Check for prohibited words
    prohibited_words = rules.get("prohibited_words", [])
    for word in prohibited_words:
        if word.lower() in content.lower():
            validation_result["is_valid"] = False
            validation_result["errors"].append(f"Content contains prohibited word: '{word}'.")

    # Check for regex patterns
    regex_patterns = rules.get("regex_patterns", [])
    for pattern in regex_patterns:
        if not re.match(pattern, content):
            validation_result["is_valid"] = False
            validation_result["errors"].append(f"Content does not match required pattern: '{pattern}'.")

    return validation_result


# Example usage:
if __name__ == "__main__":
    # Define validation rules
    rules = {
        "max_length": 500,
        "prohibited_words": ["spam", "scam"],
        "regex_patterns": [r"^[a-zA-Z0-9\s]+$"]  # Only alphanumeric and spaces
    }

    # User-generated content
    user_content = "This is a test content with spam."

    # Validate content
    result = validate_user_content(user_content, rules)

    # Print validation result
    if result["is_valid"]:
        print("Content is valid.")
    else:
        print("Content is invalid. Errors:")
        for error in result["errors"]:
            print(f"- {error}")
```
