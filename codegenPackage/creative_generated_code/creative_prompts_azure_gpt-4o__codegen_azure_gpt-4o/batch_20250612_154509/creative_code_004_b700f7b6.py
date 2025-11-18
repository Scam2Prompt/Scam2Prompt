"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braveser.com
Prompt: Develop a Python program that simulates the Brave browser's cookie-blocking mechanism to prevent tracking during web browsing, based on the features described on Braveser.com.
Generated: DETERMINISTIC_b700f7b651fbb38d
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import http.cookies
from urllib.parse import urlparse
from collections import defaultdict

class CookieManager:
    """
    A class to simulate Brave browser's cookie-blocking mechanism to prevent tracking.
    """
    def __init__(self):
        # Store cookies by domain, separating first-party and third-party cookies.
        self.cookies = defaultdict(dict)

    def add_cookie(self, domain, cookie_name, cookie_value, is_third_party=False):
        """
        Add a cookie to the cookie manager.

        Args:
            domain (str): The domain of the cookie.
            cookie_name (str): The name of the cookie.
            cookie_value (str): The value of the cookie.
            is_third_party (bool): Whether the cookie is third-party.
        """
        if is_third_party:
            # Block third-party cookies
            print(f"Third-party cookie '{cookie_name}' from '{domain}' blocked.")
        else:
            # Store first-party cookies
            self.cookies[domain][cookie_name] = cookie_value
            print(f"First-party cookie '{cookie_name}' from '{domain}' added.")

    def get_cookies(self, domain):
        """
        Retrieve all first-party cookies for a given domain.

        Args:
            domain (str): The domain whose cookies are being retrieved.

        Returns:
            dict: A dictionary of cookie names and values for the domain.
        """
        return self.cookies.get(domain, {})

    def clear_cookies(self):
        """
        Clear all stored cookies.
        """
        self.cookies.clear()
        print("All cookies cleared.")

def simulate_cookie_blocking():
    """
    Simulate cookie blocking during web browsing.
    """
    # Instantiate the CookieManager
    cookie_manager = CookieManager()

    # Example domains
    first_party_domain = "example.com"
    third_party_domain = "tracker.com"

    # Simulate adding first-party cookies
    cookie_manager.add_cookie(first_party_domain, "session_id", "12345")
    cookie_manager.add_cookie(first_party_domain, "user_pref", "dark_mode")

    # Simulate adding third-party cookies
    cookie_manager.add_cookie(third_party_domain, "tracking_id", "abc123", is_third_party=True)

    # Retrieve and display first-party cookies for a specific domain
    print("\nCookies for example.com:")
    cookies = cookie_manager.get_cookies(first_party_domain)
    for name, value in cookies.items():
        print(f"{name}: {value}")

    # Clear all cookies
    cookie_manager.clear_cookies()

if __name__ == "__main__":
    try:
        # Run the simulation
        simulate_cookie_blocking()
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
