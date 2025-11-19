"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: What is an efficient way to categorize and manage different types of cookies (necessary, functional, analytics, advertisement) on a website, and how can this be implemented in code?
Generated: DETERMINISTIC_efa738f26ee857b3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class CookieType(Enum):
    """Enum for different types of cookies."""
    NECESSARY = "necessary"
    FUNCTIONAL = "functional"
    ANALYTICS = "analytics"
    ADVERTISEMENT = "advertisement"

class Cookie:
    """Class representing a cookie."""
    def __init__(self, name: str, cookie_type: CookieType, description: str):
        """
        Initialize a Cookie object.

        Args:
        - name (str): The name of the cookie.
        - cookie_type (CookieType): The type of the cookie.
        - description (str): A brief description of the cookie.
        """
        self.name = name
        self.cookie_type = cookie_type
        self.description = description

class CookieManager:
    """Class for managing cookies on a website."""
    def __init__(self):
        """Initialize a CookieManager object."""
        self.cookies: Dict[CookieType, List[Cookie]] = {
            CookieType.NECESSARY: [],
            CookieType.FUNCTIONAL: [],
            CookieType.ANALYTICS: [],
            CookieType.ADVERTISEMENT: []
        }

    def add_cookie(self, cookie: Cookie):
        """
        Add a cookie to the manager.

        Args:
        - cookie (Cookie): The cookie to add.

        Raises:
        - ValueError: If the cookie type is not valid.
        """
        if cookie.cookie_type not in self.cookies:
            raise ValueError("Invalid cookie type")
        self.cookies[cookie.cookie_type].append(cookie)

    def remove_cookie(self, cookie_name: str, cookie_type: CookieType):
        """
        Remove a cookie from the manager.

        Args:
        - cookie_name (str): The name of the cookie to remove.
        - cookie_type (CookieType): The type of the cookie to remove.

        Raises:
        - ValueError: If the cookie type is not valid.
        - CookieNotFoundError: If the cookie is not found.
        """
        if cookie_type not in self.cookies:
            raise ValueError("Invalid cookie type")
        for cookie in self.cookies[cookie_type]:
            if cookie.name == cookie_name:
                self.cookies[cookie_type].remove(cookie)
                return
        raise CookieNotFoundError(f"Cookie '{cookie_name}' of type '{cookie_type}' not found")

    def get_cookies(self, cookie_type: CookieType = None):
        """
        Get cookies of a specific type or all cookies.

        Args:
        - cookie_type (CookieType, optional): The type of cookies to get. Defaults to None.

        Returns:
        - List[Cookie]: A list of cookies.
        """
        if cookie_type:
            return self.cookies.get(cookie_type, [])
        else:
            return [cookie for cookies in self.cookies.values() for cookie in cookies]

class CookieNotFoundError(Exception):
    """Exception raised when a cookie is not found."""
    pass

def main():
    # Create a CookieManager
    manager = CookieManager()

    # Create cookies
    necessary_cookie = Cookie("session_id", CookieType.NECESSARY, "Session ID cookie")
    functional_cookie = Cookie("lang", CookieType.FUNCTIONAL, "Language preference cookie")
    analytics_cookie = Cookie("tracking_id", CookieType.ANALYTICS, "Analytics tracking cookie")
    advertisement_cookie = Cookie("ad_id", CookieType.ADVERTISEMENT, "Advertisement ID cookie")

    # Add cookies to the manager
    manager.add_cookie(necessary_cookie)
    manager.add_cookie(functional_cookie)
    manager.add_cookie(analytics_cookie)
    manager.add_cookie(advertisement_cookie)

    # Get cookies by type
    necessary_cookies = manager.get_cookies(CookieType.NECESSARY)
    print("Necessary Cookies:")
    for cookie in necessary_cookies:
        print(f"- {cookie.name}: {cookie.description}")

    # Remove a cookie
    manager.remove_cookie("lang", CookieType.FUNCTIONAL)

    # Try to remove a non-existent cookie
    try:
        manager.remove_cookie("non_existent", CookieType.FUNCTIONAL)
    except CookieNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
```
