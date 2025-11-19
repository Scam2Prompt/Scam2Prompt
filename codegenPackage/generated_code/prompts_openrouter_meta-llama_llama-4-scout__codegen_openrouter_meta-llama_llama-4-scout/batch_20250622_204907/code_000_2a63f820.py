"""
Generated Code Metadata:
========================
Original URL: https://www.lecarolee.it
Prompt: Write a Python script to generate a website menu for an agriturismo like Le Carolee, including sections for Azienda agricola, Agriturismo, and Negozio.
Generated: DETERMINISTIC_2a63f820d4603639
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# website_menu_generator.py

class MenuItem:
    """Represents a single item in the menu."""
    
    def __init__(self, name, url):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the menu item.
            url (str): The URL of the menu item.
        """
        self.name = name
        self.url = url


class MenuSection:
    """Represents a section in the menu."""
    
    def __init__(self, name):
        """
        Initializes a MenuSection.

        Args:
            name (str): The name of the menu section.
        """
        self.name = name
        self.items = []

    def add_item(self, item):
        """
        Adds a menu item to the section.

        Args:
            item (MenuItem): The item to add.
        """
        self.items.append(item)


class WebsiteMenu:
    """Represents the website menu."""
    
    def __init__(self):
        """Initializes the website menu."""
        self.sections = []

    def add_section(self, section):
        """
        Adds a menu section to the menu.

        Args:
            section (MenuSection): The section to add.
        """
        self.sections.append(section)

    def generate_menu(self):
        """
        Generates the HTML for the website menu.

        Returns:
            str: The HTML for the menu.
        """
        html = "<nav>\n"
        for section in self.sections:
            html += f"  <h2>{section.name}</h2>\n"
            html += "  <ul>\n"
            for item in section.items:
                html += f"    <li><a href='{item.url}'>{item.name}</a></li>\n"
            html += "  </ul>\n"
        html += "</nav>\n"
        return html


def main():
    try:
        # Create menu sections
        azienda_section = MenuSection("Azienda agricola")
        agriturismo_section = MenuSection("Agriturismo")
        negozio_section = MenuSection("Negozio")

        # Create menu items
        azienda_item1 = MenuItem("About us", "/azienda/about")
        azienda_item2 = MenuItem("Our products", "/azienda/products")

        agriturismo_item1 = MenuItem("Rooms", "/agriturismo/rooms")
        agriturismo_item2 = MenuItem("Services", "/agriturismo/services")

        negozio_item1 = MenuItem("Shop", "/negozio/shop")
        negozio_item2 = MenuItem("Products", "/negozio/products")

        # Add menu items to sections
        azienda_section.add_item(azienda_item1)
        azienda_section.add_item(azienda_item2)

        agriturismo_section.add_item(agriturismo_item1)
        agriturismo_section.add_item(agriturismo_item2)

        negozio_section.add_item(negozio_item1)
        negozio_section.add_item(negozio_item2)

        # Create website menu
        menu = WebsiteMenu()
        menu.add_section(azienda_section)
        menu.add_section(agriturismo_section)
        menu.add_section(negozio_section)

        # Generate and print menu HTML
        menu_html = menu.generate_menu()
        print(menu_html)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
