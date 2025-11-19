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
import json

class CookieManager:
    """
    A class to manage and categorize cookies on a website, ensuring compliance with privacy regulations and user consent.
    """

    def __init__(self):
        """
        Initializes the CookieManager with default categories and an empty consent record.
        """
        self.cookie_categories = {
            "necessary": [],
            "functional": [],
            "analytics": [],
            "advertisement": []
        }
        self.user_consent = {
            "necessary": True,  # Necessary cookies are always enabled
            "functional": False,
            "analytics": False,
            "advertisement": False
        }

    def add_cookie(self, category, cookie_name):
        """
        Adds a cookie to a specific category.

        :param category: The category to which the cookie belongs (necessary, functional, analytics, advertisement).
        :param cookie_name: The name of the cookie to add.
        :raises ValueError: If the category is invalid.
        """
        if category not in self.cookie_categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {', '.join(self.cookie_categories.keys())}")
        self.cookie_categories[category].append(cookie_name)

    def set_user_consent(self, consent_data):
        """
        Updates user consent for cookie categories.

        :param consent_data: A dictionary containing user consent for each category.
                             Example: {"functional": True, "analytics": False, "advertisement": True}
        :raises ValueError: If the consent_data contains invalid categories.
        """
        for category, consent in consent_data.items():
            if category not in self.user_consent:
                raise ValueError(f"Invalid category in consent data: {category}. Valid categories are: {', '.join(self.user_consent.keys())}")
            self.user_consent[category] = consent

    def get_active_cookies(self):
        """
        Retrieves the list of cookies that are active based on user consent.

        :return: A dictionary of active cookies by category.
        """
        active_cookies = {}
        for category, cookies in self.cookie_categories.items():
            if self.user_consent.get(category, False):  # Include cookies only if consent is given
                active_cookies[category] = cookies
        return active_cookies

    def save_user_consent(self, file_path):
        """
        Saves user consent data to a JSON file.

        :param file_path: The path to the file where consent data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.user_consent, file, indent=4)
        except IOError as e:
            print(f"Error saving user consent to file: {e}")

    def load_user_consent(self, file_path):
        """
        Loads user consent data from a JSON file.

        :param file_path: The path to the file from which consent data will be loaded.
        :raises ValueError: If the loaded data contains invalid categories.
        """
        try:
            with open(file_path, 'r') as file:
                consent_data = json.load(file)
                self.set_user_consent(consent_data)
        except IOError as e:
            print(f"Error loading user consent from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")

# Example usage
if __name__ == "__main__":
    manager = CookieManager()

    # Add cookies to categories
    manager.add_cookie("necessary", "session_id")
    manager.add_cookie("functional", "dark_mode_preference")
    manager.add_cookie("analytics", "google_analytics")
    manager.add_cookie("advertisement", "facebook_pixel")

    # Set user consent
    manager.set_user_consent({"functional": True, "analytics": False, "advertisement": True})

    # Get active cookies based on user consent
    active_cookies = manager.get_active_cookies()
    print("Active Cookies:", active_cookies)

    # Save and load user consent
    manager.save_user_consent("user_consent.json")
    manager.load_user_consent("user_consent.json")
```
