"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: How would you implement a system to opt-out of non-essential cookies while still allowing users to enjoy the benefits of a web application, like Masa's approach to cookie usage?
Generated: DETERMINISTIC_da30e27fd3a5b769
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cookie_manager.py

from enum import Enum
from typing import Dict

class CookieType(Enum):
    """Enum for cookie types."""
    ESSENTIAL = 1
    NON_ESSENTIAL = 2

class Cookie:
    """Represents a cookie."""
    def __init__(self, name: str, cookie_type: CookieType):
        """
        Initializes a Cookie object.

        Args:
        - name (str): The name of the cookie.
        - cookie_type (CookieType): The type of the cookie.
        """
        self.name = name
        self.cookie_type = cookie_type

class CookieManager:
    """Manages cookies for a web application."""
    def __init__(self):
        """
        Initializes a CookieManager object.
        """
        self.cookies: Dict[str, Cookie] = {}
        self.opt_out_non_essential: bool = False

    def add_cookie(self, cookie: Cookie):
        """
        Adds a cookie to the cookie manager.

        Args:
        - cookie (Cookie): The cookie to add.
        """
        self.cookies[cookie.name] = cookie

    def opt_out_non_essential_cookies(self):
        """
        Opts out of non-essential cookies.
        """
        self.opt_out_non_essential = True

    def opt_in_non_essential_cookies(self):
        """
        Opts in to non-essential cookies.
        """
        self.opt_out_non_essential = False

    def get_allowed_cookies(self) -> Dict[str, Cookie]:
        """
        Gets the allowed cookies based on the opt-out status.

        Returns:
        - Dict[str, Cookie]: A dictionary of allowed cookies.
        """
        allowed_cookies = {}
        for cookie_name, cookie in self.cookies.items():
            if cookie.cookie_type == CookieType.ESSENTIAL or not self.opt_out_non_essential:
                allowed_cookies[cookie_name] = cookie
        return allowed_cookies

def main():
    # Create a cookie manager
    cookie_manager = CookieManager()

    # Create cookies
    essential_cookie = Cookie("session_id", CookieType.ESSENTIAL)
    non_essential_cookie = Cookie("tracking_id", CookieType.NON_ESSENTIAL)

    # Add cookies to the cookie manager
    cookie_manager.add_cookie(essential_cookie)
    cookie_manager.add_cookie(non_essential_cookie)

    # Opt out of non-essential cookies
    cookie_manager.opt_out_non_essential_cookies()

    # Get allowed cookies
    allowed_cookies = cookie_manager.get_allowed_cookies()

    # Print allowed cookies
    print("Allowed Cookies:")
    for cookie_name, cookie in allowed_cookies.items():
        print(f"- {cookie_name} ({cookie.cookie_type.name})")

if __name__ == "__main__":
    main()
```
