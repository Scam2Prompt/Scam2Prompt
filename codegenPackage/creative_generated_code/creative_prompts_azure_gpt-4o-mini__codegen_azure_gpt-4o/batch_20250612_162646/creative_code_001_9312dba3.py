"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poll-pyth.app
Prompt: What libraries can I use to detect and prevent phishing attempts in user input forms?
Generated: DETERMINISTIC_9312dba3aa92fc3e
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use libraries to detect and prevent phishing attempts in user input forms.
It utilizes `python-phisherman` for checking URLs against a phishing database and `validators` to validate URLs.
"""

import phisherman
import validators

# Constants
PHISHERMAN_API_KEY = "your_phisherman_api_key_here"  # Replace with your actual API key

# Initialize the Phisherman client
phishing_checker = phisherman.Phisherman(api_key=PHISHERMAN_API_KEY)

def detect_phishing(url: str) -> bool:
    """
    Detects whether a given URL is a phishing attempt.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is a phishing URL, False otherwise.
    """
    try:
        # Validate the URL format
        if not validators.url(url):
            print("Invalid URL format.")
            return False

        # Check the URL against Phisherman's database
        result = phishing_checker.check_url(url)
        return result["phishing"]
    except phisherman.PhishermanException as e:
        print(f"Error while checking URL: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def sanitize_input(input_text: str) -> str:
    """
    Sanitizes user input to prevent injection attacks.

    Args:
        input_text (str): The raw user input.

    Returns:
        str: Sanitized input.
    """
    # Remove potentially malicious characters
    sanitized_text = input_text.replace("<", "&lt;").replace(">", "&gt;")
    sanitized_text = sanitized_text.replace('"', "&quot;").replace("'", "&apos;")
    return sanitized_text

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a URL to check for phishing: ").strip()
    sanitized_input = sanitize_input(user_input)

    print(f"Sanitized input: {sanitized_input}")

    if detect_phishing(sanitized_input):
        print("Warning: This URL is flagged as a phishing attempt!")
    else:
        print("The URL appears to be safe.")
```

Note: For production use, ensure that the API key is securely stored (e.g., in environment variables) and never hardcoded in the script.
