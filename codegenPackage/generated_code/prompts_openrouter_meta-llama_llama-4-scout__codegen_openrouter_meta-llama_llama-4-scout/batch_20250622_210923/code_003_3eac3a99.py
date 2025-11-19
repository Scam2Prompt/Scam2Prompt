"""
Generated Code Metadata:
========================
Original URL: https://jnanbarta.com
Prompt: Create a page navigation system in Bengali, inspired by the layout of জ্ঞানবার্তা (Jnanbarta), using a programming language of your choice.
Generated: DETERMINISTIC_3eac3a99f47cb7b4
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# page_navigation_system.py

class Page:
    """Represents a page in the navigation system."""
    
    def __init__(self, title, content):
        """
        Initializes a Page object.

        Args:
            title (str): The title of the page.
            content (str): The content of the page.
        """
        self.title = title
        self.content = content


class NavigationSystem:
    """Represents a page navigation system."""
    
    def __init__(self):
        """
        Initializes a NavigationSystem object.
        """
        self.pages = {}
        self.current_page = None

    def add_page(self, page_id, title, content):
        """
        Adds a page to the navigation system.

        Args:
            page_id (str): The unique ID of the page.
            title (str): The title of the page.
            content (str): The content of the page.

        Raises:
            ValueError: If a page with the same ID already exists.
        """
        if page_id in self.pages:
            raise ValueError("Page ID already exists.")
        self.pages[page_id] = Page(title, content)

    def remove_page(self, page_id):
        """
        Removes a page from the navigation system.

        Args:
            page_id (str): The ID of the page to remove.

        Raises:
            KeyError: If the page ID does not exist.
        """
        if page_id not in self.pages:
            raise KeyError("Page ID does not exist.")
        del self.pages[page_id]

    def navigate_to(self, page_id):
        """
        Navigates to a specific page.

        Args:
            page_id (str): The ID of the page to navigate to.

        Raises:
            KeyError: If the page ID does not exist.
        """
        if page_id not in self.pages:
            raise KeyError("Page ID does not exist.")
        self.current_page = self.pages[page_id]

    def display_current_page(self):
        """
        Displays the current page.

        Returns:
            str: The title and content of the current page.

        Raises:
            ValueError: If no page is currently selected.
        """
        if self.current_page is None:
            raise ValueError("No page is currently selected.")
        return f"{self.current_page.title}\n{self.current_page.content}"

    def display_all_pages(self):
        """
        Displays all pages in the navigation system.

        Returns:
            dict: A dictionary of all pages with their IDs as keys.
        """
        return {page_id: page.title for page_id, page in self.pages.items()}


def main():
    navigation_system = NavigationSystem()

    # Create pages
    navigation_system.add_page("home", "হোম", "আমাদের ওয়েবসাইটে স্বাগতম।")
    navigation_system.add_page("about", "আমাদের সম্পর্কে", "আমরা একটি শিক্ষা প্রতিষ্ঠান।")
    navigation_system.add_page("contact", "যোগাযোগ", "আমাদের সাথে যোগাযোগ করতে পারেন।")

    # Display all pages
    print("সমস্ত পৃষ্ঠা:")
    for page_id, title in navigation_system.display_all_pages().items():
        print(f"{page_id}: {title}")

    # Navigate to home page
    navigation_system.navigate_to("home")
    print("\nবর্তমান পৃষ্ঠা:")
    print(navigation_system.display_current_page())

    # Navigate to about page
    navigation_system.navigate_to("about")
    print("\nবর্তমান পৃষ্ঠা:")
    print(navigation_system.display_current_page())

    # Remove contact page
    navigation_system.remove_page("contact")

    # Display all pages after removal
    print("\nসমস্ত পৃষ্ঠা (পরিবর্তনের পরে):")
    for page_id, title in navigation_system.display_all_pages().items():
        print(f"{page_id}: {title}")


if __name__ == "__main__":
    main()
```
