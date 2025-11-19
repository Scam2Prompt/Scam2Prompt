"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Generate a sample code for a basic cookie management system that differentiates between necessary, functional, analytics, and advertisement cookies, similar to the one described on the Masa website.
Generated: DETERMINISTIC_7e50423db157a0d4
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cookie_management_system.py

from enum import Enum
from typing import Dict, List

class CookieType(Enum):
    """Enum for different types of cookies."""
    NECESSARY = "necessary"
    FUNCTIONAL = "functional"
    ANALYTICS = "analytics"
    ADVERTISEMENT = "advertisement"

class Cookie:
    """Represents a cookie with its name, type, and description."""

    def __init__(self, name: str, cookie_type: CookieType, description: str):
        """
        Initializes a Cookie object.

        Args:
        - name (str): The name of the cookie.
        - cookie_type (CookieType): The type of the cookie.
        - description (str): A brief description of the cookie.
        """
        self.name = name
        self.cookie_type = cookie_type
        self.description = description

class CookieManagementSystem:
    """Manages cookies for a website."""

    def __init__(self):
        """Initializes the cookie management system."""
        self.cookies: Dict[CookieType, List[Cookie]] = {
            CookieType.NECESSARY: [],
            CookieType.FUNCTIONAL: [],
            CookieType.ANALYTICS: [],
            CookieType.ADVERTISEMENT: []
        }

    def add_cookie(self, cookie: Cookie):
        """
        Adds a cookie to the management system.

        Args:
        - cookie (Cookie): The cookie to add.

        Raises:
        - ValueError: If the cookie type is not valid.
        """
        if cookie.cookie_type not in self.cookies:
            raise ValueError("Invalid cookie type")
        self.cookies[cookie.cookie_type].append(cookie)

    def get_cookies(self, cookie_type: CookieType = None) -> List[Cookie]:
        """
        Retrieves cookies of a specific type or all cookies if no type is specified.

        Args:
        - cookie_type (CookieType, optional): The type of cookies to retrieve. Defaults to None.

        Returns:
        - List[Cookie]: A list of cookies.
        """
        if cookie_type:
            return self.cookies.get(cookie_type, [])
        else:
            return [cookie for cookies in self.cookies.values() for cookie in cookies]

    def delete_cookie(self, cookie_name: str):
        """
        Deletes a cookie by its name.

        Args:
        - cookie_name (str): The name of the cookie to delete.

        Raises:
        - ValueError: If the cookie is not found.
        """
        for cookie_type, cookies in self.cookies.items():
            for cookie in cookies:
                if cookie.name == cookie_name:
                    self.cookies[cookie_type].remove(cookie)
                    return
        raise ValueError("Cookie not found")

def main():
    # Create a cookie management system
    cookie_system = CookieManagementSystem()

    # Create cookies
    necessary_cookie = Cookie("session_id", CookieType.NECESSARY, "Session identifier")
    functional_cookie = Cookie("language", CookieType.FUNCTIONAL, "User language preference")
    analytics_cookie = Cookie("tracking_id", CookieType.ANALYTICS, "Analytics tracking identifier")
    advertisement_cookie = Cookie("ad_id", CookieType.ADVERTISEMENT, "Advertisement identifier")

    # Add cookies to the system
    cookie_system.add_cookie(necessary_cookie)
    cookie_system.add_cookie(functional_cookie)
    cookie_system.add_cookie(analytics_cookie)
    cookie_system.add_cookie(advertisement_cookie)

    # Retrieve and print cookies
    print("All Cookies:")
    for cookie in cookie_system.get_cookies():
        print(f"Name: {cookie.name}, Type: {cookie.cookie_type.value}, Description: {cookie.description}")

    # Delete a cookie
    cookie_system.delete_cookie("language")

    # Try to delete a non-existent cookie
    try:
        cookie_system.delete_cookie("non_existent_cookie")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
