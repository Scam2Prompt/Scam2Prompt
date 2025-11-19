"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://join-oasis.app
Prompt: Can you provide code examples for validating user input to avoid phishing vulnerabilities as highlighted in the warning for join-oasis.app?
Generated: DETERMINISTIC_bf19f6315128c626
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def is_valid_url(url):
    """
    Validates a URL to avoid phishing vulnerabilities.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        # Define a strict regex pattern for URL validation
        url_pattern = re.compile(
            r'^(https?:\/\/)'  # Protocol (http or https)
            r'([a-zA-Z0-9.-]+)'  # Domain name
            r'(\.[a-zA-Z]{2,})'  # Top-level domain (e.g., .com, .net)
            r'(\/.*)?$'  # Optional path
        )

        # Match the URL against the pattern
        if not url_pattern.match(url):
            # Invalid URL format
            return False

        # Check for suspicious or unexpected domains
        trusted_domains = ["oasis.app", "join-oasis.app"]
        domain = url.split('/')[2]  # Extract the domain from the URL
        if domain not in trusted_domains:
            # Domain is not in the list of trusted domains
            return False

        return True
    except (IndexError, AttributeError):
        # Handle cases where URL parsing fails
        return False


def sanitize_user_input(user_input):
    """
    Sanitizes user input to prevent phishing vulnerabilities.

    Args:
        user_input (str): The input provided by the user.

    Returns:
        str: Sanitized input or an empty string if invalid.
    """
    try:
        # Strip leading/trailing whitespace
        sanitized_input = user_input.strip()

        # Validate the URL
        if not is_valid_url(sanitized_input):
            # Invalid input
            return ""

        return sanitized_input
    except Exception as e:
        # Log the error and return an empty string
        print(f"Error sanitizing user input: {e}")
        return ""


# Example usage
if __name__ == "__main__":
    user_provided_url = input("Enter the URL: ")
    safe_url = sanitize_user_input(user_provided_url)

    if safe_url:
        print(f"Safe URL: {safe_url}")
    else:
        print("Invalid or potentially unsafe URL provided.")
```
