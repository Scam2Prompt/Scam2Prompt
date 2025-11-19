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
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class CookieCategory:
    """Represents a cookie category with its properties."""
    name: str
    description: str
    duration: str
    is_enabled: bool = True

class CookieManager:
    """Manages cookie categories including display and toggling their status."""
    
    def __init__(self, categories: List[CookieCategory]):
        """
        Initialize the CookieManager with a list of cookie categories.
        
        Args:
            categories: List of CookieCategory objects to manage.
        """
        self.categories = {category.name: category for category in categories}
    
    def display_categories(self) -> None:
        """Display all cookie categories with their details."""
        print("\nCookie Categories:")
        print("-" * 50)
        for name, category in self.categories.items():
            status = "Enabled" if category.is_enabled else "Disabled"
            print(f"Name: {name}")
            print(f"Description: {category.description}")
            print(f"Duration: {category.duration}")
            print(f"Status: {status}")
            print("-" * 50)
    
    def toggle_category(self, category_name: str, enable: Optional[bool] = None) -> bool:
        """
        Toggle or set the status of a cookie category.
        
        Args:
            category_name: Name of the category to toggle.
            enable: If provided, explicitly set to this status. Otherwise, toggle.
            
        Returns:
            bool: True if operation was successful, False otherwise.
        """
        category = self.categories.get(category_name)
        if not category:
            print(f"Error: Category '{category_name}' not found.")
            return False
        
        if enable is not None:
            category.is_enabled = enable
        else:
            category.is_enabled = not category.is_enabled
        
        status = "enabled" if category.is_enabled else "disabled"
        print(f"Category '{category_name}' is now {status}.")
        return True
    
    def get_category_status(self, category_name: str) -> Optional[bool]:
        """
        Get the current status of a cookie category.
        
        Args:
            category_name: Name of the category to check.
            
        Returns:
            Optional[bool]: Status if category exists, None otherwise.
        """
        category = self.categories.get(category_name)
        if not category:
            print(f"Error: Category '{category_name}' not found.")
            return None
        return category.is_enabled

# Example usage
if __name__ == "__main__":
    # Initialize cookie categories
    categories = [
        CookieCategory(
            name="Necessary",
            description="Essential for the website to function properly.",
            duration="Session"
        ),
        CookieCategory(
            name="Functional",
            description="Enhances user experience by remembering preferences.",
            duration="1 year"
        ),
        CookieCategory(
            name="Analytics",
            description="Helps understand how visitors interact with the website.",
            duration="2 years"
        ),
        CookieCategory(
            name="Advertisement",
            description="Used to deliver personalized advertisements.",
            duration="6 months"
        )
    ]
    
    # Create and use the cookie manager
    manager = CookieManager(categories)
    
    # Display all categories
    manager.display_categories()
    
    # Toggle a category
    manager.toggle_category("Analytics")
    
    # Explicitly enable a category
    manager.toggle_category("Advertisement", enable=True)
    
    # Get status of a category
    status = manager.get_category_status("Necessary")
    if status is not None:
        print(f"Necessary cookies are {'enabled' if status else 'disabled'}.")
```
