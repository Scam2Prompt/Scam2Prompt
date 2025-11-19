"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozali-49z.pages.dev
Prompt: Write a script to manage cookie preferences for a web application linked to a memecoin project.
Generated: DETERMINISTIC_b262f5a4a622ae76
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from http.cookies import SimpleCookie
from typing import Dict, Optional

# Constants
COOKIE_NAME = "memecoin_preferences"
VALID_COOKIE_VALUES = {"accept_all", "reject_all", "custom"}
DEFAULT_COOKIE_VALUE = "accept_all"

# Function to parse cookie from HTTP headers
def parse_cookie(header: str) -> Optional[Dict[str, str]]:
    """
    Parses the incoming HTTP cookie header to extract cookie data.

    :param header: The raw HTTP cookie header string.
    :return: A dictionary representation of cookies or None if parsing fails.
    """
    try:
        cookie = SimpleCookie(header)
        return {key: morsel.value for key, morsel in cookie.items()}
    except Exception as e:
        print(f"Error parsing cookie: {e}")
        return None

# Function to validate cookie preferences
def validate_cookie_preferences(value: str) -> bool:
    """
    Validates the cookie preference value against allowed values.

    :param value: The cookie preference value.
    :return: True if the value is valid, False otherwise.
    """
    return value in VALID_COOKIE_VALUES

# Function to set cookie preferences
def set_cookie_preferences(value: str) -> str:
    """
    Generates a cookie header string to set the cookie preferences.

    :param value: The cookie preference value.
    :return: A string representing the Set-Cookie header.
    """
    if not validate_cookie_preferences(value):
        raise ValueError(f"Invalid cookie preference value: {value}")
    
    cookie = SimpleCookie()
    cookie[COOKIE_NAME] = value
    cookie[COOKIE_NAME]["path"] = "/"
    cookie[COOKIE_NAME]["httponly"] = True
    cookie[COOKIE_NAME]["secure"] = True  # Ensure secure flag for HTTPS
    cookie[COOKIE_NAME]["max-age"] = 86400  # 1 day expiration
    return cookie.output(header="", sep="").strip()

# Function to handle cookie preferences
def handle_cookie_preferences(header: Optional[str]) -> str:
    """
    Handles cookie preferences by parsing, validating, and setting cookies.

    :param header: The raw HTTP cookie header string.
    :return: A Set-Cookie header string based on user preferences.
    """
    preferences = parse_cookie(header)
    
    if preferences and COOKIE_NAME in preferences:
        value = preferences[COOKIE_NAME]
        if validate_cookie_preferences(value):
            return set_cookie_preferences(value)
        else:
            print(f"Invalid value detected: {value}. Reverting to default.")
            return set_cookie_preferences(DEFAULT_COOKIE_VALUE)
    else:
        print("No cookie preference found. Setting default value.")
        return set_cookie_preferences(DEFAULT_COOKIE_VALUE)

# Example usage (for demonstration purposes; replace with actual HTTP handling logic)
if __name__ == "__main__":
    # Simulating incoming HTTP cookie header
    incoming_cookie_header = "memecoin_preferences=custom"
    
    try:
        set_cookie_header = handle_cookie_preferences(incoming_cookie_header)
        print(f"Set-Cookie Header: {set_cookie_header}")
    except Exception as e:
        print(f"Error handling cookie preferences: {e}")
```
