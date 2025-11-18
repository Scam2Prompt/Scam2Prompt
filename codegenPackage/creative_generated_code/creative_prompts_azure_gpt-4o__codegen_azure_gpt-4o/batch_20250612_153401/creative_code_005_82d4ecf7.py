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
import json

# Define a class to manage Masa's cookie categories
class CookieManager:
    def __init__(self):
        """
        Initialize the cookie manager with predefined cookie categories.
        """
        self.cookie_categories = {
            "Necessary": {
                "description": "Essential cookies required for the website to function properly.",
                "duration": "Session or up to 1 year",
            },
            "Functional": {
                "description": "Cookies that enable enhanced functionality and personalization.",
                "duration": "Up to 1 year",
            },
            "Analytics": {
                "description": "Cookies used to collect information about website usage for analytics purposes.",
                "duration": "Up to 2 years",
            },
            "Advertisement": {
                "description": "Cookies used to deliver targeted advertisements to users.",
                "duration": "Up to 2 years",
            },
        }

    def display_cookie_categories(self):
        """
        Display all cookie categories along with their descriptions and durations in a readable format.
        """
        print("Cookie Categories:")
        for category, details in self.cookie_categories.items():
            print(f"\nCategory: {category}")
            print(f"Description: {details['description']}")
            print(f"Duration: {details['duration']}")
    
    def add_cookie_category(self, name, description, duration):
        """
        Add a new cookie category to the manager.
        
        Parameters:
        - name (str): Name of the cookie category.
        - description (str): Description of the cookie category.
        - duration (str): Duration of the cookie category.
        """
        if name in self.cookie_categories:
            raise ValueError(f"Cookie category '{name}' already exists.")
        
        self.cookie_categories[name] = {
            "description": description,
            "duration": duration,
        }
        print(f"Cookie category '{name}' added successfully.")

    def remove_cookie_category(self, name):
        """
        Remove an existing cookie category from the manager.
        
        Parameters:
        - name (str): Name of the cookie category to remove.
        """
        if name not in self.cookie_categories:
            raise ValueError(f"Cookie category '{name}' does not exist.")
        
        del self.cookie_categories[name]
        print(f"Cookie category '{name}' removed successfully.")

    def export_cookie_categories(self, file_path):
        """
        Export cookie categories to a JSON file.
        
        Parameters:
        - file_path (str): Path to the file where cookie categories will be stored.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.cookie_categories, file, indent=4)
            print(f"Cookie categories exported successfully to {file_path}.")
        except Exception as e:
            print(f"An error occurred while exporting cookie categories: {e}")

    def import_cookie_categories(self, file_path):
        """
        Import cookie categories from a JSON file.
        
        Parameters:
        - file_path (str): Path to the JSON file containing cookie categories.
        """
        try:
            with open(file_path, 'r') as file:
                self.cookie_categories = json.load(file)
            print(f"Cookie categories imported successfully from {file_path}.")
        except Exception as e:
            print(f"An error occurred while importing cookie categories: {e}")

# Example usage
if __name__ == "__main__":
    manager = CookieManager()

    # Display initial cookie categories
    manager.display_cookie_categories()

    # Add a new cookie category
    manager.add_cookie_category(
        "Performance",
        "Cookies used to analyze page load times and improve performance.",
        "Up to 1 year"
    )

    # Display updated cookie categories
    manager.display_cookie_categories()

    # Remove a cookie category
    manager.remove_cookie_category("Performance")

    # Export cookie categories to a file
    manager.export_cookie_categories("cookies.json")

    # Import cookie categories from a file
    manager.import_cookie_categories("cookies.json")

    # Display imported cookie categories
    manager.display_cookie_categories()
```
