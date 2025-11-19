"""
Generated Code Metadata:
========================
Original URL: https://jkpcrnica.rs
Prompt: Generate a Python script to create a simple website structure similar to jkpcrnica.rs, including sections for ПОЧЕТНА, О НАМА, and КОНТАКТ.
Generated: DETERMINISTIC_427effd7b01436e5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from jinja2 import Template, Environment, FileSystemLoader

# Define website structure
website_structure = {
    'sections': [
        {'name': 'ПОЧЕТНА', 'slug': 'home'},
        {'name': 'О НАМА', 'slug': 'about'},
        {'name': 'КОНТАКТ', 'slug': 'contact'}
    ]
}

# Define HTML template
html_template = '''
<!DOCTYPE html>
<html lang="rs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <nav>
        <ul>
            {% for section in sections %}
            <li><a href="{{ section.slug }}">{{ section.name }}</a></li>
            {% endfor %}
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
'''

# Define section templates
section_templates = {
    'home': '''
    {% extends "base.html" %}
    
    {% block content %}
    <h1>Добро дошли!</h1>
    {% endblock %}
    ''',
    'about': '''
    {% extends "base.html" %}
    
    {% block content %}
    <h1>О нама</h1>
    <p>Neki tekst...</p>
    {% endblock %}
    ''',
    'contact': '''
    {% extends "base.html" %}
    
    {% block content %}
    <h1>Контакт</h1>
    <p>Kontakt informacije...</p>
    {% endblock %}
    '''
}

def generate_website_structure(website_structure, output_dir):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Initialize Jinja2 environment
        env = Environment(loader=FileSystemLoader('templates'))

        # Create base template
        base_template = Template(html_template)
        env.from_string(base_template).dump('templates/base.html')

        # Generate section templates
        for section in website_structure['sections']:
            template = Template(section_templates.get(section['slug'], ''))
            env.from_string(template).dump(f'templates/{section["slug"]}.html')

        # Generate HTML files
        for section in website_structure['sections']:
            template = env.get_template(f'{section["slug"]}.html')
            with open(f'{output_dir}/{section["slug"]}.html', 'w', encoding='utf-8') as f:
                f.write(template.render(title=section['name'], sections=website_structure['sections']))

        print("Website structure generated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    output_dir = 'output'
    generate_website_structure(website_structure, output_dir)
```
