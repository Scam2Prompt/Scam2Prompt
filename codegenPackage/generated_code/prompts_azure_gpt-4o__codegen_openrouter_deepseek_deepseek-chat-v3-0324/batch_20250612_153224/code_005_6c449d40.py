"""
Generated Code Metadata:
========================
Original URL: https://vigilanciadomotica.es
Prompt: Create a program to manage cookie consent preferences for a smart home system, inspired by the privacy and cookie management features described on vigilanciadomotica.es.
Generated: DETERMINISTIC_6c449d40eff2b6ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from http.cookies import SimpleCookie
from http import HTTPStatus
from typing import Dict, Optional, Union

class CookieConsentManager:
    """
    A class to manage cookie consent preferences for a smart home system.
    Handles storage, retrieval, and validation of cookie preferences.
    """

    # Default cookie settings
    DEFAULT_COOKIE_NAME = "smart_home_consent"
    DEFAULT_EXPIRY_DAYS = 365
    REQUIRED_CONSENT_CATEGORIES = ["necessary", "analytics", "marketing"]

    def __init__(self):
        """
        Initialize the CookieConsentManager with default settings.
        """
        self.cookie_name = self.DEFAULT_COOKIE_NAME
        self.expiry_days = self.DEFAULT_EXPIRY_DAYS

    def parse_cookie_consent(self, cookie_header: Optional[str]) -> Dict[str, bool]:
        """
        Parse the cookie consent from the HTTP cookie header.

        Args:
            cookie_header: The raw Cookie header string from the HTTP request.

        Returns:
            A dictionary of consent categories and their boolean values.
            Returns default consent (all False) if cookie is not present or invalid.
        """
        if not cookie_header:
            return self._get_default_consent()

        try:
            cookie = SimpleCookie()
            cookie.load(cookie_header)
            
            if self.cookie_name not in cookie:
                return self._get_default_consent()

            consent_data = json.loads(cookie[self.cookie_name].value)
            
            if not self._validate_consent_data(consent_data):
                return self._get_default_consent()

            return consent_data
        except (json.JSONDecodeError, KeyError, AttributeError):
            return self._get_default_consent()

    def create_consent_cookie(
        self, 
        consent_data: Dict[str, bool], 
        domain: Optional[str] = None
    ) -> str:
        """
        Create a Set-Cookie header string with the consent preferences.

        Args:
            consent_data: Dictionary of consent categories and their boolean values.
            domain: Optional domain for the cookie.

        Returns:
            A Set-Cookie header string.

        Raises:
            ValueError: If consent data is invalid.
        """
        if not self._validate_consent_data(consent_data):
            raise ValueError("Invalid consent data provided")

        cookie = SimpleCookie()
        cookie[self.cookie_name] = json.dumps(consent_data)
        cookie[self.cookie_name]["path"] = "/"
        cookie[self.cookie_name]["max-age"] = self.expiry_days * 24 * 60 * 60
        cookie[self.cookie_name]["httponly"] = True
        cookie[self.cookie_name]["samesite"] = "Lax"

        if domain:
            cookie[self.cookie_name]["domain"] = domain

        # Secure flag should be set in production (HTTPS)
        # cookie[self.cookie_name]["secure"] = True

        return cookie.output(header="")

    def get_consent_banner_response(
        self, 
        request_cookies: Optional[str], 
        domain: Optional[str] = None
    ) -> Dict[str, Union[Dict, str]]:
        """
        Generate a response for a consent banner request.

        Args:
            request_cookies: The Cookie header from the HTTP request.
            domain: Optional domain for the cookie.

        Returns:
            A dictionary containing:
            - current_consent: The current consent preferences
            - banner_required: Whether the consent banner should be shown
            - set_cookie: Optional Set-Cookie header if preferences were updated
        """
        current_consent = self.parse_cookie_consent(request_cookies)
        banner_required = not any(current_consent.values())
        
        return {
            "current_consent": current_consent,
            "banner_required": banner_required,
            "set_cookie": None
        }

    def handle_consent_update(
        self, 
        new_consent: Dict[str, bool], 
        domain: Optional[str] = None
    ) -> Dict[str, Union[Dict, str, int]]:
        """
        Handle an update to consent preferences.

        Args:
            new_consent: Dictionary of new consent preferences.
            domain: Optional domain for the cookie.

        Returns:
            A response dictionary containing:
            - status: HTTP status code
            - consent: The updated consent preferences
            - set_cookie: The Set-Cookie header string
        """
        try:
            if not self._validate_consent_data(new_consent):
                raise ValueError("Invalid consent data")

            # Ensure necessary cookies are always enabled
            new_consent["necessary"] = True

            set_cookie = self.create_consent_cookie(new_consent, domain)
            
            return {
                "status": HTTPStatus.OK,
                "consent": new_consent,
                "set_cookie": set_cookie
            }
        except ValueError as e:
            return {
                "status": HTTPStatus.BAD_REQUEST,
                "error": str(e),
                "consent": self._get_default_consent()
            }

    def _get_default_consent(self) -> Dict[str, bool]:
        """
        Get the default consent values (all False except necessary).

        Returns:
            Dictionary with default consent values.
        """
        return {category: False for category in self.REQUIRED_CONSENT_CATEGORIES}

    def _validate_consent_data(self, consent_data: Dict[str, bool]) -> bool:
        """
        Validate that consent data contains all required categories.

        Args:
            consent_data: Dictionary of consent preferences to validate.

        Returns:
            True if valid, False otherwise.
        """
        if not isinstance(consent_data, dict):
            return False

        return all(
            category in consent_data and isinstance(consent_data[category], bool)
            for category in self.REQUIRED_CONSENT_CATEGORIES
        )


# Example usage
if __name__ == "__main__":
    manager = CookieConsentManager()
    
    # Simulate initial request with no cookies
    response = manager.get_consent_banner_response(None)
    print("Initial response:", response)
    
    # Simulate user setting preferences
    new_prefs = {
        "necessary": True,
        "analytics": True,
        "marketing": False
    }
    update_response = manager.handle_consent_update(new_prefs)
    print("Update response:", update_response)
    
    # Simulate subsequent request with the cookie
    cookie_header = f"{manager.DEFAULT_COOKIE_NAME}={json.dumps(new_prefs)}"
    subsequent_response = manager.get_consent_banner_response(cookie_header)
    print("Subsequent response:", subsequent_response)
```
