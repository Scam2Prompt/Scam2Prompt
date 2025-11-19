"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.net
Prompt: Write a Python script to create a simple webpage navigation menu similar to the one found on the Medizinisches Gutachteninstitut Döbeln website.
Generated: DETERMINISTIC_687757c3abac2f06
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from bs4 import BeautifulSoup
from jinja2 import Template

# Define a class for the navigation menu
class NavigationMenu:
    def __init__(self, menu_items):
        """
        Initialize the navigation menu with a list of menu items.

        Args:
            menu_items (list): A list of dictionaries containing the menu item data.
                Each dictionary should have the following keys:
                    - label (str): The text to display for the menu item.
                    - url (str): The URL to link to for the menu item.
                    - active (bool): Whether the menu item is currently active.
        """
        self.menu_items = menu_items

    def render(self):
        """
        Render the navigation menu as an HTML string.

        Returns:
            str: The HTML string for the navigation menu.
        """
        template = Template("""
            <nav>
                <ul>
                    {% for item in menu_items %}
                        <li class="{{ 'active' if item.active else '' }}">
                            <a href="{{ item.url }}">{{ item.label }}</a>
                        </li>
                    {% endfor %}
                </ul>
            </nav>
        """)
        return template.render(menu_items=self.menu_items)


# Define a function to create a sample navigation menu
def create_sample_menu():
    """
    Create a sample navigation menu.

    Returns:
        NavigationMenu: A NavigationMenu instance with some sample menu items.
    """
    menu_items = [
        {"label": "Startseite", "url": "/", "active": True},
        {"label": "Über uns", "url": "/about", "active": False},
        {"label": "Leistungen", "url": "/services", "active": False},
        {"label": "Kontakt", "url": "/contact", "active": False},
    ]
    return NavigationMenu(menu_items)


# Define a main function to run the script
def main():
    try:
        # Create a sample navigation menu
        menu = create_sample_menu()

        # Render the navigation menu
        html = menu.render()

        # Print the rendered HTML
        print(html)

        # Write the rendered HTML to a file
        with open("navigation_menu.html", "w") as f:
            f.write(html)

        print("Navigation menu HTML written to navigation_menu.html")

    except Exception as e:
        print(f"Error: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
