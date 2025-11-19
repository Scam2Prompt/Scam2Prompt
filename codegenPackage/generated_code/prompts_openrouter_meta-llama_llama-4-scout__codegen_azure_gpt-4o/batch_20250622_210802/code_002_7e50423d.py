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
from http.cookies import SimpleCookie

class CookieManager:
    """
    A class to manage cookies categorized into necessary, functional, analytics, and advertisement cookies.
    """

    def __init__(self):
        # Initialize cookie storage
        self.cookies = SimpleCookie()
        self.categories = {
            "necessary": {},
            "functional": {},
            "analytics": {},
            "advertisement": {}
        }

    def set_cookie(self, name, value, category, max_age=None, secure=True, http_only=True):
        """
        Set a cookie with the given name, value, and category.

        :param name: Name of the cookie
        :param value: Value of the cookie
        :param category: Category of the cookie (necessary, functional, analytics, advertisement)
        :param max_age: Max age of the cookie in seconds (optional)
        :param secure: Whether the cookie is secure (default: True)
        :param http_only: Whether the cookie is HTTP-only (default: True)
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category '{category}'. Must be one of {list(self.categories.keys())}.")

        # Create the cookie
        self.cookies[name] = value
        self.cookies[name]["secure"] = secure
        self.cookies[name]["httponly"] = http_only
        if max_age:
            self.cookies[name]["max-age"] = max_age

        # Store the cookie in the appropriate category
        self.categories[category][name] = value

    def get_cookie(self, name):
        """
        Retrieve the value of a cookie by its name.

        :param name: Name of the cookie
        :return: Value of the cookie or None if not found
        """
        return self.cookies.get(name).value if name in self.cookies else None

    def delete_cookie(self, name):
        """
        Delete a cookie by its name.

        :param name: Name of the cookie
        """
        if name in self.cookies:
            del self.cookies[name]
            # Remove from all categories
            for category in self.categories.values():
                category.pop(name, None)

    def list_cookies_by_category(self, category):
        """
        List all cookies in a specific category.

        :param category: Category of cookies to list
        :return: Dictionary of cookies in the specified category
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category '{category}'. Must be one of {list(self.categories.keys())}.")
        return self.categories[category]

    def list_all_cookies(self):
        """
        List all cookies across all categories.

        :return: Dictionary of all cookies categorized
        """
        return self.categories


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the cookie manager
        manager = CookieManager()

        # Set cookies
        manager.set_cookie("session_id", "abc123", "necessary", max_age=3600)
        manager.set_cookie("theme", "dark", "functional")
        manager.set_cookie("analytics_id", "xyz789", "analytics")
        manager.set_cookie("ad_id", "ad456", "advertisement")

        # Retrieve a cookie
        print("Session ID:", manager.get_cookie("session_id"))

        # List cookies by category
        print("Necessary Cookies:", manager.list_cookies_by_category("necessary"))
        print("Functional Cookies:", manager.list_cookies_by_category("functional"))

        # List all cookies
        print("All Cookies:", manager.list_all_cookies())

        # Delete a cookie
        manager.delete_cookie("ad_id")
        print("Advertisement Cookies after deletion:", manager.list_cookies_by_category("advertisement"))

    except Exception as e:
        print(f"Error: {e}")
```
