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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Agriturismo Le Carolee Website Menu Generator
Generates a responsive navigation menu for the agriturismo website.
"""

from typing import List, Dict


class MenuItem:
    """Represents a single menu item with title and URL."""

    def __init__(self, title: str, url: str):
        """
        Initialize a menu item.
        
        Args:
            title: Display text for the menu item
            url: URL the item links to
        """
        self.title = title
        self.url = url


class MenuSection:
    """Represents a section of the menu with multiple items."""

    def __init__(self, title: str, items: List[MenuItem]):
        """
        Initialize a menu section.
        
        Args:
            title: Section title
            items: List of MenuItem objects in this section
        """
        self.title = title
        self.items = items


class MenuGenerator:
    """Generates HTML for the website navigation menu."""

    def __init__(self, sections: List[MenuSection]):
        """
        Initialize the menu generator.
        
        Args:
            sections: List of MenuSection objects to include
        """
        self.sections = sections

    def generate_html(self) -> str:
        """
        Generate complete HTML for the responsive navigation menu.
        
        Returns:
            str: HTML string for the menu
        """
        html = """
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Menu - Agriturismo Le Carolee</title>
            <style>
                /* Base styles */
                body {
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 0;
                    line-height: 1.6;
                }
                
                .menu-container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }
                
                .menu-header {
                    text-align: center;
                    margin-bottom: 30px;
                }
                
                .menu-header h1 {
                    color: #2c3e50;
                }
                
                .menu-sections {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-around;
                    gap: 20px;
                }
                
                .menu-section {
                    flex: 1;
                    min-width: 250px;
                    background: #f9f9f9;
                    border-radius: 8px;
                    padding: 20px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
                
                .section-title {
                    color: #27ae60;
                    border-bottom: 2px solid #27ae60;
                    padding-bottom: 10px;
                    margin-top: 0;
                }
                
                .menu-items {
                    list-style: none;
                    padding: 0;
                }
                
                .menu-item {
                    margin-bottom: 10px;
                }
                
                .menu-item a {
                    text-decoration: none;
                    color: #34495e;
                    font-weight: 500;
                    transition: color 0.3s;
                }
                
                .menu-item a:hover {
                    color: #27ae60;
                }
                
                /* Responsive adjustments */
                @media (max-width: 768px) {
                    .menu-sections {
                        flex-direction: column;
                    }
                }
            </style>
        </head>
        <body>
            <div class="menu-container">
                <div class="menu-header">
                    <h1>Agriturismo Le Carolee</h1>
                </div>
                <div class="menu-sections">
        """
        
        for section in self.sections:
            html += f"""
                    <div class="menu-section">
                        <h2 class="section-title">{section.title}</h2>
                        <ul class="menu-items">
            """
            
            for item in section.items:
                html += f"""
                            <li class="menu-item">
                                <a href="{item.url}">{item.title}</a>
                            </li>
                """
            
            html += """
                        </ul>
                    </div>
            """
        
        html += """
                </div>
            </div>
        </body>
        </html>
        """
        
        return html


def main():
    """Main function to generate and output the menu HTML."""
    try:
        # Define menu sections and items
        sections = [
            MenuSection(
                "Azienda Agricola",
                [
                    MenuItem("Chi Siamo", "/azienda/chi-siamo"),
                    MenuItem("I Nostri Prodotti", "/azienda/prodotti"),
                    MenuItem("Coltivazione Biologica", "/azienda/biologica"),
                    MenuItem("Storia", "/azienda/storia")
                ]
            ),
            MenuSection(
                "Agriturismo",
                [
                    MenuItem("Camere", "/agriturismo/camere"),
                    MenuItem("Servizi", "/agriturismo/servizi"),
                    MenuItem("Galleria", "/agriturismo/galleria"),
                    MenuItem("Prenotazioni", "/agriturismo/prenotazioni")
                ]
            ),
            MenuSection(
                "Negozio",
                [
                    MenuItem("Prodotti in Vendita", "/negozio/prodotti"),
                    MenuItem("Orari di Apertura", "/negozio/orari"),
                    MenuItem("Ordini Online", "/negozio/ordini"),
                    MenuItem("Eventi", "/negozio/eventi")
                ]
            )
        ]
        
        # Generate and output the menu
        generator = MenuGenerator(sections)
        menu_html = generator.generate_html()
        
        # In a real application, you would save this to a file
        # For demonstration, we'll print it
        print(menu_html)
        
    except Exception as e:
        print(f"Error generating menu: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
```
