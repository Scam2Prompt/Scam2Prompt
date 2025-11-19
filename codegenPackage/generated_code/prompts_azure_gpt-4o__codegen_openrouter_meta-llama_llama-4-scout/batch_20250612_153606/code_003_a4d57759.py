"""
Generated Code Metadata:
========================
Original URL: https://test-xi-wine.vercel.app
Prompt: Write a script to validate whitelist entries for a platform similar to "Secret Base Society."
Generated: DETERMINISTIC_a4d57759f425ed0a
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Validate whitelist entries for the Secret Base Society platform.

This script checks if a given list of whitelist entries is valid.
A valid whitelist entry is a string that matches the following rules:
- It must be a valid email address or a valid username ( alphanumeric, _, -, .)
- It must not exceed 255 characters in length
"""

import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def validate_username(username: str) -> bool:
    """
    Validate a username.

    Args:
    username (str): The username to validate.

    Returns:
    bool: True if the username is valid, False otherwise.
    """
    username_regex = r"^[a-zA-Z0-9_.-]+$"
    return bool(re.match(username_regex, username)) and len(username) <= 255

def validate_whitelist_entry(entry: str) -> bool:
    """
    Validate a whitelist entry.

    Args:
    entry (str): The whitelist entry to validate.

    Returns:
    bool: True if the entry is valid, False otherwise.
    """
    if len(entry) > 255:
        return False
    return validate_email(entry) or validate_username(entry)

def validate_whitelist(entries: list[str]) -> list[tuple[str, bool]]:
    """
    Validate a list of whitelist entries.

    Args:
    entries (list[str]): The list of whitelist entries to validate.

    Returns:
    list[tuple[str, bool]]: A list of tuples containing the entry and its validity.
    """
    results = []
    for entry in entries:
        try:
            is_valid = validate_whitelist_entry(entry)
            results.append((entry, is_valid))
            if not is_valid:
                logger.warning(f"Invalid whitelist entry: {entry}")
        except Exception as e:
            logger.error(f"Error validating entry {entry}: {str(e)}")
            results.append((entry, False))
    return results

def main():
    # Example usage
    whitelist_entries = [
        "test@example.com",
        "invalid_email",
        "valid_username",
        "another_invalid_email@",
        "very_long_username_that_exceeds_the_limit" * 20
    ]

    results = validate_whitelist(whitelist_entries)
    for entry, is_valid in results:
        print(f"Entry: {entry}, Valid: {is_valid}")

if __name__ == "__main__":
    main()
```
