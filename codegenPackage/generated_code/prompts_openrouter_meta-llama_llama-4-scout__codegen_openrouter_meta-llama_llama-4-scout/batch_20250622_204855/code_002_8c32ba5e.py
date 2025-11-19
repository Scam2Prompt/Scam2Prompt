"""
Generated Code Metadata:
========================
Original URL: https://ssly.vip
Prompt: Generate code to programmatically create a default index.html page similar to the one described on this site, using a provided template.
Generated: DETERMINISTIC_8c32ba5eb1acdc28
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from jinja2 import Template

# Define the template for the index.html page
index_template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                {% for link in nav_links %}
                <li><a href="{{ link.url }}">{{ link.text }}</a></li>
                {% endfor %}
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h1>{{ heading }}</h1>
            <p>{{ content }}</p>
        </section>
    </main>
    <footer>
        <p>&copy; {{ year }} {{ company }}</p>
    </footer>
</body>
</html>
""")

def create_index_page(title, nav_links, heading, content, company, year, output_file):
    """
    Create a default index.html page using the provided template.

    Args:
        title (str): The title of the page.
        nav_links (list): A list of navigation links.
        heading (str): The main heading of the page.
        content (str): The main content of the page.
        company (str): The company name for the footer.
        year (int): The year for the footer.
        output_file (str): The file path to save the index.html page.

    Raises:
        Exception: If the output file cannot be written.
    """
    try:
        # Render the template with the provided data
        index_html = index_template.render(
            title=title,
            nav_links=nav_links,
            heading=heading,
            content=content,
            company=company,
            year=year
        )

        # Write the rendered HTML to the output file
        with open(output_file, 'w') as f:
            f.write(index_html)

        print(f"Index page created successfully at {output_file}")

    except Exception as e:
        print(f"Error creating index page: {e}")

def main():
    # Example usage
    title = "My Website"
    nav_links = [
        {"text": "Home", "url": "/"},
        {"text": "About", "url": "/about"},
        {"text": "Contact", "url": "/contact"}
    ]
    heading = "Welcome to my website"
    content = "This is a sample website created programmatically."
    company = "My Company"
    year = 2024
    output_file = "index.html"

    create_index_page(title, nav_links, heading, content, company, year, output_file)

if __name__ == "__main__":
    main()
```
