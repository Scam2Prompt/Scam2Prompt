"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Write a function to display and manage Masa's cookie categories (e.g., Necessary, Functional, Analytics, Advertisement) with descriptions and durations as specified on the website.
Generated: DETERMINISTIC_82d4ecf78e7b5792
Batch ID: 20250612_153401
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

class CookieCategory(str, Enum):
    """Enum for cookie categories."""
    NECESSARY = "Necessary"
    FUNCTIONAL = "Functional"
    ANALYTICS = "Analytics"
    ADVERTISEMENT = "Advertisement"

class Cookie:
    """Class representing a cookie."""
    def __init__(self, category: CookieCategory, description: str, duration: str):
        """
        Initialize a Cookie object.

        Args:
        - category (CookieCategory): The category of the cookie.
        - description (str): A brief description of the cookie.
        - duration (str): The duration for which the cookie is stored.
        """
        self.category = category
        self.description = description
        self.duration = duration

class CookieManager:
    """Class for managing cookie categories."""
    def __init__(self):
        """Initialize a CookieManager object."""
        self.cookies: Dict[CookieCategory, List[Cookie]] = {
            CookieCategory.NECESSARY: [],
            CookieCategory.FUNCTIONAL: [],
            CookieCategory.ANALYTICS: [],
            CookieCategory.ADVERTISEMENT: []
        }

    def add_cookie(self, category: CookieCategory, description: str, duration: str):
        """
        Add a cookie to a specific category.

        Args:
        - category (CookieCategory): The category of the cookie.
        - description (str): A brief description of the cookie.
        - duration (str): The duration for which the cookie is stored.

        Raises:
        - ValueError: If the category is not a valid CookieCategory.
        """
        if not isinstance(category, CookieCategory):
            raise ValueError("Invalid cookie category")

        cookie = Cookie(category, description, duration)
        self.cookies[category].append(cookie)

    def display_cookies(self):
        """Display all cookie categories with their descriptions and durations."""
        for category, cookies in self.cookies.items():
            print(f"**{category.value} Cookies**")
            for i, cookie in enumerate(cookies, start=1):
                print(f"{i}. {cookie.description} - {cookie.duration}")
            print()  # Empty line for readability

def main():
    # Create a CookieManager object
    manager = CookieManager()

    # Add cookies to categories
    manager.add_cookie(CookieCategory.NECESSARY, "Essential for website functionality", "Session")
    manager.add_cookie(CookieCategory.FUNCTIONAL, "Enhances user experience", "1 month")
    manager.add_cookie(CookieCategory.ANALYTICS, "Helps us analyze website usage", "6 months")
    manager.add_cookie(CookieCategory.ADVERTISEMENT, "Tracks user behavior for targeted ads", "1 year")

    # Display cookie categories
    manager.display_cookies()

if __name__ == "__main__":
    main()
```
