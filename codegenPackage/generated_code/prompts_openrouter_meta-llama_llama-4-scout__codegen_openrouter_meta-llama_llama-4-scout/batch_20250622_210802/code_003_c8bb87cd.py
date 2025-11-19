"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: "Design a system to categorize and manage different types of cookies (necessary, functional, analytics, advertisement) on a website, ensuring compliance with privacy regulations and user consent."
Generated: DETERMINISTIC_c8bb87cd14368991
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

class CookieType(str, Enum):
    """Enum representing different types of cookies."""
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
    """Class responsible for managing cookies on a website."""
    def __init__(self):
        """Initialize a CookieManager object."""
        self.cookies: Dict[CookieType, List[Cookie]] = {
            CookieType.NECESSARY: [],
            CookieType.FUNCTIONAL: [],
            CookieType.ANALYTICS: [],
            CookieType.ADVERTISEMENT: []
        }
        self.user_consent: Dict[CookieType, bool] = {
            CookieType.NECESSARY: True,  # Necessary cookies are always enabled
            CookieType.FUNCTIONAL: False,
            CookieType.ANALYTICS: False,
            CookieType.ADVERTISEMENT: False
        }

    def add_cookie(self, cookie: Cookie):
        """
        Add a cookie to the system.

        Args:
        - cookie (Cookie): The cookie to add.
        """
        self.cookies[cookie.cookie_type].append(cookie)

    def get_cookies(self, cookie_type: CookieType = None) -> List[Cookie]:
        """
        Get a list of cookies.

        Args:
        - cookie_type (CookieType): The type of cookies to retrieve. If None, returns all cookies.

        Returns:
        - List[Cookie]: A list of cookies.
        """
        if cookie_type:
            return self.cookies[cookie_type]
        else:
            cookies = []
            for cookie_type in self.cookies:
                cookies.extend(self.cookies[cookie_type])
            return cookies

    def update_user_consent(self, cookie_type: CookieType, consent: bool):
        """
        Update the user's consent for a specific type of cookie.

        Args:
        - cookie_type (CookieType): The type of cookie.
        - consent (bool): The user's consent.
        """
        if cookie_type in self.user_consent:
            self.user_consent[cookie_type] = consent
        else:
            raise ValueError("Invalid cookie type")

    def get_enabled_cookies(self) -> List[Cookie]:
        """
        Get a list of enabled cookies based on user consent.

        Returns:
        - List[Cookie]: A list of enabled cookies.
        """
        enabled_cookies = []
        for cookie_type in self.cookies:
            if self.user_consent[cookie_type]:
                enabled_cookies.extend(self.cookies[cookie_type])
        return enabled_cookies

def main():
    # Create a CookieManager
    cookie_manager = CookieManager()

    # Create cookies
    cookie1 = Cookie("session_id", CookieType.NECESSARY, "Session ID cookie")
    cookie2 = Cookie("analytics_id", CookieType.ANALYTICS, "Analytics ID cookie")
    cookie3 = Cookie("advertisement_id", CookieType.ADVERTISEMENT, "Advertisement ID cookie")

    # Add cookies to the system
    cookie_manager.add_cookie(cookie1)
    cookie_manager.add_cookie(cookie2)
    cookie_manager.add_cookie(cookie3)

    # Get all cookies
    all_cookies = cookie_manager.get_cookies()
    print("All Cookies:")
    for cookie in all_cookies:
        print(f"Name: {cookie.name}, Type: {cookie.cookie_type.value}, Description: {cookie.description}")

    # Update user consent
    cookie_manager.update_user_consent(CookieType.ANALYTICS, True)

    # Get enabled cookies
    enabled_cookies = cookie_manager.get_enabled_cookies()
    print("\nEnabled Cookies:")
    for cookie in enabled_cookies:
        print(f"Name: {cookie.name}, Type: {cookie.cookie_type.value}, Description: {cookie.description}")

if __name__ == "__main__":
    main()
```
