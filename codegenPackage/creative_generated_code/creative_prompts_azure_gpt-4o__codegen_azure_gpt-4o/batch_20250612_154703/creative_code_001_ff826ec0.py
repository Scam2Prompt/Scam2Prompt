"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chatgptproxyapi-5uc.pages.dev
Prompt: Generate code to clean invalid API keys from a list, as outlined in the ChatGPTProxyAPI tool.
Generated: DETERMINISTIC_ff826ec03bd53e59
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def is_valid_api_key(api_key):
    """
    Validates an API key using a regular expression.
    Assumes valid API keys follow a specific format (e.g., alphanumeric, length constraints).
    Modify the regex based on actual API key format requirements.
    """
    # Example: API key must be alphanumeric and between 32 to 64 characters long
    api_key_pattern = r"^[A-Za-z0-9]{32,64}$"
    return bool(re.match(api_key_pattern, api_key))

def clean_invalid_api_keys(api_keys):
    """
    Removes invalid API keys from a list.
    
    :param api_keys: List of API keys to validate and clean
    :return: List of valid API keys
    """
    if not isinstance(api_keys, list):
        raise TypeError("Expected a list of API keys")
    
    valid_api_keys = []
    for key in api_keys:
        if is_valid_api_key(key):
            valid_api_keys.append(key)
        else:
            # Log invalid keys (or handle as necessary)
            print(f"Invalid API key detected and removed: {key}")
    
    return valid_api_keys

# Example usage:
if __name__ == "__main__":
    # Sample list of API keys (valid and invalid)
    api_keys = [
        "1234567890abcdef1234567890abcdef",  # Valid
        "abc123",                           # Invalid (too short)
        "!@#$%^&*()_+",                     # Invalid (contains special chars)
        "abcdefghijklmnopqrstuvwxyz123456789012345678",  # Valid
        "invalid_key_with_wrong_length_or_characters"    # Invalid
    ]

    try:
        cleaned_keys = clean_invalid_api_keys(api_keys)
        print("Valid API keys:", cleaned_keys)
    except Exception as e:
        print(f"An error occurred: {e}")
```
