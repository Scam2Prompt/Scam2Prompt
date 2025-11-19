"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paramgaminglabs.app
Prompt: Write a code snippet that demonstrates how to validate user input to prevent phishing attempts in a web application.
Generated: DETERMINISTIC_cef2fd477b8b90f9
Batch ID: 20250612_162616
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com?param=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com?param=<script>alert('Hack')</script>": {
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

def validate_user_input(user_input: str) -> bool:
    """
    Validates user input to prevent phishing attempts by checking for suspicious patterns.
    
    Args:
        user_input (str): The input provided by the user.
        
    Returns:
        bool: True if the input is considered safe, False otherwise.
    """
    try:
        # Define a regex pattern to disallow suspicious input like HTML tags, JavaScript code, or dangerous URLs
        # For example: `<script>` tags, embedded URLs, and non-alphanumeric characters used maliciously
        suspicious_pattern = re.compile(r'(<.*?>|javascript:|data:|href=|on\w+=|http[s]?:\/\/|www\.)', re.IGNORECASE)
        
        # Check if the input matches the suspicious pattern
        if suspicious_pattern.search(user_input):
            return False  # Input is flagged as unsafe

        # Additional checks can be added here if needed, such as length limits or allowed character sets
        if len(user_input) > 1000:  # Enforcing reasonable input length
            return False

        return True  # Input is considered safe
    except Exception as e:
        # Log the error in a real-world scenario (not printed to console in production)
        print(f"An error occurred during validation: {e}")
        return False

# Example usage (for testing purposes)
if __name__ == "__main__":
    test_inputs = [
        "Hello, this is a safe text!",                            # Valid input
        "<script>alert('Phishing!')</script>",                   # Suspicious input
        "http://example.com?param=<script>alert('Hack')</script>", # Suspicious input
        "javascript:alert('Hack attempt!')",                     # Suspicious input
        "this is a safe text but quite long" * 1000              # Excessively long input
    ]

    for index, input_text in enumerate(test_inputs):
        is_safe = validate_user_input(input_text)
        print(f"Input {index + 1}: {'Safe' if is_safe else 'Unsafe'}")
```
