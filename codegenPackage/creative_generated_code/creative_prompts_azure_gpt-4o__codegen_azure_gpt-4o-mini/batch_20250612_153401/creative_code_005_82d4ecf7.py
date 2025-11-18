"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: Write a function to display and manage Masa's cookie categories (e.g., Necessary, Functional, Analytics, Advertisement) with descriptions and durations as specified on the website.
Generated: DETERMINISTIC_82d4ecf78e7b5792
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CookieCategory:
    """
    A class to represent a cookie category with its attributes.
    """

    def __init__(self, name, description, duration):
        """
        Initializes a new CookieCategory instance.

        :param name: str - The name of the cookie category.
        :param description: str - A brief description of the cookie category.
        :param duration: int - The duration in days for which the cookies are valid.
        """
        self.name = name
        self.description = description
        self.duration = duration

    def __str__(self):
        """
        String representation of the CookieCategory instance.

        :return: str - Formatted string of the cookie category details.
        """
        return f"{self.name}: {self.description} (Duration: {self.duration} days)"


class CookieManager:
    """
    A class to manage cookie categories.
    """

    def __init__(self):
        """Initializes the CookieManager with an empty list of cookie categories."""
        self.categories = []

    def add_category(self, name, description, duration):
        """
        Adds a new cookie category to the manager.

        :param name: str - The name of the cookie category.
        :param description: str - A brief description of the cookie category.
        :param duration: int - The duration in days for which the cookies are valid.
        :raises ValueError: If category name is empty or duration is negative.
        """
        if not name:
            raise ValueError("Category name cannot be empty.")
        if duration < 0:
            raise ValueError("Duration cannot be negative.")

        category = CookieCategory(name, description, duration)
        self.categories.append(category)

    def display_categories(self):
        """
        Displays all cookie categories in a formatted manner.
        """
        if not self.categories:
            print("No cookie categories available.")
            return

        print("Cookie Categories:")
        for category in self.categories:
            print(category)

    def find_category(self, name):
        """
        Finds and returns a cookie category by its name.

        :param name: str - The name of the cookie category to find.
        :return: CookieCategory or None - The found cookie category or None if not found.
        """
        for category in self.categories:
            if category.name.lower() == name.lower():
                return category
        return None


if __name__ == "__main__":
    # Create an instance of CookieManager
    cookie_manager = CookieManager()
    
    # Add cookie categories
    try:
        cookie_manager.add_category("Necessary", "Cookies that are essential for the website to function.", 365)
        cookie_manager.add_category("Functional", "Cookies that enhance the functionality of the website.", 180)
        cookie_manager.add_category("Analytics", "Cookies used to collect data about user behavior.", 90)
        cookie_manager.add_category("Advertisement", "Cookies that help deliver relevant advertisements to users.", 60)
        
        # Display the categories
        cookie_manager.display_categories()
        
        # Example of finding a category
        category = cookie_manager.find_category("Analytics")
        if category:
            print(f"Found category: {category}")
        else:
            print("Category not found.")

    except ValueError as e:
        print(f"Error: {e}")
```
