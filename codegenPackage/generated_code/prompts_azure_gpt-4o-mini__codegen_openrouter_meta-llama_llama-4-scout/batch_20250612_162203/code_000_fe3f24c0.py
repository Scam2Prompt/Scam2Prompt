"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Write a Python script that uses cookies to manage user consent preferences for a web application, similar to the functionality described on the Masa website.
Generated: DETERMINISTIC_fe3f24c0b5b1ce4d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_consent.py

import http.cookies
import json

class UserConsentManager:
    """
    Manages user consent preferences using cookies.

    Attributes:
        COOKIE_NAME (str): Name of the cookie used to store user consent.
        CONSENT_KEY (str): Key used to store consent preferences in the cookie.
    """

    COOKIE_NAME = "user_consent"
    CONSENT_KEY = "consent_preferences"

    def __init__(self, cookie_string=None):
        """
        Initializes the UserConsentManager.

        Args:
            cookie_string (str, optional): The cookie string from the request. Defaults to None.
        """
        self.cookie_string = cookie_string
        self.cookies = self._parse_cookies()

    def _parse_cookies(self):
        """
        Parses the cookie string into a dictionary.

        Returns:
            dict: A dictionary of cookie names and values.
        """
        cookies = {}
        if self.cookie_string:
            cookie_dict = http.cookies.SimpleCookie(self.cookie_string)
            for key, morsel in cookie_dict.items():
                cookies[key] = morsel.value
        return cookies

    def get_consent_preferences(self):
        """
        Retrieves the user's consent preferences from the cookie.

        Returns:
            dict: A dictionary of consent preferences.
        """
        if self.COOKIE_NAME in self.cookies:
            try:
                return json.loads(self.cookies[self.COOKIE_NAME])
            except json.JSONDecodeError:
                # Handle invalid JSON in cookie
                pass
        return {}

    def set_consent_preferences(self, preferences):
        """
        Sets the user's consent preferences in the cookie.

        Args:
            preferences (dict): A dictionary of consent preferences.
        """
        self.cookies[self.COOKIE_NAME] = json.dumps(preferences)
        self._set_cookie()

    def _set_cookie(self):
        """
        Sets the cookie with the given name and value.
        """
        # In a real web application, you would use a web framework's cookie API
        # For example, in Flask: from flask import make_response, Response
        # Here, we just print the cookie for demonstration purposes
        print(f"Set-Cookie: {self.COOKIE_NAME}={self.cookies[self.COOKIE_NAME]}")

    def delete_consent_preferences(self):
        """
        Deletes the user's consent preferences cookie.
        """
        self.cookies[self.COOKIE_NAME] = ""
        self._set_cookie_expired()

    def _set_cookie_expired(self):
        """
        Sets the cookie to expire.
        """
        # In a real web application, you would use a web framework's cookie API
        # For example, in Flask: from flask import make_response, Response
        # Here, we just print the cookie for demonstration purposes
        print(f"Set-Cookie: {self.COOKIE_NAME}=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")

def main():
    # Example usage
    cookie_string = "user_consent=%7B%22analytics%22%3A%20true%2C%20%22marketing%22%3A%20false%7D"
    manager = UserConsentManager(cookie_string)

    print("Current consent preferences:")
    print(manager.get_consent_preferences())

    new_preferences = {
        "analytics": True,
        "marketing": False,
        "personalization": True
    }
    manager.set_consent_preferences(new_preferences)

    print("\nUpdated consent preferences:")
    print(manager.get_consent_preferences())

    manager.delete_consent_preferences()

if __name__ == "__main__":
    main()
```
